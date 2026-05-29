# Security Digest — 2026-05-29

## TL;DR
Oracle dropped a massive critical patch update with over 20 CVEs across E-Business Suite and REST Data Services — including a CVSS 10.0 unauthenticated takeover. GitHub's removal of a researcher's account after they published unpatched Windows zero-days sparked a high-profile dispute about vulnerability disclosure norms. An unpatched zero-day in Gogs (CVSS 9.4) lets any authenticated user run arbitrary code on exposed instances. Attackers are actively exploiting a FortiClient EMS authentication bypass to deploy a novel credential stealer called EKZ. Supply chain attackers hit the NuGet and npm ecosystems, targeting Brazilian banking systems and cloud credentials.

## 1. Oracle Critical Patch Update — Up to CVSS 10.0 Across E-Business Suite and REST Data Services

**Why it matters:** Multiple Oracle products used by enterprises worldwide are vulnerable to unauthenticated remote takeover; the highest-rated flaw (CVE-2026-46840, CVSS 10.0) requires no authentication and achieves full system compromise with scope change across Oracle REST Data Services.

Oracle's latest Critical Patch Update includes more than 20 high- and critical-severity CVEs spanning Oracle E-Business Suite, Oracle REST Data Services (ORDS), and Oracle Database Server. The most severe, CVE-2026-46840 (CVSS 10.0), allows an unauthenticated attacker with network access via HTTPS to fully take over Oracle REST Data Services, with attacks spilling across the scope boundary into dependent products. Several other ORDS flaws rate 9.9, including CVE-2026-46839 and CVE-2026-46775, which require only low-privilege network access. Oracle Hospitality OPERA 5 (CVE-2026-34311, CVSS 9.8) and Oracle iAssets (CVE-2026-46822, CVSS 9.9) round out the critical set — both allowing unauthenticated HTTP-based takeover.

Patching is urgent for any organization running Oracle E-Business Suite 12.2.x, ORDS 24.2–26.1, or Oracle Database Server 23.4–23.26. The scope-change flag on several ORDS flaws means a compromised ORDS instance can pivot to downstream Oracle infrastructure.

