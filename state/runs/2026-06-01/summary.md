# Security Digest — 2026-06-01

## TL;DR
WordPress site owners should immediately patch or disable WP Maps Pro: a critical authentication bypass is being actively exploited to create rogue admin accounts. Palo Alto Networks PAN-OS customers are also under fire — CVE-2026-0257, an auth bypass, was weaponized just four days after disclosure. An npm supply chain attack targeting OpenAI Codex developers is harvesting authentication tokens with nearly 30,000 weekly downloads on the malicious package. Dutch law enforcement dismantled a botnet of 17 million infected devices in a major takedown. And Russia has significantly expanded its SORM surveillance requirements, raising the operational security bar for anyone with infrastructure or personnel in Russia.

## 1. WP Maps Pro WordPress Plugin Critical Flaw Actively Exploited

**Why it matters:** Any of the 15,000+ WordPress sites using WP Maps Pro is at risk of having attackers create full administrator accounts without authentication — and exploitation is already underway.

The critical flaw in WP Maps Pro (a plugin embedding Google Maps and OpenStreetMap on WordPress sites) lets unauthenticated attackers register administrator-level accounts on vulnerable installations. Threat actors are actively targeting the vulnerability right now. Site owners should update WP Maps Pro to the latest patched release or deactivate the plugin immediately. Once a rogue admin account exists, full site compromise — malware installation, data exfiltration, redirect injection — follows quickly.

*Covered in: bleepingcomputer, thehackernews — 2 posts across 1 source family*
- [WP Maps Pro bug exploited to create admin accounts on WordPress sites](https://www.bleepingcomputer.com/news/security/wp-maps-pro-bug-exploited-to-create-admin-accounts-on-wordpress-sites)
- [Critical WP Maps Pro Flaw Actively Exploited to Create Admin Accounts](https://thehackernews.com/2026/06/critical-wp-maps-pro-flaw-actively.html)

## 2. Palo Alto PAN-OS Auth Bypass CVE-2026-0257 Exploited Within Days of Disclosure

**Why it matters:** Organizations running Palo Alto Networks PAN-OS firewalls are being actively targeted by hackers who began exploiting this authentication bypass just four days after public disclosure and have continued for weeks.

CVE-2026-0257 is an authentication bypass in Palo Alto's PAN-OS platform, which underlies the company's widely deployed next-generation firewalls. Exploitation started almost immediately post-disclosure, and SecurityWeek confirms attacks have persisted for weeks. Authentication bypass in a firewall management plane can grant attackers full control over network security infrastructure. Organizations should apply available patches immediately and audit PAN-OS management logs for suspicious activity dating back at least a month.

*Covered in: securityweek, risky_business_news — 2 posts across 1 source family*
- [Recent Palo Alto Networks Vulnerability Exploited for Weeks](https://www.securityweek.com/recent-palo-alto-networks-vulnerability-exploited-for-weeks)
- [Risky Bulletin: Russia greatly expands SORM surveillance requirements](https://news.risky.biz/risky-bulletin-russia-greatly-expands-sorm-surveillance-requirements) *(references PAN-OS exploitation)*

## 3. OpenAI Codex Authentication Tokens Stolen via codexui-android npm Supply Chain Attack

**Why it matters:** Developers using OpenAI Codex are at risk of having authentication credentials stolen via a trojanized npm package that has accumulated 29,000 weekly downloads and remains live on the registry.

The malicious package codexui-android masquerades as a remote web UI for OpenAI Codex and was advertised on GitHub. With 29,000 weekly downloads it had substantial reach before detection. It harvests OpenAI authentication tokens from infected developer machines, potentially giving attackers API access, exposure to proprietary source code submitted for AI-assisted completion, and the ability to incur API charges. The package reportedly remained downloadable at time of reporting. Developers should audit npm dependencies for codexui-android and rotate any potentially exposed OpenAI credentials.

*Covered in: thehackernews — 1 post across 1 source family*
- [OpenAI Codex Authentication Tokens Stolen in codexui-android npm Supply Chain Attack](https://thehackernews.com/2026/06/openai-codex-authentication-tokens.html)

## 4. Dutch Authorities Dismantle Botnet Linked to 17 Million Infected Devices

**Why it matters:** Dutch law enforcement and the NCSC shut down a botnet of at least 17 million compromised devices — one of the largest takedowns this year — seizing over 200 command-and-control servers.

Dutch police (Politie) and the National Cyber Security Center announced the dismantling of a massive botnet spanning computers, tablets, smartphones, and IoT devices worldwide. More than 200 servers in the Netherlands served as the command-and-control infrastructure. A botnet of this scale can be leased for DDoS attacks, credential stuffing, spam, and proxy abuse. Details on the operators have not yet been publicly released. Organizations should check endpoint and network telemetry for any signs of prior botnet-related traffic.

*Covered in: thehackernews — 1 post across 1 source family*
- [Dutch Authorities Dismantle Botnet Linked to 17 Million Infected Devices](https://thehackernews.com/2026/05/dutch-authorities-dismantle-botnet.html)

## 5. Russia Greatly Expands SORM Surveillance Requirements

**Why it matters:** A sweeping expansion of Russia's SORM framework mandates broader data capture and extended retention across Russian telecom and internet providers, raising significant operational security risks for organizations with a Russian footprint.

SORM (System for Operative Investigative Activities) is Russia's legally mandated deep-packet-inspection and interception infrastructure, requiring ISPs to install FSB-accessible hardware. The new expansion significantly broadens the scope of covered services and data retention periods. Organizations with employees, offices, or cloud infrastructure in Russia should ensure sensitive communications use end-to-end encryption and review travel and remote-access policies accordingly. The expansion also has implications for threat intelligence sourcing and any security operations that rely on Russian-hosted infrastructure.

*Covered in: risky_business_news — 1 post across 1 source family*
- [Risky Bulletin: Russia greatly expands SORM surveillance requirements](https://news.risky.biz/risky-bulletin-russia-greatly-expands-sorm-surveillance-requirements)

## Signal stats
- Total items processed: 46
- New (post-dedup): 44
- Clusters formed: 43
- Top 5 selected from: 43 candidate clusters
