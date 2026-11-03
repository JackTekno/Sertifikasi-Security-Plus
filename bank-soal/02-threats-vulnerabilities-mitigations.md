# Domain 2 — Threats, Vulnerabilities, and Mitigations (22%)

Domain dengan bobot terbesar kedua. Fokus pada **siapa penyerangnya**, **lewat mana mereka masuk**, **kerentanan apa yang dipakai**, **indikator serangan**, dan **cara mitigasinya**. Banyak soal berbentuk skenario "paling mungkin" (MOST likely).

## Soal 1
**Objektif:** 2.1
**Tipe:** Skenario
**Soal:** A group has spent two years developing custom malware and has repeatedly targeted government research networks in multiple countries. The group is well funded, patient, and interested in stealing intellectual property rather than money. Which threat actor does this BEST describe?

- A. Insider threat
- B. Hacktivist
- C. Nation-state
- D. Unskilled attacker

**Jawaban:** C
**Pembahasan:** Ciri **nation-state/APT**: pendanaan besar, malware kustom, kampanye jangka panjang, dan motif spionase. Hacktivist termotivasi ideologi dan biasanya aksinya lebih terbuka; unskilled attacker memakai tool yang sudah ada; insider berada di dalam organisasi.

## Soal 2
**Objektif:** 2.1
**Tipe:** Skenario
**Soal:** An attacker defaces a company website with a political message and leaks internal emails to protest the company's supply contracts. Which motivation BEST explains this behavior?

- A. Ideology
- B. Revenge
- C. Financial gain
- D. Espionage

**Jawaban:** A
**Pembahasan:** Aksi defacement dan kebocoran data untuk menyampaikan pesan politik adalah ciri **hacktivist** yang dimotivasi ideologi. Pencurian data untuk dijual atau spionase tidak sesuai dengan pola ini.

## Soal 3
**Objektif:** 2.1
**Tipe:** Skenario
**Soal:** A systems administrator resigns and, during the last week of employment, copies the customer database to a personal cloud drive. Which threat actor category applies?

- A. Insider threat
- B. Shadow IT
- C. Hacktivist
- D. Organized crime

**Jawaban:** A
**Pembahasan:** **Insider threat** adalah orang dengan akses sah yang menyalahgunakan aksesnya, termasuk karyawan yang akan keluar. Shadow IT lebih mengarah pada penggunaan teknologi tanpa persetujuan, bukan pencurian data dengan niat jahat.

## Soal 4
**Objektif:** 2.1
**Tipe:** Skenario
**Soal:** A criminal group operates a ransomware-as-a-service platform, recruits affiliates, and demands payment in cryptocurrency. Which threat actor is described?

- A. Unskilled attacker
- B. Nation-state
- C. Organized crime
- D. Hacktivist

**Jawaban:** C
**Pembahasan:** **Organized crime** menjalankan serangan untuk keuntungan finansial dengan struktur bisnis, termasuk model RaaS dan afiliasi. Nation-state fokus pada spionase/geo-politik, hacktivist pada ideologi.

## Soal 5
**Objektif:** 2.1
**Tipe:** Skenario
**Soal:** A marketing team signs up for an unsanctioned cloud file-sharing service to collaborate with an agency, bypassing IT review. Which term describes this situation?

- A. Insider fraud
- B. Data sovereignty
- C. Shadow IT
- D. Supply chain attack

**Jawaban:** C
**Pembahasan:** **Shadow IT** adalah penggunaan perangkat, aplikasi, atau layanan TI tanpa persetujuan/pengetahuan departemen TI. Risikonya: data tidak terklasifikasi, tidak terpantau DLP, dan sulit diaudit.

## Soal 6
**Objektif:** 2.1
**Tipe:** Skenario
**Soal:** An individual with limited technical skill downloads a ready-made exploit kit and runs it against random IP addresses. Which term BEST describes this actor?

- A. Insider threat
- B. Organized crime
- C. Advanced persistent threat
- D. Unskilled attacker

**Jawaban:** D
**Pembahasan:** **Unskilled attacker** (script kiddie) memakai tool siap pakai tanpa memahami mekanismenya, biasanya untuk mencari korban acak. ATP/APT justru memiliki keahlian dan sumber daya tinggi.

## Soal 7
**Objektif:** 2.1
**Tipe:** Perbandingan
**Soal:** Which attribute MOST clearly distinguishes a nation-state actor from organized crime?

- A. The use of malware
- B. The level of resources, sophistication, and patience in pursuing strategic goals
- C. The use of the internet
- D. The targeting of private companies

**Jawaban:** B
**Pembahasan:** Keduanya bisa memakai malware dan menyerang perusahaan. Yang membedakan adalah **sumber daya, sofistikasi, dan kesabaran** (kampanye bertahun-tahun) untuk tujuan strategis seperti spionase.

## Soal 8
**Objektif:** 2.1
**Tipe:** Definisi
**Soal:** Which pair correctly matches a threat actor with its PRIMARY motivation?

- A. Organized crime — monetary gain
- B. Nation-state — website defacement for fun
- C. Hacktivist — financial fraud
- D. Insider — ideological protest

