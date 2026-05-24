# Security Digest — 2026-05-24

## TL;DR
A critical SQL injection flaw in Ghost CMS (CVE-2026-26980) is being actively exploited in a large-scale ClickFix campaign that injects malicious JavaScript into sites. Separately, Laravel's widely-used Lang localization packages were hijacked in a supply chain attack that distributed credential-stealing malware via Composer. On the patching front, Wireshark 4.6.6 landed today fixing one vulnerability and eleven bugs — a routine but worthwhile update for anyone running packet capture infrastructure.

## 1. Ghost CMS SQL Injection Actively Exploited in ClickFix Campaign (CVE-2026-26980)
**Why it matters:** Any public-facing Ghost CMS installation is a potential attack vector for drive-by JavaScript injection leading to credential theft or malware delivery on end-user machines.

A critical SQL injection vulnerability (CVE-2026-26980) in Ghost CMS is being exploited at scale, with attackers injecting malicious JavaScript that triggers ClickFix attack flows — social-engineering prompts that trick users into running attacker-controlled code. The campaign is broad, suggesting automated scanning and exploitation. Ghost site operators should patch immediately and audit for injected scripts in their themes and content.

*Covered in: bleepingcomputer — 1 post across 1 source*
- [Ghost CMS SQL injection flaw exploited in large-scale ClickFix campaign](https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign)

## 2. Wireshark 4.6.6 Released — Patches One Vulnerability
**Why it matters:** Wireshark is ubiquitous in security and network operations; unpatched versions on analyst workstations can be exploited via crafted capture files.

Wireshark 4.6.6 was released today, addressing one security vulnerability alongside eleven bug fixes. Details on the specific CVE are sparse in the release announcement, but the SANS Internet Storm Center flagged it as worth prompt attention. If you open untrusted PCAP files as part of your workflow, update now.

*Covered in: sans_isc — 1 post across 1 source*
- [Wireshark 4.6.6 Released, (Sun, May 24th)](https://isc.sans.edu/diary/rss/33010)

## 3. Laravel Lang Packages Hijacked — Supply Chain Credential Theft
**Why it matters:** PHP developers using Laravel localization packages via Composer may have silently pulled malicious code, putting their development credentials and downstream application secrets at risk.

Attackers abused GitHub version tags to inject a sophisticated credential-stealing malware payload into the Laravel Lang localization packages — popular Composer dependencies with millions of installations. The attack used tag manipulation rather than a direct code commit, making it harder to detect in standard code review. Any Laravel project that pulled updated Lang packages recently should audit its environment and rotate credentials.

*Covered in: bleepingcomputer — 1 post across 1 source*
- [Laravel Lang packages hijacked to deploy credential-stealing malware](https://www.bleepingcomputer.com/news/security/laravel-lang-packages-hijacked-to-deploy-credential-stealing-malware)

## Signal stats
- Total items processed: 14
- New (post-dedup): 14
- Clusters formed: 3 security-relevant clusters (11 items filtered: 2 event announcements, 9 off-topic HN stories)
- Top 3 selected from: 3 candidate clusters (fewer than 5 viable security stories today)
