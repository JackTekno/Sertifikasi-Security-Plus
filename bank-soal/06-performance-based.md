# Soal Performa (Performance-Based Questions)

Di ujian SY0-701, sebagian soal berbentuk **PBQ**: Anda diminta mengonfigurasi, mencocokkan, mengurutkan, atau menganalisis, bukan sekadar memilih A/B/C/D. Latihan di bawah ini meniru gaya tersebut. Kerjakan di kertas atau file terpisah, lalu bandingkan dengan **jawaban model**.

> Tips: pada PBQ asli, baca instruksi dengan teliti (misalnya "pilih tiga" atau "urutkan"), dan jangan menghabiskan terlalu banyak waktu pada satu PBQ.

## PBQ 1 — Kategori dan tipe kontrol
**Skenario:** Sebuah perusahaan menerapkan kontrol berikut:
1. Badge reader pada pintu data center
2. Kebijakan penggunaan kata sandi yang ditandatangani CFO
3. Kamera CCTV di lobi
4. Restore database dari backup setelah insiden
5. Pelatihan phishing tahunan
6. Pagar setinggi tiga meter
7. Peringatan "aplikasi ini diblokir oleh kebijakan perusahaan" saat pengguna membuka aplikasi terlarang
8. Isolasi VLAN untuk mesin produksi yang tidak bisa dipatch

**Tugas:** Untuk setiap kontrol, tentukan **kategori** (technical, managerial, operational, physical) dan **tipe** (preventive, deterrent, detective, corrective, compensating, directive).

**Jawaban model:**

| # | Kategori | Tipe |
|---|---|---|
| 1 | Technical | Preventive |
| 2 | Managerial | Directive |
| 3 | Physical | Detective (juga deterrent) |
| 4 | Operational | Corrective |
| 5 | Managerial | Directive (preventive terhadap perilaku) |
| 6 | Physical | Deterrent |
| 7 | Technical | Preventive |
| 8 | Technical | Compensating |

**Pembahasan:** Kategori menunjukkan "dari mana" kontrol berasal (orang/proses, teknologi, fisik), sedangkan tipe menunjukkan "apa efeknya". Satu kontrol dapat punya lebih dari satu tipe; pilih yang paling dominan sesuai konteks.

## PBQ 2 — Urutan incident response
**Skenario:** Ransomware terdeteksi menyebar di 40 endpoint dan dua file server. Anda mendapat daftar tindakan berikut (tidak berurutan):

- A. Memulihkan data dari backup dan memverifikasi integritas
- B. Mengisolasi segmen jaringan yang terinfeksi dan mematikan berbagi file
- C. Menghapus malware, menghapus persistence, dan mereset kredensial
- D. Menganalisis log, sampel malware, dan menentukan ruang lingkup
- E. Menyusun laporan akhir dan memperbarui playbook
- F. Mempersiapkan tim, kontak, dan akses ke tool forensik sebelum insiden
- G. Mendeteksi alert EDR dan mengonfirmasi insiden

**Tugas:** Urutkan tindakan sesuai fase IR dan beri nama fasenya.

**Jawaban model:**
**F** (Preparation) → **G** (Detection & Analysis) → **D** (Analysis/scope) → **B** (Containment) → **C** (Eradication) → **A** (Recovery) → **E** (Post-incident/Lessons learned).

**Pembahasan:** Deteksi belum tentu sama dengan analisis; konfirmasi dan penentuan ruang lingkup harus mendahului containment agar tidak memutus bukti. Eradication dilakukan setelah penyebaran berhenti, dan recovery harus divalidasi sebelum layanan dibuka penuh.

## PBQ 3 — Desain aturan firewall untuk aplikasi tiga tier
**Skenario:** Anda memiliki:
- ALB publik `203.0.113.10` (load balancer)
- Web server `10.10.1.20`
- App server `10.10.2.30`
- Database `10.10.3.40`

**Tugas:** Tulis aturan firewall minimum (source → destination, port, protokol, aksi) agar pengguna internet dapat mengakses aplikasi dan setiap tier hanya dapat berbicara dengan tier berikutnya.

**Jawaban model:**

| # | Source | Destination | Port/Proto | Aksi |
|---|---|---|---|---|
| 1 | Any | 203.0.113.10 | 443/TCP | Allow |
| 2 | ALB | 10.10.1.20 | 443/TCP | Allow |
| 3 | 10.10.1.20 | 10.10.2.30 | 8080/TCP | Allow |
| 4 | 10.10.2.30 | 10.10.3.40 | 5432/TCP | Allow |
| 5 | Any | Any | Any | Deny |

**Pembahasan:** Prinsipnya **default deny** + least privilege: database tidak boleh menerima koneksi langsung dari internet atau dari web tier, dan tidak ada aturan "any → any" di dalam. Untuk produksi, tambahkan logging, aturan egress terbatas, dan akses administrasi melalui bastion.

