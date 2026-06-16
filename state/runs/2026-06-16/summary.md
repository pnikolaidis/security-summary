# Security Digest — 2026-06-16

## TL;DR
CISA added two actively exploited vulnerabilities to its Known Exploited Vulnerabilities catalog today: a Cisco Catalyst SD-WAN zero-day enabling arbitrary file writes and a LiteSpeed cPanel plugin flaw that escalates privileges to root — both with mandatory federal patch deadlines. Attackers are simultaneously exploiting three separate Fortinet FortiSandbox flaws disclosed in the past week. On the espionage front, ESET uncovered Windows variants of the previously Linux-only SprySOCKS backdoor being used against government targets in four countries, while a newly reported Microsoft 365 Copilot vulnerability chain (now patched) could have let attackers siphon emails and files with a single click. Finally, a supply chain attack has poisoned 1,500 Arch Linux AUR packages, prompting Arch to freeze new account registrations.

## 1. CISA Adds Cisco SD-WAN Zero-Day and cPanel Root Escalation to KEV — Patch by June 18
**Why it matters:** Federal civilian agencies must patch both vulnerabilities within days, and real-world exploitation is already underway across enterprise networks.

CISA added two new entries to its Known Exploited Vulnerabilities catalog on June 15. CVE-2026-20262 is a path traversal / directory traversal flaw in Cisco Catalyst SD-WAN Manager (formerly vManage) carrying a CVSS score of 6.5; it enables an authenticated remote attacker to write arbitrary files and escalate to root privileges — Cisco confirmed active zero-day exploitation. CVE-2026-54420 is a privilege escalation vulnerability (CVSS 8.5) in the LiteSpeed cPanel user-end plugin that also grants root access and is likewise being actively exploited in the wild. FCEB agencies face a mandatory remediation deadline of June 18, 2026 for both.

