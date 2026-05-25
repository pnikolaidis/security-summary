# Security Digest — 2026-05-25

## TL;DR
A critical SQL injection in Ghost CMS (CVE-2026-26980) is being actively exploited in a large-scale ClickFix social-engineering campaign, demanding immediate patching for site operators. North Korea's Lazarus Group has debuted a memory-only RAT called RemotePE targeting financial and crypto firms, leaving no disk artifacts for defenders to find. A coordinated supply-chain attack named TrapDoor has seeded over 34 credential-stealing packages across npm, PyPI, and Crates.io simultaneously. Risky Business News reports that automated tool Mythos has uncovered thousands of critical bugs across major codebases while Dutch police raided bulletproof hosting operators. Rounding out the day, Wireshark 4.6.6 ships a security fix that analysts should apply before opening untrusted capture files.

## 1. Ghost CMS SQL Injection (CVE-2026-26980) Exploited in Large-Scale ClickFix Campaign
**Why it matters:** Any Ghost-powered site that hasn't patched is an active vector for injecting malicious JavaScript at visitors, turning a CMS vulnerability into a user-targeting social-engineering platform.

A critical SQL injection flaw—CVE-2026-26980—in the Ghost content management system is being exploited at scale. Attackers inject malicious JavaScript into Ghost-powered sites via the vulnerability; visiting users are then presented with ClickFix-style fake error prompts that convince them to paste attacker-controlled commands into their own terminal. The campaign is described as large-scale, suggesting broad opportunistic exploitation across the Ghost install base rather than targeted attacks.

*Covered in: bleepingcomputer — 1 post across 1 source*
- [Ghost CMS SQL injection flaw exploited in large-scale ClickFix campaign](https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign)

## 2. Lazarus Group Deploys RemotePE Memory-Only RAT Against Financial and Crypto Firms
**Why it matters:** A disk-less implant from a state-sponsored North Korean group defeats most file-based detection and forensics, raising the bar significantly for defenders in targeted sectors.

North Korea's Lazarus Group has added a cross-platform, memory-only remote access tool called RemotePE to its arsenal. Fox-IT (NCC Group) documented an attack chain that uses two loaders—DPAPILoader and RemotePELoader—to decrypt and stage the final payload entirely in RAM, leaving no files on disk. Targeted organizations include financial institutions and cryptocurrency firms, consistent with Lazarus's long-running mandate to fund North Korean operations through digital-asset theft.

*Covered in: thehackernews — 1 post across 1 source*
- [Lazarus Deploys RemotePE Memory-Only RAT Against Financial and Crypto Firms](https://thehackernews.com/2026/05/lazarus-deploys-remotepe-memory-only.html)

## 3. TrapDoor: Coordinated Supply-Chain Attack Hits npm, PyPI, and Crates.io Simultaneously
**Why it matters:** Developers and CI/CD pipelines across all three major package ecosystems are at risk of silently installing credential-stealing malware in any dependency installed since May 22nd.

A coordinated campaign called TrapDoor has published more than 34 malicious packages spanning over 384 versions across npm, PyPI, and Crates.io. Activity began May 22, 2026, with waves of packages published from a cluster of actor-controlled accounts. The payloads target credentials, meaning build systems that automatically resolve and install packages are a primary infection vector alongside individual developers.

*Covered in: thehackernews — 1 post across 1 source*
- [TrapDoor Supply Chain Attack Spreads Credential-Stealing Malware via npm, PyPI, and CratesIO](https://thehackernews.com/2026/05/trapdoor-supply-chain-attack-spreads.html)

## 4. Mythos Discovers Thousands of Critical Bugs; Dutch Police Raid Bulletproof Hosters
**Why it matters:** AI-scale automated vulnerability research signals an accelerating pace of CVE production, while Dutch law-enforcement raids against bulletproof hosting degrade the infrastructure criminal groups depend on for resilience.

Risky Business News reports that Mythos, an automated vulnerability research tool, has surfaced thousands of critical bugs across major codebases—a milestone in AI-assisted bug discovery that presages a wave of disclosures and patches in coming weeks. Separately, GitHub is rolling out new npm security features aimed at combating supply-chain attacks like TrapDoor. And Dutch authorities have raided bulletproof hosting providers in the Netherlands; such operators rent no-questions-asked infrastructure to ransomware groups, phishing platforms, and botnet operators.

*Covered in: risky_business_news — 1 post across 1 source*
- [Risky Bulletin: Mythos found thousands of critical bugs](https://news.risky.biz/risky-bulletin-mythos-found-thousands-of-critical-bugs)

## 5. Wireshark 4.6.6 Released with Security Fix
**Why it matters:** Security analysts who open untrusted packet capture files should update before doing so—Wireshark vulnerabilities are typically triggered by crafted capture files.

Wireshark 4.6.6 fixes one security vulnerability alongside eleven other bugs. Details on the specific vulnerability's severity are sparse in initial reporting, but Wireshark is ubiquitous among security and network operations teams and is commonly used to analyze capture files received from external parties during incident response and threat-intelligence sharing.

*Covered in: sans_isc — 1 post across 1 source*
- [Wireshark 4.6.6 Released, (Sun, May 24th)](https://isc.sans.edu/diary/rss/33010)

## Signal stats
- Total items processed: 10
- New (post-dedup): 10
- Clusters formed: 5 (5 items filtered: 3 off-topic HN, 2 Dark Reading event listings)
- Top 5 selected from: 5 candidate clusters
