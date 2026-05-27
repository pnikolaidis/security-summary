# Security Digest — 2026-05-27

## TL;DR
Today's digest is dominated by a wave of high-severity vulnerability disclosures. FastNetMon's open-source DDoS detection platform ships with eight new CVEs — including an unauthenticated management API and two critical memory-corruption flaws in its BGP parser. IBM WebSphere and HTTP Server receive patches for a CVSS 9.8 unauthenticated RCE alongside several other critical and high-severity bugs. CISA has issued a binding four-day patch mandate for an actively-exploited flaw in the LiteSpeed cPanel plugin. Joomla CMS patches three critical privilege-escalation bugs in the same component. And KubeVirt's container virtualization layer harbors a CVSS 9.9 symlink attack that lets a developer-level user escape their Kubernetes namespace to the host.

## 1. FastNetMon Community Edition — Eight CVEs Including Unauthenticated Remote Control and Critical Memory Corruption
**Why it matters:** FastNetMon is deployed by ISPs and network operators worldwide to detect and automatically mitigate DDoS attacks; these bugs allow an unauthenticated network-adjacent attacker to execute arbitrary code, hijack router integrations, and fully control the host.

Eight CVEs affecting FastNetMon Community Edition ≤1.2.9 were published Tuesday. The two most critical (CVSS 9.8) are memory-corruption bugs in the BGP packet decoder: CVE-2026-48686 is a stack-based buffer overflow triggered by a malformed BGP NLRI message, and CVE-2026-48689 is an off-by-one heap overflow in the dynamic buffer class. Both can be triggered remotely by anyone who can send BGP traffic to the monitor. Compounding the risk, CVE-2026-48692 exposes the gRPC management API on port 50052 with *no authentication mechanism* — the source code even contains a comment explicitly acknowledging the open listener. Additional flaws include an integer overflow in packet-capture buffer allocation (CVE-2026-48690), OS command injection in the MikroTik router plugin (CVE-2026-48695), configuration injection in the Juniper plugin (CVE-2026-48694), disabled TLS certificate validation on outbound connections (CVE-2026-48697), and multiple out-of-bounds reads in the IPv6 BGP decoder (CVE-2026-48688). FastNetMon has not yet released a patched release; operators should firewall port 50052 and restrict BGP peering immediately.

