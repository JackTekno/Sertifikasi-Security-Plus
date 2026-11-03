# Domain 3 — Security Architecture (18%)

Domain ini menguji kemampuan memilih **arsitektur dan kontrol yang tepat** untuk cloud, jaringan, data, dan ketahanan sistem. Banyak soal berbentuk "which is the BEST/MOST appropriate" — perhatikan kata kunci seperti *shared responsibility*, *segmentation*, *RTO*, dan *fail-open*.

## Soal 1
**Objektif:** 3.1
**Tipe:** Skenario
**Soal:** A company moves its email service to a SaaS provider. Under the shared responsibility model, which task remains the CUSTOMER's responsibility?

- A. Patching the email application servers
- B. Managing user accounts, access, and data classification
- C. Securing the physical data center
- D. Maintaining the hypervisor

**Jawaban:** B
**Pembahasan:** Pada **SaaS**, penyedia mengelola aplikasi, OS, dan infrastruktur; pelanggan tetap bertanggung jawab atas **identitas, akses, dan data** (termasuk klasifikasi dan berbagi data). Patch aplikasi dan hypervisor menjadi tanggung jawab penyedia.

## Soal 2
**Objektif:** 3.1
**Tipe:** Skenario
**Soal:** A team deploys virtual machines in IaaS. Which security task is the CUSTOMER responsible for?

- A. Physical security of the data center
- B. Patching the guest operating system and configuring security groups
- C. Maintaining the storage firmware
- D. Securing the network backbone

**Jawaban:** B
**Pembahasan:** Pada **IaaS**, pelanggan mengelola OS tamu, patch, konfigurasi keamanan, dan aturan firewall/security group. Lapisan fisik, hypervisor, dan backbone berada pada penyedia.

## Soal 3
**Objektif:** 3.1
**Tipe:** Skenario
**Soal:** A development team uses a platform where the provider manages the runtime and OS, while the team only uploads code and configures environment variables. Which service model is this?

- A. On-premises
- B. IaaS
- C. PaaS
- D. SaaS

**Jawaban:** C
**Pembahasan:** **PaaS** menyediakan runtime dan platform terkelola; tim hanya bertanggung jawab atas aplikasi, konfigurasi, dan data. IaaS menyediakan VM mentah, SaaS menyediakan aplikasi jadi.

## Soal 4
**Objektif:** 3.1
**Tipe:** Skenario
**Soal:** A company runs sensitive workloads in its own data center but uses a public cloud for seasonal capacity. Which architecture is this?

- A. Community cloud
- B. Private cloud
- C. Multi-cloud
- D. Hybrid cloud

**Jawaban:** D
**Pembahasan:** **Hybrid cloud** menggabungkan on-premises dengan cloud publik. Multi-cloud berarti memakai dua atau lebih penyedia cloud publik, sedangkan private cloud sepenuhnya dedicated untuk satu organisasi.

## Soal 5
**Objektif:** 3.1
**Tipe:** Skenario
**Soal:** An organization defines its cloud network entirely in Terraform templates stored in Git, and changes are applied through a pipeline. Which concept is this?

- A. Microservices
- B. Software-defined perimeter
- C. Infrastructure as code
- D. Serverless computing

**Jawaban:** C
**Pembahasan:** **IaC** memungkinkan infrastruktur didefinisikan dan direview seperti kode, sehingga konsisten dan dapat diaudit. Risikonya: kesalahan konfigurasi menyebar cepat, sehingga pipeline perlu pemeriksaan keamanan (policy as code).

## Soal 6
**Objektif:** 3.1
**Tipe:** Skenario
**Soal:** A company runs short-lived functions that execute only when an event occurs, with no server to patch. Which security consideration is MOST important?

- A. Function-level permissions and secrets management
- B. Hardening the hypervisor
- C. Managing disk encryption keys
- D. Patching the underlying operating system

**Jawaban:** A
**Pembahasan:** Pada **serverless**, OS dikelola penyedia sehingga risiko bergeser ke **izin fungsi (IAM), secret, dan dependency**. Fungsi dengan izin berlebihan adalah kesalahan umum yang dapat dieksploitasi.

## Soal 7
**Objektif:** 3.1
**Tipe:** Skenario
**Soal:** An application is split into small independent services that communicate over APIs and are deployed separately. Which architecture is this?