**Jawaban:** A
**Pembahasan:** **Organized crime** dimotivasi uang (ransomware, penipuan, penjualan data). Hacktivist = ideologi, nation-state = spionase/strategi, insider bisa bermacam-macam (uang, dendam, kelalaian).

## Soal 9
**Objektif:** 2.2
**Tipe:** Skenario
**Soal:** Attackers compromise a managed service provider (MSP) and use its remote management tooling to deploy malware to dozens of the MSP's customers at once. Which threat vector is this?

- A. Watering hole
- B. Direct physical access
- C. Removable media
- D. Supply chain

**Jawaban:** D
**Pembahasan:** Serangan lewat **supply chain** memanfaatkan kepercayaan pada vendor/MSP/perangkat lunak pihak ketiga. Satu kompromi di penyedia dapat menyebar ke banyak pelanggan sekaligus.

## Soal 10
**Objektif:** 2.2
**Tipe:** Skenario
**Soal:** Users who mistype `examp1e.com` for `example.com` are redirected to a site that harvests credentials. Which technique is this?

- A. DNS tunneling
- B. Typosquatting
- C. Watering hole
- D. Domain fronting

**Jawaban:** B
**Pembahasan:** **Typosquatting** mendaftarkan domain yang mirip (salah ketik, karakter mirip) untuk menipu pengguna. Watering hole adalah situs sah yang dikompromikan untuk menyerang kelompok tertentu.

## Soal 11
**Objektif:** 2.2
**Tipe:** Skenario
**Soal:** Security researchers learn that a website frequently visited by employees of a defense contractor was compromised to serve exploit code only to visitors from that contractor's IP range. Which attack is this?

- A. Pretexting
- B. Whaling
- C. Spear phishing
- D. Watering hole

**Jawaban:** D
**Pembahasan:** **Watering hole** menyerang situs yang biasa dikunjungi target, lalu menyuntikkan malware khusus untuk kelompok tersebut. Spear phishing tetap berbasis pesan yang dikirim langsung ke korban.

## Soal 12
**Objektif:** 2.2
**Tipe:** Skenario
**Soal:** An attacker spoofs the CEO's email address and asks the finance director to urgently wire funds to a new supplier account. Which attack is this?

- A. Vishing
- B. Pharming
- C. Whaling
- D. Business email compromise

**Jawaban:** D
**Pembahasan:** **BEC** memalsukan identitas eksekutif/rekan bisnis untuk memicu transfer dana atau perubahan data pembayaran. Whaling adalah phishing yang menyasar eksekutif sebagai korban, bukan memalsukan eksekutif untuk menipu staf.

## Soal 13
**Objektif:** 2.2
**Tipe:** Skenario
**Soal:** Customers receive a text message claiming their parcel is held at customs, with a link to a credential-harvesting page. Which vector is used?

- A. Smishing
- B. Phishing
- C. Pretexting
- D. Vishing

**Jawaban:** A
**Pembahasan:** **Smishing** adalah phishing melalui SMS. Vishing melalui panggilan suara, phishing umumnya email, dan pretexting adalah teknik membangun alasan palsu (bisa dipakai di semua kanal).

## Soal 14
**Objektif:** 2.2
**Tipe:** Skenario
**Soal:** An attacker calls the help desk, claims to be a new employee locked out of the VPN, and asks the agent to reset the MFA token. Which technique is this?

- A. Vishing and pretexting
- B. Shoulder surfing
- C. Credential harvesting
- D. Tailgating

**Jawaban:** A
**Pembahasan:** Panggilan telepon (vishing) dengan cerita palsu yang meyakinkan (pretexting) untuk melewati prosedur help desk. Mitigasinya: verifikasi identitas melalui kanal terpisah dan prosedur reset MFA yang ketat.

## Soal 15
**Objektif:** 2.2
**Tipe:** Skenario
**Soal:** An employee finds a USB drive labeled "Payroll 2025" in the parking lot and plugs it into a workstation. Which threat vector is demonstrated?

- A. Unsupported system
- B. Removable media
- C. Supply chain
- D. Open service port

**Jawaban:** B
**Pembahasan:** **Removable media** (USB) dapat berisi malware atau melakukan HID attack saat dicolok. Kontrol: disable autorun, endpoint protection, dan kebijakan larangan memakai media tak dikenal.

## Soal 16
**Objektif:** 2.2
**Tipe:** Skenario
**Soal:** A database server is reachable from the internet on port 3389 with the default administrator password unchanged. Which two threat vectors are combined?

- A. Open service port and default credentials
- B. Removable media and unpatched software
- C. Wireless and Bluetooth
- D. Shadow IT and insider threat

**Jawaban:** A
**Pembahasan:** Port 3389 (RDP) yang terbuka ke internet memperluas attack surface, dan **default credentials** memudahkan akses. Mitigasi: tutup port, gunakan VPN/jump host, dan ganti kredensial default.

## Soal 17
**Objektif:** 2.2
**Tipe:** Skenario
**Soal:** A production server still runs an operating system that no longer receives security updates. Which term and risk BEST apply?

- A. Shadow IT; the system is unsupported by IT
- B. Zero-day; unknown vulnerability with no patch
- C. End-of-life system; known vulnerabilities will never be patched
- D. Legacy protocol; encryption is weaker

