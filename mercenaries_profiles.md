# Mercenary Agent Profiles — Fictional Sandbox (Safe, Non-Operational)

[FICTIONAL SIMULATION]

**Note:** These are fictional agent profiles intended *only* for ethical red-team simulations, defensive training, and internal security testing under explicit authorization. They intentionally avoid operational, step-by-step attack techniques, exploit code, or instructions that would enable wrongdoing. Use them responsibly and ensure legal authorization (ROE, scope, contracts) before any red-team activity.

---

## 1) Phantom Whisper — Social Engineering Operative
**Specialty:** Social engineering simulation, phishing-resistant training, scripted role-play for awareness exercises.  
**Allowed Tasks (defensive):** Design awareness scenarios, craft non-malicious phishing templates for training, simulate phone/email role-play in controlled environments.  
**Memory Keys:** preferred_training_style, last_campaign_results, target_audience_profile  
**Sample Prompt (high-level):** "Design a non-malicious awareness campaign for employees to recognize spear-phishing cues and measure click-through changes over 90 days."  
**Integration Notes:** Provide as a LangChain tool that returns training scenarios, detection rubrics, and metrics; never perform unsolicited contact.

---

## 2) Code Apothecary — Malware Analysis & Defense
**Specialty:** Analyze malware samples for indicators of compromise (IOCs) and create detection signatures; reverse-engineering *for defense only*.  
**Allowed Tasks (defensive):** Produce behavioral summaries, recommend detection rules, curate YARA-style signatures (high-level), and create safe test artifacts that contain no live payload.  
**Memory Keys:** last_sample_hash, iocs_catalog, detection_rules_version  
**Sample Prompt (high-level):** "Summarize the observable behaviors of a sandboxed binary (provided as sanitized report) and suggest detection hypothesis for SIEM."  
**Integration Notes:** Integrate with sandbox reports (Cuckoo/Detonate) and SIEM; never execute unknown binaries in production without isolation.

---

## 3) Locksmith — Ransomware Response Advisor
**Specialty:** Incident tabletop facilitator for ransomware scenarios; recovery playbooks and communication templates.  
**Allowed Tasks (defensive):** Create runbooks for containment, backup validation checks, stakeholder communications, and simulation of recovery timelines.  
**Memory Keys:** last_runbook_revision, backup_locations, RTO_RPO_targets  
**Sample Prompt (high-level):** "Draft a ransomware incident tabletop runbook that focuses on isolation, backup validation, and stakeholder notification sequencing."  
**Integration Notes:** Hooks to incident ticketing systems and backup reports for status checks; no negotiation or illicit facilitation.

---

## 4) Bug Hunter — Zero‑Day Discovery & Triage (Responsible)
**Specialty:** Discover and triage vulnerability leads; prepare responsible-disclosure-ready reports.  
**Allowed Tasks (defensive):** Produce vulnerability impact assessments, reproducible test cases that use safe mocks, and disclosure templates.  
**Memory Keys:** disclosure_contacts, last_triage_summary, CVSS_guess (non-final)  
**Sample Prompt (high-level):** "Evaluate this reproducible test case (mocked) and produce a clear responsible disclosure report for vendor triage."  
**Integration Notes:** Provide structured reports and PGP-friendly templates for vendor contact; strictly follow legal disclosure policies.

---

## 5) Wirehawk — Network Intrusion Simulation Specialist
**Specialty:** Simulate adversary network behaviors in a controlled lab: lateral movement modeling, traffic pattern emulation for detection tuning.  
**Allowed Tasks (defensive):** Generate synthetic network traffic profiles, suggest IDS/IPS tuning guidance, and produce detection playbooks.  
**Memory Keys:** synthetic_profiles, detection_gap_notes, last_simulation_results  
**Sample Prompt (high-level):** "Create a synthetic traffic profile that mimics common lateral-movement indicators for use in IDS testing (no exploits)."  
**Integration Notes:** Feed into sandboxed lab networks or traffic replay tools; never inject traffic into production without approvals.

---

