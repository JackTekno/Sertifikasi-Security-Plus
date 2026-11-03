# Domain 1 — General Security Concepts (12%)

Domain ini menguji pemahaman Anda tentang **kontrol keamanan**, **konsep fundamental** (CIA triad, zero trust, deception, kriptografi), **change management**, dan **solusi kriptografis**. Bobot ujiannya 12%, tetapi materinya menjadi dasar bagi seluruh domain lain — jangan lewati.

> **Cara pakai:** jawab dulu tanpa melihat kunci. Baru setelah memilih, baca pembahasan. Semua penjelasan ditulis dalam Bahasa Indonesia, sedangkan soal memakai Bahasa Inggris agar terbiasa dengan gaya ujian aslinya.

## Soal 1
**Objektif:** 1.1
**Tipe:** Konsep
**Soal:** A security team deploys a badge reader and biometric scanner at the data center entrance so that only authorized staff can enter. Which control category and control type does this BEST describe?

- A. Managerial, preventive
- B. Technical, preventive
- C. Physical, detective
- D. Operational, deterrent

**Jawaban:** B
**Pembahasan:** Badge reader dan biometric scanner adalah kontrol **technical (logical)** karena berbasis teknologi, dan bersifat **preventive** karena menghentikan akses sebelum terjadi. Kontrol physical adalah seperti pagar, kunci mekanis, atau penjaga; deterrent hanya bertujuan menakuti pelaku, bukan menolak akses.

## Soal 2
**Objektif:** 1.1
**Tipe:** Definisi
**Soal:** Which of the following is the BEST example of a managerial control?

- A. An annual risk assessment performed by the security committee
- B. A motion sensor that triggers an alarm after hours
- C. A honeypot placed in the DMZ to attract attackers
- D. A firewall rule that blocks inbound RDP traffic

**Jawaban:** A
**Pembahasan:** Managerial (administrative) control adalah kontrol berbentuk kebijakan, prosedur, standar, dan proses tata kelola seperti risk assessment. Firewall dan honeypot bersifat technical, sedangkan motion sensor bersifat physical.

## Soal 3
**Objektif:** 1.1
**Tipe:** Skenario
**Soal:** A company wants to discourage employees from attempting to tailgate into a restricted floor. Management installs highly visible cameras, warning signs, and a guard station at the elevator lobby, even though the door itself is already badge-controlled. Which control type is being added?

- A. Corrective
- B. Compensating
- C. Deterrent
- D. Detective

**Jawaban:** C
**Pembahasan:** Kamera yang terlihat jelas, papan peringatan, dan pos penjaga dimaksudkan untuk **mencegah niat** pelaku — itu definisi deterrent. Kontrol corrective memulihkan setelah insiden, compensating menggantikan kontrol yang tidak bisa diterapkan, dan detective hanya mendeteksi (misalnya alarm yang tidak terlihat).

## Soal 4
**Objektif:** 1.1
**Tipe:** Skenario
**Soal:** A hospital runs a legacy MRI workstation that cannot be patched because the vendor no longer supports the operating system. The security team places the workstation on an isolated VLAN with strict firewall rules and restricts access to a jump host. Which control type is this?

- A. Directive
- B. Corrective
- C. Preventive
- D. Compensating

**Jawaban:** D
**Pembahasan:** Karena patch tidak mungkin diterapkan, tim memakai kontrol lain sebagai pengganti — ini **compensating control**. Isolasi jaringan memang bersifat preventive juga, tetapi dalam konteks "menggantikan patch yang tidak tersedia", jawaban yang paling tepat adalah compensating.

## Soal 5
**Objektif:** 1.1
**Tipe:** Skenario
**Soal:** After a ransomware incident, the team wipes the affected servers and restores data from the previous night's backup. Which control type did the restore represent?

- A. Detective
- B. Corrective
- C. Directive
- D. Deterrent

**Jawaban:** B
**Pembahasan:** Restore dari backup memulihkan sistem ke kondisi normal setelah insiden terjadi, sehingga termasuk **corrective**. Detective hanya menemukan masalah, sedangkan deterrent dan directive bekerja sebelum insiden.