**Jawaban:** C
**Pembahasan:** **EOL/unsupported system** tidak lagi menerima patch, sehingga kerentanan yang sudah diketahui publik akan tetap terbuka. Zero-day adalah kerentanan yang belum diketahui vendor, berbeda konsep.

## Soal 18
**Objektif:** 2.2
**Tipe:** Skenario
**Soal:** An attacker within Bluetooth range connects to an unpaired headset and extracts contact data. Which wireless attack vector is this?

- A. Bluejacking
- B. Bluesnarfing
- C. Deauthentication
- D. Evil twin

**Jawaban:** B
**Pembahasan:** **Bluesnarfing** adalah pencurian data melalui koneksi Bluetooth, sedangkan bluejacking hanya mengirim pesan tak diminta. Deauthentication dan evil twin adalah serangan Wi-Fi.

## Soal 19
**Objektif:** 2.2
**Tipe:** Skenario
**Soal:** An employee downloads an invoice document from a supplier's website and opens it. The document contains a macro that downloads a payload when the user clicks "Enable Content". Which threat vector is this?

- A. Message-based
- B. Image-based
- C. Voice-based
- D. File-based

**Jawaban:** D
**Pembahasan:** **File-based vector** adalah file berbahaya (dokumen bermakro, installer, arsip) yang dieksekusi pengguna, baik dari unduhan maupun media lepas. **Message-based vector** menekankan kanal pesan seperti email, SMS, atau IM yang membawa tautan/lampiran.

## Soal 20
**Objektif:** 2.2
**Tipe:** Skenario
**Soal:** A software vendor's build server is compromised, and the attacker inserts malicious code into a signed update that customers install automatically. Which vector is used?

- A. Watering hole
- B. Open service port
- C. Unsupported system
- D. Supply chain (software provider)

**Jawaban:** D
**Pembahasan:** Ini adalah serangan **supply chain** melalui penyedia perangkat lunak: pelanggan mempercayai update bertanda tangan dari vendor. Pertahanan: verifikasi hash/tanda tangan, code signing yang aman, dan pemantauan perilaku setelah update.

## Soal 21
**Objektif:** 2.3
**Tipe:** Skenario
**Soal:** An attacker sends more input to a program than its fixed-size buffer can hold, overwriting the return address and executing shellcode. Which vulnerability is this?

- A. SQL injection
- B. Race condition
- C. Buffer overflow
- D. Directory traversal

**Jawaban:** C
**Pembahasan:** **Buffer overflow** menulis melebihi batas memori yang dialokasikan sehingga menimpa area lain, termasuk return address. Mitigasi: input validation, safe languages, ASLR, dan DEP.

## Soal 22
**Objektif:** 2.3
**Tipe:** Skenario
**Soal:** A web application checks whether a file exists and then opens it, but an attacker swaps the file with a symbolic link between the two operations. Which vulnerability class is this?

- A. Privilege escalation
- B. Injection
- C. TOCTOU race condition
- D. Buffer overflow

**Jawaban:** C
**Pembahasan:** **Race condition TOCTOU** (time-of-check to time-of-use) terjadi karena keadaan berubah antara pemeriksaan dan penggunaan. Mitigasi: operasi atomik, file locking, dan validasi ulang.

## Soal 23
**Objektif:** 2.3
**Tipe:** Skenario
**Soal:** A login form returns the error `You have an error in your SQL syntax near 'OR 1=1'`. Which vulnerability is MOST likely present?

- A. Cross-site scripting
- B. SQL injection
- C. Cross-site request forgery
- D. Directory traversal

**Jawaban:** B
**Pembahasan:** Pesan error SQL yang membocorkan sintaks menunjukkan input pengguna masuk ke query tanpa parameterisasi — **SQL injection**. Mitigasi utama: prepared statements/parameterized queries dan least privilege pada akun database.

## Soal 24
**Objektif:** 2.3
**Tipe:** Skenario
**Soal:** A comment field stores raw HTML, and a submitted `<script>` tag executes in every visitor's browser. Which vulnerability is this?

- A. Stored XSS
- B. CSRF
- C. Clickjacking
- D. Reflected XSS

**Jawaban:** A
**Pembahasan:** **Stored (persistent) XSS** menyimpan payload di server sehingga tereksekusi pada semua pengunjung. Reflected XSS hanya muncul dari parameter yang dipantulkan kembali ke satu korban.

## Soal 25
**Objektif:** 2.3
**Tipe:** Skenario
**Soal:** A user logged in to a banking site visits a malicious page that silently submits a fund-transfer request using the user's existing session cookie. Which attack is this?

- A. CSRF
- B. Session fixation
- C. SQL injection
- D. XSS

**Jawaban:** A
**Pembahasan:** **CSRF** memanfaatkan sesi korban yang masih aktif untuk mengirim permintaan yang tidak diinginkan. Mitigasi: anti-CSRF token, SameSite cookie, dan verifikasi origin.

## Soal 26
**Objektif:** 2.3
**Tipe:** Skenario
**Soal:** A request for `https://shop.example.com/download?file=../../../../etc/passwd` returns the contents of the system password file. Which vulnerability is exploited?

