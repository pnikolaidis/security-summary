# Security Digest — 2026-06-03

## TL;DR
CISA added the two-year-old Oracle WebLogic flaw CVE-2024-21182 to the Known Exploited Vulnerabilities catalog with active exploitation confirmed in the wild — patch immediately. Google's June Android update closes 124 flaws including an actively exploited zero-day (CVE-2025-48595). A newly disclosed HTTP/2 "Bomb" attack can knock NGINX, Apache, IIS, and Cloudflare offline in seconds with minimal effort. A VS Code zero-day lets attackers steal GitHub authentication tokens in a single click, with public exploit code now available. And a malware campaign called WeedHack has compromised more than 116,000 systems by targeting Minecraft players via YouTube.

## 1. Oracle WebLogic CVE-2024-21182 Added to CISA KEV — Active Exploitation Confirmed
**Why it matters:** Unauthenticated attackers can exploit this WebLogic Server path-traversal flaw to hack exposed servers; federal agencies have until mid-June to patch, and any internet-facing WebLogic instance should be treated as urgent.

CISA on Monday added CVE-2024-21182 — a high-severity Oracle WebLogic Server vulnerability originally patched in the April 2024 Critical Patch Update — to its Known Exploited Vulnerabilities catalog after confirmed active exploitation in the wild. The flaw enables unauthenticated remote attackers to read arbitrary files and, in certain configurations, achieve code execution. SecurityWeek notes exploitation has been observed against unpatched production instances. BleepingComputer reports CISA has issued a binding directive ordering federal civilian agencies to remediate by June 17, 2026.

*Covered in: BleepingComputer, The Hacker News, SecurityWeek — 3 posts across 1 source family*
- [CISA flags two-year-old Oracle flaw as actively exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-oracle-weblogic-flaw)
- [Oracle WebLogic CVE-2024-21182 Added to KEV Catalog After Active Exploitation](https://thehackernews.com/2026/06/oracle-weblogic-cve-2024-21182-added-to.html)
- [Oracle WebLogic Vulnerability Exploited in the Wild](https://www.securityweek.com/oracle-weblogic-vulnerability-exploited-in-the-wild)

## 2. Google Patches 124 Android Flaws Including Actively Exploited Zero-Day (CVE-2025-48595)
**Why it matters:** One vulnerability in the Android Framework is under active targeted exploitation right now — apply the June 2026 security patch on all Android devices as soon as it's available from your OEM.

Google released its June 2026 Android security bulletin patching 124 vulnerabilities, including CVE-2025-48595 — a high-severity elevation-of-privilege flaw in the Framework component that Google confirms has been exploited in limited, targeted attacks. The zero-day does not require user interaction beyond having a vulnerable Android version running. Patches are rolling out via Google Play system updates and monthly OEM security updates; users should check for updates immediately.

*Covered in: BleepingComputer, The Hacker News, SecurityWeek — 3 posts across 1 source family*
- [Google fixes one actively exploited Android zero-day, 124 flaws](https://www.bleepingcomputer.com/news/security/google-fixes-one-actively-exploited-android-zero-day-124-flaws)
- [Google June 2026 Android Update Patches 124 Flaws, One Actively Exploited](https://thehackernews.com/2026/06/google-june-2026-android-update-patches.html)
- [Android Update Patches Exploited Zero-Day, 123 Other Vulnerabilities](https://www.securityweek.com/android-update-patches-exploited-zero-day-123-other-vulnerabilities)

## 3. HTTP/2 "Bomb" — Remote DoS Takes Down NGINX, Apache, IIS, Envoy, and Cloudflare in Seconds
**Why it matters:** A default-configuration weakness in every major web server and proxy is now publicly documented; operators should audit HTTP/2 settings and apply vendor mitigations before attackers weaponize this at scale.

Researchers disclosed a novel denial-of-service technique dubbed the "HTTP/2 Bomb" that chains a compression bomb with a Slowloris-style connection hold to crash or incapacitate NGINX, Apache HTTPD, Microsoft IIS, Envoy, and Cloudflare Pingora — all in their default configurations. The attack requires very low bandwidth from the attacker and can render targeted servers unresponsive in seconds. SecurityWeek reports a working exploit has been demonstrated; The Hacker News notes vendors are aware and preparing patches, but no fixes are fully available yet across all affected projects.

*Covered in: The Hacker News, SecurityWeek — 2 posts across 1 source family*
- [New HTTP/2 Bomb Vulnerability Allows Remote DoS on NGINX, Apache, IIS, Envoy & Cloudflare](https://thehackernews.com/2026/06/new-http2-bomb-vulnerability-allows.html)
- ['HTTP/2 Bomb' Exploit Knocks Web Servers Offline in Seconds](https://www.securityweek.com/http-2-bomb-exploit-knocks-web-servers-offline-in-seconds)

## 4. VS Code Zero-Day — Single Click Steals GitHub Authentication Tokens
**Why it matters:** Any developer using VS Code with GitHub integration is potentially at risk; a single maliciously crafted link can silently exfiltrate GitHub tokens, giving attackers full repository and organization access.

A security researcher published proof-of-concept exploit code for an unpatched VS Code vulnerability that allows attackers to steal a victim's GitHub authentication tokens by tricking them into clicking a specially crafted link — no additional interaction required. The exploit abuses VS Code's URI handler and its trust relationship with GitHub authentication. Microsoft has been notified, and separately published a statement addressing backlash over its recent legal threats against researchers who disclose zero-days — though no patch timeline has been confirmed for this specific flaw.

*Covered in: BleepingComputer — 1 post across 1 source family*
- [VS Code zero-day lets hackers steal GitHub tokens in one click](https://www.bleepingcomputer.com/news/security/vs-code-zero-day-lets-hackers-steal-github-tokens-in-one-click)

## 5. WeedHack Malware Campaign — 116,000+ Minecraft Systems Infected Since January
**Why it matters:** WeedHack is a malware-as-a-service platform distributing stealers and cryptominers via YouTube and gaming content; gamers and their families — not just enterprise users — are now primary targets of sophisticated commodity malware operations.

A large-scale malware campaign called WeedHack has compromised over 116,000 systems since January 2026 by targeting Minecraft players primarily through YouTube video descriptions and fake mod downloads. The campaign operates as a malware-as-a-service platform, distributing multiple payloads including CountLoader (86,000+ infections) and cryptocurrency miners. The Hacker News also notes a parallel pirated-content distribution vector for cryptomining malware. Victims are typically unaware of infection as the malware runs silently in the background.

*Covered in: BleepingComputer, The Hacker News — 2 posts across 1 source family*
- [Over 116,000 Minecraft systems infected in WeedHack malware campaign](https://www.bleepingcomputer.com/news/security/over-116-000-minecraft-systems-infected-in-weedhack-malware-campaign)
- [Weedhack Attacks Minecraft Users, CountLoader Hits 86K, Miners Spread via Pirated Content](https://thehackernews.com/2026/06/weedhack-attacks-minecraft-users.html)

## Signal stats
- Total items collected: 124
- New (post-dedup): 122
- Clusters formed: 116 (algorithmic) + 3 manual merges
- Top 5 selected from: 116 candidate clusters