*Covered in: nvd — 8 posts across 1 source*
- [CVE-2026-48686 — Stack-based buffer overflow in BGP NLRI decoder (CVSS 9.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-48686)
- [CVE-2026-48689 — Off-by-one heap overflow in dynamic buffer class (CVSS 9.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-48689)
- [CVE-2026-48692 — Unauthenticated gRPC management API on port 50052 (CVSS 8.1)](https://nvd.nist.gov/vuln/detail/CVE-2026-48692)
- [CVE-2026-48695 — OS command injection in MikroTik router integration plugin (CVSS 8.1)](https://nvd.nist.gov/vuln/detail/CVE-2026-48695)
- [CVE-2026-48694 — Configuration injection in Juniper router plugin (CVSS 8.1)](https://nvd.nist.gov/vuln/detail/CVE-2026-48694)
- [CVE-2026-48688 — Out-of-bounds reads in BGP MP_REACH_NLRI IPv6 decoder (CVSS 7.5)](https://nvd.nist.gov/vuln/detail/CVE-2026-48688)

## 2. IBM WebSphere & HTTP Server — CVSS 9.8 Unauthenticated RCE and Eight Additional Vulnerabilities
**Why it matters:** IBM HTTP Server and WebSphere Liberty underpin vast enterprise Java infrastructure; the unauthenticated critical RCE (CVE-2026-8633) requires no credentials and is remotely reachable on any exposed instance.

IBM released patches for nine CVEs across HTTP Server 8.5/9.0 and the WebSphere Liberty web server plug-ins. CVE-2026-8633 (CVSS 9.8) is an unauthenticated remote code execution flaw in the WebSphere Liberty plug-in — no authentication required, no special preconditions. CVE-2026-8855 (CVSS 8.1) enables both remote code execution and denial of service in IBM HTTP Server 8.5 and 9.0. A further cluster of five CVEs (CVE-2026-8834, 8850, 8854, 8856, 8835) covers buffer overflows, invalid pointer dereferences, and denial-of-service conditions. IBM also patched CVE-2026-8620 (CVSS 7.5) in the WebSphere Liberty plug-ins. In a parallel advisory, IBM Engineering Lifecycle Management received a CVSS 9.8 authentication bypass (CVE-2026-3660) that allows unauthenticated access to 7.0.3, 7.1.0, and 7.2.0. Customers running on-premises IBM middleware should apply this patch set as a priority.

*Covered in: nvd — 9 posts across 1 source*
- [CVE-2026-8633 — Unauthenticated RCE in WebSphere Liberty plug-in (CVSS 9.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-8633)
- [CVE-2026-8855 — RCE + DoS in IBM HTTP Server 8.5/9.0 (CVSS 8.1)](https://nvd.nist.gov/vuln/detail/CVE-2026-8855)
- [CVE-2026-3660 — Authentication bypass in IBM Engineering Lifecycle Management (CVSS 9.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-3660)

## 3. CISA Mandates Federal Patch of Actively-Exploited cPanel LiteSpeed Plugin — Four-Day Deadline
**Why it matters:** The LiteSpeed plugin for cPanel is being actively exploited against internet-facing web hosting servers right now; the CISA KEV directive and four-day window signal that attacks are widespread enough for the government to force federal remediation.

CISA added a critical vulnerability in the LiteSpeed user-end plugin for cPanel to its Known Exploited Vulnerabilities catalog and issued a binding directive requiring all U.S. federal civilian agencies to patch by May 31, 2026 — just four days from today. The vulnerability allows attackers to compromise cPanel servers running the LiteSpeed plugin, potentially exposing all hosted websites, databases, and credentials on the affected system. While the binding directive applies specifically to federal agencies, the active exploitation status means any organization hosting web infrastructure via cPanel with LiteSpeed enabled should treat this as critical. Apply the vendor's fix immediately or disable the LiteSpeed plugin until patching is possible.

*Covered in: news — 1 post across 1 source*
- [CISA gives feds 4 days to patch actively exploited cPanel plugin flaw](https://www.bleepingcomputer.com/news/security/cisa-gives-feds-4-days-to-patch-actively-exploited-cpanel-plugin-flaw)

## 4. Joomla — Three Critical Privilege-Escalation CVEs (CVSS 9.8 Each) in com_users Component
**Why it matters:** Joomla powers millions of websites worldwide; three separate bugs in the same batch-processing endpoint each allow any authenticated user — regardless of their assigned role — to escalate directly to administrator, enabling complete site takeover.

Three critical privilege-escalation vulnerabilities were published for Joomla CMS: CVE-2026-48898, CVE-2026-48899, and CVE-2026-48904 (all CVSS 9.8). All three exploit improper access checks in the com_users component's batch processing and group management endpoints. An attacker who can log in with any user account — even a basic subscriber — can call these endpoints to promote themselves to a Joomla Super Administrator. From that position, they can install malicious extensions, access all site data, or use the server-side code execution capabilities to move laterally. Joomla has released a patched version; all site operators should update immediately.

*Covered in: nvd — 3 posts across 1 source*
- [CVE-2026-48898 — Privilege escalation via com_users batch (CVSS 9.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-48898)
- [CVE-2026-48899 — Privilege escalation via com_users batch (CVSS 9.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-48899)
- [CVE-2026-48904 — Privilege escalation via com_users group management (CVSS 9.8)](https://nvd.nist.gov/vuln/detail/CVE-2026-48904)

## 5. KubeVirt — Symlink Attack Escapes Kubernetes Namespace to Host Filesystem (CVE-2026-7374, CVSS 9.9)
**Why it matters:** An authenticated OpenShift or KubeVirt user with only namespace-level edit permissions — the typical access a developer has in a shared cluster — can exploit this to escape their tenant boundary and read or write arbitrary files on the Kubernetes node host, including certificates, service account tokens, and secrets.

CVE-2026-7374 scores CVSS 9.9, reflecting both the severity of impact and the low privilege required. The vulnerability is in KubeVirt's virt-handler component, which manages the connection between Kubernetes and virtual machine console sockets. When attaching to a VM console, virt-handler performs insufficient symlink validation: an attacker can swap the expected console socket with a symlink pointing to any arbitrary file on the underlying node. Once connected, they gain read/write access to that target path — including node-level credentials that could compromise the entire cluster's control plane. A patch has been released. OpenShift and self-hosted KubeVirt operators should update the virt-handler component immediately and audit recent console session activity for any anomalous symlink usage.

*Covered in: nvd — 1 post across 1 source*
- [CVE-2026-7374 — KubeVirt virt-handler symlink attack / namespace escape (CVSS 9.9)](https://nvd.nist.gov/vuln/detail/CVE-2026-7374)

## Signal stats
- Total items processed: 120
- New (post-dedup): 118
- Clusters formed: ~72
- Top 5 selected from: 72 candidate clusters