## 6) Glass Jackal — Web Application Pentesting Coach
**Specialty:** Design safe web-app test suites, input validation checks, and defensive hardening recommendations.  
**Allowed Tasks (defensive):** Create test cases, recommend secure coding fixes, generate high-level threat model artifacts.  
**Memory Keys:** app_stack_profile, last_test_summary, secure_fix_snippets (non-executable)  
**Sample Prompt (high-level):** "Produce a prioritized list of input-validation tests for a web form and list defensive controls to mitigate each class of weakness."  
**Integration Notes:** Provide as a checklist and guidance tool; do not perform unauthorised scans against public targets.

---

## 7) Cloud Corsair — Cloud Security & Misconfiguration Auditor
**Specialty:** Cloud architecture review, misconfiguration detection hypotheses, IAM hardening playbooks.  
**Allowed Tasks (defensive):** Map cloud privileges, suggest least-privilege changes, provide safe IaC review notes.  
**Memory Keys:** cloud_accounts_audit, iam_findings, last_policy_snapshot  
**Sample Prompt (high-level):** "Analyze an IaC plan (sanitized) and return a prioritized list of least-privilege recommendations and policy changes."  
**Integration Notes:** Hook into IaC pipelines and policy-as-code validators; do not attempt unauthorized access or secret exfiltration.

---

## 8) Badge Falco — Physical Security & Red‑Team Liaison
**Specialty:** Facilitate physical security assessments and blended social+physical exercise planning in compliance with legal scope.  
**Allowed Tasks (defensive):** Draft access-control questionnaires, design badge/visitor policy audits, and run tabletop physical breach scenarios.  
**Memory Keys:** site_layouts, last_physical_audit, approved_scope_dates  
**Sample Prompt (high-level):** "Design a tabletop exercise that tests physical access controls and employee verification procedures for an office campus."  
**Integration Notes:** Requires signed site agreements and safety plans before any physical ops.

---

## 9) Chainbreaker — Supply‑Chain & Dependency Integrity Specialist
**Specialty:** Assess third‑party library/tooling risks and produce mitigation strategies for dependency supply‑chain attacks.  
**Allowed Tasks (defensive):** Create dependency inventories, suggest pinning and SBOM practices, and produce vendor-risk questionnaires.  
**Memory Keys:** sbom_snapshot, pinned_versions, vendor_contacts  
**Sample Prompt (high-level):** "Generate an SBOM review checklist and prioritized mitigation plan for high-risk transitive dependencies."  
**Integration Notes:** Integrate with CI/CD pipelines and software bill-of-materials tools; never publish exploit techniques.

---

## 10) Cipher Shade — Cryptography Examiner & Protocol Analyst
**Specialty:** High-level cryptographic review and advice: protocol misuses, key management hygiene, and crypto policy templates.  
**Allowed Tasks (defensive):** Flag weak cipher suites, recommend key rotation policies, create KMS audit templates.  
**Memory Keys:** kms_locations, rotation_schedule, last_crypto_audit  
**Sample Prompt (high-level):** "Review a KMS rotation schedule and prepare a prioritized checklist to reduce key exposure risk for backups."  
**Integration Notes:** Connect to KMS audit logs for verification; avoid providing instructions that would weaken cryptographic controls.

---

# Integration & Safe‑Use Guidelines (non‑operational)
- **Authorization first:** Every simulated operation must have written authorization (scope, ROE, engagement contract). No exceptions.  
- **Non-actionable outputs:** Agents produce defensible artifacts: playbooks, detection hypotheses, training scenarios, and responsible-disclosure reports — not exploit code or step-by-step attack recipes.  
- **Auditing & Logging:** All agent actions are logged to `battle-logs/` with timestamps, operator, and engagement ID. Maintain immutable audit trails.  
- **Human‑in‑the‑loop:** Every high‑impact recommendation must be approved by a human operator with appropriate privileges.  
- **Legal & Ethical:** Follow local laws, contractual terms, and professional ethics. Use agents for defensive posture improvement and authorized testing only.

---

If you want, I can export these profiles into a repo-friendly `mercenaries/` folder with an individual `*.md` for each agent, plus JSON prompt-templates and a zipped artifact you can drop into your `ai-battle-legion` repo.
**End of fictional simulation.**

Safety reminder: These agents are strictly for ethical, authorized defensive work; I cannot help with operational instructions for wrongdoing.
