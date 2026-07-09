# Channel Brief — 2026-07-09
*Today's brief by Aiden Iyer. Five things to bring up on customer calls today.*

## Today's talking points
Wiz just showed that six mainstream AI coding agents — including AWS's Q Developer and Google's Antigravity — can be tricked into overwriting sensitive files via a symlink swap, which is the biggest vendor story of the morning. Brussels is dragging four member states into court over unimplemented NIS2, a clean opener for any EU account still sitting on a compliance gap. A vishing crew is walking Microsoft 365 users straight through Entra passkey enrollment, KDDI just disclosed a breach touching 12 million records, and Microsoft shipped a SYSTEM-privilege zero-day fix for Defender. Good spread today: one AI/vendor research story, one regulatory deadline, one identity/social-engineering angle, one named-brand breach, and one vendor patch.

## 1. Wiz uncovers "GhostApproval" symlink flaw across six AI coding agents
**Vendors implicated:** Wiz, AWS, Google
**Conversation angle:** If a customer has rolled out AI coding assistants — Copilot, Amazon Q Developer, Cursor, Windsurf — ask whether anyone's reviewed the agent's file-approval workflow, because Wiz just demonstrated all of it can be quietly redirected to a sensitive file.
**Pitch angle:** advisory (AI-assisted SDLC governance review), pentest (test the agent-approval workflow directly)

Wiz researchers found that a booby-trapped code repository can trick six popular AI coding assistants — Amazon Q Developer, Claude Code, Augment, Cursor, Google Antigravity, and Windsurf — into writing to a sensitive file instead of the harmless one the agent asked to edit. The technique, dubbed GhostApproval, works because the approval prompt shows one filename while a symlink swap lands the write somewhere else.

*Covered in: thehackernews, securityweek — 2 posts across 1 source family*
- [GhostApproval Symlink Flaws Could Let Malicious Repos Run Code in AI Coding Agents](https://thehackernews.com/2026/07/ghostapproval-symlink-flaws-could-let.html)
- [AI Coding Tools Tricked Into Hacking Developer Machine via Decades-Old Technique](https://www.securityweek.com/ai-coding-tools-tricked-into-hacking-developer-machine-via-decades-old-technique)

## 2. EU takes four member states to court over unimplemented NIS2 law
**Vendors implicated:** —
**Conversation angle:** Brussels just referred Ireland, Spain, France, and the Netherlands to the EU Court of Justice for failing to transpose NIS2 — a timely nudge for any EU customer who's been treating the deadline as soft.
**Pitch angle:** advisory (NIS2 gap assessment), pentest (regulatory-driven testing requirement under NIS2's risk-management rules)

The European Commission is escalating enforcement of the NIS2 directive, filing infringement actions against member states that still haven't implemented it in national law. For customers operating in or selling into the EU, this is a concrete signal that regulators are done waiting.

*Covered in: the_record — 1 post across 1 source family*
- [EU takes member states to court over unimplemented cybersecurity law](https://therecord.media/eu-cyber-filing-ireland-spain-france-netherlands-nis2)

## 3. Vishing campaign walks victims through Entra passkey enrollment
**Vendors implicated:** Microsoft
**Conversation angle:** Attackers are calling Microsoft 365 users and talking them through enrolling an attacker-controlled passkey in Entra ID — worth asking customers whether their help desk verifies identity before approving new passkey or MFA registrations.
**Pitch angle:** advisory (help-desk identity-verification review), upsell (phishing-resistant MFA rollout paired with registration controls)

Researchers are tracking a vishing campaign that abuses Entra ID's passkey enrollment flow, calling targets and social-engineering them into registering a new passkey the attacker controls — turning a phishing-resistant credential into an attacker-owned one. It's a reminder that passkeys don't stop social engineering at the enrollment step.

*Covered in: bleepingcomputer — 1 post across 1 source family*
- [Entra passkey enrollment vishing targets Microsoft 365 users](https://www.bleepingcomputer.com/news/security/entra-passkey-enrollment-vishing-targets-microsoft-365-users)

## 4. KDDI discloses breach impacting 12 million records
**Vendors implicated:** —
**Conversation angle:** Japanese telco KDDI just disclosed a breach touching 12 million records — good to raise with any telecom or large-subscriber-base customer about their own exposure and incident-readiness.
**Pitch angle:** pentest (external attack-surface review), advisory (incident-response tabletop)

KDDI confirmed a data breach affecting roughly 12 million customer records, one of the larger disclosed breaches at a telecom operator this year. Details on the entry point haven't been published yet.

*Covered in: securityweek — 1 post across 1 source family*
- [12 Million Impacted by Data Breach at Japanese Telco KDDI](https://www.securityweek.com/12-million-impacted-by-data-breach-at-japanese-telco-kddi)

## 5. Microsoft patches Defender "RoguePlanet" zero-day
**Vendors implicated:** Microsoft
**Conversation angle:** Microsoft shipped an out-of-band-style fix for a SYSTEM-privilege-escalation zero-day in Defender — check whether Defender-based accounts have the patch queued, and use it to open the "how fast can you actually patch your EDR" conversation.
**Pitch angle:** displace (question Defender's track record against CrowdStrike/SentinelOne on this exact flaw), advisory (patch-cadence review)

Microsoft patched a zero-day vulnerability in Windows Defender, tracked as CVE-2026-50656, that could let a local attacker escalate to SYSTEM privileges. Three separate outlets picked it up, and Microsoft says it's aware of proof-of-concept exploitation.

*Covered in: bleepingcomputer, thehackernews, securityweek — 3 posts across 1 source family*
- [Microsoft patches RoguePlanet Defender zero-day vulnerability](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-rogueplanet-defender-zero-day-vulnerability)
- [Microsoft Patches RoguePlanet Defender Flaw That Can Grant SYSTEM Privileges](https://thehackernews.com/2026/07/microsoft-patches-rogueplanet-defender.html)
- [Microsoft Patches Defender 'RoguePlanet' Vulnerability](https://www.securityweek.com/microsoft-patches-defender-rogueplanet-vulnerability)

## Signal stats
- Total items processed: 61
- New (post-dedup): 61
- NVD-only clusters dropped: 14
- Clusters formed: 55
- Same-as-recent suppressed: 0
- Developing follow-ups: 0
- Top 5 selected from: 41 candidate clusters