- A. XML external entity
- B. Directory traversal
- C. Command injection
- D. Insecure direct object reference

**Jawaban:** B
**Pembahasan:** **Directory traversal** (path traversal) memakai `../` untuk keluar dari direktori yang diizinkan. Mitigasi: validasi path, gunakan allow list nama file, dan jalankan dengan hak minimal.

## Soal 27
**Objektif:** 2.3
**Tipe:** Skenario
**Soal:** Malicious code running inside a guest VM exploits a hypervisor flaw to execute on the host. Which vulnerability is this?

- A. Container breakout via misconfiguration
- B. Resource reuse
- C. VM escape
- D. VM sprawl

**Jawaban:** C
**Pembahasan:** **VM escape** menembus isolasi hypervisor sehingga penyerang menguasai host dan VM lain. Mitigasi: patch hypervisor, matikan fitur tidak perlu, dan batasi akses manajemen.

## Soal 28
**Objektif:** 2.3
**Tipe:** Skenario
**Soal:** An organization has 400 virtual machines but only 180 are documented and patched. Many are unused but still running. Which risk is this?

- A. Resource reuse
- B. Cross-site scripting
- C. VM escape
- D. VM sprawl

**Jawaban:** D
**Pembahasan:** **VM sprawl** adalah pertumbuhan VM tak terkendali tanpa inventaris dan patch, sehingga muncul sistem tak terkelola. Solusinya: inventaris otomatis, lifecycle management, dan decommissioning.

## Soal 29
**Objektif:** 2.3
**Tipe:** Skenario
**Soal:** A developer stores backups in a cloud bucket and sets it to public-read for convenience. Which vulnerability is this?

- A. Weak encryption
- B. Supply chain
- C. Zero-day
- D. Cloud misconfiguration

**Jawaban:** D
**Pembahasan:** **Misconfiguration** cloud (bucket publik, IAM terlalu longgar, logging mati) adalah penyebab kebocoran data paling umum di cloud. Mitigasi: secure baseline, policy as code, dan pemindaian konfigurasi.

## Soal 30
**Objektif:** 2.3
**Tipe:** Definisi
**Soal:** Which statement BEST describes a zero-day vulnerability?

- A. A vulnerability unknown to the vendor, for which no patch exists
- B. A vulnerability in open-source software only
- C. A vulnerability exploited exactly once
- D. A vulnerability that has been patched but not yet deployed

**Jawaban:** A
**Pembahasan:** **Zero-day** adalah celah yang belum diketahui pembuat software, sehingga belum ada patch pada saat dieksploitasi. Mitigasi tidak bisa mengandalkan patching, melainkan deteksi perilaku, segmentasi, dan virtual patching.

## Soal 31
**Objektif:** 2.3
**Tipe:** Skenario
**Soal:** An Android user enables installation of apps from unknown sources to get a free premium app, which then steals banking credentials. Which two risks are present?

- A. Rooting and supply chain
- B. VM escape and sideloading
- C. Sideloading and malicious application
- D. Jailbreaking and bootkit

**Jawaban:** C
**Pembahasan:** **Sideloading** (memasang aplikasi dari luar toko resmi) membuka jalan bagi aplikasi berbahaya. **Jailbreaking/rooting** adalah membuka kunci sistem operasi, berbeda dari sekadar sideloading.

## Soal 32
**Objektif:** 2.3
**Tipe:** Skenario
**Soal:** A router model has not received firmware updates for four years and has known remotely exploitable flaws. Which vulnerability category applies?

- A. Application injection
- B. Cryptographic downgrade
- C. Mobile jailbreaking
- D. Hardware end-of-life and unpatched firmware

**Jawaban:** D
**Pembahasan:** Perangkat **EOL** dengan firmware usang tidak lagi menerima patch dan sering memiliki kerentanan publik. Mitigasi: ganti perangkat, isolasi VLAN, dan batasi akses manajemen.

## Soal 33
**Objektif:** 2.3
**Tipe:** Skenario
**Soal:** An application encrypts credit card numbers with a hard-coded AES key stored in the source repository. Which weakness is this?

- A. Certificate expiration
- B. Improper key storage
- C. Weak cipher algorithm choice
- D. Insufficient hashing rounds

**Jawaban:** B
**Pembahasan:** Kunci yang di-hardcode di source code dapat dibaca siapa pun yang memiliki akses repo — ini **improper key storage**. Kunci seharusnya disimpan di KMS/HSM dan dirotasi.

## Soal 34
**Objektif:** 2.3
**Tipe:** Skenario
**Soal:** Malicious code is injected into a running process by forcing it to load an attacker-controlled library. Which technique is this?

- A. Buffer overflow
- B. Logic bomb
- C. Privilege escalation
- D. DLL injection

**Jawaban:** D
**Pembahasan:** **DLL injection** memaksa proses yang sah memuat library berbahaya sehingga kode berjalan dalam konteks proses tersebut dan sulit terdeteksi. Ini sering dipakai malware untuk persistence dan menghindari deteksi.

## Soal 35
**Objektif:** 2.3
**Tipe:** Skenario
**Soal:** An old virtual machine is deleted and its disk reallocated to a new tenant, who is able to recover fragments of the previous tenant's data. Which risk applies?

