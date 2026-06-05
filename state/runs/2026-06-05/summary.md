# Security Digest — 2026-06-05

## TL;DR
Cisco has no patch for its seventh SD-WAN zero-day of 2026 (CVE-2026-20245), which is actively being exploited to gain root on enterprise network gear. Google pushed Chrome 149.0.7827.53 to fix 37 CVEs including two critical sandbox-escape bugs (CVSS 9.6) in ANGLE and FileSystem. A Rust-written npm supply-chain malware named IronWorm seeded 36 packages with credential-stealing code; Node.js developers should audit recent installs immediately. China-linked threat group TA4922 is expanding coordinated spear-phishing from North America and APAC into the U.K., Germany, Italy, and South Africa at a record campaign pace. And Anthropic open-sourced an AI-powered vulnerability-discovery framework that shot to the top of Hacker News, sparking debate over offensive reuse.

## 1. Cisco SD-WAN Zero-Day CVE-2026-20245 Actively Exploited — Seventh This Year, No Patch
**Why it matters:** An unauthenticated attacker can gain root on Cisco SD-WAN devices, which sit at the perimeter of enterprise and government networks — and no patch exists yet.

Cisco disclosed CVE-2026-20245, a critical unauthenticated remote-code-execution flaw in its SD-WAN software, confirming the vulnerability is under active exploitation in the wild. SecurityWeek notes this is the seventh SD-WAN zero-day Cisco has disclosed in 2026 alone, a pattern that is drawing scrutiny from enterprise security teams and government defenders alike. Cisco is advising customers to apply workarounds while a patch is developed. Affected deployments should be treated as potentially compromised and network telemetry reviewed for anomalous lateral movement.

