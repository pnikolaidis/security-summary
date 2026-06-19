# Security Digest — 2026-06-19

## TL;DR
CISA added Splunk Enterprise's unauthenticated RCE flaw to its Known Exploited Vulnerabilities catalog and gave federal agencies until Sunday to patch — making it the most time-critical item today. F5 shipped emergency out-of-band patches for two critical NGINX flaws (CVSS 9.2) enabling remote code execution. A researcher documented 10,000 GitHub repositories actively distributing Trojan malware in an ongoing campaign. CISA also flagged a CVSS 9.8 flaw in AVer conference cameras used in government and healthcare facilities. Rounding out the week: the "FortiBleed" leak exposed credentials for up to 86,000 Fortinet VPN and firewall devices worldwide, with CISA urging immediate credential resets.

---

## 1. Splunk Enterprise CVE-2026-20253 Added to CISA KEV — Patch by Sunday

**Why it matters:** Federal agencies must patch Splunk Enterprise within three days or risk compromise of their security monitoring platforms via unauthenticated remote code execution.

CVE-2026-20253 (Splunk Enterprise, missing authentication for a critical function) was disclosed just 8 days ago and already has confirmed in-the-wild exploitation. CISA formally added it to the Known Exploited Vulnerabilities catalog and issued a Binding Operational Directive requiring FCEB agencies to remediate by June 22. SecurityWeek notes the vulnerability allows unauthenticated attackers to achieve RCE, making it especially dangerous for internet-facing Splunk deployments. BleepingComputer reports active attack traffic was observed within days of public disclosure — a dangerously short patch window for enterprise security tools.

*Covered in: BleepingComputer, SecurityWeek, CISA KEV Catalog — 3 posts across 2 sources*
- [CISA: Splunk Enterprise flaw actively exploited, patch by Sunday](https://www.bleepingcomputer.com/news/security/cisa-splunk-enterprise-flaw-actively-exploited-patch-by-sunday)
- [Splunk Enterprise Vulnerability Exploited in Attacks Days After Disclosure](https://www.securityweek.com/splunk-enterprise-vulnerability-exploited-in-attacks-days-after-disclosure)
- [CISA Adds One Known Exploited Vulnerability to Catalog](https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-adds-one-known-exploited-vulnerability-catalog)

---

## 2. F5 Out-of-Band Patches: Critical NGINX RCE (CVSS 9.2)

**Why it matters:** Two critical use-after-free flaws in NGINX Open Source allow unauthenticated remote code execution, affecting one of the world's most widely deployed web servers.

F5 issued out-of-band security updates — skipping their normal release cadence — to address CVE-2026-42530 (CVSS v4: 9.2) and a companion flaw in `ngx_http_v3_module`. A remote, unauthenticated attacker can trigger the vulnerability simply by sending crafted HTTP/3 traffic. Because NGINX underpins millions of web and API deployments, the blast radius is substantial. The Hacker News confirmed both flaws enable code execution on affected systems. Organizations running NGINX Open Source should prioritize patching immediately, particularly any instance with HTTP/3 enabled.

*Covered in: BleepingComputer, The Hacker News — 2 posts across 1 source family*
- [F5 issues out-of-band patches for critical NGINX vulnerabilities](https://www.bleepingcomputer.com/news/security/f5-issues-out-of-band-patches-for-critical-nginx-vulnerabilities)
- [F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution](https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html)

---

## 3. Researcher Finds 10,000 GitHub Repositories Distributing Trojan Malware

**Why it matters:** A massive, ongoing campaign is using GitHub's trusted infrastructure to distribute malware at scale, targeting developers who clone or download what appear to be legitimate open-source projects.

A security researcher documented a sprawling supply-chain poisoning operation: roughly 10,000 GitHub repositories contain Trojan-laced code designed to compromise developer machines. The post, shared on Hacker News, generated 812 upvotes and over 200 comments — making it the most-engaged security story of the past 24 hours by a wide margin. The repositories impersonate popular tools and libraries, weaponizing developers' trust in GitHub as a distribution channel. The scale suggests an automated operation; GitHub has not yet publicly confirmed the takedown scope.

*Covered in: Hacker News — 1 post (812 upvotes, 211 comments)*
- [I found 10k GitHub repositories distributing Trojan malware](https://orchidfiles.com/github-repositories-distributing-malware)

---

## 4. CISA Advisory: AVer Conference Cameras — CVSS 9.8 RCE, No Auth Required

**Why it matters:** A critical-severity flaw in AVer PTC-series conference cameras lets any unauthenticated attacker on the network execute arbitrary code — and these cameras are deployed in government, healthcare, and commercial facilities worldwide.

CISA published ICS advisory ICSA-26-169-01 for CVE-2026-40624 (CVSS v3: 9.8) affecting AVer PTC500S, PTC115, PTC500+, and PTC115+ cameras. A specially crafted web request is sufficient to achieve full compromise with no credentials required. All known versions are affected; there is no version boundary listed — every deployed unit is vulnerable. Given the deployment context (federal facilities, hospitals, commercial offices), a compromised camera represents both an espionage risk and a network foothold. AVer's PSIRT page should be monitored for firmware updates.

*Covered in: CISA ICS Advisory — 1 post*
- [AVer PTC cameras (ICSA-26-169-01)](https://www.cisa.gov/news-events/ics-advisories/icsa-26-169-01)

---

## 5. FortiBleed: Up to 86,000 Fortinet Firewall and VPN Credentials Leaked

**Why it matters:** A massive credential dump — dubbed "FortiBleed" — has exposed VPN and administrative credentials for tens of thousands of Fortinet devices at organizations worldwide, enabling immediate lateral movement for any attacker who downloads the leak.

SecurityWeek puts the count at 86,000 devices; BleepingComputer reported 73,000 initially. The leaked dataset includes FortiGate firewall and SSL-VPN credentials. CISA issued a hardening advisory urging organizations to immediately terminate all active VPN sessions, reset all credentials, switch to PBKDF2 password hashing (available from FortiOS 7.2.11+), review logs for signs of lateral movement, and enforce phishing-resistant MFA on all external-facing interfaces. Risky Business News noted the dump is circulating broadly, meaning exploitation opportunity is wide-open for opportunistic actors. The cause of the original credential exposure has not been confirmed by Fortinet.

*Covered in: BleepingComputer, SecurityWeek, CISA Advisory, Risky Business News — 5 posts across 2 sources*
- [FortiBleed leak exposes Fortinet VPN credentials for 73,000 devices](https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices)
- [CISA warns Fortinet users to secure devices after FortiBleed leak](https://www.bleepingcomputer.com/news/security/cisa-warns-fortinet-users-to-secure-devices-after-fortibleed-leak)
- [FortiBleed: 86,000 Fortinet Device Credentials Compromised](https://www.securityweek.com/fortibleed-86000-fortinet-device-credentials-compromised)
- [CISA Urges Hardening Fortinet Devices After Reports of Credential Exposure](https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-urges-hardening-fortinet-devices-after-reports-credential-exposure)

---

## Signal stats
- Total items processed: 60
- New (post-dedup): 60
- Clusters formed: ~18 meaningful clusters
- Top 5 selected from: 10 highest-scoring clusters
