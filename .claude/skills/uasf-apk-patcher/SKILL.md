---
name: uasf-apk-patcher
description: Surgical APK reverse engineering, license vector discovery, smali & frida patching with strict Zero-UI modification invariant.
triggers:
  - apk
  - smali
  - dex
  - frida
  - license bypass
  - feature gate
---

# UASF APK Analysis & Patching Module

Automated static and dynamic binary mapping and surgical bytecode patch synthesis for Android applications.

## Hard Constraint — Zero UI Modification
Under no circumstances shall an APK feature-unlock task alter, replace, or inject UI resources, themes, colors, or views.
- `res/layout/`, `res/values/`, `res/drawable/`, and AndroidManifest themes must remain **100% byte-for-byte identical**.
- Logic patches remain strictly in bytecode (`.dex` / `.smali`) and runtime hooks (Frida).

## Operational Workflow
1. **Manifest Inspection:** Parse package name, main activity, services, and billing permissions.
2. **License Vector Tracing:** Trace call graphs for Google Play Billing (v3/v4/v5), subscription validators, and boolean gate checks (`isVip()`, `isPro()`, `checkLicense()`).
3. **Bytecode Patch Synthesis:**
   - Modify boolean return registers in Smali (`const/4 v0, 0x1`, `return v0`).
   - Generate zero-footprint runtime Frida hooks (`Java.use(...)`).
4. **Verification:** Validate that no resource or layout XML was touched.
