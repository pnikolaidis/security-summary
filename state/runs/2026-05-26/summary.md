# Security Digest — 2026-05-26

## TL;DR
CISA is ordering federal agencies to patch an actively exploited Drupal SQL injection vulnerability by Wednesday — if you run Drupal, the same urgency applies. A zero-day in the KnowledgeDeliver LMS was used to plant Godzilla web shells and Cobalt Strike implants, a reminder that hard-coded ASP.NET machine keys are still a live attack vector. India's CERT-In is now mandating 12-hour patching windows for internet-facing critical flaws, a timeline shift driven by AI-accelerated exploitation. A May 2026 Windows security update is breaking domain controller lookups on Server 2016, so check your AD environments before rolling out KB5087537. And California is set to exempt Linux from its age-verification law after significant community pushback — the first major test of OS-level privacy legislation.

## 1. CISA Orders Feds to Patch Actively Exploited Drupal Vulnerability by Wednesday
**Why it matters:** An SQL injection flaw in Drupal is under active exploitation — federal agencies have until Wednesday, and any organization running Drupal should treat this with the same urgency.

CISA has added a Drupal SQL injection vulnerability to its Known Exploited Vulnerabilities catalog and issued a binding operational directive requiring U.S. government agencies to remediate by Wednesday evening. The flaw allows unauthenticated attackers to read arbitrary data from the database, giving threat actors a foothold into the underlying content store without any credentials. Drupal is widely deployed in government portals, higher education, and enterprise environments. With confirmed active exploitation now on record, unpatched public-facing instances should be considered actively targeted.

*Covered in: BleepingComputer — 1 post across 1 source*
- [CISA orders feds to patch actively exploited Drupal vulnerability](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-drupal-vulnerability)

## 2. KnowledgeDeliver LMS CVE-2026-5426 Zero-Day Exploited to Deploy Godzilla Web Shell and Cobalt Strike
**Why it matters:** Hard-coded ASP.NET machine keys let attackers forge viewstate payloads and achieve remote code execution — any ASP.NET application using default or leaked machine keys shares this same exposure.

Attackers exploited CVE-2026-5426, a zero-day in the KnowledgeDeliver Learning Management System popular in Japan, before a patch was available. The vulnerability stems from hard-coded ASP.NET machine keys embedded in the application — a configuration flaw that lets an attacker craft a malicious viewstate payload, triggering deserialization and remote code execution on the server. From there, attackers deployed the Godzilla web shell for persistent access, then used it as a staging point to drop Cobalt Strike Beacon for command-and-control. A patch is now available (CVSS 7.5). Organizations running any ASP.NET application should audit their machine key configuration and ensure they are not using default, shared, or publicly documented key values.

*Covered in: The Hacker News — 1 post across 1 source*
- [KnowledgeDeliver LMS Flaw Exploited to Deploy Godzilla and Cobalt Strike](https://thehackernews.com/2026/05/knowledgedeliver-lms-flaw-exploited-to.html)

## 3. CERT-In Mandates 12-Hour Patching for Internet-Facing Critical Flaws Amid AI-Assisted Attacks
**Why it matters:** India's CERT-In is pushing the industry toward a 12-hour remediation window for critical internet-exposed vulnerabilities — a timeline driven by the recognition that AI tools are collapsing the gap between disclosure and exploitation.

India's Computer Emergency Response Team issued new guidelines requiring organizations to patch critical vulnerabilities in internet-exposed systems within 12 hours of being flagged, where feasible. The guidance explicitly calls out AI and large language models as tools being used by threat actors to automate vulnerability scanning and exploitation at a speed that traditional patching cycles cannot match. While "where feasible" softens the mandate, the directional signal is significant: regulators are beginning to encode AI-accelerated threat timelines into policy. Security teams should review their patch prioritization processes against this emerging standard, particularly for systems with internet exposure.

*Covered in: The Hacker News — 1 post across 1 source*
- [CERT-In Mandates 12-Hour Patching for Internet-Facing Flaws Amid AI-Assisted Attacks](https://thehackernews.com/2026/05/cert-in-mandates-12-hour-patching-for.html)

## 4. Microsoft: May 2026 Security Update KB5087537 May Break Domain Controller Lookups on Windows Server 2016
**Why it matters:** A May 2026 security patch is causing domain controller lookup failures on Windows Server 2016, which can break authentication across any AD environment relying on those DCs — test before deploying widely.

Microsoft has confirmed a known issue in the May 2026 security update KB5087537 affecting Windows Server 2016: after installation, domain controller lookups may fail intermittently. For organizations that have not yet deployed the update, this is a critical hold signal for Server 2016 systems in production Active Directory environments. For those who have already applied it and are seeing authentication or login failures, Microsoft acknowledges the issue and workarounds should be checked via the Windows release health dashboard. The practical impact extends to any service relying on Kerberos or NTLM authentication through affected DCs.

*Covered in: BleepingComputer — 1 post across 1 source*
- [Microsoft: Domain Controller lookup may fail on Windows Server 2016](https://www.bleepingcomputer.com/news/microsoft/microsoft-domain-controller-lookup-may-fail-on-windows-server-2016)

## 5. California Moves to Exempt Linux from Age-Verification Law After Backlash Over OS-Level Age Collection
**Why it matters:** A California bill that would have required operating systems to collect user ages — with no carve-out for open-source software — is being amended after broad pushback, marking the first major test of OS-level privacy mandates and signaling that legislators are beginning to feel community pressure on privacy-by-design architecture.

California's age-verification legislation, as originally drafted, created a requirement for OS-level age collection that would have been architecturally impossible for open-source distributions like Linux to implement without introducing significant privacy risks. The Linux community organized and pushed back forcefully, and the bill's original author has now proposed an amendment that would exempt Linux. The story is notable beyond the Linux angle: it represents the first significant attempt in the U.S. to push age-verification enforcement down to the operating system layer rather than the application layer, and the amendment debate is shaping how that boundary gets drawn. Security and privacy professionals following digital identity policy should track this.

*Covered in: Hacker News (Tom's Hardware) — 1 post across 1 source*
- [California moves to exempt Linux from its age-verification law after backlash](https://www.tomshardware.com/software/linux/california-moves-to-exempt-linux-from-its-upcoming-age-verification-law-after-backlash-over-forcing-operating-systems-to-collect-users-ages-amendment-proposed-by-the-same-lawmaker-who-wrote-the-original-law)

## Signal stats
- Total items processed: 28
- New (post-dedup): 27
- Clusters formed: 16 (including 1 dropped as cross-day "same", 2 merged as near-duplicate titles, several non-security HN items scored but ranked out)
- Top 5 selected from: 15 candidate clusters
