# Channel Brief — 2026-09-17
*Today's brief by Aiden Iyer. Five things to bring up on customer calls today.*

## Today's talking points
Cisco just shipped an emergency patch for a max-severity ISE zero-day that's being actively exploited — that's the call to make first if you carry Cisco identity/network gear. ShinyHunters dumped Florida's motor-vehicle database after the state refused to pay, a clean pipeline trigger for public-sector prospects worried they're next. Google confirmed a Pixel modem zero-day under targeted exploitation, and a hijacked AI coding-assistant session let the Shai-Hulud worm spread across ~100 repos — both good openers for mobile threat defense and AI/dev-security advisory conversations. Rounding it out, ransomware against manufacturers is up 40% as supply-chain pressure builds, a solid vertical-prospecting angle for advisory and pentest work.

## 1. Cisco ISE zero-day under active exploitation — emergency patch out
**Vendors implicated:** Cisco
**Conversation angle:** Ask every Cisco ISE / identity customer if they've applied the emergency patch yet — this is unauthenticated, remotely exploitable, and already being used in attacks.
**Pitch angle:** advisory (emergency patch-and-posture review), renew (urgency on ISE renewals), displace (open a ZTNA/identity conversation with Zscaler/Okta/CyberArk shops watching this)

Cisco disclosed and patched a maximum-severity Identity Services Engine vulnerability that attackers are actively exploiting, alongside a broader batch of ISE, FMC, and Nexus Dashboard flaws (root access, command execution, SQL injection). Six CRITICAL CVEs are involved; Cisco's own advisory frames it as an emergency, out-of-band fix.

*Covered in: BleepingComputer, SecurityWeek, NVD — 3 posts across 2 sources*
- [Cisco warns of max severity ISE zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks)
- [Active Exploitation Triggers Emergency Patch for Cisco ISE Zero-Day](https://www.securityweek.com/active-exploitation-triggers-emergency-patch-for-cisco-ise-zero-day)
- [Cisco Fixes Dozens of Flaws Across FMC, ISE and Nexus Dashboard](https://www.securityweek.com/cisco-fixes-dozens-of-flaws-across-fmc-ise-and-nexus-dashboard)

## 2. ShinyHunters leak Florida DMV driver data after ransom refusal
**Vendors implicated:** —
**Conversation angle:** Use this with state/local government and any customer holding citizen PII — Florida's motor-vehicle agency said no to the ransom, and the data went public anyway.
**Pitch angle:** advisory (incident-response readiness / ransomware negotiation posture), pentest (test the exposure before an extortion gang finds it)

The ShinyHunters extortion gang published thousands of Florida drivers' records online after the state's motor-vehicle database was breached and the agency declined to pay. It's a clean "pay-or-don't-pay" cautionary tale for public-sector prospects.

*Covered in: TechCrunch — 1 post across 1 source*
- [Hackers publish thousands of drivers' data after breaching Florida motor vehicle database](https://techcrunch.com/2026/09/16/hackers-publish-thousands-of-drivers-data-after-breaching-florida-motor-vehicle-database)

## 3. Google confirms Pixel modem zero-day exploited in targeted attacks
**Vendors implicated:** Google
**Conversation angle:** Good mobile-threat-defense opener — ask customers whether their MDM/MTD stack would have caught exploitation at the modem/baseband layer.
**Pitch angle:** expand (mobile threat defense attach), advisory (mobile fleet posture review)

Google says a bug in the Pixel modem "may be under limited, targeted exploitation," with some Pixel owners confirmed hacked in zero-day attacks. Details are still thin, but it's the kind of headline mobile-security customers will ask about directly.

*Covered in: TechCrunch — 1 post across 1 source*
- [Google says some Pixel phone owners were hacked in zero-day attacks](https://techcrunch.com/2026/09/16/google-says-some-pixel-phone-owners-were-hacked-in-zero-day-attacks)

## 4. Shai-Hulud worm spreads via hijacked AI coding-assistant session across ~100 repos
**Vendors implicated:** Mend
**Conversation angle:** Every customer rolling out AI coding assistants needs to hear this one — an attacker hijacked a live assistant session, got it to recommend poisoned packages, and the worm spread from there.
**Pitch angle:** advisory (AI coding-assistant / SDLC security review), pentest (red-team the AI dev tooling before an attacker does)

Mandiant (via Mend's reporting) says an attacker hijacked an active AI coding-assistant session at an unnamed SaaS provider; the assistant recommended attacker-poisoned software, and the accepted recommendation let the Shai-Hulud worm spread across roughly 100 internal repositories, stealing secrets and source code along the way.

*Covered in: The Hacker News — 1 post across 1 source*
- [Attacker Hijacks AI Coding Assistant Session, Spreads Shai-Hulud Across About 100 Repositories](https://thehackernews.com/2026/09/attacker-hijacks-ai-coding-assistant.html)

## 5. Ransomware attacks on manufacturers surge 40% as supply-chain risk grows
**Vendors implicated:** —
**Conversation angle:** If you've got manufacturing accounts, lead with this stat — ransomware groups are explicitly targeting the sector to weaponize operational-shutdown pressure.
**Pitch angle:** advisory (OT/IT posture assessment), pentest (manufacturing-vertical engagement), expand (cross-sell into supply-chain-exposed accounts)

New research shows ransomware attacks on manufacturers rose 40% in early 2026, with groups increasingly exploiting the operational disruption caused by shutdowns to pressure victims into paying. Good vertical-specific talking point for any rep with manufacturing prospects.

*Covered in: SecurityWeek — 1 post across 1 source*
- [Ransomware Attacks on Manufacturers Surge as Supply Chain Risk Grows](https://www.securityweek.com/ransomware-attacks-on-manufacturers-surge-as-supply-chain-risk-grows)

## Signal stats
- Total items processed: 83
- New (post-dedup): 83
- NVD-only clusters dropped: ~16 (covering 23 CVE items — generic library/product CVEs with no vendor-of-interest match; see claude.log)
- Clusters formed: ~69
- Same-as-recent suppressed: 0
- Developing follow-ups: 0
- Top 5 selected from: 5 candidate clusters that cleared the vendor/commercial filter (Cisco ISE, Florida DMV, Pixel zero-day, Shai-Hulud, manufacturing ransomware) out of a longer tail of generic threat-intel and library-CVE clusters that didn't