*Covered in: BleepingComputer, The Hacker News, SecurityWeek, CISA.gov — 6 posts across 2 sources*
- [CISA warns of another cPanel plugin flaw exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-another-actively-exploited-cpanel-plugin-flaw)
- [Cisco fixes SD-WAN vManage flaw exploited in zero-day attacks](https://www.bleepingcomputer.com/news/security/cisco-fixes-sd-wan-vmanage-flaw-exploited-in-zero-day-attacks)
- [CISA Flags LiteSpeed cPanel Plugin Flaw Exploited for Root Privilege Escalation](https://thehackernews.com/2026/06/cisa-flags-litespeed-cpanel-plugin-flaw.html)
- [Cisco Releases Security Updates for Actively Exploited SD-WAN Manager Flaw](https://thehackernews.com/2026/06/cisco-releases-security-updates-for.html)
- [Cisco Patches Another SD-WAN Zero-Day Exploited in Attacks](https://www.securityweek.com/cisco-patches-another-sd-wan-zero-day-exploited-in-attacks)
- [CISA Adds Two Known Exploited Vulnerabilities to Catalog](https://www.cisa.gov/news-events/alerts/2026/06/15/cisa-adds-two-known-exploited-vulnerabilities-catalog)

## 2. Three Fortinet FortiSandbox CVEs Exploited in the Wild Within 24 Hours of Each Other
**Why it matters:** Attackers are chaining or simultaneously exploiting three separate vulnerabilities in a security product designed to detect threats — a deeply ironic and dangerous situation for defenders relying on it.

Threat intelligence firm Defused Cyber observed active in-the-wild exploitation of three FortiSandbox vulnerabilities — CVE-2026-39813, CVE-2026-39808, and CVE-2026-25089 — all within a 24-hour window. At least one of the three (CVE-2026-25089) was only patched last week. The flaws reside in Fortinet's FortiSandbox cyber threat detection platform, which enterprises use to inspect suspicious files and network traffic. No KEV listing yet as of publish time, but active exploitation has been confirmed.

*Covered in: BleepingComputer, The Hacker News — 2 posts across 1 source family*
- [Critical Fortinet FortiSandbox flaws now exploited in attacks](https://www.bleepingcomputer.com/news/security/critical-fortinet-fortisandbox-flaws-now-exploited-in-attacks)
- [Attackers Exploit Three Fortinet FortiSandbox Flaws, One Patched Last Week](https://thehackernews.com/2026/06/attackers-exploit-three-fortinet.html)

## 3. Microsoft 365 Copilot "SearchLeak" — A Three-Bug Chain for One-Click Email and File Theft
**Why it matters:** Any enterprise user of Microsoft 365 Copilot could have had their mailbox, OneDrive, and SharePoint files silently exfiltrated by clicking a single legitimate-looking Microsoft URL — now patched, but illustrates the new prompt-injection attack surface opened by AI assistants.

Varonis Threat Labs researchers chained three separate vulnerabilities in Microsoft 365 Copilot Enterprise Search into an attack they call SearchLeak. A victim clicking a specially crafted link pointing to a trusted Microsoft domain would trigger Copilot to silently search and exfiltrate emails, calendar events, indexed OneDrive/SharePoint files, and even MFA codes — all in a single HTTP interaction. The three-bug chain exploits prompt injection via hidden URLs and bypasses normal Copilot safety controls. Microsoft has patched all three flaws. The research highlights a growing class of AI-assistant attacks that weaponize implicit trust in platform-native links.

*Covered in: BleepingComputer, The Hacker News, Dark Reading — 3 posts across 1 source family*
- [New attack turned Microsoft 365 Copilot into 1-click data theft tool](https://www.bleepingcomputer.com/news/security/new-attack-turned-microsoft-365-copilot-into-1-click-data-theft-tool)
- [One-Click Microsoft 365 Copilot Flaw Could Have Let Attackers Steal Emails, Files, and MFA Codes](https://thehackernews.com/2026/06/one-click-microsoft-365-copilot-flaw.html)
- [Copilot 'SearchLeak' Attack Allows 1-Click Data Theft](https://www.darkreading.com/application-security/copilot-searchleak-attack-1-click-data-theft)

## 4. "Atomic Arch" Supply Chain Attack Poisons 1,500 AUR Packages — Arch Linux Halts Registrations
**Why it matters:** A coordinated supply chain attack targeting the Arch User Repository affects potentially millions of Arch and derivative Linux users who rely on AUR for community-maintained packages.

SecurityWeek reports that a campaign named "Atomic Arch" has uploaded malicious versions of approximately 1,500 packages to the Arch Linux AUR (Arch User Repository), the community-driven repository that hosts user-submitted packages outside the official Arch repos. In response, Arch Linux suspended new AUR account registrations to contain further poisoning while the extent of the compromise is investigated. AUR packages are installed directly by users and used extensively in developer environments; a supply chain compromise at this scale can introduce backdoors or credential stealers across a large population of technical users. The attack was reported this morning and investigation is ongoing.

*Covered in: SecurityWeek — 1 post across 1 source family*
- [Atomic Arch Supply Chain Attack Hits 1,500 AUR Packages](https://www.securityweek.com/atomic-arch-supply-chain-attack-hits-1500-aur-packages)

## 5. ESET Finds Windows Variants of Linux-Only SprySOCKS Backdoor Hitting Government Targets
**Why it matters:** A China-linked threat actor has expanded a previously Linux-only espionage tool to Windows, using kernel driver stealth techniques, and has already compromised government organizations in at least four countries.

ESET researchers discovered two previously undocumented Windows variants of SprySOCKS — dubbed WIN_DRV and WIN_PLUS — which were previously believed to be a Linux-exclusive backdoor linked to a Chinese threat actor. The Windows builds use driver-based rootkit techniques for stealth, making them significantly harder to detect with standard endpoint tools. BleepingComputer reports that the Windows variant has been used in confirmed attacks against government organizations in at least four countries. The capability expansion — from Linux servers to Windows desktops and servers — broadens the potential victim pool considerably and suggests ongoing development of this toolkit.

*Covered in: BleepingComputer, The Hacker News — 2 posts across 1 source family*
- [Windows version of SprySOCKS Linux malware used to attack govt orgs](https://www.bleepingcomputer.com/news/security/windows-version-of-sprysocks-linux-malware-used-to-attack-govt-orgs)
- [China-Linked SprySOCKS Backdoor Expands to Windows with Driver-Based Stealth](https://thehackernews.com/2026/06/china-linked-sprysocks-backdoor-expands.html)

## Signal stats
- Total items processed: 142
- New (post-dedup): 142
- Clusters formed: 130
- Top 5 selected from: 130 candidate clusters
