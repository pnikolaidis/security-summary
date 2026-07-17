# Channel Brief — 2026-07-17
*Today's brief by Avery Ito. Five things to bring up on customer calls today.*

## Today's talking points
CISA dropped two Sunday-deadline patch orders overnight — one for actively-exploited Fortinet FortiSandbox flaws, one for a critical Microsoft SharePoint zero-day already in the KEV catalog — both are urgent-call material for anyone running that gear on-prem. Ernst & Young disclosed a breach through a third-party support-ticket system, a clean opener for vendor-risk conversations even with customers who don't touch EY directly. Coca-Cola's Fairlife dairy unit is still down after a ransomware hit that halted US production, a mainstream story every manufacturing and CPG customer will have seen. And the Pentagon's CMMC Phase 2 suspension doesn't kill the underlying compliance obligation — it's a window to sell readiness work before audits resume.

## 1. CISA urges immediate action on actively exploited Fortinet flaws
**Vendors implicated:** Fortinet
**Conversation angle:** Any customer running FortiSandbox needs to know CISA gave federal agencies until Sunday to patch two actively-exploited flaws — call your Fortinet accounts today, don't wait for their patch cycle.
**Pitch angle:** pentest (validate exposure before Sunday), advisory (patch-management gap review), expand (MDR/monitoring around the sandbox platform)

CISA ordered federal agencies to prioritize patching two actively exploited vulnerabilities in Fortinet's FortiSandbox threat-detection platform by Sunday. The flaws are already being used in the wild, which raises the urgency for any Fortinet shop — federal mandate or not.

*Covered in: BleepingComputer — 1 post across 1 source*
- [CISA urges immediate action on actively exploited Fortinet flaws](https://www.bleepingcomputer.com/news/security/cisa-warns-feds-to-patch-exploited-fortinet-fortisandbox-flaws-by-sunday)

## 2. CISA Adds Exploited SharePoint RCE Zero-Day CVE-2026-58644 to KEV
**Vendors implicated:** Microsoft
**Conversation angle:** Every customer running on-prem SharePoint Server needs to hear about this: CVE-2026-58644 (CVSS 9.8) is a critical deserialization RCE already being exploited, and CISA gave federal agencies until July 19 to patch — that deadline is a natural trigger for outreach today.
**Pitch angle:** pentest (external attack-surface check for exposed SharePoint), advisory (patch validation), displace (push cloud/Zero Trust alternatives to aging on-prem SharePoint)

CISA added a newly patched Microsoft SharePoint Server flaw to its Known Exploited Vulnerabilities catalog after confirming active exploitation soon after disclosure. The bug allows remote, authenticated attackers to execute arbitrary code on the server — a favorite target class for ransomware crews staging follow-on attacks.

*Covered in: The Hacker News, SecurityWeek — 2 posts across 2 sources*
- [CISA Adds Exploited SharePoint RCE Zero-Day CVE-2026-58644 to KEV](https://thehackernews.com/2026/07/cisa-adds-exploited-sharepoint-rce-zero.html)
- [Fresh SharePoint Vulnerability Exploited Soon After Disclosure](https://www.securityweek.com/fresh-sharepoint-vulnerability-exploited-soon-after-disclosure)

## 3. Ernst & Young discloses data breach after support system hack
**Vendors implicated:** —
**Conversation angle:** A Big Four firm just got popped through a third-party support-ticket system its IT staff used — a clean, low-pressure opener for vendor-risk and third-party-access conversations with any customer running outsourced support tooling.
**Pitch angle:** advisory (third-party risk assessment), upsell (PAM/identity controls on support and helpdesk tooling)

Ernst & Young is notifying customers of a data breach traced back to a compromised third-party support ticket system used by its IT personnel. Scope details are still emerging, but the vector — a support tool with broad internal access — is a pattern that shows up across plenty of enterprise accounts.

*Covered in: BleepingComputer — 1 post across 1 source*
- [Ernst & Young discloses data breach after support system hack](https://www.bleepingcomputer.com/news/security/ernst-and-young-discloses-data-breach-after-support-system-hack)

## 4. Coca-Cola says Fairlife ransomware attack halts US dairy production
**Vendors implicated:** —
**Conversation angle:** A Fortune 500 brand's manufacturing line went dark from ransomware — this is the story your manufacturing and CPG customers will already be talking about, so lead with OT/IT segmentation and incident-response readiness.
**Pitch angle:** advisory (IR retainer, OT security posture review), pentest (OT/ICS assessment), expand

Coca-Cola disclosed that a ransomware attack against its Fairlife dairy subsidiary has disrupted operations and suspended US production of Fairlife products. The company says it hasn't yet determined the full scope or impact — production remains suspended as of this morning across plants in Michigan, New York, and Arizona.

*Covered in: BleepingComputer, SecurityWeek, TechCrunch, The Record — 4 posts across 4 sources*
- [Coca-Cola says Fairlife ransomware attack halts US dairy production](https://www.bleepingcomputer.com/news/security/coca-cola-says-fairlife-ransomware-attack-halts-us-dairy-production)
- [Coca-Cola Suspends US Fairlife Production Due to Ransomware Attack](https://www.securityweek.com/coca-cola-suspends-us-fairlife-production-due-to-ransomware-attack)
- [Coca-Cola suspended production at its Fairlife dairy after a ransomware attack](https://techcrunch.com/2026/07/16/coca-cola-suspended-production-at-its-fairlife-dairy-after-a-ransomware-attack)
- [Dairy company Fairlife suspends production in US after cyber incident](https://therecord.media/dairy-company-fairlife-suspends-production-us-cyber-incident)

## 5. Industry Reactions to Pentagon Suspending CMMC Phase 2
**Vendors implicated:** —
**Conversation angle:** Defense-industrial-base customers may think the compliance pressure is off — remind them the suspension only pauses third-party CMMC audits, not the underlying legal obligation to protect CUI, so this is the moment to sell readiness work before audits resume.
**Pitch angle:** advisory (CMMC / NIST 800-171 readiness assessment), renew (don't let compliance budget lapse while the deadline is soft)

The Pentagon's suspension of CMMC Phase 2 third-party audits is drawing mixed industry reaction. The consensus: contractors still have to protect controlled unclassified information under existing contract clauses, they just won't be independently audited on it for now — a gap that advisory-minded resellers can get ahead of.

*Covered in: SecurityWeek — 1 post across 1 source*
- [Industry Reactions to Pentagon Suspending CMMC Phase 2: Feedback Friday](https://www.securityweek.com/industry-reactions-to-pentagon-suspending-cmmc-phase-2-feedback-friday)

## Signal stats
- Total items processed: 86
- New (post-dedup): 84
- NVD-only clusters dropped: 30 (no vendor-of-interest tie-in; see claude.log for near-misses)
- Clusters formed: ~80
- Same-as-recent suppressed: 0
- Developing follow-ups: 0
- Top 5 selected from: 8 candidate clusters