## PBQ 4 — Cocokkan indikator dengan serangan
**Skenario:** Temuan dari SIEM:
1. `UNION SELECT` pada parameter `id` di URL
2. Ribuan percobaan login dengan password sama ke banyak akun
3. Login sukses dari dua negara dalam 10 menit
4. ARP reply berulang yang memetakan gateway ke MAC baru
5. Lonjakan trafik UDP ke port 53 dari banyak sumber ke satu host
6. Proses `powershell.exe` mengambil script dari IP eksternal dan berjalan di memori

**Tugas:** Cocokkan setiap temuan dengan jenis serangan dan satu kontrol mitigasi utama.

**Jawaban model:**
1. **SQL injection** → parameterized query + WAF.
2. **Password spraying** → lockout/rate limiting + MFA.
3. **Impossible travel / credential theft** → risk-based auth, cabut sesi, MFA.
4. **ARP poisoning** → dynamic ARP inspection + port security.
5. **DNS amplification DDoS** → rate limiting, anycast/scrubbing, tutup resolver terbuka.
6. **Fileless malware** → EDR, script block logging, PowerShell constrained mode.

**Pembahasan:** Indikator harus dikaitkan dengan vektor dan kontrol yang spesifik. Menjawab "pasang antivirus" untuk fileless menunjukkan pemahaman yang kurang; EDR dan logging perilaku lebih tepat.

## PBQ 5 — Pilih respons risiko
**Skenario:** Sebuah perusahaan memiliki lima risiko:
1. Kebocoran data pelanggan yang dapat ditanggung polis asuransi siber
2. Layanan legacy berisiko tinggi yang bisa dihentikan tanpa dampak bisnis
3. Kerentanan pada server internal yang dapat ditambal minggu depan
4. Risiko kecil pada printer lobby yang biaya kontrolnya lebih besar dari dampaknya
5. Risiko pihak ketiga yang tidak dapat dikendalikan, tetapi kontraknya mengalihkan tanggung jawab finansial

**Tugas:** Tentukan respons risiko (avoid, mitigate, transfer, accept) dan jelaskan alasannya.

**Jawaban model:**
1. **Transfer** — asuransi memindahkan dampak finansial.
2. **Avoid** — hentikan layanan.
3. **Mitigate** — patch dan kontrol tambahan.
4. **Accept** — dokumentasikan dengan persetujuan pemilik risiko.
5. **Transfer** (sebagian) — klausul kontrak/indemnification; risiko operasional tetap dipantau.

**Pembahasan:** Respons harus sesuai konteks; "accept" bukan berarti mengabaikan, melainkan keputusan terdokumentasi berdasarkan analisis biaya-manfaat. Risiko residual tetap dicatat di risk register.

## PBQ 6 — Cocokkan konsep kriptografi
**Skenario:** Kebutuhan berikut:
1. Membuktikan dokumen tidak berubah dan berasal dari pengirim tertentu
2. Memulihkan data bila admin lupa password enkripsi
3. Menyimpan password pengguna agar tidak bisa dibalik dan tahan rainbow table
4. Mengganti nomor kartu kredit pada sistem kasir agar tidak menyimpan PAN asli
5. Melindungi data saat dikirim antara browser dan server
6. Menyimpan kunci root CA secara offline dan tahan manipulasi

**Tugas:** Pilih konsep/alat yang paling tepat untuk setiap kebutuhan.

**Jawaban model:**
1. **Digital signature** (private key pengirim + verifikasi public key).
2. **Key escrow**.
3. **Hashing + salt** (misalnya Argon2/bcrypt).
4. **Tokenization**.
5. **TLS**.
6. **HSM offline**.

**Pembahasan:** Perhatikan tujuan: integritas + autentikasi + non-repudiation = signature; kerahasiaan = enkripsi; verifikasi satu arah = hash. Tokenization berbeda dari enkripsi karena nilai asli tidak dapat direkonstruksi tanpa vault.

## PBQ 7 — Analisis header email
**Skenario:** Email mengaku dari `cfo@perusahaan.co.id` memiliki hasil autentikasi:
- SPF: **fail**
- DKIM: **none**
- DMARC: **none**
- Reply-To: `cfo.perusahaan@gmail.com`

**Tugas:** Sebutkan tiga indikasi phishing dan tiga tindakan yang harus diambil.

**Jawaban model:**
Indikasi: (1) SPF gagal berarti pengirim tidak berwenang untuk domain tersebut; (2) tidak ada DKIM/DMARC sehingga tidak ada jaminan integritas dan kebijakan; (3) Reply-To berbeda domain — ciri BEC.

Tindakan: (1) jangan membalas atau membuka lampiran; (2) laporkan ke tim keamanan dan teruskan header asli; (3) verifikasi melalui nomor telepon yang diketahui, serta blokir pengirim/domain di gateway.

**Pembahasan:** SPF memeriksa IP pengirim, DKIM memverifikasi tanda tangan, DMARC memberi kebijakan dan alignment. Ketiganya saling melengkapi; ketiadaan DMARC membuat email palsu lebih mudah lolos.

## PBQ 8 — Hardening Wi-Fi kantor
**Skenario:** Kantor memiliki jaringan korporat untuk karyawan dan jaringan tamu. Perangkat lama masih mendukung WPA2. Anda harus mengonfigurasi SSID korporat dan tamu.

