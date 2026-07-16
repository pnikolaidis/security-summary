# Channel Brief — 2026-07-16
*Today's brief by Aiden Iyer. Five things to bring up on customer calls today.*

## Today's talking points
Two vendor-patch fire drills lead the morning: Oracle has a federally-mandated Saturday deadline for an actively exploited E-Business Suite flaw, and Splunk plus Zoom both shipped critical patches overnight, including a 9.8-CVSS Zoom account-takeover bug. F5 customers have their own critical BIG-IP/NGINX patch batch to work through. Away from the patch queue, the Scattered Spider sentencing (five and a half years for the Transport for London hack) is the story every customer will have seen in mainstream press, and a cyberattack on a Japanese cold-chain logistics giant that dented KFC's supply chain is a clean opener for OT and supply-chain risk conversations.

## 1. CISA orders feds to patch actively exploited Oracle E-Business Suite flaw by Saturday
**Vendors implicated:** Oracle
**Conversation angle:** Ask any customer running Oracle E-Business Suite whether they've hit the CISA-mandated Saturday deadline yet — federal agencies are on the clock for a flaw already being exploited in the wild.
**Pitch angle:** advisory (emergency patch/config review), pentest (verify exposure before Saturday)

CISA issued an emergency directive ordering federal agencies to secure Oracle E-Business Suite systems by this Saturday against an actively-exploited critical vulnerability in the financial application. The binding deadline gives any customer running EBS a concrete, dated reason to act now rather than at the next maintenance window.

*Covered in: bleepingcomputer — 1 post across 1 source*
- [CISA orders feds to patch actively exploited Oracle flaw by Saturday](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-oracle-flaw-by-saturday)

## 2. Scattered Spider Hackers Sentenced to 5.5 Years Over Transport for London Hack
**Vendors implicated:** —
**Conversation angle:** This is the story every customer saw in mainstream press this morning — use it to open a conversation about identity and social-engineering defenses, since Scattered Spider's playbook is helpdesk vishing and MFA bypass, not zero-days.
**Pitch angle:** advisory (identity/help-desk hardening review), pentest (social-engineering assessment)

Two members of the Scattered Spider cybercrime collective were sentenced to five years and six months in prison for the 2024 ransomware attack on Transport for London. Coverage spans trade press, BBC (via Hacker News), and TechCrunch — this one escaped the security trade press and hit mainstream news, so expect customers to ask about it unprompted.

*Covered in: bleepingcomputer, securityweek, the_record, techcrunch_security, hackernews (bbc.com) — 5 posts across 2 sources*
- [Scattered Spider members behind TfL hack get five years in prison](https://www.bleepingcomputer.com/news/security/scattered-spider-members-behind-transport-for-london-hack-get-five-years-in-prison)
- [Two Scattered Spider Hackers Sentenced to Jail in UK](https://www.securityweek.com/two-scattered-spider-hackers-sentenced-to-jail-in-uk)
- [Scattered Spider hackers sentenced to 5.5 years over £29 million Transport for London hack](https://therecord.media/scattered-spider-hackers-tfl-sentenced)
- [UK cops say arrest of two young hackers disrupted the operations of an infamous hacking group](https://techcrunch.com/2026/07/16/uk-cops-say-arrest-of-two-young-hackers-disrupted-the-operations-of-an-infamous-hacking-group)
- [Teen hackers who live streamed cyber-attack on TfL jailed](https://www.bbc.com/news/articles/c4gyg0y6yg2o)

## 3. Splunk and Zoom Patch Critical Vulnerabilities (CVE-2026-53412, CVSS 9.8)
**Vendors implicated:** Splunk, Zoom
**Conversation angle:** If you're carrying Splunk, flag the critical patch batch to your top accounts today; separately, every customer runs Zoom, and the Windows client account-takeover bug (CVSS 9.8) is unauthenticated — that's a same-day patch conversation, not a "get to it next sprint" one.
**Pitch angle:** advisory (patch-cadence review), renew (Splunk renewal touchpoint)

Splunk and Zoom both shipped critical security updates this week. Zoom's flaw (CVE-2026-53412) affects the Windows desktop client, VDI client, and Meeting SDK, and could let an unauthenticated attacker hijack accounts. Splunk's patches separately close credential-access and privilege-escalation bugs.

*Covered in: bleepingcomputer, thehackernews, securityweek — 3 posts across 1 source*
- [Zoom warns of critical account takeover vulnerability](https://www.bleepingcomputer.com/news/security/zoom-warns-of-critical-account-takeover-vulnerability)
- [Zoom Patches Critical Windows Flaw That Could Enable Account Takeover](https://thehackernews.com/2026/07/zoom-patches-critical-windows-flaw-that.html)
- [Splunk, Zoom Patch Critical Vulnerabilities](https://www.securityweek.com/splunk-zoom-patch-critical-vulnerabilities)

## 4. F5 Patches Multiple NGINX, BIG-IP Vulnerabilities
**Vendors implicated:** F5
**Conversation angle:** F5 accounts should hear from you before they read about it — multiple critical BIG-IP/NGINX bugs let attackers modify configs, kill processes, and leak memory, which is exactly the kind of headline that reopens a "when did we last audit this" conversation.
**Pitch angle:** advisory (config/hardening review), pentest (validate exposure), displace (competitive review if patch fatigue is setting in)

F5 patched multiple critical vulnerabilities across NGINX and BIG-IP that could let attackers modify configurations, terminate or restart processes, cross security boundaries, leak memory, and execute code. F5 has a track record of high-profile incidents, so this is a credible reason to check in with every BIG-IP account.

*Covered in: securityweek — 1 post across 1 source*
- [F5 Patches Multiple NGINX, BIG-IP Vulnerabilities](https://www.securityweek.com/f5-patches-multiple-nginx-big-ip-vulnerabilities)

## 5. Cyberattack on Japan's Largest Cold-Chain Operator Disrupts KFC, Supermarket Supplies
**Vendors implicated:** —
**Conversation angle:** Use this as the OT/supply-chain opener: "if a logistics operator can take down KFC's ingredient supply, what does a similar hit do to your operations?" — good bridge into an OT security or business-continuity advisory conversation.
**Pitch angle:** advisory (OT/supply-chain risk assessment), expand (cross-sell into operational-technology accounts)

A cyberattack on Nichirei Logistics Group, Japan's largest cold-chain logistics operator, has left KFC restaurants short on ingredients and other major chains struggling to keep supermarket shelves stocked. It's a clean, named-brand example of how a single logistics-vendor compromise cascades into retail and food-service outages.

*Covered in: the_record — 1 post across 1 source*
- [Cyberattack on Japan's largest cold-chain operator disrupts KFC, supermarket supplies](https://therecord.media/cyberattack-japan-nichirei-logistics-impacts-kfc)

## Signal stats
- Total items processed: 81
- New (post-dedup): 81
- NVD-only clusters dropped: 18
- Clusters formed: 67
- Same-as-recent suppressed: 0
- Developing follow-ups: 0
- Top 5 selected from: 49 candidate clusters
