# Security Digest — 2026-05-28

## TL;DR
A wave of ten critical WordPress plugin vulnerabilities disclosed today includes a CVSS 9.9 unrestricted file-upload flaw enabling web shell deployment. Carnival Cruise Corporation confirmed a ShinyHunters breach affecting nearly 6 million guests. The GlassWorm developer supply-chain botnet was dismantled by CrowdStrike, Google, and Shadowserver — its C2 ran over Solana and BitTorrent DHT to resist takedown. A newly documented threat actor, JINX-0164, is hitting cryptocurrency firms with fake recruiter lures and custom macOS malware targeting CI/CD pipelines. And a cryptojacking campaign is now exploiting both SEO poisoning and AI chatbot recommendations to deliver GPU mining malware.

## 1. WordPress Plugin Critical Vulnerability Wave — CVSS 9.9 Peaks
**Why it matters:** WordPress sites running any of ten newly patched plugins are exposed to web shell uploads, privilege escalation, path traversal, and blind SQL injection — at least three vulnerabilities reach CVSS 9.9.

NVD disclosed ten critical-to-high WordPress plugin vulnerabilities in a single batch on May 27. The most severe, CVE-2026-42748 (WPify Woo Czech, CVSS 9.9), allows unrestricted upload of dangerous file types — in practice granting attackers web shell deployment on vulnerable WooCommerce stores. CVE-2026-42756 (QuickWebP image optimizer, CVSS 9.9) and CVE-2026-42757 (WebinarIgnition, CVSS 9.9) both carry path traversal flaws; CVE-2026-42758 adds a separate privilege escalation in the same WebinarIgnition plugin. CVE-2026-42731 (miniOrange OTP Verification, CVSS 9.8) enables full privilege escalation. Five additional plugins — WooCommerce Active Products Tables, Tainacan, Easy Form Builder, TableOn, and MasterStudy LMS — carry blind SQL injection flaws at CVSS 9.3. WordPress admins should open the plugin dashboard, verify installed versions against these CVEs, and apply pending updates immediately; unpatched web-shell-capable plugins require urgent attention.