**Tugas:** Tentukan konfigurasi minimum untuk SSID korporat dan tamu.

**Jawaban model:**
- **Korporat:** WPA3-Enterprise (transisi WPA2-Enterprise bila perlu), 802.1X/EAP-TLS dengan sertifikat perangkat, RADIUS, PMF (802.11w) aktif, WPS dimatikan, SSID terpisah + VLAN, management frame protection, dan logging ke RADIUS.
- **Tamu:** SSID terpisah, WPA2/WPA3-PSK dengan password yang dirotasi, client isolation, bandwidth limit, captive portal, dan akses hanya ke internet.

**Pembahasan:** Jangan gunakan PSK untuk karyawan karena kunci bersama tidak dapat dicabut per pengguna. Segmentasi VLAN dan client isolation mencegah tamu mengakses resource internal.

## PBQ 9 — Cocokkan protokol IAM
**Skenario:** Kebutuhan:
1. SSO antar organisasi dengan assertion XML
2. Aplikasi pihak ketiga mengakses API pengguna dengan izin terbatas
3. Autentikasi pengguna pada aplikasi mobile modern dengan token identitas
4. AAA untuk perangkat jaringan dengan enkripsi seluruh payload
5. AAA untuk Wi-Fi dengan dukungan luas
6. Query direktori untuk atribut pengguna

**Tugas:** Cocokkan dengan protokol yang tepat.

**Jawaban model:**
1. **SAML 2.0**
2. **OAuth 2.0**
3. **OpenID Connect (OIDC)**
4. **TACACS+**
5. **RADIUS**
6. **LDAP**

**Pembahasan:** OAuth bukan protokol autentikasi; OIDC menambahkan layer identitas di atas OAuth. RADIUS mengenkripsi password saja, TACACS+ seluruh body dan memisahkan AAA.

## PBQ 10 — RTO, RPO, dan strategi backup
**Skenario:** Sistem penjualan:
- Kehilangan data maksimum yang dapat diterima: 15 menit
- Waktu pemulihan maksimum: 2 jam
- Backup penuh harian pukul 01.00 ke tape, disimpan di lokasi yang sama

**Tugas:** (a) Tentukan RTO dan RPO. (b) Jelaskan mengapa strategi backup saat ini tidak memenuhi. (c) Usulkan perbaikan.

**Jawaban model:**
(a) RTO = 2 jam; RPO = 15 menit.
(b) Backup harian berarti RPO hingga 24 jam, jauh melebihi 15 menit; tape di lokasi yang sama tidak terlindung dari bencana dan rawan ikut terenkripsi ransomware.
(c) Terapkan transaction log/continuous backup (atau replikasi), simpan salinan offsite/offline (3-2-1), uji restore berkala, dan siapkan site/warm standby agar RTO 2 jam tercapai.

**Pembahasan:** RPO menentukan frekuensi backup; RTO menentukan arsitektur pemulihan. Backup yang belum diuji restore tidak dapat dijamin memenuhi RTO.

## PBQ 11 — Shared responsibility matrix
**Skenario:** Perusahaan menggunakan IaaS untuk VM, PaaS untuk aplikasi internal, dan SaaS untuk email.

**Tugas:** Tentukan siapa (Customer/Provider) yang bertanggung jawab atas: patch OS, patch aplikasi email, konfigurasi IAM, keamanan fisik data center, enkripsi data pelanggan, dan patch runtime PaaS.

**Jawaban model:**

| Item | IaaS | PaaS | SaaS |
|---|---|---|---|
| Patch OS | Customer | Provider | Provider |
| Patch aplikasi email | — | — | Provider |
| Konfigurasi IAM | Customer | Customer | Customer |
| Keamanan fisik | Provider | Provider | Provider |
| Enkripsi data pelanggan | Customer | Customer | Customer (shared) |
| Patch runtime | — | Provider | Provider |

**Pembahasan:** Semakin tinggi model layanan, semakin banyak tanggung jawab operasional yang diambil penyedia, tetapi **identitas, akses, dan data** selalu menjadi tanggung jawab pelanggan.

## PBQ 12 — Urutan volatilitas bukti
**Skenario:** Sebuah server Linux dicurigai sebagai host pivot penyerang. Anda harus mengumpulkan bukti tanpa merusaknya.

**Tugas:** Urutkan sumber bukti dari paling volatil ke paling persisten, dan sebutkan tiga tindakan pertama yang harus dilakukan.

**Jawaban model:**
Urutan: **register/CPU cache → RAM (proses, koneksi, kunci) → swap/pagefile → disk (file, log) → arsip/backup → konfigurasi jaringan/printout**.

Tiga tindakan pertama:
1. Isolasi host dari jaringan (jangan matikan) dan dokumentasikan waktu.
2. Ambil image memori dengan tool forensik dan catat hash.
3. Buat image disk bit-by-bit (write blocker), catat chain of custody.

**Pembahasan:** Mematikan host menghilangkan memori dan koneksi aktif. Urutan volatilitas memastikan bukti yang paling mudah hilang diambil lebih dulu, dan setiap langkah harus tercatat untuk menjaga integritas bukti.
