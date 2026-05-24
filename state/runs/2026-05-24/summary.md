# Security Digest — 2026-05-24

## TL;DR
Three stories surfaced today. Ghost CMS (CVE-2026-26980) is under active large-scale exploitation via a SQL injection flaw being used to inject ClickFix malware payloads into visitor browsers — Ghost site operators should patch immediately. Wireshark 4.6.6 shipped hours ago, patching a vulnerability in a tool that routinely handles untrusted network traffic. And a supply chain attack against Laravel Lang localization packages abused GitHub version tagging to deliver credential-stealing malware through Composer — PHP/Laravel developers should audit and rotate.

## 1. Ghost CMS SQL Injection (CVE-2026-26980) Actively Exploited in Large-Scale ClickFix Campaign
**Why it matters:** Any public-facing Ghost CMS installation is exposed to active exploitation that can compromise site visitors by injecting malicious JavaScript into page loads.

A critical SQL injection vulnerability in Ghost CMS, tracked as CVE-2026-26980, is being weaponized at scale. Attackers are exploiting the flaw to inject malicious JavaScript into Ghost-powered sites, which then triggers the ClickFix social-engineering attack flow — tricking site visitors into running malware on their own machines. The campaign is described as large-scale and appears automated rather than targeted, meaning every unpatched Ghost instance is a potential infection vector for its audience. Ghost administrators should apply the patch or take instances offline until remediation is complete.

*Covered in: BleepingComputer — 1 post across 1 source*
- [Ghost CMS SQL injection flaw exploited in large-scale ClickFix campaign](https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign)

## 2. Wireshark 4.6.6 Released — Patches One Vulnerability, Fixes 11 Bugs
**Why it matters:** Wireshark is used everywhere to analyze potentially hostile network traffic; a vulnerability in the analyzer itself can flip the tool from defensive asset to attack surface.

Wireshark 4.6.6 was released today, patching one security vulnerability alongside eleven bug fixes. Full CVE details for the vulnerability were not yet available at collection time. Because Wireshark frequently processes untrusted packet captures — including traffic from adversary-controlled hosts — any exploitable parsing flaw carries real risk in security operations and incident response environments. Update via your package manager or directly from the Wireshark download page.

*Covered in: SANS ISC — 1 post across 1 source*
- [Wireshark 4.6.6 Released, (Sun, May 24th)](https://isc.sans.edu/diary/rss/33010)

## 3. Laravel Lang Packages Hijacked — Supply Chain Attack Delivers Credential-Stealing Malware
**Why it matters:** PHP developers who installed the compromised Laravel Lang package versions may have silently had credentials exfiltrated from their development machines or CI pipelines.

Attackers compromised the widely used Laravel Lang localization packages in a sophisticated supply chain attack, exploiting GitHub's version tagging mechanism to push malicious releases into the Composer package ecosystem. The tampered packages deployed credential-stealing malware that harvested secrets from developer environments. Laravel Lang packages are used by a large share of the PHP/Laravel developer community, making the blast radius significant. Affected developers should: check Composer lockfiles for unexpected version pins, rotate any credentials (API keys, database passwords, cloud tokens) that existed in affected environments, and update to verified clean package versions.

*Covered in: BleepingComputer — 1 post across 1 source*
- [Laravel Lang packages hijacked to deploy credential-stealing malware](https://www.bleepingcomputer.com/news/security/laravel-lang-packages-hijacked-to-deploy-credential-stealing-malware)

## Signal stats
- Total items processed: 13
- New (post-dedup): 13
- Clusters formed: 3 (security-relevant only; 2 event-calendar listings and 8 off-topic HN items excluded before scoring)
- Top 5 selected from: 3 candidate clusters (fewer than 5 security stories found today)
