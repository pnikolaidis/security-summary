# Security Digest — 2026-05-22

## TL;DR
CISA added two actively exploited flaws — a CVSS 9.4 Langflow vulnerability and a CVSS 9.8 Trend Micro Apex One remote code execution bug — to its Known Exploited Vulnerabilities catalog, pressing organizations to patch immediately. Cisco simultaneously disclosed a CVSS 10.0 authentication bypass in Secure Workload, while Ubiquiti patched three separate CVSS 10.0 flaws in UniFi OS devices. On the law enforcement front, Canadian and U.S. authorities arrested the alleged operator of the Kimwolf DDoS-for-hire botnet, which had enlisted nearly two million IoT devices. Rounding out the day, China's Webworm APT was found routing espionage traffic through Discord and Microsoft Graph to quietly compromise European government networks.

## 1. CISA Adds Actively Exploited Langflow and Trend Micro Apex One Flaws to KEV
**Why it matters:** Attackers are actively exploiting a CVSS 9.4 Langflow flaw and a CVSS 9.8 Apex One remote code execution vulnerability, giving organizations a regulatory deadline to patch.

CISA added two vulnerabilities to its Known Exploited Vulnerabilities catalog Thursday: CVE-2025-34291, an origin validation error in the Langflow AI workflow builder (CVSS 9.4), and a companion flaw in Trend Micro Apex One's management console that allows an unauthenticated remote attacker to upload malicious code and execute arbitrary commands (CVE-2025-71210, CVSS 9.8). Both carry confirmed evidence of active in-the-wild exploitation. Langflow is widely used by enterprises building LLM-powered applications, making this a notable risk vector for AI development pipelines. Trend Micro notes that SaaS-hosted Apex One instances have already received server-side mitigations, but on-premise customers must patch immediately.