- A. Mainframe
- B. Client-server
- C. Monolithic
- D. Microservices

**Jawaban:** D
**Pembahasan:** **Microservices** memecah aplikasi menjadi layanan kecil dengan API. Keuntungan: isolasi kegagalan dan deployment independen; risikonya: permukaan API luas, autentikasi antar-layanan rumit, dan perlu service mesh/mTLS.

## Soal 8
**Objektif:** 3.1
**Tipe:** Skenario
**Soal:** Two containers on the same host are compromised through a kernel vulnerability, allowing the attacker to affect the other container. Which architectural weakness does this illustrate?

- A. Containers share the host kernel
- B. Containers do not support encryption
- C. Containers cannot use network policies
- D. Containers require a hypervisor for isolation

**Jawaban:** A
**Pembahasan:** **Container** berbagi kernel host, sehingga isolasinya lebih lemah daripada VM. Mitigasi: minimal base image, tidak menjalankan sebagai root, seccomp/AppArmor, dan pemisahan host untuk beban kerja sensitif.

## Soal 9
**Objektif:** 3.1
**Tipe:** Skenario
**Soal:** A hospital's infusion pumps run an embedded real-time operating system that must respond within milliseconds. Which security constraint is MOST significant?

- A. The devices do not support Wi-Fi
- B. The devices store no data
- C. The devices cannot tolerate standard patching downtime or latency-heavy controls
- D. The devices use outdated web browsers

**Jawaban:** C
**Pembahasan:** Sistem **embedded/RTOS** menuntut determinisme waktu dan ketersediaan tinggi, sehingga patch dan agen keamanan berat sulit diterapkan. Pendekatannya: segmentasi, kontrol jaringan, dan pemantauan pasif.

## Soal 10
**Objektif:** 3.1
**Tipe:** Skenario
**Soal:** A power plant uses SCADA to control physical equipment. Which security objective is prioritized above confidentiality in this environment?

- A. Non-repudiation
- B. Data minimization
- C. Anonymity
- D. Availability and safety

**Jawaban:** D
**Pembahasan:** Pada **ICS/SCADA**, gangguan dapat membahayakan nyawa dan peralatan, sehingga **availability dan safety** menjadi prioritas, diikuti integritas. Confidentiality tetap penting, tetapi bukan prioritas utama.

## Soal 11
**Objektif:** 3.1
**Tipe:** Skenario
**Soal:** A 5G deployment uses network slicing to give emergency services guaranteed bandwidth separate from consumer traffic. Which security benefit does network slicing provide?

- A. Automatic encryption of all application data
- B. Elimination of the need for authentication
- C. Replacement for endpoint detection
- D. Isolation between logical networks with distinct policies

**Jawaban:** D
**Pembahasan:** **Network slicing** memisahkan jaringan logis dengan karakteristik dan kebijakan masing-masing, sehingga gangguan atau serangan pada satu slice tidak otomatis meluas. Enkripsi aplikasi tetap diperlukan.

## Soal 12
**Objektif:** 3.1
**Tipe:** Skenario
**Soal:** A company wants to centralize routing decisions in a controller while switches forward traffic based on those decisions. Which architecture is described?

- A. Virtual private network
- B. Network access control
- C. Spanning tree protocol
- D. Software-defined networking

**Jawaban:** D
**Pembahasan:** **SDN** memisahkan control plane (controller) dari data plane (switch), sehingga kebijakan dapat diprogram terpusat. Kontroler menjadi aset kritis yang harus diamankan.

## Soal 13
**Objektif:** 3.2
**Tipe:** Skenario
**Soal:** A firewall is configured to allow all traffic if its rule engine crashes, to avoid business interruption. Which failure mode is this, and what is the risk?

- A. Fail-over; traffic goes to a standby device
- B. Fail-closed; traffic is blocked until fixed
- C. Fail-open; all traffic is allowed during failure
- D. Fail-safe; traffic is inspected twice

**Jawaban:** C
**Pembahasan:** **Fail-open** mengutamakan ketersediaan: saat perangkat gagal, semua lalu lintas diizinkan sehingga kebijakan keamanan hilang. **Fail-closed** lebih aman tetapi berisiko memutus layanan.