*Covered in: Bleeping Computer, SecurityWeek — 2 posts across 1 source family*
- [Cisco warns of unpatched SD-WAN zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/new-cisco-sd-wan-flaw-exploited-in-zero-day-attacks-to-gain-root)
- [Cisco Warns of 7th SD-WAN Zero-Day Exploited in 2026](https://www.securityweek.com/cisco-warns-of-7th-sd-wan-zero-day-exploited-in-2026)

## 2. Google Chrome 149.0.7827.53: 37 CVEs, Two Critical Sandbox Escapes (CVSS 9.6)
**Why it matters:** The two critical bugs — a memory-safety flaw in the ANGLE graphics layer and a use-after-free in the FileSystem API — are rated sandbox-escape primitives, meaning a malicious web page could potentially break out of Chrome and gain code execution on the underlying system.

Google released Chrome 149.0.7827.53 patching 37 vulnerabilities across ANGLE, FileSystem, V8, WebRTC, Ozone, Cast, Dawn, Skia, and other subsystems. CVE-2026-10881 (CVSS 9.6, out-of-bounds read/write in ANGLE) and CVE-2026-10886 (CVSS 9.6, use-after-free in FileSystem) are the two critical-severity issues, both flagged as potential sandbox escapes allowing renderer-to-OS elevation. The remaining 35 CVEs include numerous use-after-free bugs (rated 8.3–8.8) and type-confusion issues in V8. The update covers Chrome on Windows, macOS, Linux, iOS, and Android. Users and organizations running Chrome should verify auto-update has applied.

*Covered in: NVD — 37 CVEs across 1 source family*
- [CVE-2026-10881 (CRITICAL, CVSS 9.6) — Out-of-bounds read/write in ANGLE; sandbox escape](https://nvd.nist.gov/vuln/detail/CVE-2026-10881)
- [CVE-2026-10886 (CRITICAL, CVSS 9.6) — Use-after-free in FileSystem; sandbox escape](https://nvd.nist.gov/vuln/detail/CVE-2026-10886)

## 3. IronWorm Rust Malware Hits 36 npm Packages in Supply-Chain Attack
**Why it matters:** Any developer who installed one of the 36 compromised packages in the past 48 hours may have had credentials, environment variables, and sensitive project files silently exfiltrated to attacker infrastructure.

Security researchers identified IronWorm, a Rust-compiled credential-stealer distributed through 36 malicious packages on the npm registry. The packages impersonate popular utilities; once installed, IronWorm harvests API keys, cloud credentials, SSH keys, and environment variables before exfiltrating them to a remote C2. The use of Rust is a deliberate choice to complicate detection by tools optimized for JavaScript or Python payloads. npm has been notified and is removing the packages, but removal does not remediate systems that have already run the compromised code. Developers and CI/CD pipelines that ran `npm install` against affected packages should rotate all secrets immediately.

*Covered in: Bleeping Computer, Dark Reading — 2 posts across 1 source family*
- [New IronWorm malware hits 36 packages in npm supply-chain attack](https://www.bleepingcomputer.com/news/security/new-ironworm-malware-hits-36-packages-in-npm-supply-chain-attack)
- [Rust-Written IronWorm Hits NPM Supply Chain](https://www.darkreading.com/cyberattacks-data-breaches/rust-written-ironworm-npm-supply-chain)

## 4. China-Linked TA4922 Scales Phishing to U.K., Germany, Italy, and South Africa
**Why it matters:** TA4922's geographic expansion into Europe and Africa, combined with a record campaign pace, signals the group is moving from opportunistic targeting toward a systematic, multinational offensive — with government and military personnel the primary marks.

Three outlets independently reported that TA4922, a Chinese cybercrime group with suspected state-nexus, is now running coordinated spear-phishing campaigns in four new countries, having previously concentrated on North American and APAC targets. The campaigns use fake job offers and polished LinkedIn-style lure documents to harvest credentials and deliver implants. SecurityWeek noted the group set a new quarterly campaign-volume record. The Five Eyes advisory apparatus is expected to publish a joint advisory in the coming days. Organizations in the newly targeted regions should review inbound phishing telemetry and enforce phishing-resistant MFA on internet-facing applications.

*Covered in: The Hacker News, Dark Reading, SecurityWeek — 3 posts across 1 source family*
- [China-Linked TA4922 Expands Phishing Attacks to U.K., Germany, Italy, and South Africa](https://thehackernews.com/2026/06/china-linked-ta4922-expands-phishing.html)
- [China's TA4922 Expands Cybercrime Attacks Globally](https://www.darkreading.com/threat-intelligence/china-ta4922-cybercrime-attacks-globally)
- [Chinese Cybercrime Group in Spotlight for Record Campaign Pace](https://www.securityweek.com/chinese-cybercrime-group-ta4922-in-spotlight-for-record-campaign-pace)

## 5. Anthropic Open-Sources AI-Powered Vulnerability Discovery Framework (499 HN Points)
**Why it matters:** The framework lowers the barrier for AI-assisted code auditing at scale — an unambiguous win for defenders, but one that will also accelerate offensive research if adopted by adversaries.

Anthropic published an open-source framework on GitHub designed to help security researchers use large language models to automatically discover and triage vulnerabilities in codebases. The project reached the top of Hacker News with 499 points, generating active community discussion about its defensive value and its dual-use potential. The framework bundles tooling for AI-guided fuzzing augmentation, static-analysis triage, and automated proof-of-concept sketch generation. Security practitioners are debating whether the same pipeline can be adapted for offensive automated bug discovery — a concern Anthropic acknowledged, noting the framework is intended for authorized security research and defense.

*Covered in: Hacker News — 1 post across 1 source family*
- [Anthropic's open-source framework for AI-powered vulnerability discovery](https://github.com/anthropics/defending-code-reference-harness)

## Signal stats
- Total items processed: 159
- New (post-dedup): 158
- Clusters formed: ~95 (after CVE-ID grouping, URL dedup, fuzzy-title matching ≥85 within 48h)
- Top 5 selected from: 95 candidate clusters
