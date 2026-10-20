---
name: uasf-learning-loop
description: Captures in-session operator preferences and persists cross-session rules in encrypted local profile store.
triggers:
  - learning loop
  - persistent profile
  - preference
  - operator memory
---

# Continuous Learning Loop

Captures operator feedback, stylistic standards, and tool preferences across sessions.

## 1. In-Session Memory
- Dynamically logs corrections (e.g. *"prefer pure C++ over Python"*, *"don't use flexbox here"*).
- Applies updated weights immediately to subsequent turns in the active session.

## 2. Persistent Local Profile (`uasf_profile.json`)
- Stores recurring project patterns, verified environment paths, and code formatting conventions.
- Automatically injected into runtime context at session bootstrap.

## 3. Hard Memory Gate
- Historical learned tendencies are completely overridden if the operator provides an explicit directive that contradicts previous habits.