## Soal 14
**Objektif:** 3.2
**Tipe:** Skenario
**Soal:** An IDS is connected to a mirrored switch port and only receives copies of traffic, so it cannot block an attack. Which deployment characteristic is this?

- A. Transparent proxy
- B. Inline
- C. Passive (tap/SPAN)
- D. Fail-closed

**Jawaban:** C
**Pembahasan:** IDS biasanya **passive** (menerima salinan trafik dari TAP/SPAN) dan hanya memberi alert. IPS ditempatkan **inline** sehingga dapat memblokir paket secara real time.

## Soal 15
**Objektif:** 3.2
**Tipe:** Skenario
**Soal:** A security team must inspect encrypted HTTPS traffic for data leaks. Which capability is required?

- A. Port mirroring only
- B. NetFlow sampling
- C. TLS inspection with a trusted internal CA
- D. DNSSEC validation

**Jawaban:** C
**Pembahasan:** **TLS inspection** melakukan dekripsi, inspeksi, lalu enkripsi ulang; perangkat klien harus mempercayai CA internal yang dipakai untuk menandatangani ulang. Ini menimbulkan isu privasi dan harus dikecualikan untuk kategori tertentu (misalnya perbankan).

## Soal 16
**Objektif:** 3.2
**Tipe:** Skenario
**Soal:** Which device provides application-layer protection against SQL injection and cross-site scripting for a public web application?

- A. Load balancer
- B. Router with ACL
- C. Layer 4 firewall
- D. WAF

**Jawaban:** D
**Pembahasan:** **WAF** (Web Application Firewall) memeriksa payload HTTP dan dapat memblokir pola serangan aplikasi. Firewall layer 4 hanya melihat IP/port, load balancer membagi trafik, ACL router memfilter alamat/port.

## Soal 17
**Objektif:** 3.2
**Tipe:** Skenario
**Soal:** A company replaces separate firewall, IPS, and antivirus gateway appliances with a single device that combines these functions. Which term BEST describes it?

- A. HIDS
- B. UTM
- C. WAF
- D. Reverse proxy

**Jawaban:** B
**Pembahasan:** **UTM** (Unified Threat Management) menggabungkan beberapa fungsi keamanan dalam satu perangkat. Kelemahannya: satu titik kegagalan dan potensi penurunan performa saat semua fitur aktif.

## Soal 18
**Objektif:** 3.2
**Tipe:** Skenario
**Soal:** Remote workers must access internal applications without exposing them directly to the internet, and access should be granted per application after device and identity checks. Which solution is BEST?

- A. Traditional site-to-site VPN
- B. ZTNA
- C. Port forwarding on the firewall
- D. RDP gateway with MFA only

**Jawaban:** B
**Pembahasan:** **ZTNA** memberikan akses per aplikasi berdasarkan identitas dan postur perangkat, tanpa mengekspos jaringan internal. VPN klasik memberi akses jaringan luas (network-level) setelah terhubung.

## Soal 19
**Objektif:** 3.2
**Tipe:** Skenario
**Soal:** An organization wants to connect two branch offices over the internet with encrypted traffic at the network layer, supporting multiple protocols. Which technology is MOST appropriate?

- A. IPsec VPN
- B. SSH tunnel per user
- C. DNSSEC
- D. TLS on each application

**Jawaban:** A
**Pembahasan:** **IPsec** melindungi lalu lintas pada layer network dan mendukung banyak protokol dalam satu tunnel (mode tunnel untuk site-to-site). TLS hanya melindungi aplikasi tertentu, SSH untuk sesi administratif.

## Soal 20
**Objektif:** 3.2
**Tipe:** Skenario
**Soal:** A cloud-first company wants to combine network and security functions (SWG, CASB, firewall, ZTNA) delivered as a service at the edge. Which architecture is this?

- A. SASE
- B. SD-WAN only
- C. DMZ
- D. VDI

**Jawaban:** A
**Pembahasan:** **SASE** menggabungkan SD-WAN dengan layanan keamanan cloud (secure web gateway, CASB, ZTNA, firewall-as-a-service). SD-WAN hanya mengoptimalkan konektivitas WAN.

## Soal 21
**Objektif:** 3.2
**Tipe:** Skenario
**Soal:** Administrators must manage servers without exposing SSH to the internet. Which architecture is MOST appropriate?

- A. Public RDP with IP allow list
- B. Jump host/bastion in a management subnet with MFA
- C. Direct SSH with password authentication
- D. Port knocking only