## Soal 6
**Objektif:** 1.1
**Tipe:** Definisi
**Soal:** Which control type is represented by a policy that states "employees must lock their screens when leaving their desks"?

- A. Detective
- B. Compensating
- C. Directive
- D. Physical

**Jawaban:** C
**Pembahasan:** **Directive control** mengarahkan perilaku melalui aturan tertulis, kebijakan, atau instruksi. Kebijakan lock screen tidak memblokir secara teknis, tidak mendeteksi, dan bukan kontrol fisik.

## Soal 7
**Objektif:** 1.2
**Tipe:** Skenario
**Soal:** An attacker modifies a wire transfer record in a database. The bank later uses SHA-256 hashes stored alongside each record to prove the data was altered. Which security property is being protected?

- A. Confidentiality
- B. Integrity
- C. Availability
- D. Non-repudiation

**Jawaban:** B
**Pembahasan:** Hashing membuktikan data tidak berubah — itu **integrity**. Confidentiality dijaga dengan enkripsi, availability dengan redundansi, sedangkan non-repudiation membutuhkan bukti identitas seperti digital signature.

## Soal 8
**Objektif:** 1.2
**Tipe:** Definisi
**Soal:** Which combination correctly maps the AAA components to their purpose?

- A. Authentication encrypts traffic, authorization records activity, accounting proves identity
- B. Authentication proves identity, authorization grants access, accounting records activity
- C. Authentication grants access, authorization proves identity, accounting encrypts traffic
- D. Authentication records activity, authorization proves identity, accounting grants access

**Jawaban:** B
**Pembahasan:** **Authentication** = membuktikan siapa Anda; **authorization** = menentukan apa yang boleh Anda lakukan; **accounting** = mencatat apa yang Anda lakukan (log/audit trail). Urutannya selalu identifikasi → autentikasi → otorisasi → akuntansi.

## Soal 9
**Objektif:** 1.2
**Tipe:** Skenario
**Soal:** A user signs in with a username, password, and a code from an authenticator app. The system then checks that the user's role permits access to the payroll module. Which two AAA phases are described?

- A. Authentication and authorization
- B. Identification and accounting
- C. Authorization and accounting
- D. Accounting and authorization

**Jawaban:** A
**Pembahasan:** Password + kode OTP adalah **authentication** (plus identification di awal), dan pemeriksaan role terhadap modul payroll adalah **authorization**. Accounting baru terjadi saat aktivitas pengguna dicatat.

## Soal 10
**Objektif:** 1.2
**Tipe:** Skenario
**Soal:** In a zero trust architecture, which component makes the decision about whether a request should be granted?

- A. Data plane
- B. Policy enforcement point
- C. Policy administrator
- D. Policy engine

**Jawaban:** D
**Pembahasan:** Dalam model NIST SP 800-207, **policy engine** mengambil keputusan (allow/deny) berdasarkan kebijakan dan sinyal konteks. **Policy administrator** mengeksekusi keputusan dengan membuat/menghapus sesi, dan **policy enforcement point** menegakkan keputusan pada lalu lintas aktual.

## Soal 11
**Objektif:** 1.2
**Tipe:** Skenario
**Soal:** A company divides its internal network into many small zones so that a compromised web server cannot reach the database subnet directly. Each zone enforces its own least-privilege rules. Which zero trust concept is this?

- A. Security through obscurity
- B. Network address translation
- C. Implicit trust zone
- D. Microsegmentation

**Jawaban:** D
**Pembahasan:** **Microsegmentation** membagi jaringan menjadi segmen kecil dengan aturan akses spesifik, menghilangkan implicit trust antar sistem. Implicit trust zone justru konsep yang harus dihilangkan dalam zero trust.

## Soal 12
**Objektif:** 1.2
**Tipe:** Skenario
**Soal:** A security team places a fake file named `payroll_master.xlsx` on a file server and alerts whenever it is opened. Which technique is being used?

- A. Honeytoken
- B. Sinkhole
- C. Sandbox
- D. Honeypot

**Jawaban:** A
**Pembahasan:** **Honeytoken** adalah data umpan (file, record, kredensial) yang tidak punya kegunaan sah; siapa pun yang menyentuhnya hampir pasti penyerang atau insider. Honeypot adalah sistem/ host umpan, bukan artefak data.

