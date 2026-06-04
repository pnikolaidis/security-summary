# Security Digest — 2026-06-04

## TL;DR
CISA added a critical Magento RCE (CVE-2026-45247, CVSS 9.8) to its Known Exploited Vulnerabilities catalog with active exploitation confirmed in the wild — e-commerce operators running the Mirasvit Cache Warmer extension must patch immediately. OpenStack Mistral carries a CVSS 9.9 RCE flaw that turns any exposed workflow API into an unauthenticated backdoor into the cloud environment. ABB T-MAC Plus industrial devices have a CVSS 9.9 file-exposure vulnerability alongside an 8.8 auth bypass, a cluster that should concern OT security teams. A researcher dropped a one-click PoC that steals GitHub OAuth tokens from VS Code without notifying Microsoft first. And Let's Encrypt announced production post-quantum hybrid certificates, a landmark moment for the encrypted web.

## 1. CISA KEV: Magento RCE CVE-2026-45247 (CVSS 9.8) Exploited in the Wild

**Why it matters:** E-commerce stores running the Mirasvit Cache Warmer Magento extension are being actively attacked — this unauthenticated deserialization flaw allows full remote code execution and is now on the federal patch-it-now list.

CISA added CVE-2026-45247 to its Known Exploited Vulnerabilities catalog after confirmed reports of active exploitation in the wild. The vulnerability is a deserialization of untrusted data flaw in the Mirasvit Cache Warmer full-page cache extension for Magento, rated CVSS 9.8. No authentication is needed; an attacker can send a crafted request to achieve remote code execution on the host server. Federal agencies face a mandatory patching deadline, and any organization running the affected extension should treat this as urgent given active exploitation is already underway.

*Covered in: thehackernews — 1 post across 1 source*
- [CISA Adds Exploited Magento RCE Flaw CVE-2026-45247 to KEV Catalog (The Hacker News)](https://thehackernews.com/2026/06/cisa-adds-exploited-magento-rce-flaw.html)

## 2. OpenStack Mistral CVSS 9.9 RCE — Exposed Workflow API Hands Over Cloud Credentials (CVE-2026-41283)

**Why it matters:** Any OpenStack deployment with the Mistral workflow service API reachable from the network is vulnerable to unauthenticated remote code execution that can cascade into full exfiltration of cloud service credentials.

CVE-2026-41283 affects OpenStack Mistral through version 22.0.0. The workflow automation service exposes API endpoints that allow direct code execution, rated CVSS 9.9 with scope change — meaning exploitation spills beyond Mistral itself into the broader cloud environment and yields service credentials. Cloud operators running Mistral with the API reachable from any untrusted segment should restrict access at the network level immediately as an interim control while planning the patch.

*Covered in: nvd — 1 CVE across 1 source*
- [CVE-2026-41283 (CRITICAL 9.9) — OpenStack Mistral Arbitrary RCE via exposed workflow API](https://nvd.nist.gov/vuln/detail/CVE-2026-41283)

## 3. ABB T-MAC Plus Industrial Devices: CVSS 9.9 File Exposure + Auth Bypass Cluster (CVE-2025-14771/14772/14773/14774)

**Why it matters:** ABB T-MAC Plus industrial networking modules have a CVSS 9.9 unauthenticated file-access flaw paired with an 8.8 authorization bypass — a combination that gives external attackers both a read path and a login bypass on OT network devices.

Four CVEs were published for ABB T-MAC Plus version 4.0-24. CVE-2025-14771 (CVSS 9.9) is a "files or directories accessible to external parties" vulnerability — any external party can read configuration data and sensitive files directly from the device without authentication. CVE-2025-14772 (CVSS 8.8) adds an authorization bypass through a user-controlled key, removing the need for valid credentials. Two additional flaws cover XSS (CVE-2025-14773, CVSS 8.0) and incorrect authorization (CVE-2025-14774, CVSS 7.4). Industrial facilities with T-MAC Plus modules reachable from untrusted network segments should apply patches or implement network segmentation immediately.

*Covered in: nvd — 4 CVEs across 1 source*
- [CVE-2025-14771 (CRITICAL 9.9) — ABB T-MAC Plus files accessible to external parties](https://nvd.nist.gov/vuln/detail/CVE-2025-14771)
- [CVE-2025-14772 (HIGH 8.8) — ABB T-MAC Plus authorization bypass via user-controlled key](https://nvd.nist.gov/vuln/detail/CVE-2025-14772)
- [CVE-2025-14773 (HIGH 8.0) — ABB T-MAC Plus cross-site scripting](https://nvd.nist.gov/vuln/detail/CVE-2025-14773)
- [CVE-2025-14774 (HIGH 7.4) — ABB T-MAC Plus incorrect authorization](https://nvd.nist.gov/vuln/detail/CVE-2025-14774)

## 4. Let's Encrypt Announces Post-Quantum Hybrid Certificates in Production

**Why it matters:** The world's largest free certificate authority has shipped hybrid classical/post-quantum certificates to the open web, marking the beginning of the web PKI's transition to quantum-resistant encryption at real scale.

Let's Encrypt published a blog post announcing production rollout of hybrid certificates combining classical ECDSA keys with ML-KEM (CRYSTALS-Kyber), one of NIST's finalized post-quantum standards. The hybrid design means connections remain protected even if classical cryptography is eventually broken by a sufficiently powerful quantum computer. Let's Encrypt issues certificates for a significant fraction of the HTTPS web, making this a genuine infrastructure shift rather than a research preview. The Hacker News post gathered 267 points and 149 comments from practitioners working through compatibility tradeoffs — larger certificate payloads, slightly longer TLS handshakes, and partial client support are the known costs.

*Covered in: hackernews — 1 post across 1 source*
- [A Post-Quantum Future for Let's Encrypt (Let's Encrypt blog via Hacker News)](https://letsencrypt.org/2026/06/03/pq-certs)

## 5. VS Code One-Click GitHub OAuth Token Theft — Full PoC Dropped Without Vendor Notice

**Why it matters:** A single crafted link clicked inside VS Code hands over the user's full GitHub OAuth token to an attacker, granting read/write access to all their repositories including private ones — with a working exploit now public and no coordinated disclosure made to Microsoft beforehand.

Researcher Ammar Askar disclosed a vulnerability in VS Code's GitHub.dev feature: a single click on a malicious link steals the victim's GitHub OAuth token. The token grants full read/write access to all repositories — no login prompt, no additional action required. The researcher published complete technical details and a proof-of-concept without prior notice to Microsoft. SecurityWeek confirmed the PoC is publicly available. The disclosure method will likely reignite coordinated-disclosure debates after last week's GitHub researcher account removal controversy. Any developer who opens untrusted links inside VS Code, or anyone who receives a crafted GitHub.dev URL, is at risk while a patch is pending.

*Covered in: thehackernews, securityweek — 2 posts across 1 source family*
- [One-Click GitHub Dev Attack Lets Attackers Steal Full GitHub OAuth Tokens (The Hacker News)](https://thehackernews.com/2026/06/one-click-github-dev-attack-lets.html)
- [VS Code Vulnerability Allows One-Click GitHub Token Theft (SecurityWeek)](https://www.securityweek.com/vs-code-vulnerability-allows-one-click-github-token-theft)

## Signal stats
- Total items processed: 96
- New (post-dedup): 95
- Clusters formed: 22
- Top 5 selected from: 22 candidate clusters