- A. Resource reuse
- B. VM sprawl
- C. Data sovereignty
- D. VM escape

**Jawaban:** A
**Pembahasan:** **Resource reuse** terjadi ketika resource (disk, memori, IP) dialokasikan ulang tanpa sanitasi menyeluruh. Mitigasi: enkripsi disk, secure wipe, dan sanitasi sebelum reuse.

## Soal 36
**Objektif:** 2.3
**Tipe:** Skenario
**Soal:** A network switch received from a hardware supplier contains an undocumented cellular modem that beacons out. Which vulnerability category is this?

- A. Firmware downgrade
- B. Misconfiguration
- C. Zero-day
- D. Supply chain (hardware provider)

**Jawaban:** D
**Pembahasan:** **Hardware supply chain** compromise menanam komponen atau backdoor pada perangkat fisik. Mitigasi: vendor vetting, inspeksi perangkat, dan pemantauan lalu lintas keluar.

## Soal 37
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** Users report that files on a shared drive have been renamed with a `.locked` extension and a text file demands cryptocurrency. Which malware type is this?

- A. Rootkit
- B. Spyware
- C. Worm
- D. Ransomware

**Jawaban:** D
**Pembahasan:** **Ransomware** mengenkripsi data dan meminta tebusan. Mitigasi: backup offline teruji, segmentasi, dan deteksi perilaku enkripsi massal.

## Soal 38
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** Malware spreads to every host on a network within minutes without any user interaction, exploiting a single unpatched SMB flaw. Which malware type is this?

- A. Worm
- B. Virus
- C. Logic bomb
- D. Trojan

**Jawaban:** A
**Pembahasan:** **Worm** menyebar sendiri melalui jaringan tanpa interaksi pengguna. Virus membutuhkan eksekusi pengguna/host, trojan menyamar sebagai program sah, logic bomb menunggu pemicu.

## Soal 39
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** A compromised host shows no signs of malware in Task Manager, yet attackers retain administrative access across reboots. Which malware type is MOST likely?

- A. Adware
- B. Ransomware
- C. Keylogger
- D. Rootkit

**Jawaban:** D
**Pembahasan:** **Rootkit** bersembunyi di kernel/firmware dan memanipulasi tampilan sistem sehingga prosesnya tidak terlihat. Deteksinya sering memerlukan boot dari media tepercaya atau pemindaian offline.

## Soal 40
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** A workstation periodically sends keystrokes and clipboard contents to an external IP address. Which malware behavior is this?

- A. Ransomware
- B. Logic bomb
- C. Keylogger
- D. Cryptominer

**Jawaban:** C
**Pembahasan:** **Keylogger** merekam input pengguna (dan sering clipboard) untuk mencuri kredensial. Indikatornya: koneksi keluar periodik, proses tak dikenal, dan alert EDR pada API hooking keyboard.

## Soal 41
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** A terminated employee's script deletes all HR records when it detects that his account has been disabled. Which malware type is this?

- A. Backdoor
- B. Trojan
- C. Logic bomb
- D. Worm

**Jawaban:** C
**Pembahasan:** **Logic bomb** adalah kode yang dieksekusi saat kondisi tertentu terpenuhi (waktu, event, status akun). Pencegahannya: code review, kontrol perubahan, dan pencabutan akses segera saat terminasi.

## Soal 42
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** Multiple internal hosts beacon to the same external IP every 60 seconds using HTTPS, and that IP is a known command-and-control server. Which malware infrastructure is present?

- A. Sinkhole
- B. Proxy chain
- C. Botnet
- D. Honeypot

**Jawaban:** C
**Pembahasan:** Pola **beaconing** periodik ke C2 menunjukkan host terinfeksi dan tergabung dalam **botnet**. Tindakan: isolasi host, blokir IOC, dan analisis lateral movement.

## Soal 43
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** A server's CPU usage jumps to 100 percent and the security team finds a process mining cryptocurrency. Which malware category applies?

- A. Ransomware
- B. Rootkit
- C. Spyware
- D. Cryptomalware

**Jawaban:** D
**Pembahasan:** **Cryptomalware/cryptojacking** memakai resource korban untuk menambang kripto; indikatornya konsumsi CPU/GPU tinggi, tagihan cloud naik, dan koneksi ke pool mining.

## Soal 44
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** An investigation finds no malicious executable on disk, but a PowerShell process loaded a script directly into memory and established outbound connections. Which malware characteristic is this?

- A. Polymorphic malware
- B. Armored virus
- C. Multipartite virus
- D. Fileless malware

**Jawaban:** D
**Pembahasan:** **Fileless malware** berjalan di memori memakai tool sah (PowerShell, WMI) sehingga tidak ada file untuk dipindai signature. Deteksi mengandalkan EDR, script block logging, dan analisis perilaku.

## Soal 45
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** A wireless survey finds two access points with the same SSID, but one has a stronger signal and a different BSSID near the lobby. Which attack is MOST likely?

- A. Deauthentication
- B. WPS brute force
- C. MAC flooding
- D. Evil twin