## Soal 13
**Objektif:** 1.2
**Tipe:** Definisi
**Soal:** Which activity BEST describes a gap analysis?

- A. Testing whether backups can be restored within the RTO
- B. Reviewing firewall rules for unused entries
- C. Comparing the current security posture against a desired framework or standard to identify missing controls
- D. Scanning the network for unpatched hosts

**Jawaban:** C
**Pembahasan:** **Gap analysis** membandingkan kondisi saat ini dengan target (misalnya ISO 27001 atau NIST CSF) lalu mengidentifikasi kekurangan. Opsi lain adalah aktivitas operasional spesifik, bukan analisis kesenjangan menyeluruh.

## Soal 14
**Objektif:** 1.3
**Tipe:** Skenario
**Soal:** Before approving a change to the production VPN concentrator, the change advisory board asks: "If the change fails, how do we get back to the previous state within 30 minutes?" Which change management element does this question address?

- A. Stakeholder approval
- B. Impact analysis
- C. Backout plan
- D. Maintenance window

**Jawaban:** C
**Pembahasan:** **Backout plan** (rollback plan) menjelaskan cara mengembalikan sistem ke kondisi semula bila perubahan gagal. Impact analysis menilai dampak perubahan, maintenance window menentukan jadwal, dan approval adalah persetujuan itu sendiri.

## Soal 15
**Objektif:** 1.3
**Tipe:** Skenario
**Soal:** A developer wants to push an emergency patch at 2 p.m. on a Tuesday. The security manager requires a documented approval, a tested result in staging, and notification to all stakeholders before the change is applied. Which process is being enforced?

- A. Configuration baseline
- B. Incident response
- C. Change management
- D. Vulnerability scanning

**Jawaban:** C
**Pembahasan:** Persetujuan, pengujian, komunikasi stakeholder, dan jadwal perubahan adalah elemen **change management**. Tujuannya mencegah perubahan yang tidak terdokumentasi dan memicu gangguan produksi.

## Soal 16
**Objektif:** 1.4
**Tipe:** Definisi
**Soal:** A digital signature provides which set of security properties?

- A. Confidentiality, integrity, and availability
- B. Integrity, authentication, and non-repudiation
- C. Confidentiality, authentication, and accounting
- D. Availability, non-repudiation, and authorization

**Jawaban:** B
**Pembahasan:** Digital signature mengenkripsi hash pesan dengan private key pengirim, sehingga penerima dapat memverifikasi **integrity**, memastikan identitas pengirim (**authentication**), dan penandatangan tidak bisa menyangkal (**non-repudiation**). Signature tidak menyembunyikan isi pesan, jadi bukan confidentiality.

## Soal 17
**Objektif:** 1.4
**Tipe:** Skenario
**Soal:** A company encrypts its backup tapes and stores a copy of the encryption keys with a trusted third party so that data can be recovered if the administrator leaves. Which concept is this?

- A. Key rotation
- B. Key escrow
- C. Key stretching
- D. Key exchange

**Jawaban:** B
**Pembahasan:** **Key escrow** menyimpan salinan kunci pada pihak ketiga tepercaya untuk keperluan pemulihan. Key rotation adalah pergantian kunci berkala, key stretching memperkuat password lemah, dan key exchange adalah pertukaran kunci (misalnya Diffie-Hellman).

## Soal 18
**Objektif:** 1.4
**Tipe:** Perbandingan
**Soal:** Which statement correctly distinguishes a TPM from an HSM?

- A. A TPM stores certificates only; an HSM stores passwords only
- B. A TPM is a dedicated appliance for high-volume transaction cryptography; an HSM is a chip soldered to a motherboard
- C. A TPM is a chip that stores keys and measurements on a single host; an HSM is a hardened appliance or service that performs cryptographic operations for many systems
- D. Both are software libraries used to generate certificates

**Jawaban:** C
**Pembahasan:** **TPM** adalah chip kriptografi pada satu perangkat (untuk BitLocker, measured boot, attestation). **HSM** adalah perangkat/ layanan khusus yang diperkuat untuk operasi kriptografi bervolume tinggi dan penyimpanan kunci pada level organisasi.

