# Security Digest — 2026-06-10

## TL;DR
Microsoft's June 2026 Patch Tuesday is the largest in history—206 flaws, three publicly disclosed zero-days, and a fourth new Defender exploit dropped the same evening. Ivanti and Fortinet each shipped max-severity remote-code-execution fixes for network perimeter products that attackers routinely target. OpenSSL released a critical patch that includes a PKCS#7 use-after-free potentially leading to RCE, and a subtle AES-OCB encryption bypass. Veeam's backup servers are again in the crosshairs via a CVSS 9.4 authenticated RCE. And ServiceNow has confirmed attackers exploited an unauthenticated API endpoint against real customer instances before the patch landed—a delay the company had two months to close.

---

## 1. Microsoft June 2026 Patch Tuesday — Record 206 Flaws, Three Zero-Days, and a Same-Day Bonus Exploit

**Why it matters:** Every Windows system on earth needs patching; three zero-days were already public when the update shipped, and a fourth SYSTEM-privilege exploit for Defender hit GitHub that same evening.

Microsoft's June 2026 Patch Tuesday fixes 206 vulnerabilities—a record for the company's monthly cycle—including 39 rated Critical. Three flaws had been publicly disclosed before today: YellowKey and GreenPlasma, both privilege-escalation zero-days that grant SYSTEM on a fully patched Windows system, and MiniPlasma, which allows attackers to bypass BitLocker encryption on protected drives. Exploit code for at least three weaknesses is publicly available.

Within hours of the Patch Tuesday release, an anonymous researcher known as "Nightmare-Eclipse" dropped a fresh proof-of-concept called RoguePlanet for yet another Microsoft Defender privilege escalation—a race condition the researcher claims achieves 100% success rate on tested systems. On the NVD side, two Critical Windows CVEs stand out: CVE-2026-44815 (Windows DHCP Client stack overflow, CVSS 9.8, unauthenticated network RCE) and CVE-2026-42904 (Windows TCP/IP heap overflow, CVSS 9.6). Dark Reading notes that AI-assisted fuzzing is being credited for the surge in CVE volume, suggesting record Patch Tuesdays could become the norm.

