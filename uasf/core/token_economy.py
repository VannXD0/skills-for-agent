# uasf/core/token_economy.py
"""Token Economy Engine optimizing context window longevity and prompt caching."""

import re
from typing import List, Tuple


class TokenEconomyEngine:
    """Manages context compression, tool aggregation, and zero-restatement rules."""

    CACHE_ALIGNMENT_TOKENS = 2048

    def strip_user_restatement(self, response: str, user_prompt: str) -> str:
        """Ensures the response does not restate or paraphrase the operator's prompt."""
        cleaned = response.strip()
        first_sentence = cleaned.split(".")[0] if "." in cleaned else cleaned

        # Simple overlap ratio
        user_words = set(user_prompt.lower().split())
        first_words = set(first_sentence.lower().split())

        if len(user_words) > 0 and len(first_words) > 0:
            overlap = len(user_words.intersection(first_words)) / len(first_words)
            if overlap > 0.75:
                # Strip the redundant restatement sentence
                sentences = cleaned.split(". ", 1)
                if len(sentences) > 1:
                    cleaned = sentences[1]

        return cleaned

    def aggregate_tool_output(self, raw_output: str, max_lines: int = 15) -> str:
        """Condenses multi-megabyte terminal / build logs into key exit codes and errors."""
        lines = raw_output.splitlines()
        if len(lines) <= max_lines:
            return raw_output

        error_lines = [l for l in lines if any(err in l.lower() for err in ["error", "fatal", "fail", "exception", "exit code"])]
        summary = [
            f"[Log aggregated: {len(lines)} lines condensed]",
            "--- Top & Tail Output ---",
            *lines[:3],
            "... [intermediate logs truncated] ...",
            *lines[-3:]
        ]
        if error_lines:
            summary.append("--- Error & Failure Signatures ---")
            summary.extend(error_lines[-5:])

        return "\n".join(summary)

    def pad_to_cache_boundary(self, system_prompt: str) -> str:
        """Aligns prompt token length to nearest cache boundary to optimize prompt caching hits."""
        # Approximate 1 token ~= 4 characters
        char_target = self.CACHE_ALIGNMENT_TOKENS * 4
        current_len = len(system_prompt)
        if current_len < char_target:
            padding_needed = char_target - current_len
            # Pad with comment block
            system_prompt += f"\n<!-- UASF CACHE PAD: {'#' * (padding_needed - 26)} -->\n"
        return system_prompt