**Jawaban:** D
**Pembahasan:** **Evil twin** adalah AP palsu dengan SSID sama untuk menipu klien agar terhubung dan menyerahkan kredensial/lalu lintas. Mitigasi: WPA3-Enterprise, certificate validation, dan wireless IDS.

## Soal 46
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** Wireless clients are repeatedly disconnected and forced to reconnect to an attacker's access point. Which attack is being used?

- A. DNS poisoning
- B. VLAN hopping
- C. Deauthentication attack
- D. ARP poisoning

**Jawaban:** C
**Pembahasan:** **Deauthentication attack** mengirim frame deauth palsu sehingga klien terputus dan mencoba terhubung ulang — sering dikombinasikan dengan evil twin. Mitigasi: 802.11w (PMF) dan WPA3.

## Soal 47
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** An attacker on the same LAN sends forged ARP replies so that traffic destined for the gateway goes through the attacker's machine. Which attack is this?

- A. On-path attack via BGP hijack
- B. ARP poisoning
- C. DNS poisoning
- D. MAC flooding

**Jawaban:** B
**Pembahasan:** **ARP poisoning** memetakan IP gateway ke MAC penyerang sehingga terjadi on-path (MITM) di jaringan lokal. Mitigasi: dynamic ARP inspection, port security, dan segmentasi.

## Soal 48
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** Users typing `www.bank.com` are directed to an attacker's IP address because a compromised DNS record was modified. Which attack is this?

- A. ARP poisoning
- B. Typosquatting
- C. Domain fronting
- D. DNS poisoning

**Jawaban:** D
**Pembahasan:** **DNS poisoning** (cache poisoning) mengubah pemetaan nama domain ke IP penyerang. Mitigasi: DNSSEC, resolver tepercaya, dan pemantauan perubahan record.

## Soal 49
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** An attacker configures a switch port as a trunk and gains access to traffic from multiple VLANs. Which attack is this?

- A. MAC flooding
- B. ARP poisoning
- C. DNS tunneling
- D. VLAN hopping

**Jawaban:** D
**Pembahasan:** **VLAN hopping** (double tagging/switch spoofing) melewati isolasi VLAN. Mitigasi: matikan DTP, set port access secara eksplisit, dan gunakan VLAN native yang tidak dipakai.

## Soal 50
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** An attacker floods a switch with thousands of fake MAC addresses until it starts broadcasting all frames to every port. Which attack is this?

- A. ARP poisoning
- B. VLAN hopping
- C. MAC flooding
- D. MAC cloning

**Jawaban:** C
**Pembahasan:** **MAC flooding** membanjiri tabel CAM switch sehingga switch berperilaku seperti hub dan lalu lintas dapat disadap. Mitigasi: port security dengan batas MAC dan monitoring.

## Soal 51
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** A user connects to a hotel Wi-Fi and later discovers the captive portal was operated by an attacker who intercepted all traffic. Which attack occurred?

- A. On-path attack
- B. SQL injection
- C. DDoS
- D. Privilege escalation

**Jawaban:** A
**Pembahasan:** **On-path (MITM)** menempatkan penyerang di antara klien dan tujuan. Mitigasi: HTTPS dengan certificate pinning/HSTS, VPN, dan tidak mengabaikan peringatan sertifikat.

## Soal 52
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** An attacker captures a valid authentication token and resends it later to gain access. Which attack is this?

- A. Brute force
- B. Session fixation
- C. Replay attack
- D. Pass-the-hash

**Jawaban:** C
**Pembahasan:** **Replay attack** menggunakan ulang kredensial/token yang sah. Mitigasi: timestamp, nonce, sequence number, dan token berumur pendek (short-lived).

## Soal 53
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** A web service is overwhelmed by traffic from a large botnet, exhausting bandwidth so that legitimate users cannot connect. Which attack type is this?

- A. Application-layer DoS
- B. SYN flood only
- C. Smurf attack
- D. Volumetric DDoS

**Jawaban:** D
**Pembahasan:** Serangan **volumetric** membanjiri bandwidth (misalnya UDP/ICMP amplification). Application-layer DoS menghabiskan resource aplikasi (misalnya HTTP request mahal), dan SYN flood adalah salah satu teknik DDoS, bukan kategori yang paling tepat di sini.

## Soal 54
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** An attacker tries the password `Spring2025!` against 500 different accounts, staying under the lockout threshold for each account. Which attack is this?

- A. Credential stuffing
- B. Dictionary attack
- C. Rainbow table attack
- D. Password spraying

**Jawaban:** D
**Pembahasan:** **Password spraying** mencoba sedikit password umum ke banyak akun untuk menghindari lockout. Credential stuffing memakai pasangan username/password hasil kebocoran; dictionary attack menebak banyak password pada satu akun.

## Soal 55
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** Attackers use a list of username/password pairs leaked from another company to log in to your service, succeeding on accounts where users reused passwords. Which attack is this?

- A. Pass-the-hash
- B. Credential stuffing
- C. Password spraying
- D. Brute force

**Jawaban:** B
**Pembahasan:** **Credential stuffing** memanfaatkan kredensial bocor dan kebiasaan reuse password. Mitigasi: cek terhadap breach corpus, MFA, dan passwordless.