*Covered in: NVD — 10 CVEs*
- [CVE-2026-42748 — WPify Woo Czech unrestricted file upload (CVSS 9.9)](https://nvd.nist.gov/vuln/detail/CVE-2026-42748)
- [CVE-2026-42756 — QuickWebP path traversal (CVSS 9.9)](https://nvd.nist.gov/vuln/detail/CVE-2026-42756)
- [CVE-2026-42757 — WebinarIgnition path traversal (CVSS 9.9)](https://nvd.nist.gov/vuln/detail/CVE-2026-42757)
- [CVE-2026-42758 — WebinarIgnition privilege escalation (CVSS 9.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-42758)
- [CVE-2026-42731 — miniOrange OTP Verification privilege escalation (CVSS 9.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-42731)

## 2. Carnival Cruise Confirms ShinyHunters Breach — Nearly 6 Million Affected
**Why it matters:** The world's largest cruise operator has confirmed that a breach claimed by ShinyHunters in April 2026 is real, exposing personal data of approximately 6 million customers.

Carnival Corporation disclosed today that data belonging to nearly 6 million people was compromised in an incident the ShinyHunters extortion gang claimed in April. Carnival operates nine cruise brands — including Carnival Cruise Line, Princess Cruises, Holland America, and Cunard — with a combined customer base in the tens of millions. ShinyHunters has a long track record of targeting major consumer brands and leveraging stolen datasets for extortion and downstream fraud. Affected individuals should be alert for phishing attempts that reference specific booking or travel details, and consider monitoring personal information through identity-protection services.

*Covered in: BleepingComputer — 1 post*
- [Carnival Cruise confirms data breach affecting nearly 6 million people](https://www.bleepingcomputer.com/news/security/carnival-cruise-confirms-data-breach-affecting-nearly-6-million-people)

## 3. GlassWorm Developer Supply-Chain Botnet Dismantled — C2 Used Solana and BitTorrent DHT
**Why it matters:** A persistent software supply-chain campaign targeting developers has been shut down by an industry coalition, removing a threat that used decentralized blockchain and peer-to-peer networks as command-and-control channels to resist conventional takedowns.

CrowdStrike, Google, and the Shadowserver Foundation jointly dismantled GlassWorm, a supply-chain botnet active since at least early 2025. Operators distributed malicious packages and IDE extensions targeting software developers, then routed C2 instructions through Solana blockchain transactions and the BitTorrent DHT network — architectures specifically chosen because they cannot be taken down by seizing a handful of servers. The simultaneous disruption of all C2 channels required coordinated multi-party action. Developers should audit installed packages and IDE extensions for GlassWorm indicators of compromise, paying particular attention to packages added in 2025 from lesser-known repositories.

*Covered in: BleepingComputer, The Hacker News, CrowdStrike YouTube — 3 posts across 2 source families*
- [Glassworm botnet disrupted after resilient C2 infrastructure takedown](https://www.bleepingcomputer.com/news/security/glassworm-botnet-disrupted-after-resilient-c2-infrastructure-takedown)
- [GlassWorm Malware Takedown Disrupts Developer Supply Chain Attack Infrastructure](https://thehackernews.com/2026/05/glassworm-malware-takedown-disrupts.html)
- [Threat Snapshot: Defending Against Global Supply Chain Threats](https://www.youtube.com/shorts/wlR0-0V9ibc)

## 4. JINX-0164: New Threat Actor Targets Cryptocurrency Firms with macOS Malware and CI/CD Infiltration
**Why it matters:** A previously undocumented threat actor is targeting cryptocurrency organizations to steal digital assets using sophisticated social engineering and bespoke macOS malware that digs into CI/CD infrastructure.

Wiz researchers disclosed JINX-0164, a new threat actor conducting recruitment-themed social engineering attacks against cryptocurrency firms. Fake recruiter personas are used to lure technical staff into executing custom macOS malware, with a distinctive focus on compromising CI/CD pipeline infrastructure rather than just the endpoint. Gaining access to build pipelines means access to code-signing keys, deployment credentials, and the ability to inject malicious code into software releases — a much deeper and more persistent foothold than typical credential theft. Cryptocurrency firms and any organization with high-value digital assets should scrutinize unsolicited recruiter outreach and audit CI/CD access controls and build-pipeline integrity.

*Covered in: The Hacker News — 1 post*
- [JINX-0164 Targets Cryptocurrency Firms with Fake Recruiter Lures and macOS Malware](https://thehackernews.com/2026/05/jinx-0164-targets-cryptocurrency-firms.html)

## 5. GPU Cryptojacking Campaign Spreads via SEO Poisoning and Hijacked AI Chatbot Recommendations
**Why it matters:** Attackers are poisoning both search engine results and AI assistant responses to steer users toward GPU mining malware — a new delivery vector that exploits growing reliance on AI tools for software discovery.

An ongoing cryptojacking campaign targets systems with high-performance GPUs via a dual delivery mechanism: SEO poisoning of search results and manipulation of AI chatbot recommendations. Victims who search for legitimate GPU-intensive software — or ask an AI assistant for tool suggestions — are directed to malicious downloads that silently install mining malware. The exploitation of AI assistants as a distribution vector extends the attack surface beyond traditional phishing and web injection. Organizations running high-performance compute workstations should monitor for anomalous GPU utilization and introduce a verification step before installing software suggested by AI assistants.

*Covered in: BleepingComputer — 1 post*
- [GPU mining malware spreads via SEO poisoning, AI chatbots](https://www.bleepingcomputer.com/news/security/gpu-mining-malware-spreads-via-seo-poisoning-ai-chatbots)

## Signal stats
- Total items processed: 69
- New (post-dedup): 67
- Clusters formed: 19
- Top 5 selected from: 15 candidate clusters (above min_score threshold)