**Jawaban:** B
**Pembahasan:** **Jump host/bastion** terpusat di subnet manajemen, dengan MFA, logging, dan akses terbatas. Ini mengurangi attack surface dibandingkan mengekspos SSH/RDP langsung.

## Soal 22
**Objektif:** 3.2
**Tipe:** Skenario
**Soal:** A security architect must place a public web server so that it can be reached from the internet but cannot initiate connections to the internal database subnet. Which design is BEST?

- A. Put the web server on the internal LAN with a host firewall
- B. Put the database in the DMZ with the web server
- C. Use NAT to hide the web server
- D. Put the web server in a DMZ with rules allowing only required outbound flows

**Jawaban:** D
**Pembahasan:** **DMZ** memisahkan sistem yang dapat diakses publik dari jaringan internal, dengan aturan ketat untuk koneksi keluar. Menempatkan database di DMZ justru meningkatkan risiko.

## Soal 23
**Objektif:** 3.2
**Tipe:** Skenario
**Soal:** An organization needs to monitor all traffic between two internal segments without affecting latency or risking a single point of failure. Which deployment is MOST appropriate?

- A. Host-based firewall
- B. Inline IPS
- C. Passive sensor on a TAP
- D. Transparent proxy

**Jawaban:** C
**Pembahasan:** **TAP/passive sensor** menyalin trafik tanpa berada di jalur data, sehingga tidak menambah latensi atau titik kegagalan. Konsekuensinya, sensor tidak dapat memblokir trafik.

## Soal 24
**Objektif:** 3.2
**Tipe:** Perbandingan
**Soal:** Which statement about agent-based versus agentless security monitoring is CORRECT?

- A. Agent-based cannot detect file changes
- B. Agentless requires kernel drivers on every host
- C. Agent-based collects detailed host telemetry but requires software on each endpoint; agentless relies on network or API data
- D. Agentless provides better endpoint process visibility than agent-based

**Jawaban:** C
**Pembahasan:** **Agent-based** memberi visibilitas mendalam (proses, file, registry) tetapi perlu dipasang dan dirawat di setiap host. **Agentless** memakai data jaringan/API, lebih mudah diterapkan tetapi kurang detail.

## Soal 25
**Objektif:** 3.3
**Tipe:** Definisi
**Soal:** Which data classification label typically requires the HIGHEST level of protection?

- A. Confidential
- B. Sensitive
- C. Extremely sensitive
- D. Public

**Jawaban:** C
**Pembahasan:** Dalam skema umum SY0-701, urutan dari paling sensitif: **extremely sensitive > sensitive > confidential > private > public**. Extremely sensitive mencakup data yang kebocorannya dapat menyebabkan kerugian besar (misalnya rahasia dagang inti).

## Soal 26
**Objektif:** 3.3
**Tipe:** Skenario
**Soal:** A company must ensure that customer data stored in a cloud region in Germany does not leave the EU. Which concept applies?

- A. Data minimization
- B. Data masking
- C. Data retention
- D. Data sovereignty

**Jawaban:** D
**Pembahasan:** **Data sovereignty** mengharuskan data tunduk pada hukum negara tempat data berada, sehingga lokasi penyimpanan dan replikasi harus dibatasi. Ini memengaruhi pilihan region cloud dan penyedia.

## Soal 27
**Objektif:** 3.3
**Tipe:** Skenario
**Soal:** A support portal shows only the last four digits of a customer's card number. Which technique is this?

- A. Tokenization
- B. Data masking
- C. Hashing
- D. Anonymization

**Jawaban:** B
**Pembahasan:** **Data masking** menyamarkan sebagian data sehingga tetap terlihat formatnya tetapi tidak dapat dipakai. Tokenization mengganti seluruh nilai dengan token yang dipetakan di vault.

## Soal 28
**Objektif:** 3.3
**Tipe:** Skenario
**Soal:** A payment processor replaces card numbers with random tokens, keeping the mapping in a secure vault. Which benefit is PRIMARY?

- A. The token has no value if stolen, reducing PCI scope
- B. The token can be reversed by anyone
- C. The token shortens the card number for storage
- D. The token encrypts the entire database