## Soal 56
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** An attacker steals a password hash database and uses precomputed tables to recover common passwords quickly. Which attack and mitigation pair is CORRECT?

- A. Rainbow table; salting passwords
- B. Brute force; longer passwords
- C. Password spraying; account lockout
- D. Dictionary attack; MFA

**Jawaban:** A
**Pembahasan:** Tabel **rainbow** memetakan hash ke password yang sudah dihitung sebelumnya; **salt** unik per pengguna membuat tabel tersebut tidak berguna. MFA dan panjang password tetap penting, tetapi bukan penangkal utama serangan offline ini.

## Soal 57
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** Web server logs show requests containing `' UNION SELECT username, password FROM users--`. Which attack is occurring?

- A. Command injection
- B. SQL injection
- C. Cross-site scripting
- D. Directory traversal

**Jawaban:** B
**Pembahasan:** Pola `UNION SELECT` adalah **SQL injection** untuk mengekstrak data dari tabel lain. Mitigasi: parameterized query, WAF sebagai lapisan tambahan, dan least privilege akun DB.

## Soal 58
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** A user account successfully authenticates from Jakarta and, 20 minutes later, from Frankfurt. Which indicator is this?

- A. Account lockout
- B. Resource consumption
- C. Impossible travel
- D. Concurrent session usage

**Jawaban:** C
**Pembahasan:** **Impossible travel** menandakan kredensial dipakai dari dua lokasi yang tidak mungkin dijangkau dalam waktu tersebut — indikasi akun dicuri. Perlu verifikasi dan pemeriksaan MFA.

## Soal 59
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** A single user account shows five active VPN sessions from different countries at the same time. Which indicator is present?

- A. Missing logs
- B. Concurrent session usage
- C. Impossible travel
- D. Account lockout

**Jawaban:** B
**Pembahasan:** **Concurrent session usage** di luar kebiasaan menandakan kredensial dibagikan atau dicuri. Kebijakan biasanya membatasi jumlah sesi simultan dan memicu verifikasi tambahan.

## Soal 60
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** An account is locked after 40 failed logins in two minutes, followed by a help desk call from someone claiming to be the user. Which attack might this indicate?

- A. Ransomware
- B. DNS poisoning
- C. Logic bomb
- D. Brute force or targeted lockout, possibly social engineering follow-up

**Jawaban:** D
**Pembahasan:** Lonjakan login gagal menunjukkan **brute force** atau sengaja mengunci akun agar korban menghubungi help desk (untuk menipu reset MFA). Ini juga indikator social engineering lanjutan.

## Soal 61
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** A SIEM alert shows a sudden spike in outbound traffic from a database server to an unknown external IP at 3 a.m., while the server's normal traffic is internal only. Which indicator is this?

- A. Account lockout
- B. Blocked content
- C. Missing logs
- D. Resource consumption and unusual data flow

**Jawaban:** D
**Pembahasan:** Lonjakan trafik keluar yang tidak wajar dapat menandakan **exfiltration** atau C2. Indikator lain seperti resource consumption (CPU/disk) juga bisa menyertai pencurian data atau cryptomining.

## Soal 62
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** An administrator notices that firewall logs for a specific 30-minute window are absent, although the firewall remained online. Which indicator should be investigated?

- A. Missing logs, possibly indicating tampering
- B. Out-of-cycle logging
- C. Account lockout
- D. Blocked content

**Jawaban:** A
**Pembahasan:** **Missing logs** bisa berarti log dihapus, logging dimatikan, atau penyerang menutupi jejak. Bandingkan dengan sumber log lain (SIEM, syslog server) untuk memastikan.

## Soal 63
**Objektif:** 2.4
**Tipe:** Skenario
**Soal:** An organization discovers screenshots of its internal documents posted on a public paste site, along with a claim of stolen data. Which indicator category is this?

- A. Concurrent session
- B. Resource inaccessibility
- C. Published or documented data
- D. Out-of-cycle logging

**Jawaban:** C
**Pembahasan:** **Published/documented** berarti penyerang mempublikasikan bukti akses atau data curian (leak site, paste site) untuk menekan korban. Ini juga sering menjadi awal negosiasi ransomware.

## Soal 64
**Objektif:** 2.5
**Tipe:** Skenario
**Soal:** A legacy manufacturing system cannot be patched. The team places it in its own VLAN with a firewall that permits only one needed protocol to one server. Which mitigation is this?

- A. Segmentation
- B. Isolation
- C. Decommissioning
- D. Patching

**Jawaban:** A
**Pembahasan:** **Segmentation** membatasi lalu lintas antar zona; sistem tetap beroperasi tetapi attack surface-nya kecil. **Isolation** biasanya berarti memisahkan sepenuhnya (misalnya air-gap atau VM terisolasi) tanpa konektivitas produksi.

## Soal 65
**Objektif:** 2.5
**Tipe:** Skenario
**Soal:** An organization allows only approved executables to run on endpoints; all others are blocked by hash. Which mitigation is this?

- A. EDR quarantine
- B. Application allow list
- C. Application block list
- D. Host-based firewall