## Soal 19
**Objektif:** 1.4
**Tipe:** Skenario
**Soal:** An administrator must verify whether a certificate was revoked without downloading the entire revocation list. Which mechanism should be used?

- A. OCSP
- B. Trust anchor
- C. CSR
- D. CRL

**Jawaban:** A
**Pembahasan:** **OCSP** (Online Certificate Status Protocol) memungkinkan pemeriksaan status satu sertifikat secara real time tanpa mengunduh seluruh daftar. CRL adalah daftar lengkap yang diunduh, CSR adalah permintaan sertifikat, dan trust anchor adalah root certificate yang dipercaya.

## Soal 20
**Objektif:** 1.4
**Tipe:** Definisi
**Soal:** Why is a unique random salt added to each password before hashing?

- A. To prevent identical passwords from producing identical hashes and to defeat precomputed rainbow tables
- B. To encrypt the password with the server's public key
- C. To allow the password to be reversed by the administrator
- D. To shorten the hash output

**Jawaban:** A
**Pembahasan:** **Salt** memastikan dua pengguna dengan password sama menghasilkan hash berbeda, sehingga rainbow table yang sudah dihitung sebelumnya tidak berguna. Salt bukan enkripsi dan tidak membuat hash bisa dibalik.

## Soal 21
**Objektif:** 1.4
**Tipe:** Definisi
**Soal:** Which technique is designed to make brute-force attacks against stored passwords slower by repeatedly applying a hash function?

- A. Steganography
- B. Salting
- C. Key stretching
- D. Tokenization

**Jawaban:** C
**Pembahasan:** **Key stretching** (misalnya PBKDF2, bcrypt, Argon2) menerapkan fungsi hash berulang kali dengan biaya komputasi tinggi sehingga setiap tebakan menjadi lambat. Salting mencegah rainbow table tetapi tidak memperlambat per tebakan.

## Soal 22
**Objektif:** 1.4
**Tipe:** Perbandingan
**Soal:** Which statement about hashing and encryption is CORRECT?

- A. Hashing requires a shared secret key
- B. Hashing is reversible with the correct key; encryption is not
- C. Hashing is a one-way function used for integrity; encryption is reversible and used for confidentiality
- D. Both provide confidentiality

**Jawaban:** C
**Pembahasan:** **Hash** bersifat satu arah (tidak bisa dikembalikan) dan dipakai untuk integritas/verifikasi. **Enkripsi** bersifat reversibel dengan kunci yang tepat dan melindungi kerahasiaan.

## Soal 23
**Objektif:** 1.4
**Tipe:** Skenario
**Soal:** A company stores transaction records in a distributed ledger where each block contains the hash of the previous block and is replicated across nodes. Which property does this design primarily provide?

- A. Tamper-evident integrity through chaining
- B. Faster transaction processing
- C. Automatic key rotation
- D. Confidentiality of the records

**Jawaban:** A
**Pembahasan:** **Blockchain** mengaitkan setiap blok dengan hash blok sebelumnya sehingga perubahan satu blok merusak seluruh rantai — sifatnya tamper-evident (integritas). Blockchain tidak otomatis menjamin kerahasiaan karena isinya bisa terbaca semua node.

## Soal 24
**Objektif:** 1.4
**Tipe:** Skenario
**Soal:** An organization wants full-disk encryption keys to be sealed to the hardware and released only when the boot measurements match a known-good state. Which technology is MOST appropriate?

- A. HSM
- B. TPM
- C. KMS
- D. Secure enclave

**Jawaban:** B
**Pembahasan:** **TPM** menyegel kunci ke platform dan melakukan **measured boot**; kunci hanya dilepas bila PCR (measurement) sesuai. HSM melayani banyak sistem, sedangkan secure enclave melindungi kode/data dalam CPU, bukan mengukur boot.

## Soal 25
**Objektif:** 1.4
**Tipe:** Perbandingan
**Soal:** Why do most TLS connections use asymmetric cryptography only during the handshake?

- A. Because asymmetric algorithms cannot encrypt data
- B. Because symmetric encryption is much faster for bulk data transfer
- C. Because asymmetric keys are always public
- D. Because symmetric keys cannot be rotated