**Jawaban:** A
**Pembahasan:** **Tokenization** membuat data curian tidak berguna tanpa akses ke vault, dan dapat mengurangi cakupan kepatuhan (PCI DSS). Token memang dapat dipetakan kembali, tetapi hanya oleh sistem berwenang.

## Soal 29
**Objektif:** 3.3
**Tipe:** Skenario
**Soal:** A research dataset must remain usable for analytics but cannot identify individuals even if combined with other datasets. Which technique is MOST appropriate?

- A. Anonymization
- B. Encryption
- C. Tokenization
- D. Salting

**Jawaban:** A
**Pembahasan:** **Anonymization** menghapus atau menggeneralisasi identitas sehingga data tidak dapat dikaitkan kembali ke individu. Enkripsi dan tokenization masih memungkinkan re-identifikasi bila kunci/vault tersedia.

## Soal 30
**Objektif:** 3.3
**Tipe:** Skenario
**Soal:** A company keeps customer records indefinitely "just in case". Which policy gap is MOST significant?

- A. No MFA
- B. No data retention and destruction policy
- C. No encryption at rest
- D. No DLP

**Jawaban:** B
**Pembahasan:** Tanpa **retention policy**, data lama menumpuk dan memperbesar dampak kebocoran serta melanggar kewajiban regulasi. Retention harus menentukan berapa lama disimpan dan bagaimana dihancurkan.

## Soal 31
**Objektif:** 3.3
**Tipe:** Skenario
**Soal:** Which method is BEST for destroying data on a failed SSD before disposal?

- A. Quick format
- B. Delete the partition
- C. Overwrite with zeros using software
- D. Physical destruction (shredding) or crypto-erase

**Jawaban:** D
**Pembahasan:** SSD memakai wear leveling sehingga overwrite tidak menjangkau semua sel; **physical destruction** atau **crypto-erase** (jika terenkripsi) adalah pilihan aman. Format cepat dan hapus partisi tidak menghilangkan data.

## Soal 32
**Objektif:** 3.3
**Tipe:** Skenario
**Soal:** A company wants to prevent sensitive files from being uploaded to personal cloud storage while allowing approved services. Which control is MOST appropriate?

- A. SIEM
- B. CASB
- C. NAC
- D. WAF

**Jawaban:** B
**Pembahasan:** **CASB** memberikan visibilitas dan kontrol atas penggunaan cloud (shadow IT), termasuk blokir unggahan ke layanan tidak disetujui. NAC mengontrol akses jaringan perangkat, bukan isi unggahan.

## Soal 33
**Objektif:** 3.3
**Tipe:** Definisi
**Soal:** Which data state is protected by TLS while data moves between a browser and a web server?

- A. Data at rest
- B. Data in transit
- C. Data in use
- D. Data at rest and in use

**Jawaban:** B
**Pembahasan:** **Data in transit** (in motion) dilindungi oleh TLS/IPsec. Data at rest dilindungi enkripsi disk/database, dan data in use dilindungi secure enclave/confidential computing.

## Soal 34
**Objektif:** 3.3
**Tipe:** Skenario
**Soal:** A company collects only the customer's email address for a newsletter, even though it could collect birth date and phone number. Which principle is applied?

- A. Data retention
- B. Non-repudiation
- C. Data minimization
- D. Data sovereignty

**Jawaban:** C
**Pembahasan:** **Data minimization** mengumpulkan hanya data yang benar-benar diperlukan untuk tujuan tertentu, mengurangi risiko dan kewajiban kepatuhan.

## Soal 35
**Objektif:** 3.4
**Tipe:** Skenario
**Soal:** A system must tolerate the failure of one entire data center with no data loss and near-zero downtime. Which solution is MOST appropriate?

- A. Active-active clustering across geographically dispersed sites
- B. Cold site with tape restore
- C. Single site with RAID 5
- D. Warm site with nightly backups

**Jawaban:** A
**Pembahasan:** **Active-active** di dua lokasi menjalankan beban kerja bersamaan sehingga kegagalan satu site tidak menghentikan layanan dan data direplikasi sinkron. Warm site masih butuh waktu pemulihan; RAID hanya melindungi kegagalan disk.

## Soal 36
**Objektif:** 3.4
**Tipe:** Definisi
**Soal:** Which metric represents the maximum acceptable amount of data loss measured in time?

- A. RTO
- B. RPO
- C. MTTR
- D. MTBF

