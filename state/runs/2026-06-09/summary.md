# Security Digest — 2026-06-09

## TL;DR
Today's digest is led by two actively exploited zero-days: a CVSS 9.3 critical flaw in Check Point VPN gateways now tied to Qilin ransomware operations (CISA 3-day mandate issued), and Google's fifth Chrome zero-day patch of 2026 — an actively exploited V8 memory corruption. Apache HTTP Server received six new CVEs including a CVSS 9.8 critical buffer underwrite. On the threat-actor front, the "Hades" supply chain campaign poisoned 19 PyPI packages with a Bun-based credential stealer targeting scientific computing projects. And Meta filed a contempt-of-court motion after catching NSO Group launching new WhatsApp spyware attacks in direct defiance of a federal court injunction.

## 1. Check Point VPN Zero-Day (CVE-2026-50751) Exploited by Qilin Ransomware — CISA 3-Day Mandate
**Why it matters:** A critical logic flaw in Check Point Remote Access and Mobile Access VPN allows attackers to bypass certificate-based authentication in IKEv1 setups, and the Qilin ransomware gang has been exploiting it since early May — making this a drop-everything patch for any organization using Check Point remote access.

CISA added CVE-2026-50751 (CVSS 9.3) to the Known Exploited Vulnerabilities catalog and gave federal agencies three days to apply patches. Check Point confirmed the flaw resides in certificate validation logic for deprecated IKEv1 configurations, allowing authentication bypass without valid credentials. Qilin — an active ransomware-as-a-service group — has been documented exploiting this vector for initial access, lateral movement, and data exfiltration across enterprise targets since at least the first week of May.

