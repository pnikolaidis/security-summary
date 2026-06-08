# Security Digest — 2026-06-08

## TL;DR
Multiple unauthenticated WordPress plugins have critical 9.8 CVSS remote code execution flaws published today alongside three Tenda home-router models with stack-overflow vulnerabilities, at least one rated critical. SolarWinds has confirmed its Serv-U managed file-transfer product is being actively exploited in the wild and has issued an emergency patch. A Risky Business bulletin flags a newly disclosed Cisco SD-WAN zero-day alongside a supply-chain hygiene move by RubyGems. Finally, VMware has patched three stored cross-site scripting vulnerabilities in Cloud Foundation Operations that could allow privilege escalation.

## 1. Batch of Critical WordPress CVEs: Unauthenticated RCE Across Multiple Plugins and Themes

**Why it matters:** Any WordPress site running the Seotheme, Background Image Cropper, Travelscape, or Augmented-Reality plugins is exposed to complete server takeover by unauthenticated remote attackers — no credentials required.

NVD published five WordPress-related CVEs today, three rated critical (CVSS 9.8). CVE-2023-54352 (Seotheme theme) and CVE-2024-58348 (Background Image Cropper) allow unauthenticated PHP file upload and execution, giving attackers a persistent shell. CVE-2024-58349 (Travelscape 1.0.3 theme) similarly allows arbitrary file upload to achieve remote code execution. CVE-2023-54350 (Augmented-Reality plugin) exposes an elFinder connector that lets attackers create and execute malicious PHP files without authentication. CVE-2023-54351 (Sonaar Music Plugin 4.7) adds a stored XSS to the set. Exploits for all five have been made public.

WordPress administrators should audit installed plugins and themes against this list and update or remove affected components immediately. The availability of public exploits makes mass scanning and opportunistic compromise highly likely.