**Jawaban:** B
**Pembahasan:** Kriptografi asimetris dipakai untuk autentikasi dan menyepakati kunci sesi karena mahal secara komputasi; transfer data massal kemudian memakai **symmetric** (AES) yang jauh lebih cepat. Asymmetric tetap bisa mengenkripsi data kecil, hanya tidak efisien.

## Soal 26
**Objektif:** 1.4
**Tipe:** Skenario
**Soal:** A stolen laptop is recovered. Investigators find the disk was protected with BitLocker, but a single sensitive file copied to a USB drive was readable. Which encryption scope would have protected that file?

- A. File-level encryption
- B. Database encryption
- C. Full-disk encryption
- D. Partition encryption

**Jawaban:** A
**Pembahasan:** FDE melindungi data saat disk dalam keadaan mati, tetapi file yang sudah dikopi ke media lain tidak lagi terlindungi. **File-level encryption** (atau container terenkripsi) tetap melekat pada file tersebut di mana pun ia berada.

## Soal 27
**Objektif:** 1.4
**Tipe:** Pemetaan
**Soal:** Which protocol pairing is CORRECT for protecting email contents end to end?

- A. S/MIME for email, IPsec for network layer
- B. TLS for email storage, SSH for web traffic
- C. DNSSEC for email, SFTP for web traffic
- D. HTTPS for email, SNMPv3 for file transfer

**Jawaban:** A
**Pembahasan:** **S/MIME** memberi enkripsi dan tanda tangan pada pesan email, sedangkan **IPsec** melindungi lalu lintas pada layer network (mode tunnel/transport). TLS melindungi hop transport, bukan isi email end-to-end.

## Soal 28
**Objektif:** 1.4
**Tipe:** Perbandingan
**Soal:** Which technique replaces sensitive data with a non-sensitive placeholder that maps back to the original value in a secure vault?

- A. Tokenization
- B. Steganography
- C. Hashing
- D. Data masking

**Jawaban:** A
**Pembahasan:** **Tokenization** menukar data asli (misalnya nomor kartu kredit) dengan token yang tidak bermakna; pemetaan disimpan di vault. Data masking biasanya mengubah tampilan secara permanen (misalnya `****-****-****-1234`), sedangkan steganografi menyembunyikan data di dalam media lain.

## Soal 29
**Objektif:** 1.4
**Tipe:** Skenario
**Soal:** An attacker finds two different documents that produce the same MD5 hash and uses this to replace a legitimate file undetected. Which cryptographic weakness was exploited?

- A. Collision
- B. Rainbow table
- C. Brute force
- D. Downgrade attack

**Jawaban:** A
**Pembahasan:** **Collision** terjadi ketika dua input berbeda menghasilkan hash yang sama; MD5 dan SHA-1 sudah terbukti rentan. Downgrade menurunkan versi protokol, rainbow table menyerang password, dan brute force menebak kunci.

## Soal 30
**Objektif:** 1.4
**Tipe:** Skenario
**Soal:** A client and server negotiate TLS, but an on-path attacker forces them to use TLS 1.0 with weak ciphers. Which attack is described?

- A. Downgrade attack
- B. Replay attack
- C. Pass-the-hash
- D. Birthday attack

**Jawaban:** A
**Pembahasan:** **Downgrade attack** memaksa kedua pihak memakai versi protokol atau cipher suite yang lebih lemah agar mudah diserang. Mitigasinya: menonaktifkan protokol lama dan mengaktifkan strict security settings di kedua sisi.

## Soal 31
**Objektif:** 1.4
**Tipe:** Skenario
**Soal:** A root certificate authority's private key is compromised. What is the MOST immediate risk?

- A. All leaf certificates can no longer be encrypted
- B. Attackers can issue trusted certificates for any domain, enabling impersonation
- C. All hashed passwords become reversible
- D. OCSP responders stop working automatically

**Jawaban:** B
**Pembahasan:** Dengan private key root CA, penyerang dapat menerbitkan sertifikat yang tampak sah untuk domain apa pun (misalnya bank), sehingga terjadi impersonation dan MITM. Inilah alasan root CA dijaga offline di HSM dan ada mekanisme revocation.