*Covered in: nvd — 22 CVEs*
- [CVE-2026-46840 (CVSS 10.0) — Oracle REST Data Services unauthenticated takeover](https://nvd.nist.gov/vuln/detail/CVE-2026-46840)
- [CVE-2026-46822 (CVSS 9.9) — Oracle iAssets low-priv takeover via scope change](https://nvd.nist.gov/vuln/detail/CVE-2026-46822)
- [CVE-2026-46839 (CVSS 9.9) — Oracle ORDS low-priv takeover via scope change](https://nvd.nist.gov/vuln/detail/CVE-2026-46839)
- [CVE-2026-34311 (CVSS 9.8) — Oracle Hospitality OPERA 5 unauthenticated HTTP takeover](https://nvd.nist.gov/vuln/detail/CVE-2026-34311)
- [CVE-2026-46833 (CVSS 9.0) — Oracle Database Server Net Service TLS takeover](https://nvd.nist.gov/vuln/detail/CVE-2026-46833)

## 2. GitHub Bans Security Researcher Over Windows Zero-Days — Disclosure War Erupts

**Why it matters:** Microsoft's removal of a researcher's GitHub account after they published unpatched Windows exploits reignited a fractious debate about who controls the timeline for vulnerability disclosure, with hundreds of comments on Hacker News and a sharp public counter-essay calling Microsoft's disclosure posture a "dumpster fire."

A researcher going by Chaotic Eclipse (aka Nightmare-Eclipse) disclosed multiple unpatched zero-day vulnerabilities in Windows and had their GitHub account removed shortly afterward. Microsoft publicly advocated for Coordinated Vulnerability Disclosure (CVD), arguing researchers should give vendors time to patch before going public. Critics responded that Microsoft routinely misses deadlines, dismisses low-severity reports, and retaliates against researchers — pointing to a history of contentious interactions with external bug hunters. The HN thread "GitHub bans security researcher who posted zero-day Windows exploits" reached over 500 engagement points with 188 comments, making it the most-discussed security story on the platform this cycle.

The removal of a researcher's account from GitHub (owned by Microsoft) drew particular criticism, as it was seen as using platform power to suppress security disclosures rather than fix the underlying vulnerabilities.

*Covered in: hackernews (×2), thehackernews — 3 posts across 2 sources*
- [GitHub bans security researcher who posted zero-day Windows exploits (Tom's Hardware via HN)](https://www.tomshardware.com/tech-industry/cyber-security/microsofts-github-bans-security-researcher-who-posted-zero-day-windows-exploits-because-company-ruined-their-life-expert-claims-action-is-vindictive-and-promises-further-retaliation)
- [Microsoft's stance on zero day exploits is a dumpster fire of their own making (DoublePulsar via HN)](https://doublepulsar.com/microsofts-stance-on-zero-day-exploits-is-a-dumpster-fire-of-their-own-making-0946117940a4)
- [Microsoft Slams Public Zero-Day Disclosures Amid GitHub Researcher Account Removal (The Hacker News)](https://thehackernews.com/2026/05/microsoft-slams-public-zero-day.html)

## 3. Unpatched Gogs Zero-Day — Authenticated Users Get Full RCE (CVSS 9.4)

**Why it matters:** Any authenticated user on a public-facing Gogs instance — no special privilege required — can achieve remote code execution right now, with no patch available.

Rapid7 disclosed a critical RCE vulnerability in Gogs, a popular open-source self-hosted Git service with broad adoption among teams that don't want to run GitLab or Gitea. Rated CVSS 9.4, the flaw requires only an authenticated session — not admin rights — to execute arbitrary code on the server. There is currently no CVE assigned and no patch available from the Gogs project, making this a true zero-day. Both BleepingComputer and The Hacker News reported independently on the same day, confirming its significance. Administrators are advised to restrict network access to Gogs instances or require stronger authentication controls until a fix lands.

*Covered in: bleepingcomputer, thehackernews — 2 posts across 2 sources*
- [New Gogs zero-day flaw lets hackers get remote code execution (BleepingComputer)](https://www.bleepingcomputer.com/news/security/new-gogs-zero-day-flaw-lets-hackers-get-remote-code-execution)
- [Critical Gogs RCE Vulnerability Lets Any Authenticated User Execute Arbitrary Code (The Hacker News)](https://thehackernews.com/2026/05/critical-gogs-rce-vulnerability-lets.html)

## 4. Attackers Exploit FortiClient EMS Auth-Bypass to Deploy Novel Credential Stealer

**Why it matters:** CVE-2026-35616, an authentication bypass in FortiClient Enterprise Management Server, is being actively weaponized to push a previously undocumented credential stealer called EKZ across managed enterprise endpoints.

Arctic Wolf and other researchers confirmed that threat actors are exploiting CVE-2026-35616 — a now-patched authentication bypass in FortiClient EMS — to deliver EKZ, an undocumented infostealer disguised as a legitimate Fortinet endpoint binary. The attack abuses the trusted endpoint management infrastructure itself to push malware to all connected managed devices, multiplying the blast radius far beyond a single compromised machine. Organizations running FortiClient EMS deployments that have not applied the latest patches should treat this as urgent; the campaign specifically exploits the trusted relationship between EMS and its managed fleet.

*Covered in: bleepingcomputer, thehackernews — 2 posts across 2 sources*
- [Hackers exploit FortiClient EMS flaw to push infostealer malware (BleepingComputer)](https://www.bleepingcomputer.com/news/security/hackers-exploit-forticlient-ems-flaw-to-push-infostealer-malware)
- [Threat Actors Exploit Critical FortiClient EMS Flaw to Deploy Credential Stealer (The Hacker News)](https://thehackernews.com/2026/05/threat-actors-exploit-critical.html)

## 5. Supply Chain: Malicious NuGet Package Steals Banking Credentials; npm Packages Hit Cloud Secrets

**Why it matters:** Software supply chain attackers are targeting both the .NET and JavaScript ecosystems simultaneously — one campaign harvesting PFX certificates from Brazilian banking SDK users, another siphoning cloud credentials from npm package consumers.

Socket researchers discovered that versions 2.0.0–2.0.4 of "Sicoob.Sdk" on NuGet are malicious — they impersonate the legitimate C# SDK for Sicoob, one of Brazil's largest cooperative banking networks, and exfiltrate PFX certificates and client IDs used for financial authentication. In parallel, The Hacker News also reported npm packages targeting cloud secrets from developer environments. The dual-ecosystem timing suggests coordinated or copycat supply chain activity. Developers using either ecosystem should audit recent package additions and verify publisher identity for any SDK touching financial or cloud infrastructure.

*Covered in: thehackernews — 1 post*
- [Malicious Sicoob NuGet Steals Banking Credentials as npm Packages Target Cloud Secrets (The Hacker News)](https://thehackernews.com/2026/05/malicious-sicoob-nuget-steals-banking.html)

## Signal stats
- Total items processed: 117
- New (post-dedup): 116
- Clusters formed: 28
- Top 5 selected from: 28 candidate clusters