*Covered in: Krebs on Security, Bleeping Computer, The Hacker News, Dark Reading, SecurityWeek, SANS ISC — 11 posts across 2 source families*
- [A Record-Breaking Patch Tuesday for June 2026](https://krebsonsecurity.com/2026/06/a-record-breaking-patch-tuesday-for-june-2026)
- [Microsoft patches YellowKey, GreenPlasma, MiniPlasma zero-days](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days)
- [Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs](https://thehackernews.com/2026/06/microsoft-patches-record-206-flaws.html)
- [Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows](https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html)
- [Blame AI: Patch Tuesday Hits Record 206 CVEs](https://www.darkreading.com/vulnerabilities-threats/blame-ai-patch-tuesday-record-206-cves)

---

## 2. Ivanti Sentry CVSS 10.0 + Fortinet FortiSandbox CVSS 9.8 — Unauthenticated RCE on Perimeter Security Gear

**Why it matters:** Two of the most widely deployed network security appliances just patched unauthenticated remote-code-execution flaws that require no credentials and deliver root or full-admin access.

Ivanti patched two critical vulnerabilities in its Sentry secure mobile gateway. CVE-2026-10520 (CVSS 10.0) is an OS command injection allowing a remote unauthenticated attacker to execute arbitrary commands as root. Its companion, CVE-2026-10523 (CVSS 9.9), is an authentication bypass that lets an unauthenticated attacker create arbitrary administrative accounts, achieving full administrative control. Affected versions span Sentry R10.5.x, R10.6.x, and R10.7.x; customers should upgrade to R10.5.2, R10.6.2, or R10.7.1.

Simultaneously, Fortinet patched CVE-2026-25089 (CVSS 9.8) in FortiSandbox, a critical OS command injection that allows an unauthenticated attacker to execute unauthorized commands via specially crafted HTTP requests. Affected versions cover FortiSandbox 4.2 (all), 4.4.0–4.4.8, and 5.0.0–5.0.5. Ivanti products have been persistently exploited in prior years; these appliances commonly sit at network perimeters with direct internet exposure.

*Covered in: Bleeping Computer, SecurityWeek, NVD — 5 items across 2 source families*
- [Ivanti: Max severity Sentry flaw allows code execution as root](https://www.bleepingcomputer.com/news/security/new-max-severity-ivanti-sentry-flaw-allows-code-execution-as-root)
- [Critical Vulnerabilities Patched in Fortinet, Ivanti Products](https://www.securityweek.com/critical-vulnerabilities-patched-in-fortinet-ivanti-products)
- [CVE-2026-10520 (NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-10520)
- [CVE-2026-25089 (NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-25089)

---

## 3. OpenSSL Patches 18 Vulnerabilities, Including Critical PKCS#7 Use-After-Free and AES-OCB Encryption Bypass

**Why it matters:** A critical use-after-free in OpenSSL's S/MIME and PKCS#7 verification path could allow remote code execution in any application that processes signed email or code-signing messages, and a separate bug silently discards AES-OCB initialization vectors, enabling universal message forgery.

OpenSSL's June 2026 release addresses 18 vulnerabilities, many of which are attributed to AI-assisted fuzzing—consistent with the broader AI-driven vulnerability discovery trend noted in this week's Microsoft Patch Tuesday coverage. The headliner is CVE-2026-45447 (CVSS 9.8), a use-after-free triggered by a specially crafted PKCS#7 or S/MIME signed message with an empty `digestAlgorithms` SET. OpenSSL may incorrectly free a caller-owned BIO during `PKCS7_verify()`, and a subsequent use by the calling application can result in process crashes, heap corruption, or potentially remote code execution.

A subtler but insidious second vulnerability is CVE-2026-45445: when an application uses the `EVP_Cipher()` one-shot API with AES-OCB, the initialization vector supplied by the caller is silently discarded. Every message encrypted under the same key uses the same effective nonce, defeating confidentiality. Worse, the resulting authentication tag becomes a function of (key, IV) only and verifies against any ciphertext, enabling universal forgery from a single captured message. Applications using `EVP_CipherUpdate`/`EVP_CipherFinal_ex` are not affected. CVE-2026-34180 adds a 2 GB ASN.1 buffer over-read risk on 64-bit Unix platforms.

*Covered in: SecurityWeek, NVD — 6 items across 2 source families*
- [OpenSSL Patches High-Severity Vulnerability Found With AI](https://www.securityweek.com/openssl-patches-high-severity-vulnerability-found-with-ai)
- [CVE-2026-45447 (NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-45447)
- [CVE-2026-45445 (NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-45445)
- [CVE-2026-34180 (NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-34180)

---

## 4. Veeam Backup & Replication CVE-2026-44963 — CVSS 9.4 Authenticated Domain User RCE

**Why it matters:** Veeam backup servers are a perennial ransomware pivot point; an authenticated domain user on the same network can now execute code remotely on the backup server, potentially destroying the last line of defense before extortion.

Veeam has released patches for CVE-2026-44963, a critical remote code execution vulnerability in Backup & Replication carrying a CVSS score of 9.4. The flaw requires only domain authentication—not a local Veeam account—meaning any user whose Windows credentials are valid on the domain can trigger RCE on the backup server. Veeam backup infrastructure has been targeted in numerous ransomware campaigns precisely because destroying backups removes recovery options; this vulnerability lowers the bar from "compromise a Veeam admin" to "compromise any domain account."

Veeam's advisory recommends immediate patching and, where patching is not immediately possible, isolating backup servers from broad domain membership or restricting domain authentication to dedicated service accounts.

*Covered in: Bleeping Computer, The Hacker News — 2 posts across 1 source family*
- [New Veeam vulnerability exposes backup servers to RCE attacks](https://www.bleepingcomputer.com/news/security/new-veeam-vulnerability-exposes-backup-servers-to-rce-attacks)
- [Veeam Backup & Replication RCE Flaw Lets Domain Users Run Remote Code](https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html)

---

## 5. ServiceNow Exploited via Unauthenticated API Endpoint — Customer Instance Data Accessed

**Why it matters:** Attackers exploited a ServiceNow API flaw against real customer instances—and the company reportedly knew about the issue since April 7, applying the server-side patch only on June 5, leaving a two-month window of exposure.

ServiceNow has disclosed that unknown threat actors exploited a vulnerability in a vulnerable API endpoint to gain unauthenticated access and query data from customer hosted instances. The company applied a security update to hosted customer instances on June 5, 2026. According to reporting from SecurityWeek, the vulnerability had been known to ServiceNow since approximately April 7, 2026—nearly two months before the patch was deployed to customer environments.

The company's advisory (behind customer login) confirms the issue "could allow an unauthenticated user" deeper access to susceptible instances. ServiceNow is a widely deployed enterprise IT service management platform handling sensitive ticketing, change management, and HR data for large organizations. Customers should verify their instance is on the June 5 patched version, audit API access logs for anomalous queries from the period April–June 2026, and follow any specific incident notifications from ServiceNow.

*Covered in: Bleeping Computer, The Hacker News, SecurityWeek — 3 posts across 1 source family*
- [ServiceNow discloses security incident exposing customer data](https://www.bleepingcomputer.com/news/security/servicenow-discloses-security-incident-exposing-customer-data)
- [ServiceNow Flaw Exploited to Gain Unauthorized Access to Customer Instances](https://thehackernews.com/2026/06/servicenow-flaw-exploited-to-gain.html)
- [ServiceNow Patches Vulnerability Exploited Against Some Customers](https://www.securityweek.com/servicenow-patches-vulnerability-exploited-against-some-customers)

---

## Signal stats
- Total items processed: 150
- New (post-dedup): 149
- Clusters formed: 15
- Top 5 selected from: 12 candidate clusters