**Jawaban:** B
**Pembahasan:** **Allow list** hanya mengizinkan program yang terdaftar (biasanya berdasarkan hash atau sertifikat), sehingga malware baru otomatis diblokir. Block list mudah dilewati karena hanya menolak yang sudah diketahui.

## Soal 66
**Objektif:** 2.5
**Tipe:** Skenario
**Soal:** Before a laptop is granted network access, the switch port checks its patch level and antivirus status through an agent. Which technology is this?

- A. NAC
- B. DLP
- C. MDM
- D. SIEM

**Jawaban:** A
**Pembahasan:** **NAC** (Network Access Control) memeriksa postur perangkat sebelum memberi akses, dan dapat menempatkan perangkat tidak patuh di VLAN remediasi. MDM mengelola perangkat, bukan mengontrol akses jaringan.

## Soal 67
**Objektif:** 2.5
**Tipe:** Skenario
**Soal:** A security team wants to detect and automatically respond to malicious behavior such as process injection on endpoints, with the ability to isolate a host. Which tool is MOST appropriate?

- A. Antivirus signature scanner
- B. NetFlow analyzer
- C. HIDS
- D. EDR

**Jawaban:** D
**Pembahasan:** **EDR** mengumpulkan telemetri perilaku, mendeteksi teknik seperti process injection, dan dapat mengisolasi endpoint. HIDS hanya mendeteksi perubahan file/log, antivirus berbasis signature mudah dilewati malware baru.

## Soal 68
**Objektif:** 2.5
**Tipe:** Skenario
**Soal:** A company must prevent employees from emailing unencrypted customer ID numbers to personal accounts. Which control is MOST appropriate?

- A. Full-disk encryption
- B. DLP
- C. NAC
- D. WAF

**Jawaban:** B
**Pembahasan:** **DLP** memeriksa konten (pola nomor identitas) dan memblokir/ mengarantina pengiriman ke tujuan tidak sah. FDE melindungi data saat perangkat hilang, bukan saat dikirim keluar.

## Soal 69
**Objektif:** 2.5
**Tipe:** Skenario
**Soal:** A suspicious email attachment must be detonated to observe its behavior before release. Which mitigation technique is used?

- A. Honeypot
- B. Tokenization
- C. Sandboxing
- D. Quarantine

**Jawaban:** C
**Pembahasan:** **Sandboxing** menjalankan file di lingkungan terisolasi dan memantau perilakunya (network callbacks, file changes). Quarantine hanya menahan pesan, bukan menganalisis perilaku.

## Soal 70
**Objektif:** 2.5
**Tipe:** Skenario
**Soal:** A new server is deployed from a hardened image that disables unnecessary services, enforces password rules, and configures logging. Which concept is this?

- A. Secure baseline
- B. Change management
- C. Least privilege
- D. Network segmentation

**Jawaban:** A
**Pembahasan:** **Secure baseline** adalah konfigurasi acuan yang sudah diperkuat dan dipakai untuk semua deployment. Baseline harus diverifikasi berkala (configuration enforcement) agar tidak melenceng.

## Soal 71
**Objektif:** 2.5
**Tipe:** Skenario
**Soal:** A server reaches end of life and is removed from the network, its disks are wiped, and its DNS records are deleted. Which mitigation is being performed?

- A. Segmentation
- B. Decommissioning
- C. Patching
- D. Isolation

**Jawaban:** B
**Pembahasan:** **Decommissioning** menghapus sistem dari produksi secara aman: cabut akses, sanitasi media, hapus record, dan perbarui inventaris. Ini mengurangi attack surface permanen.

## Soal 72
**Objektif:** 2.5
**Tipe:** Skenario
**Soal:** A company must support personal phones for email while enforcing encryption and remote wipe on those devices. Which solution is MOST appropriate?

- A. MDM with BYOD policy
- B. NAC
- C. DLP
- D. VDI only

**Jawaban:** A
**Pembahasan:** **MDM** menerapkan kebijakan perangkat (enkripsi, PIN, remote wipe) dan dapat memisahkan data kerja dari data pribadi pada perangkat **BYOD**. NAC hanya mengontrol akses jaringan.

## Soal 73
**Objektif:** 2.5
**Tipe:** Skenario
**Soal:** An administrator wants to block lateral SMB traffic between workstations while allowing it to the file server only. Which control is MOST efficient?

- A. DLP
- B. Full-disk encryption
- C. Host-based firewall rules
- D. Application allow list

**Jawaban:** C
**Pembahasan:** **Host-based firewall** dapat membatasi lalu lintas per host tanpa mengubah topologi jaringan. Segmentasi jaringan juga bisa, tetapi untuk aturan per-endpoint, host firewall lebih langsung.

## Soal 74
**Objektif:** 2.5
**Tipe:** Skenario
**Soal:** Sensitive cryptographic keys must be processed inside a CPU-protected area isolated from the main operating system. Which technology is this?

- A. HSM
- B. Vault
- C. Secure enclave
- D. TPM

**Jawaban:** C
**Pembahasan:** **Secure enclave** adalah area terisolasi di dalam prosesor yang melindungi kode dan kunci dari OS utama. TPM adalah chip terpisah untuk menyimpan kunci/measurement, HSM adalah perangkat eksternal.
