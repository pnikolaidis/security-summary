# Channel Brief — 2026-08-25
*Today's brief by Adam Insight. Five things to bring up on customer calls today.*

## Today's talking points
Zscaler just shipped four Client Connector CVEs, including an unauthenticated RCE — a same-day renewal/patch-urgency call for every Zscaler account. CISA added an Oracle WebLogic flaw with a perfect 10.0 CVSS to its KEV catalog with evidence of active exploitation, so any customer running Oracle HTTP Server or WebLogic needs an emergency-patch conversation now. A phishing-as-a-service kit called Mirage2FA has hit 4,500 companies by bypassing Microsoft 365's built-in two-factor auth — a clean opener for a phishing-resistant MFA advisory engagement. Security vendor ReliaQuest confirmed one of its own employees was social-engineered by the ShinyHunters extortion crew, giving competitors in the MDR space a reposition angle. And a Blackstone-owned real estate platform exposed tenant SSNs and dates of birth, which is exactly the kind of headline that turns a cold prospect into a pentest or advisory lead.

## 1. Zscaler Client Connector: four new CVEs, including unauthenticated RCE and auth bypass
**Vendors implicated:** Zscaler
**Conversation angle:** Ask every Zscaler Client Connector customer whether they've patched yet — one of the four flaws lets an unauthenticated attacker run arbitrary code in the ZCC context, and another is a straight auth-bypass between the client and its own portal.
**Pitch angle:** renew (patch-cycle check-in), advisory (config/patch-management review)

NVD published four new Zscaler Client Connector CVEs on the same day: an authentication bypass between ZCC and its portal (CVE-2026-59564, critical), a remotely triggerable buffer overflow causing kernel DoS on Windows (CVE-2026-59565), a local privilege-escalation chain (CVE-2026-59567), and an unauthenticated remote code execution bug in the ZCC agent itself (CVE-2026-59568, critical). No public reports of active exploitation yet, but the RCE and auth-bypass combination is the kind of thing attackers move fast on.

