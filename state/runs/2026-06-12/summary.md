# Security Digest — 2026-06-12

## TL;DR
ShinyHunters is actively exploiting a critical Oracle PeopleSoft zero-day to steal data from universities and enterprises. CISA responded to a max-severity Ivanti Sentry exploit — now spreading to honeypots — by issuing Binding Operational Directive 26-04, mandating that federal agencies patch actively-exploited flaws within three days. A CVSS 10.0 command-injection flaw in MariaDB's Galera cluster replication puts database clusters at risk of full takeover. Ubiquiti has disclosed multiple CVSS 9.9 vulnerabilities in UniFi OS networking hardware. And Google shipped Chrome 149, patching 28 flaws — including 12 use-after-free bugs with critical Chromium severity ratings.

---

## 1. ShinyHunters Exploits Oracle PeopleSoft Zero-Day (CVE-2026-35273) to Breach Universities

**Why it matters:** An unauthenticated remote code execution zero-day in Oracle's widely-deployed PeopleSoft suite was actively exploited by ShinyHunters before Oracle even published an advisory — universities and enterprises are among the confirmed victims.

Oracle has mitigated CVE-2026-35273, a critical unauthenticated RCE vulnerability in PeopleSoft, after Google's Mandiant attributed active exploitation to ShinyHunters (tracked as UNC6240). The campaign ran from May 27 to June 9, hitting universities hardest. Oracle quietly shipped mitigations on June 10 without officially confirming in-the-wild exploitation, but SecurityWeek reports Google's confirmation independently. ShinyHunters is demanding payment from victims to suppress stolen data.