**Jawaban:** B
**Pembahasan:** **RPO** (Recovery Point Objective) menentukan berapa lama data boleh hilang — menentukan frekuensi backup/replikasi. **RTO** adalah waktu maksimal pemulihan layanan, MTTR waktu perbaikan rata-rata, MTBF waktu antar-kegagalan.

## Soal 37
**Objektif:** 3.4
**Tipe:** Skenario
**Soal:** A company requires a recovery site that is fully equipped with hardware and data replicated continuously, ready to take over within minutes. Which site type is this?

- A. Cold site
- B. Warm site
- C. Hot site
- D. Reciprocal site

**Jawaban:** C
**Pembahasan:** **Hot site** memiliki infrastruktur lengkap dan data terbaru sehingga dapat mengambil alih hampir seketika. Warm site punya sebagian infrastruktur, cold site hanya ruang dan daya.

## Soal 38
**Objektif:** 3.4
**Tipe:** Skenario
**Soal:** A team runs an exercise where participants discuss their response to a simulated ransomware scenario without actually invoking systems. Which test is this?

- A. Penetration test
- B. Tabletop exercise
- C. Failover test
- D. Parallel processing test

**Jawaban:** B
**Pembahasan:** **Tabletop exercise** adalah diskusi skenario untuk menguji prosedur, peran, dan komunikasi tanpa mengubah sistem. Failover test benar-benar memindahkan beban kerja, parallel processing menjalankan site sekunder bersamaan.

## Soal 39
**Objektif:** 3.4
**Tipe:** Skenario
**Soal:** Which backup strategy follows the 3-2-1 rule?

- A. Three backups per day, two servers, one cloud
- B. Three administrators, two approvals, one change window
- C. Three sites, two ISPs, one firewall
- D. Three copies, on two different media, with one copy offsite

**Jawaban:** D
**Pembahasan:** **3-2-1**: tiga salinan data, pada dua jenis media berbeda, dengan satu salinan di lokasi terpisah. Tujuannya melindungi dari kegagalan perangkat, bencana, dan ransomware yang menyebar.

## Soal 40
**Objektif:** 3.4
**Tipe:** Skenario
**Soal:** A company wants to avoid dependence on a single cloud provider's availability zone or proprietary services. Which strategies apply?

- A. Data masking and tokenization
- B. Load balancing and caching
- C. Patching and hardening
- D. Geographic dispersion and platform diversity

**Jawaban:** D
**Pembahasan:** **Geographic dispersion** menyebar beban ke beberapa lokasi, dan **platform diversity/multi-cloud** mengurangi risiko kegagalan atau lock-in satu penyedia. Keduanya meningkatkan ketahanan.

## Soal 41
**Objektif:** 3.4
**Tipe:** Skenario
**Soal:** A UPS provides 15 minutes of runtime, and a generator starts automatically after 10 seconds. Which risk remains if the generator fails to start?

- A. Increased bandwidth consumption
- B. Certificate expiration
- C. Extended outage once the UPS battery is depleted
- D. Data corruption from too much power

**Jawaban:** C
**Pembahasan:** UPS hanya jembatan sementara; jika generator gagal, sistem akan mati setelah baterai habis. Karena itu generator harus diuji berkala dan bahan bakar dipantau.

## Soal 42
**Objektif:** 3.4
**Tipe:** Skenario
**Soal:** A load balancer distributes traffic to three web servers, but session data is stored locally on each server, causing users to be logged out randomly. Which solution is MOST appropriate?

- A. Enable RAID on the load balancer
- B. Add a second load balancer
- C. Sticky sessions or shared session store
- D. Increase the number of servers

**Jawaban:** C
**Pembahasan:** Tanpa **sticky sessions** atau penyimpanan sesi terpusat, pengguna berpindah server dan kehilangan sesi. Solusi umum: session store bersama (Redis) atau cookie berbasis token.

## Soal 43
**Objektif:** 3.4
**Tipe:** Skenario
**Soal:** A company must ensure a database can be restored to any point in time within the last 24 hours after accidental deletion. Which capability is required?

- A. Continuous transaction log backups (point-in-time recovery)
- B. RAID 6
- C. Snapshot once per month
- D. Full backups once per week