*Covered in: thehackernews, nvd — 3 posts across 2 sources*
- [CISA Adds Exploited Langflow and Trend Micro Apex One Vulnerabilities to KEV](https://thehackernews.com/2026/05/cisa-adds-exploited-langflow-and-trend.html)
- [CVE-2025-71210 (CRITICAL) — Trend Micro Apex One management console RCE](https://nvd.nist.gov/vuln/detail/CVE-2025-71210)
- [CVE-2025-71211 (CRITICAL) — Trend Micro Apex One management console RCE (variant)](https://nvd.nist.gov/vuln/detail/CVE-2025-71211)

## 2. Cisco Patches CVSS 10.0 Flaw in Secure Workload REST API
**Why it matters:** An unauthenticated remote attacker can read sensitive data from any exposed Cisco Secure Workload deployment — the highest possible severity score, with no available workaround other than patching.

Cisco disclosed CVE-2026-20223 (CVSS 10.0), a critical vulnerability stemming from insufficient validation and authentication on Secure Workload's REST API endpoints. Any attacker who can reach the API over the network can extract sensitive data without credentials. Cisco has released patched software and urges immediate upgrade; there is no workaround. The flaw affects the on-premise deployment of Secure Workload, a micro-segmentation platform used in large enterprise and government data centers where lateral movement prevention is a core security control.

*Covered in: bleepingcomputer, thehackernews — 2 posts across 2 sources*
- [Max severity Cisco Secure Workload flaw gives Site Admin privileges](https://www.bleepingcomputer.com/news/security/cisco-max-severity-secure-workload-flaw-gives-hackers-site-admin-privileges)
- [Cisco Patches CVSS 10.0 Secure Workload REST API Flaw Enabling Data Access](https://thehackernews.com/2026/05/cisco-patches-cvss-100-secure-workload.html)

## 3. Ubiquiti Discloses Multiple CVSS 10.0 Vulnerabilities in UniFi OS
**Why it matters:** Three separate maximum-severity bugs let any network-adjacent attacker take unauthorized control of, execute commands on, or read arbitrary files from UniFi OS devices — hardware deployed in millions of homes, offices, and enterprise sites.

Ubiquiti disclosed five CVEs in UniFi OS this week, three scoring CVSS 10.0: CVE-2026-34908 (improper access control enabling unauthorized system changes), CVE-2026-34909 (path traversal allowing file access leading to account compromise), and CVE-2026-34910 (input validation error enabling command injection). A fourth, CVE-2026-33000, scores CVSS 9.1 and requires higher privileges but also achieves command injection. A fifth, CVE-2026-34911 (CVSS 7.7), allows low-privilege file reads that could expose sensitive configuration data. UniFi equipment is ubiquitous in SMBs, multi-tenant residential buildings, and enterprise branch sites; firmware updates should be treated as urgent.

*Covered in: nvd — 5 posts across 1 source*
- [CVE-2026-34908 (CRITICAL) — UniFi OS Improper Access Control](https://nvd.nist.gov/vuln/detail/CVE-2026-34908)
- [CVE-2026-34909 (CRITICAL) — UniFi OS Path Traversal](https://nvd.nist.gov/vuln/detail/CVE-2026-34909)
- [CVE-2026-34910 (CRITICAL) — UniFi OS Command Injection](https://nvd.nist.gov/vuln/detail/CVE-2026-34910)
- [CVE-2026-33000 (CRITICAL) — UniFi OS Command Injection (high-privilege)](https://nvd.nist.gov/vuln/detail/CVE-2026-33000)
- [CVE-2026-34911 (HIGH) — UniFi OS Path Traversal (low-privilege)](https://nvd.nist.gov/vuln/detail/CVE-2026-34911)

## 4. Alleged Kimwolf DDoS Botnet Operator Arrested in U.S.–Canada Joint Action
**Why it matters:** A 23-year-old Canadian man allegedly enslaved nearly two million IoT devices for DDoS-for-hire and personally launched retaliatory attacks — including swatting — against the security journalist who named him publicly.

U.S. and Canadian authorities arrested Jacob Butler (alias "Dort"), 23, of Ottawa, in connection with operating the Kimwolf botnet — a variant of AISURU that amassed roughly two million enslaved IoT devices used for distributed denial-of-service-for-hire attacks over the past six months. KrebsOnSecurity had publicly identified Butler in February 2026, after which he allegedly launched retaliatory DDoS floods, doxing campaigns, and swatting attacks against Brian Krebs and a security researcher. Butler now faces criminal hacking charges in both the United States and Canada. The takedown removes a significant DDoS-for-hire capability and demonstrates active cross-border enforcement cooperation.

*Covered in: krebs, bleepingcomputer, thehackernews — 3 posts across 3 sources*
- [Alleged Kimwolf Botmaster 'Dort' Arrested, Charged in U.S. and Canada](https://krebsonsecurity.com/2026/05/alleged-kimwolf-botmaster-dort-arrested-charged-in-u-s-and-canada)
- [US and Canada arrest and charge suspected Kimwolf botnet admin](https://www.bleepingcomputer.com/news/security/us-and-canada-arrest-and-charge-suspected-kimwolf-botnet-admin)
- [Kimwolf DDoS Botnet Operator Arrested in Canada Over DDoS-for-Hire Attacks](https://thehackernews.com/2026/05/kimwolf-ddos-botnet-operator-arrested.html)

## 5. China's Webworm APT Abuses Discord and Microsoft Graph to Target EU Governments
**Why it matters:** A China-linked threat actor is routing command-and-control traffic through widely trusted cloud platforms to blend into legitimate enterprise traffic while conducting espionage against European government networks.

Dark Reading reports that Webworm, a Chinese advanced persistent threat group, is running espionage campaigns against European government entities by tunneling command-and-control communications through Discord and the Microsoft Graph API — platforms almost universally permitted by enterprise firewalls and rarely scrutinized. The technique lets malicious traffic look indistinguishable from normal business use of these services. Webworm additionally uses SOCKS proxy tools including SoftEther VPN for further obfuscation. This approach follows a growing pattern among state-sponsored actors of living off trusted cloud infrastructure to evade network-based detection.

*Covered in: darkreading — 1 post across 1 source*
- [China's Webworm Uses Discord, Microsoft Graphs to Hack EU Govts.](https://www.darkreading.com/endpoint-security/chinas-webworm-discord-microsoft-graphs)

## Signal stats
- Total items processed: 83
- New (post-dedup): 83
- Clusters formed: ~28
- Top 5 selected from: 28 candidate clusters