*Covered in: BleepingComputer, The Hacker News, SecurityWeek, Dark Reading, NVD — 6 posts across 5 sources*
- [CISA gives feds 3 days to patch Check Point VPN bug exploited as zero-day](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-check-point-flaw-exploited-by-ransomware-gangs)
- [Check Point links VPN zero-day attacks to Qilin ransomware gang](https://www.bleepingcomputer.com/news/security/check-point-links-vpn-zero-day-attacks-to-qilin-ransomware-gang)
- [Critical Check Point VPN Flaw Exploited to Bypass Passwords in IKEv1 Setups](https://thehackernews.com/2026/06/critical-check-point-vpn-flaw-exploited.html)
- [Check Point VPN Zero-Day Exploited in Qilin Ransomware Attacks](https://www.securityweek.com/check-point-vpn-zero-day-exploited-in-qilin-ransomware-attacks)
- [Check Point VPN Flaw Exploited Since Early May](https://www.darkreading.com/vulnerabilities-threats/check-point-vpn-flaw-exploited-early-may)
- [CVE-2026-50751 (NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-50751)

## 2. Google Chrome Zero-Day #5 (CVE-2026-11645) Actively Exploited in the Wild
**Why it matters:** Google has patched its fifth actively exploited Chrome zero-day of 2026, meaning threat actors have leveraged a Chrome vulnerability in real attacks roughly every five to seven weeks this year — a sustained pace that underscores Chrome's status as a premier initial-access target.

CVE-2026-11645 is an out-of-bounds read and write in V8, Chrome's JavaScript engine, observed exploited in the wild prior to the patch. The Chrome 149.0.7827.103 update bundles 15 additional security fixes including three CVSS 9.6 critical use-after-free vulnerabilities in Gamepad (CVE-2026-11634), Printing (CVE-2026-11638), and Network (CVE-2026-11651) components. Organizations relying on Chrome or any Chromium-based browser — including Microsoft Edge — should treat this update as urgent.

*Covered in: BleepingComputer, SecurityWeek, NVD — 16 posts across 3 sources*
- [Google patches new Chrome zero-day flaw exploited in the wild](https://www.bleepingcomputer.com/news/security/google-patches-fifth-chrome-zero-day-bug-exploited-in-attacks-this-year)
- [Google Patches 5th Chrome Zero-Day Exploited in 2026](https://www.securityweek.com/google-patches-5th-chrome-zero-day-exploited-in-2026)
- [CVE-2026-11645 (NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-11645)
- [CVE-2026-11651 — CVSS 9.6 Critical (NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-11651)

## 3. Apache HTTP Server: Six New CVEs Including CVSS 9.8 Critical Buffer Underwrite
**Why it matters:** Six vulnerabilities landed in NVD for Apache HTTP Server today, headlined by a CVSS 9.8 critical buffer underwrite (CVE-2026-44631) that could allow unauthenticated remote code execution on one of the most widely deployed web server platforms in the world.

CVE-2026-44631 is triggered by a crafted HTTP request and causes a buffer underwrite condition; paired with CVE-2026-34355/34356 (buffer overflows in mod_proxy_html), CVE-2026-42536 (heap-based buffer overflow), CVE-2026-44185 (buffer over-read via outbound proxy), and CVE-2026-48913 (use-after-free in mod_http2), the batch represents a substantial patching event. Affected versions include Apache httpd 2.4.67 and earlier. Administrators should check vendor advisories for the exact patched release and prioritize internet-facing instances.

*Covered in: NVD — 6 posts across 1 source*
- [CVE-2026-44631 (CRITICAL, CVSS 9.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-44631)
- [CVE-2026-34355](https://nvd.nist.gov/vuln/detail/CVE-2026-34355)
- [CVE-2026-34356](https://nvd.nist.gov/vuln/detail/CVE-2026-34356)
- [CVE-2026-42536](https://nvd.nist.gov/vuln/detail/CVE-2026-42536)
- [CVE-2026-44185](https://nvd.nist.gov/vuln/detail/CVE-2026-44185)
- [CVE-2026-48913](https://nvd.nist.gov/vuln/detail/CVE-2026-48913)

## 4. Hades Campaign Poisons 19 PyPI Packages to Harvest Credentials
**Why it matters:** The "Hades" supply chain campaign — an evolution of the earlier Shai-Hulud technique — trojanized 19 science-focused PyPI packages to deploy a Bun-based credential stealer, placing developers, researchers, and data scientists in the crosshairs.

Attackers modified 19 PyPI packages targeting scientific computing workflows with code that auto-executes on `pip install`, silently downloads the Bun JavaScript runtime, and exfiltrates stored credentials and secrets. The scientific computing focus suggests deliberate targeting of research institutions whose dependency hygiene may be less rigorous than enterprise software teams. PyPI has removed the affected packages; developers should audit pip install logs for the past two weeks and check for unexpected Bun binaries. Separate SANS ISC reporting links this activity to the broader "TeamPCP" supply chain cluster active through June 7.

*Covered in: BleepingComputer, The Hacker News, Dark Reading, SANS ISC — 4 posts across 4 sources*
- [New Shai-Hulud attack trojanizes 19 science-focused PyPI packages](https://www.bleepingcomputer.com/news/security/new-shai-hulud-attack-trojanizes-19-science-focused-pypi-packages)
- ['Hades' Campaign Against PyPI Puts New Spin on Shai-Hulud](https://www.darkreading.com/application-security/hades-campaign-pypi-shai-hulud)
- [Hades PyPI Attack: 19 Packages Poisoned to Auto-Run Bun Credential Stealer](https://thehackernews.com/2026/06/hades-pypi-attack-19-packages-poisoned.html)
- [TeamPCP Supply Chain Campaign: Activity Through 2026-06-07](https://isc.sans.edu/diary/rss/33060)

## 5. NSO Group Caught Defying Court Order with New WhatsApp Spyware Campaign
**Why it matters:** Meta caught NSO Group launching new WhatsApp phishing attacks in direct violation of a federal court injunction and has filed a contempt-of-court motion — the highest-stakes legal escalation yet in the campaign to hold commercial spyware vendors accountable.

WhatsApp's security team discovered and disrupted a new NSO Group campaign deploying phishing infrastructure designed to install surveillance software on targeted users' devices. NSO is subject to a court injunction from Meta's 2019 lawsuit barring it from accessing WhatsApp's systems, making this a brazen violation. Meta's contempt filing asks the court to impose sanctions; if granted, it could significantly constrain NSO's operational capacity and signal to other commercial spyware vendors that civil litigation has real teeth.

*Covered in: BleepingComputer, The Hacker News, SecurityWeek — 3 posts across 3 sources*
- [WhatsApp says it disrupted new NSO spyware phishing attacks](https://www.bleepingcomputer.com/news/security/whatsapp-says-it-disrupted-new-nso-spyware-phishing-attacks)
- [Meta Blocks NSO Group's New WhatsApp Phishing Attack, Files Contempt Order](https://thehackernews.com/2026/06/meta-blocks-nso-groups-new-whatsapp.html)
- [WhatsApp Catches Spyware Firm NSO Defying No-Hacking Court Order](https://www.securityweek.com/whatsapp-catches-spyware-firm-nso-defying-no-hacking-court-order)

## Signal stats
- Total items processed: 116
- New (post-dedup): 115
- Clusters formed: 28
- Top 5 selected from: 18 candidate clusters (score ≥ 0.5)