**Jawaban:** A
**Pembahasan:** **Point-in-time recovery** memakai backup penuh + log transaksi berkelanjutan sehingga database dapat dipulihkan ke detik tertentu. Backup mingguan saja tidak memenuhi kebutuhan 24 jam.

## Soal 44
**Objektif:** 3.4
**Tipe:** Perhitungan
**Soal:** A system has an MTBF of 2,000 hours and an MTTR of 4 hours. What is its approximate availability?

- A. 95.0%
- B. 99.8%
- C. 99.2%
- D. 98.0%

**Jawaban:** B
**Pembahasan:** Availability = MTBF / (MTBF + MTTR) = 2000 / 2004 ≈ **99.8%**. Ini setara downtime sekitar 1,75 jam per tahun.

## Soal 45
**Objektif:** 3.4
**Tipe:** Skenario
**Soal:** During a failover test, the team switches traffic to the secondary site while keeping the primary running, then compares results. Which test type is this?

- A. Simulation
- B. Cold-site activation
- C. Parallel processing
- D. Tabletop

**Jawaban:** C
**Pembahasan:** **Parallel processing** menjalankan sistem primer dan sekunder bersamaan untuk memvalidasi hasil sebelum beralih penuh. Ini lebih aman daripada failover penuh karena primer tetap tersedia.

## Soal 46
**Objektif:** 3.4
**Tipe:** Skenario
**Soal:** A company stores backups on the same SAN as production to simplify recovery. Which principle is violated?

- A. Data minimization
- B. Separation of duties
- C. Geographic separation and offline copy (3-2-1)
- D. Least privilege

**Jawaban:** C
**Pembahasan:** Backup pada sistem yang sama rentan ikut terhapus saat ransomware atau kegagalan storage. Prinsip **3-2-1** membutuhkan salinan di media dan lokasi berbeda, idealnya satu offline/immutable.

## Soal 47
**Objektif:** 3.1
**Tipe:** Skenario
**Soal:** An organization wants to reduce the attack surface of its public API by exposing only required endpoints and validating input at the gateway. Which architecture is MOST appropriate?

- A. API gateway with schema validation, rate limiting, and authentication
- B. Direct exposure of each microservice
- C. VPN for every customer
- D. WAF in monitor-only mode

**Jawaban:** A
**Pembahasan:** **API gateway** memusatkan autentikasi, validasi skema, rate limiting, dan logging, sehingga service internal tidak terekspos langsung. Ini juga memudahkan inventaris endpoint.

## Soal 48
**Objektif:** 3.2
**Tipe:** Skenario
**Soal:** A network architect needs to enforce that only domain-joined, patched devices can reach the finance VLAN, regardless of user credentials. Which combination is MOST appropriate?

- A. Captive portal with email registration
- B. 802.1X with NAC posture assessment and VLAN assignment
- C. WPA2-PSK with a shared password
- D. MAC address allow list only

**Jawaban:** B
**Pembahasan:** **802.1X + NAC** memeriksa identitas perangkat dan postur (domain join, patch) sebelum menempatkannya di VLAN yang tepat. MAC allow list mudah dipalsukan dan tidak memeriksa postur.

## Soal 49
**Objektif:** 3.2
**Tipe:** Multi-select
**Soal:** Which TWO statements describe a fail-closed security device? (Select TWO.)

- A. It prioritizes availability over security
- B. It can cause an outage if the device fails
- C. It allows all traffic during a failure
- D. It is always deployed passively
- E. It blocks traffic when the inspection engine fails

**Jawaban:** B, E
**Pembahasan:** **Fail-closed** memblokir lalu lintas saat terjadi kegagalan sehingga kebijakan tetap terjaga, tetapi berisiko memutus layanan. Fail-open justru mengizinkan semua trafik dan mengutamakan ketersediaan.

## Soal 50
**Objektif:** 3.3
**Tipe:** Multi-select
**Soal:** Which TWO methods can render data unrecoverable before disposal? (Select TWO.)

- A. Quick format
- B. Moving files to the recycle bin
- C. Deleting the partition table
- D. Physical destruction
- E. Cryptographic erase

**Jawaban:** D, E
**Pembahasan:** **Physical destruction** dan **crypto-erase** (menghapus kunci enkripsi) membuat data tidak dapat dipulihkan. Quick format, recycle bin, dan hapus partisi hanya menghapus referensi, bukan isi media.
