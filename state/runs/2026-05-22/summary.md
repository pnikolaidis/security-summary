# Security Digest — 2026-05-22

## TL;DR
Microsoft patched two Defender zero-days being actively exploited in the wild, making those the most urgent story of the day. Chinese state-sponsored APT groups were caught deploying a novel Linux backdoor against telecom operators across the Middle East and Central Asia. A sophisticated supply-chain attack traced to a malicious VS Code extension breached GitHub's internal repositories and poisoned a popular npm package. A nine-year-old Linux kernel bug enabling root command execution on major distributions was disclosed. Finally, U.S. and Canadian authorities arrested the alleged operator of the Kimwolf botnet, one of the fastest-spreading botnets in recent memory.

## 1. Microsoft Warns of Two Actively Exploited Defender Zero-Days

**Why it matters:** Attackers are already exploiting unpatched vulnerabilities in Microsoft Defender — the security tool most enterprises rely on to protect Windows endpoints — meaning defenders must patch or mitigate immediately.

Microsoft disclosed two vulnerabilities in Microsoft Defender that are being actively exploited in the wild. CVE-2026-41091 is the primary tracked identifier; a second flaw was also confirmed. The company issued out-of-band guidance and patches, urging organizations to apply updates as a priority. Because Defender is embedded across nearly every Windows enterprise deployment, the attack surface is enormous.

Security researchers noted that exploitation was already observed before the public advisory, pointing to likely pre-patch abuse by threat actors with prior knowledge of the flaws. Organizations running Defender should apply the latest patches immediately and audit endpoint telemetry for signs of compromise.

*Covered in: BleepingComputer, The Hacker News — 2 posts across 1 source family*
- [Microsoft warns of new Defender zero-days exploited in attacks](https://www.bleepingcomputer.com/news/security/microsoft-warns-of-new-defender-zero-days-exploited-in-attacks)
- [Microsoft Warns of Two Actively Exploited Defender Vulnerabilities](https://thehackernews.com/2026/05/microsoft-warns-of-two-actively.html)

## 2. Chinese APTs Share Linux Backdoor in Coordinated Telecom Attacks

**Why it matters:** Multiple Chinese state-sponsored threat groups are sharing a new Linux backdoor — dubbed Showboat — to simultaneously target telecom operators across the Middle East and Central Asia, signaling a coordinated, strategic campaign against critical communications infrastructure.

The Showboat malware establishes a SOCKS5 proxy backdoor on compromised Linux hosts inside telecom networks, enabling persistent covert access and lateral movement. Researchers at multiple firms independently observed distinct Chinese APT groups deploying the same tooling, suggesting shared resources or coordinated direction. Targets span operators in the Middle East and Central Asia, regions of significant geopolitical interest to Beijing.

The backdoor targets Linux servers — which underpin most carrier-grade infrastructure — and is designed to blend with legitimate traffic. Organizations in telecom and adjacent critical-infrastructure sectors should audit Linux server baselines, look for unexpected SOCKS5 listeners, and review network egress for anomalous proxy traffic.

*Covered in: BleepingComputer, The Hacker News, Dark Reading — 3 posts across 1 source family*
- [Chinese hackers target telcos with new Linux, Windows malware](https://www.bleepingcomputer.com/news/security/chinese-hackers-target-telcos-with-new-linux-windows-malware)
- [Showboat Linux Malware Hits Middle East Telecom with SOCKS5 Proxy Backdoor](https://thehackernews.com/2026/05/showboat-linux-malware-hits-middle-east.html)
- [Chinese APTs Share Linux Backdoor in Central Asia Telco Attacks](https://www.darkreading.com/threat-intelligence/chinese-apts-linux-backdoor-telco-attacks)

## 3. GitHub Internal Repos Breached via Malicious VS Code Extension / TanStack npm Supply-Chain Attack

**Why it matters:** A malicious extension in the VS Code marketplace was used to exfiltrate GitHub credentials, resulting in the breach of GitHub's own internal repositories and the poisoning of the TanStack npm package — a widely used JavaScript library — putting downstream developers at risk.

The attack chain began with a trojanized Nx Console extension distributed through the Visual Studio Code extension marketplace. Developers who installed the extension had their GitHub tokens silently harvested. Attackers used those tokens to access GitHub's internal repositories and then injected malicious code into the TanStack npm package, a popular open-source library with millions of weekly downloads. GitHub has since linked the two incidents and is working with affected parties.

This incident underscores the risk of the VS Code extension ecosystem as an initial access vector for supply-chain attacks. Developers should audit their installed extensions, rotate any potentially exposed GitHub tokens, and verify the integrity of npm packages they depend on, particularly TanStack-family libraries.

*Covered in: BleepingComputer, The Hacker News — 2 posts across 1 source family*
- [GitHub links repo breach to TanStack npm supply-chain attack](https://www.bleepingcomputer.com/news/security/github-links-repo-breach-to-tanstack-npm-supply-chain-attack)
- [GitHub Internal Repositories Breached via Malicious Nx Console VS Code Extension](https://thehackernews.com/2026/05/github-internal-repositories-breached.html)

## 4. Nine-Year-Old Linux Kernel Bug Enables Root Command Execution (CVE-2026-46333)

**Why it matters:** A vulnerability that has been hiding in the Linux kernel for nine years allows any local user to execute arbitrary commands as root on most major Linux distributions, threatening the vast number of servers, containers, and workstations running Linux.

CVE-2026-46333 was introduced in a kernel code path that has been present since 2017 and affects virtually all mainstream Linux distributions, including those used in enterprise data centers, cloud infrastructure, and developer workstations. Successful exploitation gives an unprivileged local user root-level command execution, enabling complete system takeover, data theft, or persistent backdoor installation. Patches have been issued upstream and are rolling out through distribution channels.

Administrators should prioritize kernel updates on Linux hosts, especially those that allow multi-user access or run shared container workloads. Given the age and breadth of the flaw, patching is essential even for systems considered low-risk.

*Covered in: The Hacker News — 1 post across 1 source family*
- [9-Year-Old Linux Kernel Flaw Enables Root Command Execution on Major Distros](https://thehackernews.com/2026/05/9-year-old-linux-kernel-flaw-enables.html)

## 5. Alleged Kimwolf Botmaster 'Dort' Arrested and Charged in the U.S. and Canada

**Why it matters:** Authorities in the U.S. and Canada arrested the alleged operator of Kimwolf — one of the fastest-spreading botnets observed in recent years — dealing a significant blow to a criminal infrastructure used for large-scale attacks.

Canadian authorities arrested a 23-year-old Ottawa man known online as "Dort" and charged him in connection with building and operating the Kimwolf botnet. Kimwolf spread rapidly across the internet and was used to facilitate cyberattacks, though specific end-targets and the full scope of damage are still under investigation. The case was a joint U.S.–Canada effort, reflecting the continued emphasis on cross-border law enforcement cooperation against cybercriminal operations.

The arrest is a notable win for law enforcement, though botnet infrastructure often survives the takedown of individual operators. Security teams should continue monitoring for Kimwolf indicators of compromise even as the investigation proceeds.

*Covered in: KrebsOnSecurity — 1 post across 1 source family*
- [Alleged Kimwolf Botmaster 'Dort' Arrested, Charged in U.S. and Canada](https://krebsonsecurity.com/2026/05/alleged-kimwolf-botmaster-dort-arrested-charged-in-u-s-and-canada)

## Signal stats
- Total items processed: 99
- New (post-dedup): 99
- Clusters formed: 45
- Top 5 selected from: 15 candidate clusters with score ≥ 0.5
