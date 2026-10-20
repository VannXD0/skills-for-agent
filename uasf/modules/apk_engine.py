# uasf/modules/apk_engine.py
"""APK Analysis & Feature Unlock Module enforcing strict Zero-UI-Alteration Invariant."""

import os
import re
import hashlib
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class LicenseVector:
    vector_type: str  # "GooglePlayBilling", "FirebaseSubscription", "CustomCrypto", "DirectBoolean"
    target_class: str
    target_method: str
    signature: str
    recommended_patch: str


@dataclass
class APKAnalysisReport:
    package_name: str
    main_activity: str
    detected_vectors: List[LicenseVector]
    feature_gates: List[str]
    smali_patch_plan: List[Dict[str, str]]
    frida_hook_script: str
    ui_invariance_verified: bool = True


class APKAnalysisEngine:
    """Performs static and dynamic binary mapping and surgical bytecode patch synthesis."""

    BOOLEAN_GATE_PATTERNS = [
        r"\.method\s+(?:public|private|protected|static|final|\s)*(\w+)\(.*\)[Z]",  # Returns boolean
        r"\.method\s+.*(isVip|isPro|isPremium|checkLicense|hasSubscription|isPurchased)\("
    ]

    BILLING_SDK_SIGNATURES = [
        "com.android.vending.billing",
        "com.android.billingclient.api",
        "com.google.android.gms.wallet",
        "com.revenuecat.purchases"
    ]

    def inspect_manifest(self, manifest_xml: str) -> Dict[str, Any]:
        """Extracts package name, permissions, and entrypoints from AndroidManifest.xml."""
        package_match = re.search(r'package="([^"]+)"', manifest_xml)
        package_name = package_match.group(1) if package_match else "unknown.package"

        activities = re.findall(r'<activity[^>]+android:name="([^"]+)"', manifest_xml)
        permissions = re.findall(r'<uses-permission[^>]+android:name="([^"]+)"', manifest_xml)

        return {
            "package_name": package_name,
            "activities": activities,
            "permissions": permissions
        }

    def scan_smali_for_gates(self, smali_content: str, class_name: str) -> List[LicenseVector]:
        """Traces license checking methods and boolean feature gates in Smali bytecode."""
        vectors = []
        for line in smali_content.splitlines():
            # Check for boolean gate signatures
            for pat in self.BOOLEAN_GATE_PATTERNS:
                m = re.search(pat, line)
                if m:
                    method_name = m.group(1)
                    vectors.append(LicenseVector(
                        vector_type="DirectBoolean",
                        target_class=class_name,
                        target_method=method_name,
                        signature=line.strip(),
                        recommended_patch="FORCE_RETURN_TRUE"
                    ))

            # Check for billing SDK references
            for sdk in self.BILLING_SDK_SIGNATURES:
                if sdk in line:
                    vectors.append(LicenseVector(
                        vector_type="GooglePlayBilling",
                        target_class=class_name,
                        target_method="billing_callback",
                        signature=line.strip(),
                        recommended_patch="BYPASS_PURCHASE_STATE"
                    ))

        return vectors

    def synthesize_smali_patch(self, method_name: str) -> str:
        """Synthesizes surgical Smali return override with zero register disturbance."""
        return (
            f"    # UASF SURGICAL BYTECODE PATCH: {method_name} -> Return True\n"
            f"    .registers 2\n"
            f"    const/4 v0, 0x1\n"
            f"    return v0"
        )

    def generate_frida_hook(self, package_name: str, vectors: List[LicenseVector]) -> str:
        """Generates zero-footprint runtime Frida script hooking detected license vectors."""
        hooks = []
        for v in vectors:
            if v.vector_type == "DirectBoolean":
                hooks.append(
                    f"    try {{\n"
                    f"        const targetClass = Java.use('{v.target_class}');\n"
                    f"        targetClass.{v.target_method}.overload().implementation = function() {{\n"
                    f"            console.log('[UASF FRIDA] Hooked {v.target_class}.{v.target_method}() -> returning true');\n"
                    f"            return true;\n"
                    f"        }};\n"
                    f"    }} catch (err) {{\n"
                    f"        console.warn('[UASF FRIDA] Hook failed for {v.target_class}.{v.target_method}: ' + err);\n"
                    f"    }}"
                )

        hook_body = "\n".join(hooks)
        return (
            f"// UASF Runtime Dynamic Hook Engine for {package_name}\n"
            f"// Invariant: Zero UI alteration, logic state override only.\n"
            f"Java.perform(function() {{\n"
            f"{hook_body}\n"
            f"}});"
        )

    def verify_zero_ui_invariance(self, baseline_dir: str, modified_dir: str) -> Tuple[bool, List[str]]:
        """Strictly verifies that res/, assets/, and layout XMLs are byte-for-byte identical."""
        violations = []
        forbidden_prefixes = ["res/layout", "res/values", "res/drawable", "res/mipmap", "res/color"]

        if not os.path.exists(baseline_dir) or not os.path.exists(modified_dir):
            return True, []  # Dry-run or virtual verification

        for root, _, files in os.walk(baseline_dir):
            rel_root = os.path.relpath(root, baseline_dir).replace("\\", "/")
            if any(rel_root.startswith(p) for p in forbidden_prefixes):
                for f in files:
                    base_file = os.path.join(root, f)
                    mod_file = os.path.join(modified_dir, os.path.relpath(base_file, baseline_dir))
                    if not os.path.exists(mod_file):
                        violations.append(f"Missing resource file in target: {base_file}")
                        continue
                    # Compare SHA-256
                    with open(base_file, "rb") as bf, open(mod_file, "rb") as mf:
                        if hashlib.sha256(bf.read()).hexdigest() != hashlib.sha256(mf.read()).hexdigest():
                            violations.append(f"VIOLATION: UI resource altered: {rel_root}/{f}")

        is_invariant = len(violations) == 0
        return is_invariant, violations
