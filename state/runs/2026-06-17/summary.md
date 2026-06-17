# Security Digest — 2026-06-17

## TL;DR
CISA added a CVSS 10.0 Joomla plugin flaw to its Known Exploited Vulnerabilities catalog with a Friday patching deadline for federal agencies. Mozilla and Google both shipped emergency browser updates patching three critical vulnerabilities in Firefox 152 and Chrome. Microsoft confirmed a public PoC zero-day in Defender — dubbed RoguePlanet — that spawns a system-level command prompt via a race condition, with no patch yet available. DragonForce ransomware operators were caught piggybacking on Microsoft Teams relay servers as covert C2 infrastructure using a new Go-based backdoor. Finally, a coordinated campaign planted at least 15 malicious AI-coding-assistant plugins in the JetBrains Marketplace to silently steal AI API keys from developers.

## 1. Joomla JCE Plugin (CVE-2026-48907) Actively Exploited — CISA Orders Patch by Friday

**Why it matters:** This CVSS 10.0 flaw in the widely-used JCE editor plugin lets unauthenticated attackers execute arbitrary PHP code on any Joomla site running it, and CISA says it is already being exploited in the wild.

The Widget Factory Joomla Content Editor (JCE) plugin contains an improper access control bug tracked as CVE-2026-48907, now officially on CISA's Known Exploited Vulnerabilities catalog. Federal civilian agencies have until Friday to apply the patch; SecurityWeek also reports a companion LiteSpeed vulnerability being abused to gain root on shared hosting servers. The exploit chain is particularly dangerous because it requires no authentication — attackers can drop a webshell directly via the editor's file-upload component.

*Covered in: BleepingComputer, The Hacker News, SecurityWeek, CISA KEV — 4 posts across 3 sources*
- [CISA orders feds to patch max severity Joomla plugin flaw by Friday](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-max-severity-joomla-plugin-flaw-by-friday)
- [CISA Warns of Actively Exploited Joomla JCE Flaw Allowing PHP Code Execution](https://thehackernews.com/2026/06/cisa-warns-of-actively-exploited-joomla.html)
- [Joomla, LiteSpeed Vulnerabilities Exploited in Attacks](https://www.securityweek.com/joomla-litespeed-vulnerabilities-exploited-in-attacks)
- [CISA Adds One Known Exploited Vulnerability to Catalog](https://www.cisa.gov/news-events/alerts/2026/06/16/cisa-adds-one-known-exploited-vulnerability-catalog)

## 2. Firefox 152 and Chrome Patch Critical Same-Origin Bypass and DOM Mitigation Bypasses

**Why it matters:** Three critical-severity CVEs in Firefox — including a same-origin policy bypass and two DOM security mitigation bypasses — could allow a malicious webpage to execute code across site boundaries; update your browsers now.

Mozilla shipped Firefox 152 and Firefox ESR 140.12 patching CVE-2026-12304 (same-origin policy bypass in the Networking/Cookies component), CVE-2026-12315, and CVE-2026-12316 (DOM security mitigation bypasses). Thunderbird 152 received the same fixes. Google also released a Chrome update addressing critical and high-severity memory safety bugs in the same window. SecurityWeek notes these memory safety issues could potentially lead to remote code execution — consistent with the CRITICAL rating from NVD.

*Covered in: SecurityWeek, NVD — 4 posts across 2 sources*
- [Chrome and Firefox Updated to Patch Critical, High-Severity Vulnerabilities](https://www.securityweek.com/chrome-and-firefox-updated-to-patch-critical-high-severity-vulnerabilities)
- [CVE-2026-12304 — Same-origin policy bypass (NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-12304)
- [CVE-2026-12315 — DOM mitigation bypass (NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-12315)
- [CVE-2026-12316 — DOM mitigation bypass (NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-12316)

## 3. Microsoft Defender "RoguePlanet" Zero-Day (CVE-2026-50656) — Public PoC, No Patch Yet

**Why it matters:** A publicly available proof-of-concept exploits a race condition in Microsoft Defender to elevate to SYSTEM — every Windows machine running Defender is potentially at risk until Microsoft ships a patch.

Disclosed one week ago and now tracked as CVE-2026-50656, "RoguePlanet" is an elevation of privilege in the Microsoft Malware Protection Engine. The public PoC exploits a race condition to spawn a command prompt with SYSTEM privileges. Microsoft has confirmed the issue and says it is working on a high-quality fix, but has provided no timeline. BleepingComputer reports the disclosure was coordinated and the PoC has been circulating since the original report; SecurityWeek confirmed the race condition detail independently.

*Covered in: BleepingComputer, SecurityWeek, NVD — 3 posts across 3 sources*
- [Microsoft working on Defender patch for RoguePlanet zero-day](https://www.bleepingcomputer.com/news/microsoft/microsoft-working-on-defender-patch-for-rogueplanet-zero-day)
- [Microsoft Working on Patch for 'RoguePlanet' Zero-Day](https://www.securityweek.com/microsoft-working-on-patch-for-rogueplanet-zero-day)
- [CVE-2026-50656 (NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-50656)

## 4. DragonForce Ransomware Deploys Go Backdoor Using Microsoft Teams as C2

**Why it matters:** By tunneling command-and-control traffic through legitimate Microsoft Teams relay infrastructure, DragonForce operators can evade perimeter controls that allow Teams traffic — a novel pivot for enterprise ransomware groups.

Researchers reported that DragonForce operators deployed a new Go-based backdoor that registers as a Teams client and uses Microsoft's own relay servers for C2 communications, making traffic indistinguishable from normal collaborative traffic at the network layer. The backdoor was discovered during a recent incident response engagement. Teams-relay C2 is a significant operational security upgrade for the group and will require defenders to inspect Teams traffic at the application layer or rely on endpoint detection rather than network signatures.

*Covered in: SecurityWeek — 1 post across 1 source*
- [Microsoft Teams Relay Servers Abused in DragonForce Ransomware Attack](https://www.securityweek.com/microsoft-teams-relay-servers-abused-in-dragonforce-ransomware-attack)

## 5. 15 Malicious JetBrains Marketplace Plugins Exfiltrate AI API Keys

**Why it matters:** Developers who installed any of these fake AI-coding-assistant plugins may have had their OpenAI, Anthropic, or DeepSeek API keys silently stolen — keys that grant access to potentially expensive or sensitive AI workloads.

At least 15 plugins posing as DeepSeek-powered coding assistants were published to the JetBrains Marketplace in a coordinated campaign. Each plugin offered features like chat, commit-message generation, code review, and unit tests — then quietly exfiltrated whatever AI provider API keys it found in the IDE environment. The Hacker News notes a parallel campaign in Chrome extensions capturing AI chatbot conversations. JetBrains has been notified; developers should audit their installed plugins and rotate any AI API keys that may have been exposed.

*Covered in: BleepingComputer, The Hacker News — 2 posts across 2 sources*
- [Malicious JetBrains Marketplace plugins steal AI API keys from developers](https://www.bleepingcomputer.com/news/security/malicious-jetbrains-marketplace-plugins-steal-ai-api-keys-from-developers)
- [Malicious JetBrains Plugins Steal AI API Keys as Chrome Extensions Capture Chatbot Chats](https://thehackernews.com/2026/06/malicious-jetbrains-plugins-steal-ai.html)

## Signal stats
- Total items processed: 100
- New (post-dedup): 100
- Clusters formed: 14
- Top 5 selected from: 14 candidate clusters