*Covered in: BleepingComputer, The Hacker News, SecurityWeek (×2), Risky Business News — 5 posts across 2 outlets*
- [Oracle mitigates PeopleSoft zero-day exploited in data theft attacks](https://www.bleepingcomputer.com/news/security/oracle-mitigates-peoplesoft-zero-day-exploited-in-data-theft-attacks)
- [ShinyHunters Exploits Oracle PeopleSoft Zero-Day (CVE-2026-35273) to Breach Universities](https://thehackernews.com/2026/06/shinyhunters-exploits-oracle-peoplesoft.html)
- [Google Confirms Exploitation of Oracle PeopleSoft Zero-Day by ShinyHunters](https://www.securityweek.com/google-confirms-exploitation-of-oracle-peoplesoft-zero-day-by-shinyhunters)
- [Oracle Addresses PeopleSoft Vulnerability Amid Reports of Zero-Day Attacks](https://www.securityweek.com/oracle-addresses-peoplesoft-vulnerability-amid-reports-of-zero-day-attacks)
- [Risky Bulletin: In the age of AI, CISA changes federal patching rules](https://news.risky.biz/risky-bulletin-in-the-age-of-ai-cisa-changes-federal-patching-rules)

---

## 2. Developing: Ivanti Sentry Exploitation Hits Honeypots as CISA Issues New 3-Day Patch Mandate

**Why it matters:** The max-severity Ivanti Sentry flaw from yesterday is spreading — exploit attempts are now reaching honeypots — and CISA's new Binding Operational Directive 26-04 turns this into a federal compliance deadline, with a Sunday patch deadline for government agencies.

Exploitation of the critical OS command-injection vulnerability in Ivanti Sentry began within 24 hours of public disclosure and has already reached honeypot infrastructure, according to SecurityWeek. CISA issued BOD 26-04, a new Binding Operational Directive that compresses the mandatory patch window for exploited flaws from the old 15/60-day tiers to three days for critical flaws. The Ivanti flaw is the directive's first real test, with CISA ordering all FCEB agencies to remediate by Sunday. Separately, CISA's BOD also mandates agencies review and update their entire vulnerability management policies around the Known Exploited Vulnerabilities catalog.

*Covered in: BleepingComputer (×2), Dark Reading, SecurityWeek (×2) — 5 posts across 3 outlets*
- [CISA orders feds to patch actively exploited Ivanti flaw by Sunday](https://www.bleepingcomputer.com/news/security/cisa-gives-feds-3-days-to-patch-ivanti-flaw-exploited-in-attacks)
- [Max-Severity Ivanti Flaw Exploited 24 Hours After Disclosure](https://www.darkreading.com/vulnerabilities-threats/max-severity-ivanti-sentry-flaw-exploited-24-hours)
- [Ivanti Sentry Exploitation Attempts Hitting Honeypots](https://www.securityweek.com/ivanti-sentry-exploitation-attempts-hitting-honeypots)
- [CISA tells govt agencies to patch critical exploited flaws in 3 days](https://www.bleepingcomputer.com/news/security/cisa-tells-govt-agencies-to-patch-critical-exploited-flaws-in-3-days)
- [CISA Directs Federal Agencies to Prioritize Security Patches Based on Risk](https://www.securityweek.com/cisa-directs-federal-agencies-to-prioritize-security-patches-based-on-risk)

---

## 3. MariaDB CVSS 10.0 — CVE-2026-49261 Command Injection via Galera Cluster Node Name

**Why it matters:** A maximum-severity vulnerability in MariaDB's Galera cluster replication lets any Galera node name embed shell commands that execute on the server — anyone running a MariaDB cluster with `wsrep_notify_cmd` enabled is at risk of full system compromise.

CVE-2026-49261 (CVSS 10.0) affects MariaDB server versions 10.6.1–10.6.26, 10.11.1–10.11.17, 11.4.1–11.4.11, 11.8.1–11.8.7, and 12.3.1 when `wsrep_notify_cmd` is enabled. The vulnerability stems from shell commands being embedded in the joiner node's name, which are executed unsanitized by the server. Patches are available in 10.6.27, 10.11.18, 11.4.12, 11.8.8, and 12.3.2. Organizations that cannot upgrade immediately should disable `wsrep_notify_cmd` as a workaround. This affects all standard MariaDB Galera Cluster and MariaDB Replication Cluster deployments where the notify command is configured.

*Covered in: NVD — 1 post across 1 source*
- [CVE-2026-49261 — MariaDB wsrep_notify_cmd Command Injection (CVSS 10.0)](https://nvd.nist.gov/vuln/detail/CVE-2026-49261)

---

## 4. Ubiquiti UniFi OS — Multiple CVSS 9.9 Vulnerabilities Including Command Injection and Privilege Escalation

**Why it matters:** Ubiquiti has disclosed a batch of critical and high-severity vulnerabilities in UniFi OS — the firmware running UniFi routers, switches, and gateways in millions of enterprise and SMB networks — including unauthenticated command injection and privilege escalation requiring only low-privilege network access.

Four CVEs were published simultaneously for UniFi OS devices: CVE-2026-47369 and CVE-2026-47370 (both CVSS 9.9) allow low-privileged network attackers to escalate privileges and execute arbitrary commands. CVE-2026-47368 (CVSS 8.6) is a path traversal enabling data exfiltration. CVE-2026-48610 (CVSS 8.1) allows unauthorized configuration changes. Additionally, related CVE-2026-47367 (CVSS 9.9) affects the UID Enterprise Agent with unauthenticated command injection. No public exploitation has been reported yet but the low privilege bar makes these high-priority for any UniFi deployment.

*Covered in: NVD — 4 posts across 1 source*
- [CVE-2026-47369 — UniFi OS Privilege Escalation (CVSS 9.9)](https://nvd.nist.gov/vuln/detail/CVE-2026-47369)
- [CVE-2026-47370 — UniFi OS Command Injection (CVSS 9.9)](https://nvd.nist.gov/vuln/detail/CVE-2026-47370)
- [CVE-2026-47368 — UniFi OS Path Traversal (CVSS 8.6)](https://nvd.nist.gov/vuln/detail/CVE-2026-47368)
- [CVE-2026-48610 — UniFi OS Improper Access Control (CVSS 8.1)](https://nvd.nist.gov/vuln/detail/CVE-2026-48610)

---

## 5. Chrome 149 Patches 28 Vulnerabilities, Including 12 Use-After-Free Bugs

**Why it matters:** Google's Chrome 149 update closes 28 security flaws — including a dozen memory-safety bugs that allow remote code execution or sandbox escape — affecting billions of users across Windows, Mac, Android, Linux, and ChromeOS.

Chrome 149.0.7827.115 addresses 28 vulnerabilities spanning use-after-free in Core (CVE-2026-12007, CVSS 8.8), WebMIDI, Media, GPU, Cast, and Autofill; heap buffer overflows in GPU and Codecs; inappropriate implementation in DevTools, Mojo, Views, and Linux Toolkit Theming; and a race condition in Safe Browsing. Many of the use-after-free bugs carry critical Chromium severity ratings despite NVD assigning CVSS scores in the 8.1–8.8 range. Exploitation requires a compromised renderer for most of the sandbox-escape bugs, but CVE-2026-12007 allows direct remote code execution via a crafted page without renderer compromise. Update via Chrome's built-in updater or your OS package manager.

*Covered in: SecurityWeek, NVD — 14 posts across 2 sources*
- [Chrome 149 Update Patches 28 Vulnerabilities](https://www.securityweek.com/chrome-149-update-patches-28-vulnerabilities)
- [CVE-2026-12007 — Chrome Core Use-After-Free RCE (CVSS 8.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-12007)
- [CVE-2026-12013 — Chrome Media Use-After-Free (CVSS 8.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-12013)

---

## Signal stats
- Total items processed: 137
- New (post-dedup): 135
- Clusters formed: ~25 (including single-item clusters above score threshold)
- Top 5 selected from: 10 scored candidate clusters
- Notable drops: AudiA6 crypto-laundering takedown (score 2.63), INTERPOL Sniper Dz / Operation Ramz (2.76), LangGraph/Langflow AI framework RCE (2.9), OpenClaw AI agent attacks (3.04)
- Source coverage gaps: Bluesky (all 403 Forbidden), Mastodon (all 422 Unprocessable), Reddit (credentials not configured)