*Covered in: nvd — 5 posts across 1 source*
- [CVE-2023-54352 (CRITICAL 9.8) — WordPress Seotheme unauthenticated RCE](https://nvd.nist.gov/vuln/detail/CVE-2023-54352)
- [CVE-2024-58348 (CRITICAL 9.8) — WordPress Background Image Cropper arbitrary file upload](https://nvd.nist.gov/vuln/detail/CVE-2024-58348)
- [CVE-2024-58349 (CRITICAL 9.8) — WordPress Travelscape theme arbitrary file upload](https://nvd.nist.gov/vuln/detail/CVE-2024-58349)
- [CVE-2023-54350 (HIGH 7.5) — WordPress Augmented-Reality plugin RCE via elFinder](https://nvd.nist.gov/vuln/detail/CVE-2023-54350)
- [CVE-2023-54351 (HIGH 7.2) — WordPress Sonaar Music Plugin stored XSS](https://nvd.nist.gov/vuln/detail/CVE-2023-54351)

## 2. Tenda Router Stack Overflows: Critical and High CVEs Across Multiple Models

**Why it matters:** Three Tenda home and SOHO router models contain remotely exploitable stack-based buffer overflows, one rated critical at CVSS 9.8, putting home networks and small businesses at risk of complete device compromise.

CVE-2026-11499 (CRITICAL 9.8) affects the Tenda HG7, HG9, and HG10 routers' domain-blocking function; an attacker can trigger a stack overflow remotely without authentication. CVE-2026-11498 (HIGH 8.8) hits the same device family via the VoIP configuration interface. CVE-2026-11503 (HIGH 8.8) targets the Tenda CX12L via a Wi-Fi SSID configuration endpoint. All three flaws allow remote exploitation and public exploits are available or likely imminent.

Tenda routers are widely deployed in home and small-office environments and are rarely updated. Administrators who cannot patch immediately should consider disabling the web management interface from the WAN or restricting access by firewall rules. No vendor patch timeline has been publicly announced.

*Covered in: nvd — 3 posts across 1 source*
- [CVE-2026-11499 (CRITICAL 9.8) — Tenda HG7/HG9/HG10 formDOMAINBLK stack overflow](https://nvd.nist.gov/vuln/detail/CVE-2026-11499)
- [CVE-2026-11498 (HIGH 8.8) — Tenda HG7/HG9/HG10 VoIP OtherSet stack overflow](https://nvd.nist.gov/vuln/detail/CVE-2026-11498)
- [CVE-2026-11503 (HIGH 8.8) — Tenda CX12L Wi-Fi configuration stack overflow](https://nvd.nist.gov/vuln/detail/CVE-2026-11503)

## 3. SolarWinds Serv-U Vulnerability Actively Exploited in the Wild

**Why it matters:** Unauthenticated attackers are already exploiting a flaw in SolarWinds' Serv-U managed file-transfer server — organizations that have not yet patched are actively being targeted.

SolarWinds has disclosed and patched a vulnerability in Serv-U that allows unauthenticated attackers to crash the service via specially crafted HTTP POST requests. Active exploitation in the wild has been confirmed, making this an urgent patching priority for all organizations running Serv-U. SolarWinds products have been repeatedly targeted in significant breaches, so threat actors are keenly aware of their enterprise footprint.

Organizations should apply the SolarWinds patch immediately and review Serv-U access logs for unusual POST request patterns indicative of exploitation attempts.

*Covered in: securityweek — 1 post across 1 source*
- [SolarWinds Serv-U Vulnerability Exploited in the Wild](https://www.securityweek.com/solarwinds-patches-exploited-serv-u-vulnerability)

## 4. Cisco SD-WAN Zero-Day Disclosed; RubyGems Adds Supply-Chain Cooldowns; AT&T/IBM Foreign Hack Allegations

**Why it matters:** A newly disclosed Cisco SD-WAN zero-day could affect enterprise network infrastructure, while simultaneous moves by RubyGems and allegations against AT&T and IBM underscore a broad, ongoing supply-chain and infrastructure security pressure.

Today's Risky Business security bulletin reports that Cisco has warned of a new zero-day in its SD-WAN product, an enterprise networking staple. The same bulletin flags that AT&T and IBM have been accused of concealing foreign hacking incidents from regulators. On the defensive side, RubyGems is adding dependency cooldown periods to its package registry to blunt supply-chain attacks — similar in spirit to what npm has deployed — slowing down the window for typosquatting or malicious version bumps. Google security team layoffs were also noted as a concern for defensive research capacity.

Cisco SD-WAN administrators should monitor for Cisco's advisory and apply mitigations as soon as available. The RubyGems change is a net positive for Ruby ecosystem security.

*Covered in: risky_business_news — 1 post across 1 source*
- [Risky Bulletin: RubyGems adds dependency cooldowns to counter supply chain attacks](https://news.risky.biz/risky-bulletin-rubygems-adds-dependency-cooldowns-to-counter-supply-chain-attacks)

## 5. VMware Cloud Foundation Operations: Three Stored XSS Vulnerabilities (CVE-2026-41722/41723/41724)

**Why it matters:** Authenticated VMware Cloud Foundation users with policy-creation privileges can inject persistent scripts to perform administrative actions on behalf of other users, enabling privilege escalation in virtualization management planes.

VMware has patched three stored cross-site scripting vulnerabilities (CVE-2026-41722, CVE-2026-41723, CVE-2026-41724, all CVSS 8.0) in Cloud Foundation Operations. An attacker with limited privileges — sufficient to create policies, views, or text widgets — can embed malicious JavaScript that executes in other administrators' browsers, potentially taking over higher-privileged sessions. These flaws are concerning in VMware environments where Cloud Foundation Operations is used to manage large virtualization estates.

Administrators should apply VMware's patch promptly and audit who has policy/view-creation permissions in Cloud Foundation Operations.

*Covered in: nvd — 3 posts across 1 source*
- [CVE-2026-41722 (HIGH 8.0) — VMware Cloud Foundation Operations stored XSS](https://nvd.nist.gov/vuln/detail/CVE-2026-41722)
- [CVE-2026-41723 (HIGH 8.0) — VMware Cloud Foundation Operations stored XSS](https://nvd.nist.gov/vuln/detail/CVE-2026-41723)
- [CVE-2026-41724 (HIGH 8.0) — VMware Cloud Foundation Operations stored XSS](https://nvd.nist.gov/vuln/detail/CVE-2026-41724)

## Signal stats
- Total items processed: 52
- New (post-dedup): 52
- Clusters formed: 17
- Top 5 selected from: 17 candidate clusters
