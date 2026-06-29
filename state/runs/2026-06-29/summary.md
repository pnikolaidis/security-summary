# Security Digest — 2026-06-29

## TL;DR
Russia's Gamaredon APT has published 35 new spear-phishing campaigns targeting Ukraine, now abusing cloud services for command-and-control — fresh ESET research with direct relevance to anyone carrying endpoint or cloud security. Microsoft took down 119 Edge extensions that used steganography to hide credential-stealing payloads, under the name "StegoAd." Japan's KDDI confirmed a breach exposing 14.2 million email logins across six ISPs — a strong email-security opener for similar accounts. A public proof-of-concept just dropped for CVE-2026-55200 in libssh2 (CVSS 9.2), a no-auth RCE reachable from any malicious SSH server. And a new Linux kernel variant called DirtyClone lets unprivileged local users manipulate the page cache to gain root — important for any customers running Linux workloads.

---

## 1. Gamaredon APT Expands Ukraine Attacks with New Malware and Cloud Abuse

**Why it matters:** Russia's Gamaredon group is actively adding new malware and pivoting to legitimate cloud services for C2 — a vector that bypasses many perimeter controls, and ESET's fresh research gives channel partners a compelling proof point for network and endpoint conversations.

A new ESET report documents 35 distinct Gamaredon spear-phishing campaigns through 2025 and into 2026, each introducing new tooling. The group, which is assessed to operate from Russian-occupied Crimea, is now abusing cloud platforms to host command-and-control infrastructure — making detections harder for signature-based tools and traditional firewall policies. Targets remain Ukrainian government, military, and allied organizations, though ESET notes spillover into Western organizations with Ukrainian business ties. For MSSPs and VARs: this is the "Russia is still active" brief with fresh IOCs and a cloud-evasion angle that maps directly to SSE/ZTNA and MDR upsell conversations.

*Covered in: The Hacker News — 1 post*
- [Gamaredon Expands Ukraine Attacks with New Malware and Cloud Service Abuse](https://thehackernews.com/2026/06/gamaredon-expands-ukraine-attacks-with.html)

---

## 2. Microsoft Dismantles StegoAd: 119 Malicious Edge Extensions Using Steganography

**Why it matters:** A sophisticated, five-year-old credential-theft and ad-fraud operation was hiding payloads inside ordinary image and font files before waking up days after install — a method that evaded most detection for years, and Microsoft only caught it now.

Microsoft pulled 119 extensions from the Edge Add-ons store, all tied to a single threat actor operating since at least 2021 under the campaign name "StegoAd." The malware hid its code inside steganographically encoded images and fonts embedded in the extension package, activating days after install to steal credentials and run large-scale ad fraud. The delay-before-activation technique was specifically designed to survive initial behavioral analysis. For channel partners: this reinforces why browser extension governance and behavioral EDR matter — this is a concrete case where traditional AV and even sandboxing missed it for years. Proofpoint, Microsoft Defender, and ESET-aligned conversations all benefit.

*Covered in: The Hacker News, Risky Business News — 2 posts across 2 sources*
- [Microsoft Removes 119 Edge Extensions That Hid Malware in Images and Fonts](https://thehackernews.com/2026/06/microsoft-removes-119-edge-extensions.html)
- [Risky Bulletin: Microsoft disrupts StegoAd operation](https://news.risky.biz/risky-bulletin-microsoft-disrupts-stegoad-operation)

---

## 3. KDDI Data Breach: Up to 14.2 Million Email Logins Exposed Across Six ISPs

**Why it matters:** Japan's largest telecom confirmed a breach of a shared email system used by five ISPs, exposing up to 14.2 million credentials — a named-brand incident that gives resellers a natural lead-in for email security and identity protection pitches at carrier-scale accounts.

KDDI Corporation disclosed that threat actors accessed an email infrastructure platform shared with five other Japanese internet service providers, resulting in the potential compromise of up to 14.2 million email login credentials. The breach underscores the cascading risk when shared infrastructure fails — a single platform compromise rolls up to six operators and millions of end users. For the channel: this is a Proofpoint, Okta, and CyberArk conversation starter. Ask your telecom and infrastructure accounts: "If your email backend were compromised, how quickly would you detect it and contain blast radius across your downstream?"

*Covered in: BleepingComputer — 1 post*
- [Data breach exposes up to 14.2 million email logins at six ISPs](https://www.bleepingcomputer.com/news/security/data-breach-exposes-up-to-142-million-email-logins-at-six-isps)

---

## 4. Public PoC for Critical libssh2 Flaw CVE-2026-55200 (CVSS 9.2) — No Auth Required

**Why it matters:** A public exploit proof-of-concept is now available for a memory-corruption bug in libssh2 that lets any malicious SSH server compromise a connecting client with no credentials and no user interaction — affecting every version up to 1.11.1.

CVE-2026-55200 is a critical client-side vulnerability in libssh2, the widely embedded SSH library used by cURL, Python's Paramiko-like implementations, and hundreds of automation tools and appliances. A malicious or compromised SSH server can trigger memory corruption on a connecting client, with potential for full code execution. The CVSS 4.0 score is 9.2, and a public PoC is now circulating. Because libssh2 is bundled inside many appliances and SaaS backends rather than patched via OS updates, the exposure window will be long. For the channel: this is a patch-verification and asset-inventory conversation — ask customers how they track which internal tools or embedded devices are calling SSH and whether they can confirm libssh2 version.

*Covered in: The Hacker News — 1 post*
- [Public PoC Released for Critical libssh2 CVE-2026-55200 Client-Side SSH Flaw](https://thehackernews.com/2026/06/public-poc-released-for-critical.html)

---

## 5. 'DirtyClone' Linux Kernel Vulnerability Grants Unprivileged Users Root Access

**Why it matters:** A variant of the DirtyFrag technique lets any unprivileged local user manipulate the Linux page cache to escalate to root — a serious threat for any customer running shared Linux infrastructure, containers, or cloud VMs.

SecurityWeek reports DirtyClone, a newly disclosed variant of the DirtyFrag kernel exploit class, allows unprivileged local users to corrupt the Linux page cache and gain root privileges. No CVE has been assigned yet and the CVSS score is pending, but the impact is clear: any multi-tenant environment or shared-hosting setup with untrusted local users is at risk. Container escapes are a natural next step. For the channel: this is a Wiz, Palo Alto Prisma Cloud, and CrowdStrike Falcon conversation. Ask cloud-native accounts whether their runtime protection covers page-cache manipulation and whether their kernel versions are patched for DirtyFrag-family issues.

*Covered in: SecurityWeek — 1 post*
- ['DirtyClone' Linux Kernel Vulnerability Leads to Root Access](https://www.securityweek.com/dirtyclone-linux-kernel-vulnerability-leads-to-root-access)

---

## Signal stats
- Total items processed: 35
- New (post-dedup): 35
- Clusters formed: 9 (after NVD-only and off-topic filters)
- Top 5 selected from: 9 candidate clusters
- NVD-only clusters dropped: 5 (Tenda ×5, Wavlink, D-Link, libzypp, Edimax ×3 — 14 NVD items combined)
- Off-topic/low-signal dropped: 6 HN items + 3 news items
