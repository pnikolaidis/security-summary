# Security Digest — 2026-06-15

## TL;DR
A Palo Alto Networks GlobalProtect VPN flaw (CVE-2026-0257) is under active exploitation, making patching urgent for enterprise networks. GL.iNet consumer routers have two public-exploit command-injection bugs (CVSS 8.8) that need immediate firmware updates. The curl project is announcing a one-month vulnerability-report blackout in July, raising responsible-disclosure concerns. The FCC is proposing rules that would end anonymous prepaid phones by mandating government ID collection from all telecom customers. And the ShinyHunters extortion group claims to have stolen 297 GB from the Council of Europe, including employee personal data.

---

## 1. Palo Alto PAN-OS GlobalProtect Auth Bypass Actively Exploited (CVE-2026-0257)

**Why it matters:** Any organization running Palo Alto GlobalProtect as a VPN gateway is at immediate risk — an unknown threat actor is exploiting this auth bypass in the wild right now.

Palo Alto Networks confirmed "active exploitation" of CVE-2026-0257, a CVSS 7.8 authentication bypass affecting the portal and gateway components of PAN-OS GlobalProtect. The flaw allows unauthenticated access to GlobalProtect portals, giving attackers a foothold into corporate networks. Palo Alto has released patches; no KEV listing was present at collection time but active exploitation means patching or mitigation should be treated as P0.

*Covered in: thehackernews — 1 post across 1 source*
- [Palo Alto Warns of Active Exploitation of PAN-OS GlobalProtect VPN Flaw](https://thehackernews.com/2026/06/palo-alto-warns-of-active-exploitation.html)

---

## 2. GL.iNet GL-MT3000 Remote Command Injection — Two CVSS 8.8 Bugs, Public Exploits (CVE-2026-12186, CVE-2026-12187)

**Why it matters:** GL.iNet travel routers are popular with privacy-conscious users and remote workers; both vulnerabilities are remotely exploitable and proof-of-concept code is already public.

Two command-injection CVEs affect GL.iNet GL-MT3000 routers up to firmware 4.4.5. CVE-2026-12186 targets the Tor Proxy Service configuration handler (`replace_country` in `oui-httpd`), and CVE-2026-12187 targets the online firmware upgrade handler (`one_click_upgrade`). Both allow unauthenticated remote command execution; exploits are publicly disclosed. The vendor responded quickly and patched in version 4.7 — update immediately.

*Covered in: NVD — 2 CVEs across 1 source*
- [CVE-2026-12186 — GL.iNet GL-MT3000 Command Injection (CVSS 8.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-12186)
- [CVE-2026-12187 — GL.iNet GL-MT3000 Firmware Upgrade Handler Command Injection (CVSS 8.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-12187)

---

## 3. Curl Announces Vulnerability-Report Blackout for July 2026

**Why it matters:** A month-long window where the curl project won't accept new CVE reports is unusual and has sparked debate about responsible disclosure backlogs, researcher behavior, and what happens to vulnerabilities that surface during that period.

Daniel Stenberg posted that curl will not accept vulnerability reports during July 2026 — framing it as a "summer of bliss" for the maintainer team. The announcement drew significant discussion on Hacker News (449 points, 176 comments), with security researchers debating what responsible disclosers should do if they find a critical bug during the blackout, whether attackers will time exploitation to the window, and whether burnout-driven policies like this are sustainable for critical open-source infrastructure.

*Covered in: Hacker News — 1 post across 1 source*
- [Curl will not accept vulnerability reports during July 2026](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss)

---

## 4. FCC Proposes Rules to Eliminate Anonymous Prepaid ("Burner") Phones

**Why it matters:** The proposed mandate would require all U.S. telecoms to collect government-issued IDs from every customer — including prepaid — creating a national registry of phone-to-identity linkages with broad surveillance implications for journalists, activists, and abuse survivors.

Bruce Schneier flagged an FCC rulemaking proposal that would force telecoms to verify and store government identification for all new and renewing customers. Framed as an anti-scammer measure, the rule would also require collection of intended use cases for bulk phone plans and IP addresses. Privacy advocates and civil liberties groups compare the approach to telecom ID mandates in authoritarian states; the proposal is currently in comment period.

*Covered in: Schneier on Security — 1 post across 1 source*
- [The FCC Wants to Eliminate Burner Phones](https://www.schneier.com/blog/archives/2026/06/the-fcc-wants-to-eliminate-burner-phones.html)

---

## 5. ShinyHunters Claims Council of Europe Hack — 297 GB Allegedly Stolen

**Why it matters:** The Council of Europe is a major intergovernmental human-rights body; a successful breach would expose employee data for diplomats, legal staff, and human-rights monitors across 46 member states.

The ShinyHunters extortion group is claiming responsibility for a breach of the Council of Europe, alleging theft of 297 GB of data including employee personal information. ShinyHunters has a track record of substantiated large-scale breaches (Carnival Cruise, Ticketmaster). No official confirmation from the Council of Europe had been issued at collection time. The group is threatening to leak the data, suggesting ransom demands are likely in play.

*Covered in: SecurityWeek — 1 post across 1 source*
- [ShinyHunters Claims Council of Europe Hack](https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack)

---

## Signal stats
- Total items processed: 41
- New (post-dedup): 40
- Clusters formed: 22
- Top 5 selected from: 22 candidate clusters