*Covered in: NVD — 4 CVE entries across 1 source*
- [CVE-2026-59564](https://nvd.nist.gov/vuln/detail/CVE-2026-59564)
- [CVE-2026-59565](https://nvd.nist.gov/vuln/detail/CVE-2026-59565)
- [CVE-2026-59567](https://nvd.nist.gov/vuln/detail/CVE-2026-59567)
- [CVE-2026-59568](https://nvd.nist.gov/vuln/detail/CVE-2026-59568)

## 2. Actively exploited Oracle WebLogic flaw (CVSS 10.0) added to CISA's KEV catalog
**Vendors implicated:** Oracle, CISA
**Conversation angle:** Any customer running Oracle HTTP Server or WebLogic Server needs to hear about this today — CISA confirmed active, unauthenticated exploitation against a maximum-severity flaw, not a theoretical risk.
**Pitch angle:** advisory (emergency exposure assessment), pentest (external attack-surface validation)

CVE-2026-21962 (CVSS 10.0) lets an unauthenticated attacker with network access reach critical data on unpatched Oracle HTTP Server and WebLogic Server deployments. CISA added it to the Known Exploited Vulnerabilities catalog citing evidence of in-the-wild exploitation, and both trade outlets covering it framed it as a "patch immediately" situation rather than a routine advisory.

*Covered in: TheHackerNews, SecurityWeek — 2 posts across 1 source family (both citing CISA KEV)*
- [Actively Exploited Oracle WebLogic Flaw Lets Unauthenticated Attackers Access Critical Data](https://thehackernews.com/2026/08/actively-exploited-oracle-weblogic-flaw.html)
- [CISA Warns of Exploited Oracle WebLogic Vulnerability](https://www.securityweek.com/cisa-warns-of-exploited-oracle-weblogic-vulnerability)

## 3. Mirage2FA AiTM phishing kit hits 4,500 companies abusing Microsoft 365 logins
**Vendors implicated:** Microsoft, Microsoft 365
**Conversation angle:** If a customer's MFA story is "we use whatever Microsoft ships by default," this is your opener — Mirage2FA is a commercial adversary-in-the-middle kit that's already compromised nearly half its targeted mailboxes by relaying legitimate M365 login flows.
**Pitch angle:** advisory (phishing-resistant MFA / conditional-access review), upsell (email security add-on)

Researchers at ANY.RUN tracked the Mirage2FA phishing-as-a-service toolkit running since 2024, now hitting roughly 4,500 US and EU companies by abusing legitimate Microsoft 365 login flows to sit between the user and Microsoft and relay session tokens — defeating standard SMS/app-based 2FA. An estimated 48% of targeted addresses were potentially compromised.

*Covered in: TheHackerNews — 1 post*
- [Mirage2FA Surge Hits 4,500 US and EU Companies, Abusing Microsoft 365 Login Flows](https://thehackernews.com/2026/08/mirage2fa-surge-hits-4500-us-and-eu.html)

## 4. ReliaQuest confirms ShinyHunters breach via social-engineered employee
**Vendors implicated:** —
**Conversation angle:** A security vendor's own team got phished — good ammunition for MDR competitors (Arctic Wolf, eSentire, Expel, Red Canary) to ask prospects how their current provider handles insider social engineering, and a reminder for everyone else that "we're a security company" isn't immunity.
**Pitch angle:** displace (MDR competitive opening), advisory (social-engineering resilience review)

ReliaQuest confirmed that hackers impersonating a member of its own security team social-engineered an employee, gaining access to an internal dashboard as part of the broader ShinyHunters extortion campaign. The company says the attempted data theft failed and customer impact was limited, but the intrusion vector — a trusted-team impersonation — is the same one hitting many of the Salesforce/Salesloft-adjacent breaches this year.

*Covered in: BleepingComputer, SecurityWeek — 2 posts across 1 source family*
- [ReliaQuest confirms failed data-theft attack after ShinyHunters breach](https://www.bleepingcomputer.com/news/security/reliaquest-confirms-failed-data-theft-attack-after-shinyhunters-breach)
- [ReliaQuest Confirms ShinyHunters Hack, but Says Impact Was Limited](https://www.securityweek.com/reliaquest-confirms-shinyhunters-hack-but-says-impact-was-limited)

## 5. Blackstone real estate subsidiary exposes SSNs, DOBs and addresses
**Vendors implicated:** —
**Conversation angle:** A Blackstone-owned property-management platform (Beam Living) leaked tenant Social Security digits, dates of birth, and addresses through an exposed GraphQL API — a concrete, named-brand example to raise with any real estate, property-management, or PE-portfolio prospect about API security testing.
**Pitch angle:** pentest (API security assessment), advisory (data-exposure incident response readiness)

A researcher disclosure (originally published in mid-July, picked up on Hacker News today with strong engagement) details how Beam Living, a Blackstone real estate portfolio company, exposed partial SSNs, dates of birth, and addresses via an unauthenticated GraphQL endpoint. It's a clean, named-brand example of API-layer data exposure — the kind of story that opens a pentest or advisory conversation with any customer running customer-facing APIs.

*Covered in: Hacker News — 1 post (high engagement)*
- [A Blackstone real estate company exposed SSN digits, DOBs, addresses and more](https://alexschapiro.com/security/vulnerability/2026/07/16/beam-living-graphql-data-exposure)

## Signal stats
- Total items processed: 84
- New (post-dedup): 84
- NVD-only clusters dropped: 25
- Clusters formed: 76 (raw algorithmic count; 2 involve over-merging on generic tokens — see claude.log)
- Same-as-recent suppressed: 0
- Developing follow-ups: 0
- Top 5 selected from: ~49 candidate clusters after NVD-only and generic library-CVE filtering