## Soal 32
**Objektif:** 1.2
**Tipe:** Skenario
**Soal:** A data center uses two sets of doors with an interlocking mechanism: the first door must close before the second opens, preventing piggybacking. What is this called?

- A. Bollard
- B. Access control vestibule
- C. Faraday cage
- D. Mantrap sensor

**Jawaban:** B
**Pembahasan:** **Access control vestibule** (mantrap) adalah ruang kecil dengan dua pintu interlock untuk mencegah tailgating/piggybacking. Bollard adalah penghalang kendaraan, Faraday cage memblokir sinyal elektromagnetik.

## Soal 33
**Objektif:** 1.2
**Tipe:** Definisi
**Soal:** Which physical control is specifically designed to prevent a vehicle from ramming a building entrance?

- A. Motion sensor
- B. Proximity reader
- C. Lighting
- D. Bollards

**Jawaban:** D
**Pembahasan:** **Bollards** adalah tiang penghalang fisik untuk mencegah kendaraan menabrak bangunan atau area terlarang. Lighting bersifat deterrent/detective, motion sensor detective, proximity reader untuk kontrol akses.

## Soal 34
**Objektif:** 1.2
**Tipe:** Skenario
**Soal:** A SOC wants to detect attackers early by exposing a decoy server with fake credentials and monitoring all interaction with it. Which two concepts are combined here?

- A. VLAN and NAC
- B. Honeypot and honeytoken
- C. Sandbox and WAF
- D. IDS and DLP

**Jawaban:** B
**Pembahasan:** Server umpan adalah **honeypot**, sedangkan kredensial palsu di dalamnya adalah **honeytoken**. Kombinasi ini mendeteksi dan mempelajari teknik penyerang tanpa memberi akses ke aset nyata.

## Soal 35
**Objektif:** 1.3
**Tipe:** Skenario
**Soal:** A critical zero-day forces administrators to apply an emergency patch outside the normal approval cycle. Which action keeps the change management process intact?

- A. Apply the patch immediately, then document it and obtain retrospective approval from the change advisory board
- B. Skip documentation because the change is urgent
- C. Wait for the next monthly change window regardless of risk
- D. Let the administrator approve their own change without review

**Jawaban:** A
**Pembahasan:** **Emergency change** tetap harus dicatat dan ditinjau (sering secara retroaktif) oleh CAB. Melewati dokumentasi menghilangkan jejak audit dan membuat rollback sulit; menunggu jadwal normal justru membiarkan risiko aktif.

## Soal 36
**Objektif:** 1.3
**Tipe:** Skenario
**Soal:** Which document provides the step-by-step tasks, responsible roles, and verification checks for applying a security patch?

- A. Risk register
- B. Standard operating procedure
- C. Acceptable use policy
- D. Business impact analysis

**Jawaban:** B
**Pembahasan:** **SOP** merinci langkah operasional, peran, dan verifikasi sehingga perubahan konsisten dan dapat diaudit. Kebijakan AUP mengatur perilaku pengguna; BIA dan risk register bukan instruksi teknis.

## Soal 37
**Objektif:** 1.1
**Tipe:** Multi-select
**Soal:** Which TWO of the following are managerial (administrative) controls? (Select TWO.)

- A. Acceptable use policy
- B. Security guard stationed in the lobby
- C. Annual risk assessment
- D. Motion sensor that triggers an alarm
- E. Web application firewall

**Jawaban:** A, C
**Pembahasan:** Kebijakan AUP dan risk assessment adalah kontrol **managerial** karena berbentuk aturan dan proses tata kelola. Penjaga dan sensor gerak bersifat physical, WAF bersifat technical.

## Soal 38
**Objektif:** 1.4
**Tipe:** Multi-select
**Soal:** Which TWO statements about cryptographic hashing are correct? (Select TWO.)

- A. It is reversible with the correct private key
- B. It produces an output of fixed length
- C. It provides confidentiality without any encryption
- D. It requires both parties to share a secret key
- E. It is a one-way function

**Jawaban:** B, E
**Pembahasan:** Hash bersifat **satu arah** dan menghasilkan panjang output tetap (misalnya SHA-256 selalu 256 bit). Hash tidak dapat dibalik, tidak memberi kerahasiaan, dan tidak memerlukan kunci bersama.
