# Security Digest — 2026-06-11

## TL;DR
Ivanti Sentry has a maximum-severity vulnerability that is already being exploited in the wild — patch immediately. Splunk released a batch of fixes including a critical unauthenticated code-execution flaw in Enterprise and Cloud Platform. Microsoft's June Patch Tuesday addressed an Exchange Server zero-day that attackers had been actively using before the fix dropped. On the disclosure front, the Fission Kubernetes serverless framework and the Roxy-WI load-balancer management UI each received clusters of critical-severity CVEs, signalling a busy patch cycle for infrastructure teams.

---

## 1. Ivanti Sentry Max-Severity Vulnerability Exploited in Attacks

**Why it matters:** A CVSS 10.0 flaw in Ivanti Sentry is being weaponized in active attacks, making this the most urgent patching task of the week for any organisation running this mobile-device-gateway product.

Ivanti has disclosed a maximum-severity vulnerability in Sentry that attackers are already exploiting. While Ivanti has not published full technical details, the confirmed in-the-wild exploitation means defenders cannot wait for convenience — environments running Ivanti Sentry should treat this as an emergency patch. Ivanti has had a difficult run with exploited vulnerabilities over the past 18 months, and this disclosure continues that pattern.

*Covered in: BleepingComputer — 1 post across 1 source*
- [Max severity Ivanti Sentry vulnerability now exploited in attacks](https://www.bleepingcomputer.com/news/security/max-severity-ivanti-sentry-vulnerability-now-exploited-in-attacks)

---

## 2. Splunk Patches Critical Unauthenticated RCE Plus Multiple High-Severity Flaws

**Why it matters:** CVE-2026-20253, a critical unauthenticated remote-code-execution flaw in Splunk Enterprise and Splunk Cloud Platform, could let an attacker take over the SIEM/observability layer that many organisations rely on to detect intrusions.

Splunk released fixes covering Splunk Enterprise (below 10.2.4 / 10.0.7 / 9.4.12 / 9.3.13) and Splunk Cloud Platform across multiple supported versions. The headline issue, CVE-2026-20253, allows an unauthenticated attacker to execute arbitrary code — a dangerous primitive in a product that sits at the heart of many security operations centres. Three additional high-severity CVEs (CVE-2026-20251, CVE-2026-20252, CVE-2026-20258) round out the patch batch. SecurityWeek also notes Palo Alto Networks released its own batch of patches in the same window.

*Covered in: SecurityWeek, NVD — 5 posts across 2 sources*
- [Splunk, Palo Alto Networks Patch Severe Vulnerabilities](https://www.securityweek.com/splunk-palo-alto-networks-patch-severe-vulnerabilities)
- [CVE-2026-20253 — Splunk Enterprise/Cloud unauthenticated RCE](https://nvd.nist.gov/vuln/detail/CVE-2026-20253)

---

## 3. Microsoft Patches Exchange Server Zero-Day Exploited Before Patch Tuesday

**Why it matters:** CVE-2026-42897 was being exploited in attacks against Exchange Server before Microsoft shipped a fix, meaning some organisations may already be compromised and need to review logs alongside patching.

Microsoft's June 2026 Patch Tuesday included a fix for an actively exploited Exchange Server vulnerability (CVE-2026-42897). Exchange zero-days have historically been high-value targets for both nation-state actors and ransomware groups due to Exchange's central role in corporate email infrastructure. Organisations should apply the patch immediately and check for signs of exploitation — particularly unusual web-shell activity or unexpected authentication events — in the period before patching.

*Covered in: BleepingComputer, SecurityWeek — 2 posts across 2 sources*
- [Microsoft patches Exchange Server zero-day exploited in attacks](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-exchange-server-zero-day-exploited-in-attacks)
- [Microsoft Patches Exploited Exchange Server Vulnerability](https://www.securityweek.com/microsoft-patches-exploited-exchange-server-vulnerability)

---

## 4. Fission Kubernetes Serverless Framework: Five Critical CVEs Disclosed

**Why it matters:** Teams running the open-source Fission serverless framework on Kubernetes are exposed to critical unauthenticated attack paths including remote code execution and privilege escalation — upgrade to a patched release immediately.

NVD published a cluster of twelve CVEs against the Fission project, five of which are rated CRITICAL. The issues span unauthenticated access to privileged APIs, insecure routing of function invocations, and broken access controls in the Fission executor and router components. Fission is used by teams who want a lightweight event-driven serverless layer on top of existing Kubernetes clusters. While mainstream adoption is narrower than platforms like Knative, the criticality of the flaws warrants immediate attention for any team running it.

*Covered in: NVD — 12 posts across 1 source*
- [CVE-2026-46614 — Fission critical unauthenticated RCE](https://nvd.nist.gov/vuln/detail/CVE-2026-46614)
- [CVE-2026-50545 — Fission critical privilege escalation](https://nvd.nist.gov/vuln/detail/CVE-2026-50545)
- [CVE-2026-50563 — Fission critical access control bypass](https://nvd.nist.gov/vuln/detail/CVE-2026-50563)
- [CVE-2026-50564 — Fission critical unauth function invocation](https://nvd.nist.gov/vuln/detail/CVE-2026-50564)
- [CVE-2026-50566 — Fission critical executor misconfiguration](https://nvd.nist.gov/vuln/detail/CVE-2026-50566)

---

## 5. Roxy-WI Load-Balancer UI: Four Critical and Five High-Severity CVEs

**Why it matters:** Roxy-WI, a popular open-source web interface for managing HAProxy, Nginx, Apache, and Keepalived, has four critical remote code execution and authentication-bypass flaws in versions 8.2.6.4 and prior — any internet-exposed instance should be treated as compromised until patched.

NVD published nine CVEs against Roxy-WI ≤ 8.2.6.4 on 2026-06-11, four of which are rated CRITICAL. The critical issues include unauthenticated command injection, OS command execution via HAProxy service management endpoints, and arbitrary file write through the WAF configuration interface. The high-severity issues add authentication bypass, log injection, and EscapedString mishandling. Roxy-WI instances are often deployed on network-perimeter infrastructure; a compromise could give attackers direct access to load-balancer configuration, enabling traffic interception or denial-of-service.

*Covered in: NVD — 9 posts across 1 source*
- [CVE-2026-45550 — Roxy-WI critical unauthenticated RCE via /smon/check](https://nvd.nist.gov/vuln/detail/CVE-2026-45550)
- [CVE-2026-45552 — Roxy-WI critical command injection via install block](https://nvd.nist.gov/vuln/detail/CVE-2026-45552)
- [CVE-2026-45556 — Roxy-WI critical OS command via WAF endpoint](https://nvd.nist.gov/vuln/detail/CVE-2026-45556)
- [CVE-2026-45558 — Roxy-WI critical HAProxy service RCE](https://nvd.nist.gov/vuln/detail/CVE-2026-45558)

---

## Signal stats
- Total items processed: 128
- New (post-dedup): 127
- Clusters formed: 28
- Top 5 selected from: 28 candidate clusters
