# Domain 4 — Security Operations (28%)

Domain terbesar dalam ujian. Mencakup **hardening**, **manajemen aset**, **vulnerability management**, **monitoring**, **penguatan kapabilitas enterprise**, **IAM**, **otomasi**, **incident response**, dan **investigasi**. Hafalkan perbedaan tool yang mirip (IDS vs IPS, EDR vs XDR, SIEM vs SOAR) dan urutan proses IR.

## Soal 1
**Objektif:** 4.1
**Tipe:** Skenario
**Soal:** A new Linux server is deployed with only the required packages, SSH key-only authentication, and a host firewall. Which activity does this describe?

- A. Hardening
- B. Patching
- C. Segmentation
- D. Decommissioning

**Jawaban:** A
**Pembahasan:** **Hardening** mengurangi attack surface dengan menonaktifkan layanan tidak perlu, menghapus akun default, dan menerapkan konfigurasi aman. Patching hanya menutup kerentanan yang sudah diketahui.

## Soal 2
**Objektif:** 4.1
**Tipe:** Skenario
**Soal:** A wireless network must authenticate each user individually and support certificate-based authentication without a shared key. Which configuration is BEST?

- A. WPA2-PSK with a strong passphrase
- B. WPA3-Enterprise with 802.1X/EAP
- C. WEP with MAC filtering
- D. Open network with captive portal

**Jawaban:** B
**Pembahasan:** **WPA3-Enterprise + 802.1X** memberi autentikasi per pengguna dan mendukung EAP-TLS berbasis sertifikat. PSK memakai kunci bersama yang dapat dibagikan; WEP sudah usang dan mudah dipecahkan.

## Soal 3
**Objektif:** 4.1
**Tipe:** Skenario
**Soal:** A company issues smartphones to field staff and requires full device encryption, a PIN, and remote wipe, while separating corporate data from personal data. Which solution is MOST appropriate?

- A. MDM with containerization/MAM
- B. NAC
- C. DLP only
- D. VPN only

**Jawaban:** A
**Pembahasan:** **MDM** menerapkan kebijakan perangkat dan dapat memisahkan data kerja (container/MAM) dari data pribadi. Ini penting pada model **BYOD/COPE**.

## Soal 4
**Objektif:** 4.1
**Tipe:** Skenario
**Soal:** Which risk is created by allowing users to sideload applications on corporate mobile devices?

- A. Apps from untrusted sources may contain malware and bypass store review
- B. The device battery drains faster
- C. The device cannot connect to Wi-Fi
- D. The device loses its IMEI

**Jawaban:** A
**Pembahasan:** **Sideloading** melewati kurasi toko aplikasi sehingga malware, spyware, atau aplikasi berbahaya bisa terpasang. Kebijakan MDM biasanya memblokir sumber tidak dikenal.

## Soal 5
**Objektif:** 4.1
**Tipe:** Skenario
**Soal:** A company wants to let contractors use their own laptops but requires that corporate applications run in an isolated environment. Which approach is BEST?

- A. Full disk encryption on personal laptops
- B. Dual-boot with a corporate OS
- C. Local admin rights for contractors
- D. VDI or application virtualization

**Jawaban:** D
**Pembahasan:** **VDI/application virtualization** menjalankan aplikasi dan data di lingkungan terkontrol, sehingga perangkat pribadi tidak menyimpan data perusahaan. FDE pada perangkat pribadi sulit ditegakkan.

## Soal 6
**Objektif:** 4.1
**Tipe:** Skenario
**Soal:** Which action BEST reduces the attack surface of a web server?

- A. Install additional monitoring agents
- B. Increase CPU and RAM
- C. Enable directory listing for troubleshooting
- D. Disable unused modules and services, remove sample applications

**Jawaban:** D
**Pembahasan:** Menonaktifkan modul/layanan tidak terpakai dan menghapus aplikasi contoh menghilangkan jalur serangan yang tidak perlu. Menambah resource tidak mengurangi attack surface.

## Soal 7
**Objektif:** 4.1
**Tipe:** Skenario
**Soal:** A workstation is configured to block execution of any binary not signed by the company's certificate authority. Which control is this?

- A. Host-based IDS
- B. Full-disk encryption
- C. DLP
- D. Application allow listing

**Jawaban:** D
**Pembahasan:** **Allow listing** hanya mengizinkan binary bertanda tangan/terdaftar, sehingga malware tanpa signature tidak dapat berjalan. Ini termasuk teknik hardening endpoint.

## Soal 8
**Objektif:** 4.1
**Tipe:** Skenario
**Soal:** A company must ensure that a decommissioned laptop's drive cannot be read even if the platters are removed. Which method is BEST?

- A. Deleting the user profile
- B. Quick format
- C. Physical destruction (shredding)
- D. Moving files to the recycle bin

**Jawaban:** C
**Pembahasan:** **Physical destruction** menjamin data tidak dapat dipulihkan, bahkan dari komponen disk. Quick format dan penghapusan file hanya menghapus referensi, bukan data.

## Soal 9
**Objektif:** 4.2
**Tipe:** Skenario
**Soal:** A security team cannot determine which servers are missing patches because there is no authoritative list of deployed systems. Which process is missing?

- A. Asset inventory and discovery
- B. Incident response
- C. Change management
- D. Data loss prevention

**Jawaban:** A
**Pembahasan:** **Asset management** mencakup inventaris, penemuan (discovery/enumeration), dan pelacakan kepemilikan. Tanpa itu, pemindaian dan patching tidak lengkap karena aset tak dikenal (shadow assets) terlewat.

## Soal 10
**Objektif:** 4.2
**Tipe:** Skenario
**Soal:** Which document BEST tracks who is responsible for a laptop throughout its lifecycle?

- A. Network diagram
- B. Incident log
- C. Firewall rule set
- D. Asset tag with assignment records

**Jawaban:** D
**Pembahasan:** **Asset tag dan catatan penugasan** menghubungkan perangkat dengan pemilik/pengguna, lokasi, dan status. Ini penting untuk audit, pemulihan, dan investigasi.

## Soal 11
**Objektif:** 4.2
**Tipe:** Skenario
**Soal:** Before disposing of a multifunction printer, which step is MOST important?

- A. Update the firmware
- B. Change the admin password
- C. Sanitize or destroy the internal storage that may contain scanned documents
- D. Remove the paper tray

**Jawaban:** C
**Pembahasan:** Perangkat multifungsi menyimpan gambar dokumen di disk internal; **sanitasi/destruksi** media tersebut mencegah kebocoran data. Mengganti password tidak menghapus data lama.

## Soal 12
**Objektif:** 4.2
**Tipe:** Definisi
**Soal:** Which term describes verifying that a storage device has been properly sanitized before reuse or disposal?

- A. Certification of sanitization
- B. Chain of custody
- C. Asset tagging
- D. Baseline comparison

**Jawaban:** A
**Pembahasan:** **Certification** (sertifikat sanitasi/destruksi) mendokumentasikan metode dan hasil sehingga organisasi dapat membuktikan kepatuhan. Chain of custody berkaitan dengan bukti forensik.

## Soal 13
**Objektif:** 4.3
**Tipe:** Skenario
**Soal:** A vulnerability scan reports a critical flaw on a server, but the security analyst confirms the affected service is disabled. What should the analyst do?

- A. Mark it as a false positive with justification and evidence
- B. Patch the server immediately during business hours
- C. Ignore all future scans from that scanner
- D. Escalate it as an active incident

**Jawaban:** A
**Pembahasan:** Temuan yang tidak dapat dieksploitasi karena layanan nonaktif adalah **false positive**; dokumentasikan bukti dan tutup dengan justifikasi. Ini berbeda dari false negative (kerentanan nyata yang tidak terdeteksi).

## Soal 14
**Objektif:** 4.3
**Tipe:** Skenario
**Soal:** Which CVSS metric group reflects the characteristics of the vulnerability that change over time, such as exploit maturity?

- A. Impact score
- B. Base score
- C. Temporal score
- D. Environmental score

**Jawaban:** C
**Pembahasan:** **Temporal** mempertimbangkan faktor yang berubah seiring waktu (exploit code availability, remediation level). **Base** adalah sifat intrinsik, **environmental** disesuaikan dengan konteks organisasi.

## Soal 15
**Objektif:** 4.3
**Tipe:** Skenario
**Soal:** A scanner reports 400 vulnerabilities, but only 12 affect internet-facing systems with known exploits. Which approach BEST prioritizes remediation?

- A. Patch all 400 simultaneously
- B. Ignore all low-severity findings permanently
- C. Fix in CVSS score order regardless of exposure
- D. Prioritize by exploitability, exposure, and business impact

**Jawaban:** D
**Pembahasan:** Prioritas risiko mempertimbangkan **eksposur, exploitability, dan dampak bisnis**, bukan hanya skor mentah. Ini juga alasan CVSS environmental score dan threat intelligence dipakai.

## Soal 16
**Objektif:** 4.3
**Tipe:** Skenario
**Soal:** A critical vulnerability cannot be patched for 60 days due to vendor constraints. Which response is MOST appropriate?

- A. Hide the finding from the report
- B. Disable the vulnerability scanner
- C. Immediately decommission the system without a plan
- D. Request a documented exception with compensating controls and review date

**Jawaban:** D
**Pembahasan:** **Exception** yang terdokumentasi dengan kontrol kompensasi (segmentasi, WAF rule, monitoring) dan tanggal review adalah praktik yang benar. Menyembunyikan temuan melanggar tata kelola.

## Soal 17
**Objektif:** 4.3
**Tipe:** Skenario
**Soal:** After applying a patch, which activity BEST validates that the vulnerability is actually remediated?

- A. Review the change ticket
- B. Rescan the host and verify the finding no longer appears
- C. Ask the vendor whether the patch works
- D. Check that the server reboots

**Jawaban:** B
**Pembahasan:** **Rescan/validation** membuktikan perbaikan berhasil dan tidak ada regresi. Verifikasi juga dapat memakai audit konfigurasi atau uji eksploitasi terkontrol.

## Soal 18
**Objektif:** 4.3
**Tipe:** Skenario
**Soal:** A researcher discovers a vulnerability and privately notifies the vendor, agreeing to withhold details until a patch is released. Which practice is this?

- A. Bug bounty
- B. Penetration testing
- C. Threat hunting
- D. Responsible disclosure

**Jawaban:** D
**Pembahasan:** **Responsible disclosure** memberi vendor waktu memperbaiki sebelum detail dipublikasikan. Bug bounty adalah program berhadiah, pen test adalah pengujian terkontrak, threat hunting mencari ancaman aktif.

## Soal 19
**Objektif:** 4.3
**Tipe:** Skenario
**Soal:** A penetration test is authorized in writing with defined scope, time window, and emergency contacts. Which document governs this?

- A. Incident response plan
- B. Rules of engagement
- C. Service level agreement
- D. Acceptable use policy

**Jawaban:** B
**Pembahasan:** **Rules of engagement** menetapkan ruang lingkup, batasan, jadwal, dan kontak darurat pen test sehingga pengujian legal dan aman. SLA mengatur tingkat layanan, bukan aktivitas pengujian.

## Soal 20
**Objektif:** 4.3
**Tipe:** Skenario
**Soal:** Which scan configuration is MOST likely to find missing patches and insecure settings on a server?

- A. Unauthenticated external scan
- B. Credentialed internal scan
- C. Ping sweep only
- D. Port scan only

**Jawaban:** B
**Pembahasan:** **Credentialed scan** masuk ke sistem dan memeriksa patch serta konfigurasi secara akurat. Unauthenticated scan hanya melihat dari luar dan lebih banyak false positive/negative.

## Soal 21
**Objektif:** 4.3
**Tipe:** Skenario
**Soal:** A company wants to continuously identify vulnerabilities in container images before deployment. Which practice is BEST?

- A. Rely on the base image being official
- B. Disable the registry scanner to speed builds
- C. Scan images in the CI/CD pipeline and block builds with critical findings
- D. Scan production once a year

**Jawaban:** C
**Pembahasan:** **Shift-left**: memindai image saat build/pipeline sehingga kerentanan tidak pernah mencapai produksi. Pemindaian tahunan terlalu lambat untuk lingkungan yang sering berubah.

## Soal 22
**Objektif:** 4.4
**Tipe:** Skenario
**Soal:** Which tool aggregates logs from firewalls, servers, and applications, correlates events, and generates alerts?

- A. NetFlow collector
- B. WAF
- C. NAC
- D. SIEM

**Jawaban:** D
**Pembahasan:** **SIEM** mengumpulkan, menormalkan, dan mengorelasikan log untuk deteksi serta investigasi. NetFlow hanya metadata trafik, WAF melindungi aplikasi web, NAC mengontrol akses perangkat.

## Soal 23
**Objektif:** 4.4
**Tipe:** Skenario
**Soal:** An analyst wants to automatically enrich alerts, create tickets, and block an IP without manual steps. Which technology is MOST appropriate?

- A. SIEM only
- B. SOAR
- C. HIDS
- D. DLP

**Jawaban:** B
**Pembahasan:** **SOAR** mengotomatiskan playbook respons: enrichment, ticketing, dan tindakan seperti blokir IP. SIEM berfokus pada pengumpulan dan korelasi, bukan orkestrasi tindakan.

## Soal 24
**Objektif:** 4.4
**Tipe:** Skenario
**Soal:** A network engineer needs summary metadata about which hosts communicate most, without capturing full packet contents. Which technology is BEST?

- A. Syslog
- B. NetFlow
- C. Packet capture
- D. Honeypot

**Jawaban:** B
**Pembahasan:** **NetFlow** memberi metadata aliran (source/destination, port, byte count) dengan overhead rendah. Packet capture menyimpan isi paket dan jauh lebih besar.

## Soal 25
**Objektif:** 4.4
**Tipe:** Skenario
**Soal:** An alert fires for the same benign administrative script every morning, drowning out real alerts. Which action is MOST appropriate?

- A. Tune the alert with an exception for that known-good behavior
- B. Disable the SIEM
- C. Ignore all alerts from that host
- D. Increase the alert threshold for every rule

**Jawaban:** A
**Pembahasan:** **Alert tuning** mengurangi false positive dengan mengecualikan perilaku yang diketahui aman, tanpa mematikan deteksi lain. Mengabaikan seluruh host berisiko melewatkan serangan nyata.

## Soal 26
**Objektif:** 4.4
**Tipe:** Skenario
**Soal:** Which data source is BEST for identifying a malicious process that ran only in memory on an endpoint?

- A. DNS zone file
- B. EDR telemetry
- C. Firewall logs
- D. NetFlow records

**Jawaban:** B
**Pembahasan:** **EDR** merekam eksekusi proses, command line, dan interaksi API sehingga aktivitas fileless dapat terlihat. Firewall/NetFlow hanya menunjukkan koneksi jaringan.

## Soal 27
**Objektif:** 4.4
**Tipe:** Skenario
**Soal:** A SOC wants to detect compromised hosts by analyzing DNS queries for domains associated with malware. Which tool is MOST appropriate?

- A. DLP
- B. DNS filtering with threat intelligence feeds
- C. Full-disk encryption
- D. NAC

**Jawaban:** B
**Pembahasan:** **DNS filtering/threat intel** dapat memblokir atau menandai resolusi ke domain jahat (C2, phishing). Ini juga membantu menemukan host yang terinfeksi meski trafiknya terenkripsi.

## Soal 28
**Objektif:** 4.4
**Tipe:** Skenario
**Soal:** Which protocol should be used to collect device status and traps securely from network equipment?

- A. Telnet
- B. TFTP
- C. SNMPv3
- D. SNMPv1

**Jawaban:** C
**Pembahasan:** **SNMPv3** mendukung autentikasi dan enkripsi, sedangkan v1/v2c mengirim community string dalam plaintext. Telnet dan TFTP juga tidak terenkripsi.

## Soal 29
**Objektif:** 4.4
**Tipe:** Skenario
**Soal:** A file integrity monitoring tool alerts that `/etc/passwd` changed outside the change window. Which type of monitoring is this?

- A. DLP
- B. NAC
- C. WAF
- D. FIM

**Jawaban:** D
**Pembahasan:** **FIM** memantau perubahan file kritis dengan hash dan memberi alert saat ada modifikasi tak terduga — indikasi persistence atau backdoor.

## Soal 30
**Objektif:** 4.5
**Tipe:** Skenario
**Soal:** A company wants to prevent users from visiting known phishing and malware domains at the DNS level. Which control is MOST appropriate?

- A. DLP
- B. DNS filtering
- C. Host-based firewall
- D. Full-disk encryption

**Jawaban:** B
**Pembahasan:** **DNS filtering** memblokir resolusi domain berbahaya untuk seluruh jaringan, termasuk perangkat yang tidak bisa dipasangi agen. Ini lapisan pertahanan tambahan, bukan pengganti endpoint protection.

## Soal 31
**Objektif:** 4.5
**Tipe:** Skenario
**Soal:** An organization wants to ensure that only authenticated and encrypted LDAP queries are allowed. Which configuration is required?

- A. Kerberos on port 88 only
- B. RADIUS on port 1812
- C. LDAPS on port 636
- D. LDAP on port 389

**Jawaban:** C
**Pembahasan:** **LDAPS** membungkus LDAP dalam TLS (port 636) sehingga kredensial dan query tidak dikirim plaintext. LDAP 389 tanpa StartTLS rentan disadap.

## Soal 32
**Objektif:** 4.5
**Tipe:** Skenario
**Soal:** Which email authentication mechanism allows a domain owner to specify which servers may send email on its behalf?

- A. DKIM
- B. DMARC
- C. S/MIME
- D. SPF

**Jawaban:** D
**Pembahasan:** **SPF** mendaftarkan IP/server yang diizinkan mengirim email untuk domain. **DKIM** menandatangani pesan, **DMARC** memberi kebijakan berdasarkan hasil SPF/DKIM dan laporan.

## Soal 33
**Objektif:** 4.5
**Tipe:** Skenario
**Soal:** A company wants to receive reports about emails that fail authentication and instruct receivers to reject them. Which record provides this?

- A. DMARC record with p=reject and rua reporting
- B. SPF record with -all
- C. DKIM public key
- D. MX record

**Jawaban:** A
**Pembahasan:** **DMARC** dengan `p=reject` memerintahkan penolakan pesan yang gagal alignment, dan `rua` mengirim laporan agregat. SPF saja tidak memberi kebijakan penanganan atau laporan.

## Soal 34
**Objektif:** 4.5
**Tipe:** Skenario
**Soal:** Which secure protocol should replace Telnet for remote administration of network devices?

- A. SSH
- B. FTP
- C. HTTP
- D. SNMPv1

**Jawaban:** A
**Pembahasan:** **SSH** menyediakan sesi administratif terenkripsi dan terautentikasi. FTP, HTTP, dan SNMPv1 mengirim data (termasuk kredensial) tanpa enkripsi.

## Soal 35
**Objektif:** 4.5
**Tipe:** Skenario
**Soal:** A SOC wants to detect anomalous user behavior such as accessing unusual volumes of data at odd hours. Which technology is MOST appropriate?

- A. UEBA
- B. WAF
- C. NAC
- D. FIM

**Jawaban:** A
**Pembahasan:** **UEBA** (User and Entity Behavior Analytics) membangun baseline perilaku dan menandai anomali seperti akses data masif atau login di luar kebiasaan — berguna untuk insider threat.

## Soal 36
**Objektif:** 4.5
**Tipe:** Skenario
**Soal:** To reduce the risk of credential theft from memory, which Windows protection should be enabled?

- A. Remote Registry
- B. SMBv1
- C. Credential Guard / LSASS protection
- D. AutoPlay

**Jawaban:** C
**Pembahasan:** **Credential Guard** mengisolasi secret (NTLM hash, Kerberos TGT) dari LSASS sehingga sulit diambil dengan Mimikatz. AutoPlay dan SMBv1 justru meningkatkan risiko.

## Soal 37
**Objektif:** 4.5
**Tipe:** Skenario
**Soal:** Which capability allows an organization to block USB mass storage on endpoints while still permitting keyboards and mice?

- A. Full-disk encryption
- B. NAC
- C. DLP
- D. Endpoint device control policy

**Jawaban:** D
**Pembahasan:** **Device control** (bagian dari endpoint protection/Group Policy) dapat membedakan kelas perangkat dan memblokir storage massal tanpa mematikan HID. Ini mengurangi risiko exfiltration dan infeksi via USB.

## Soal 38
**Objektif:** 4.6
**Tipe:** Skenario
**Soal:** An employee left the company three weeks ago, but her account still authenticates and has access to email. Which IAM process failed?

- A. Federation
- B. Attestation
- C. Deprovisioning
- D. Provisioning

**Jawaban:** C
**Pembahasan:** **Deprovisioning** harus menonaktifkan/menghapus akun, mencabut token, dan memindahkan data segera saat karyawan keluar. Akun yatim (orphaned account) adalah temuan audit yang serius.

## Soal 39
**Objektif:** 4.6
**Tipe:** Skenario
**Soal:** After signing in once to a corporate identity provider, a user can access email, CRM, and the intranet without re-entering credentials. Which capability is this?

- A. SSO
- B. MFA
- C. PAM
- D. RADIUS

**Jawaban:** A
**Pembahasan:** **SSO** memungkinkan satu autentikasi untuk banyak aplikasi melalui trust ke IdP. Risikonya: satu kredensial yang dicuri membuka banyak aplikasi, sehingga MFA dan Conditional Access wajib.

## Soal 40
**Objektif:** 4.6
**Tipe:** Perbandingan
**Soal:** Which statement correctly distinguishes SAML from OAuth?

- A. OAuth authenticates users directly; SAML authorizes APIs
- B. SAML is an authentication/authorization federation standard using XML assertions; OAuth is an authorization framework for delegated access using tokens
- C. SAML is used for API authorization; OAuth is used for browser SSO only
- D. Both are password hashing algorithms

**Jawaban:** B
**Pembahasan:** **SAML** mengirim assertion XML tentang identitas dan atribut untuk SSO enterprise. **OAuth 2.0** mendelegasikan akses (misalnya aplikasi pihak ketiga ke API) memakai access token; autentikasi di atas OAuth dilakukan oleh **OIDC**.

## Soal 41
**Objektif:** 4.6
**Tipe:** Skenario
**Soal:** A user authenticates to Active Directory and receives a ticket-granting ticket used to request service tickets. Which protocol is this?

- A. TACACS+
- B. LDAP
- C. Kerberos
- D. RADIUS

**Jawaban:** C
**Pembahasan:** **Kerberos** memakai KDC, TGT, dan service ticket untuk autentikasi mutual dalam domain. RADIUS/TACACS+ untuk AAA jaringan, LDAP untuk query direktori.

## Soal 42
**Objektif:** 4.6
**Tipe:** Perbandingan
**Soal:** Which statement about RADIUS and TACACS+ is CORRECT?

- A. RADIUS encrypts the entire packet; TACACS+ encrypts only the password
- B. Both use UDP and encrypt nothing
- C. TACACS+ is only for wireless authentication
- D. RADIUS typically uses UDP and encrypts only the password; TACACS+ uses TCP and encrypts the entire payload

**Jawaban:** D
**Pembahasan:** **RADIUS** (UDP 1812/1813) umum untuk AAA jaringan dan mengenkripsi password saja; **TACACS+** (TCP 49) memisahkan authentication, authorization, accounting dan mengenkripsi seluruh body — sering dipakai untuk admin perangkat.

## Soal 43
**Objektif:** 4.6
**Tipe:** Skenario
**Soal:** An application must query user attributes and group membership from Active Directory over a standard protocol. Which protocol is used?

- A. SMTP
- B. SNMP
- C. NTP
- D. LDAP

**Jawaban:** D
**Pembahasan:** **LDAP** adalah protokol direktori untuk membaca/mengubah objek seperti user dan group. Aksesnya harus melalui LDAPS/StartTLS agar kredensial tidak terekspos.

## Soal 44
**Objektif:** 4.6
**Tipe:** Skenario
**Soal:** Access to a resource is determined by the resource owner who sets permissions for individual users. Which access control model is this?

- A. DAC
- B. MAC
- C. RBAC
- D. ABAC

**Jawaban:** A
**Pembahasan:** **DAC** (Discretionary Access Control) memberi pemilik resource kebebasan menetapkan izin. **MAC** memakai label klasifikasi dan kebijakan sistem, **RBAC** berbasis peran, **ABAC** berbasis atribut.

## Soal 45
**Objektif:** 4.6
**Tipe:** Skenario
**Soal:** A defense contractor requires that access be based on clearance level and object classification labels, and users cannot change permissions. Which model is this?

- A. Rule-based
- B. MAC
- C. DAC
- D. RBAC

**Jawaban:** B
**Pembahasan:** **MAC** (Mandatory Access Control) memakai label keamanan dan kebijakan yang ditetapkan sistem (misalnya SELinux, Bell-LaPadula). Pengguna tidak dapat menurunkan klasifikasi atau membagikan akses.

## Soal 46
**Objektif:** 4.6
**Tipe:** Skenario
**Soal:** A hospital grants nurses access based on their job function rather than individual permissions. Which model is this?

- A. DAC
- B. ABAC
- C. MAC
- D. RBAC

**Jawaban:** D
**Pembahasan:** **RBAC** memberikan izin melalui peran (nurse, doctor, billing) sehingga pengelolaan lebih sederhana dan konsisten. **ABAC** akan memakai atribut seperti departemen, waktu, dan lokasi.

## Soal 47
**Objektif:** 4.6
**Tipe:** Skenario
**Soal:** An organization wants access decisions based on department, device compliance, time of day, and geolocation. Which model is MOST appropriate?

- A. DAC
- B. MAC
- C. ABAC
- D. RBAC

**Jawaban:** C
**Pembahasan:** **ABAC** mengevaluasi atribut subjek, objek, dan lingkungan sehingga sangat fleksibel untuk kebijakan kontekstual. Semakin banyak atribut, semakin kompleks pengujian kebijakannya.

## Soal 48
**Objektif:** 4.6
**Tipe:** Skenario
**Soal:** A developer needs temporary admin access to production for two hours to troubleshoot an outage. Which practice is BEST?

- A. Just-in-time elevation with approval and automatic revocation
- B. Grant permanent admin rights to avoid future delays
- C. Share the admin password with the team
- D. Disable MFA for the admin account

**Jawaban:** A
**Pembahasan:** **JIT access** memberi hak istimewa sementara setelah persetujuan dan mencabutnya otomatis, mengurangi jendela penyalahgunaan. Hak permanen dan password bersama melanggar least privilege.

## Soal 49
**Objektif:** 4.6
**Tipe:** Skenario
**Soal:** Which authentication method is considered phishing-resistant and passwordless?

- A. Security questions
- B. Email magic link
- C. FIDO2 security key with passkeys
- D. SMS one-time code

**Jawaban:** C
**Pembahasan:** **FIDO2/passkey** memakai kriptografi kunci publik yang terikat pada origin, sehingga tidak dapat di-phish ke domain palsu. SMS OTP rentan SIM swapping dan real-time phishing.

## Soal 50
**Objektif:** 4.6
**Tipe:** Skenario
**Soal:** A company wants to reduce the risk of credential stuffing against its web portal without changing the login experience for legitimate users. Which control is MOST appropriate?

- A. Risk-based authentication with device fingerprint and impossible-travel checks
- B. Forcing password changes every 30 days
- C. Disabling account lockout
- D. Removing MFA to reduce friction

**Jawaban:** A
**Pembahasan:** **Risk-based/adaptive authentication** memicu langkah tambahan hanya saat risiko tinggi (perangkat baru, lokasi anomali). Rotasi password berkala justru mendorong password lemah dan tidak menghentikan credential stuffing.

## Soal 51
**Objektif:** 4.6
**Tipe:** Skenario
**Soal:** Which account type should be used by an application to run scheduled tasks, with permissions limited to only the required resources?

- A. Personal account of the developer
- B. Guest account
- C. Service account with least privilege and managed credentials
- D. Shared administrator account

**Jawaban:** C
**Pembahasan:** **Service account** khusus aplikasi, dengan hak minimal dan kredensial terkelola (rotasi otomatis). Shared admin dan akun pribadi menghilangkan akuntabilitas.

## Soal 52
**Objektif:** 4.6
**Tipe:** Skenario
**Soal:** A manager reviews a report listing all users with access to the finance share and confirms each still needs it. Which process is this?

- A. Provisioning
- B. Federation
- C. Password reset
- D. Access review/attestation

**Jawaban:** D
**Pembahasan:** **Access review/attestation** memastikan hak akses masih sesuai kebutuhan dan kepatuhan. Temuan umum: hak berlebih (privilege creep) setelah mutasi jabatan.

## Soal 53
**Objektif:** 4.6
**Tipe:** Skenario
**Soal:** An organization must store administrative passwords in a vault, rotate them automatically, and record who checked them out. Which solution is this?

- A. DLP
- B. PAM
- C. SSO
- D. MDM

**Jawaban:** B
**Pembahasan:** **PAM** (Privileged Access Management) menyimpan, memutar, dan mengaudit kredensial istimewa, serta sering menyediakan session recording untuk akun admin.

## Soal 54
**Objektif:** 4.6
**Tipe:** Skenario
**Soal:** A company wants new employees to receive accounts and group memberships automatically based on their HR role, and to have them removed automatically on termination. Which approach is BEST?

- A. Annual cleanup only
- B. Automated provisioning/deprovisioning driven by HR (SCIM)
- C. Manual ticket for every account
- D. Shared department account

**Jawaban:** B
**Pembahasan:** **Automated provisioning** (sering via **SCIM**) menyelaraskan akun dengan data HR, mengurangi akun yatim dan kesalahan manual. Proses tahunan terlalu lambat untuk risiko insider.

## Soal 55
**Objektif:** 4.7
**Tipe:** Skenario
**Soal:** A cloud team wants to prevent developers from deploying storage buckets with public access, regardless of who runs the pipeline. Which control is BEST?

- A. Manual review of every deployment
- B. Annual penetration test
- C. Security awareness training
- D. Guardrails/policy as code enforced in the pipeline

**Jawaban:** D
**Pembahasan:** **Guardrails** (misalnya OPA/SCP) menolak konfigurasi berbahaya secara otomatis dan konsisten. Review manual tidak dapat diskalakan dan mudah terlewat.

## Soal 56
**Objektif:** 4.7
**Tipe:** Skenario
**Soal:** Which is a PRIMARY benefit of automating security operations with SOAR?

- A. Removal of the need for human approval
- B. Faster, consistent response and reduced analyst toil
- C. Elimination of the need for logging
- D. Guaranteed prevention of all incidents

**Jawaban:** B
**Pembahasan:** Otomasi mempercepat respons, menstandarkan langkah, dan mengurangi pekerjaan berulang. Otomasi tidak menggantikan logging, tidak menjamin pencegahan total, dan tetap memerlukan persetujuan manusia untuk aksi berisiko.

## Soal 57
**Objektif:** 4.7
**Tipe:** Skenario
**Soal:** An automation script that disables compromised accounts fails silently when the HR API changes, and no one notices for a week. Which risk of automation is demonstrated?

- A. Reduced efficiency
- B. Increased licensing cost
- C. Loss of audit trail
- D. Single point of failure and lack of monitoring

**Jawaban:** D
**Pembahasan:** Otomasi menjadi **single point of failure** bila tidak dipantau; kegagalan harus memicu alert dan ada jalur manual (fallback). Ini juga contoh **technical debt** jika integrasi tidak dipelihara.

## Soal 58
**Objektif:** 4.7
**Tipe:** Skenario
**Soal:** A CI/CD pipeline requires that secrets be fetched at runtime from a vault rather than stored in the repository. Which risk is being mitigated?

- A. Certificate expiration
- B. Hard-coded credentials exposure
- C. Insufficient logging
- D. Network latency

**Jawaban:** B
**Pembahasan:** Menyimpan secret di repo (termasuk history Git) membuatnya bocor ke siapa pun yang punya akses. Vault dengan akses berbasis identitas dan rotasi menghilangkan hard-coded credentials.

## Soal 59
**Objektif:** 4.8
**Tipe:** Definisi
**Soal:** Which sequence correctly represents the incident response lifecycle?

- A. Preparation → Detection and analysis → Containment → Eradication → Recovery → Lessons learned
- B. Detection → Preparation → Recovery → Containment → Eradication
- C. Containment → Preparation → Detection → Recovery → Eradication
- D. Preparation → Eradication → Containment → Detection → Recovery

**Jawaban:** A
**Pembahasan:** Urutan NIST: **Preparation, Detection & Analysis, Containment/Eradication/Recovery, Post-incident activity (lessons learned)**. Containment selalu sebelum eradication agar penyebaran berhenti lebih dulu.

## Soal 60
**Objektif:** 4.8
**Tipe:** Skenario
**Soal:** A workstation is confirmed infected with malware that may still be running. Investigators need volatile evidence. Which action should be taken FIRST?

- A. Delete temporary files
- B. Isolate the host from the network but keep it powered on, then capture memory
- C. Immediately power off the host
- D. Reimage the host

**Jawaban:** B
**Pembahasan:** Mematikan host menghilangkan isi memori (proses, koneksi, kunci). **Isolasi jaringan** menghentikan penyebaran sambil mempertahankan bukti volatil; urutan volatilitas: memori → cache → disk → arsip.

## Soal 61
**Objektif:** 4.8
**Tipe:** Skenario
**Soal:** After containing a ransomware outbreak, the team removes the malware, rebuilds encrypted servers, and restores data. Which phase follows next?

- A. Recovery and validation, then lessons learned
- B. Preparation
- C. Detection
- D. Legal hold

**Jawaban:** A
**Pembahasan:** **Recovery** mengembalikan layanan secara terkontrol dan memvalidasi integritas, lalu **lessons learned** memperbarui prosedur dan kontrol. Preparation adalah fase sebelum insiden.

## Soal 62
**Objektif:** 4.8
**Tipe:** Skenario
**Soal:** During an investigation, a laptop is seized and each transfer is logged with signatures, dates, and storage location. Which concept is this?

- A. Chain of custody
- B. Order of volatility
- C. Legal hold
- D. Root cause analysis

**Jawaban:** A
**Pembahasan:** **Chain of custody** mendokumentasikan siapa memegang bukti, kapan, dan di mana, sehingga bukti dapat diterima di pengadilan. Tanpa itu, integritas bukti dipertanyakan.

## Soal 63
**Objektif:** 4.8
**Tipe:** Skenario
**Soal:** A legal department instructs IT to preserve all email and logs related to a lawsuit and to suspend automatic deletion. Which process is this?

- A. Backup rotation
- B. Legal hold
- C. Data minimization
- D. Retention policy

**Jawaban:** B
**Pembahasan:** **Legal hold** menghentikan penghapusan data yang relevan dengan litigasi. Menghapus data setelah hold dapat dianggap obstruction of justice.

## Soal 64
**Objektif:** 4.8
**Tipe:** Skenario
**Soal:** After an incident, the team asks "why did the phishing email bypass the gateway and why was the user not trained?" Which activity is this?

- A. Root cause analysis
- B. Tabletop exercise
- C. Vulnerability scan
- D. Threat hunting

**Jawaban:** A
**Pembahasan:** **Root cause analysis** mencari penyebab mendasar (kontrol gagal, proses kurang) agar perbaikan tidak sekadar gejala. Hasilnya masuk ke lessons learned dan perbaikan kontrol.

## Soal 65
**Objektif:** 4.8
**Tipe:** Skenario
**Soal:** A threat hunter forms a hypothesis that attackers are using signed binaries to evade detection, then searches telemetry for evidence. Which activity is this?

- A. Compliance audit
- B. Threat hunting
- C. Vulnerability assessment
- D. Incident response

**Jawaban:** B
**Pembahasan:** **Threat hunting** berangkat dari hipotesis (bukan alert) dan mencari bukti di telemetri. Berbeda dari IR yang merespons insiden yang sudah terdeteksi.

## Soal 66
**Objektif:** 4.9
**Tipe:** Skenario
**Soal:** An analyst must determine which internal host initiated a connection to a known malicious IP at 02:14. Which log source is MOST directly useful?

- A. Asset inventory
- B. Password policy document
- C. Firewall logs showing source IP, destination IP, and timestamp
- D. DNS zone file

**Jawaban:** C
**Pembahasan:** **Firewall logs** mencatat 5-tuple (source/dest IP, port, protokol) dan aksi, sehingga dapat mengidentifikasi host asal. DNS log membantu bila hanya domain yang diketahui.

## Soal 67
**Objektif:** 4.9
**Tipe:** Skenario
**Soal:** Which tool is BEST for reconstructing an HTTP session and viewing the actual payload exchanged?

- A. SIEM correlation only
- B. SNMP polling
- C. Protocol analyzer (packet capture)
- D. NetFlow

**Jawaban:** C
**Pembahasan:** **Packet capture/protocol analyzer** (Wireshark, tcpdump) menyimpan isi paket sehingga sesi dapat direkonstruksi. NetFlow hanya metadata, SIEM menampilkan log/alert.

## Soal 68
**Objektif:** 4.9
**Tipe:** Skenario
**Soal:** An investigator needs a timeline of user logons, process execution, and file changes on a Windows host. Which source provides the MOST complete evidence?

- A. NetFlow only
- B. Antivirus scan report
- C. EDR telemetry combined with Windows event logs
- D. Firewall log only

**Jawaban:** C
**Pembahasan:** **EDR telemetry** memberi process tree dan command line, sedangkan **event logs** memberi logon/audit. Menggabungkan keduanya menghasilkan timeline yang koheren.

## Soal 69
**Objektif:** 4.9
**Tipe:** Skenario
**Soal:** Logs from servers are being overwritten after seven days, but an incident is discovered 30 days later. Which control should have been in place?

- A. Disabling logging to save space
- B. Shorter backup windows
- C. Centralized log aggregation with retention/archiving
- D. Larger local disks

**Jawaban:** C
**Pembahasan:** **Log aggregation** mengirim log ke SIEM/arsip terpusat dengan retensi sesuai kebijakan, sehingga bukti tetap tersedia dan tahan terhadap penghapusan lokal oleh penyerang.

## Soal 70
**Objektif:** 4.9
**Tipe:** Skenario
**Soal:** An analyst wants to compare the volume of outbound traffic per host over the last week to spot possible data exfiltration. Which data source is MOST appropriate?

- A. NetFlow records
- B. Full packet captures
- C. Windows registry
- D. DHCP lease file

**Jawaban:** A
**Pembahasan:** **NetFlow** menyimpan statistik byte/paket per aliran sehingga tren volume per host mudah dianalisis. Packet capture penuh terlalu besar untuk analisis jangka panjang.

## Soal 71
**Objektif:** 4.8
**Tipe:** Skenario
**Soal:** A ransomware incident is contained, but the team must decide whether to pay the ransom. Which factor is MOST important to consider first?

- A. Whether tested, isolated backups can restore the data within RTO
- B. The attackers' reputation for returning data
- C. The cryptocurrency exchange rate
- D. The number of infected hosts

**Jawaban:** A
**Pembahasan:** Pemulihan dari **backup teruji** adalah jalur utama; membayar tidak menjamin data kembali dan mendanai kejahatan. Keputusan harus melibatkan manajemen, hukum, dan asuransi.

## Soal 72
**Objektif:** 4.5
**Tipe:** Skenario
**Soal:** A company wants to block outbound traffic to known malicious IPs at the network edge while allowing all other outbound traffic. Which control is MOST appropriate?

- A. DLP
- B. Full-disk encryption
- C. Egress filtering with threat intelligence blocklist
- D. Ingress filtering only

**Jawaban:** C
**Pembahasan:** **Egress filtering** mencegah host terinfeksi berkomunikasi dengan C2 dan mempersulit exfiltration. Ingress filtering melindungi dari koneksi masuk, tetapi tidak membatasi komunikasi keluar.

## Soal 73
**Objektif:** 4.5
**Tipe:** Skenario
**Soal:** An organization wants to detect and block malicious PowerShell scripts that download and execute code. Which control combination is BEST?

- A. Allowing only local administrators to use PowerShell
- B. Script block logging, constrained language mode, and EDR behavior detection
- C. Disabling Windows Update
- D. Increasing the PowerShell execution timeout

**Jawaban:** B
**Pembahasan:** **Script block logging** merekam isi skrip, **constrained language mode** membatasi API, dan **EDR** mendeteksi perilaku mencurigakan. Membatasi ke admin saja tidak cukup karena akun admin juga bisa dicuri.

## Soal 74
**Objektif:** 4.3
**Tipe:** Skenario
**Soal:** A penetration test finds that a low-privileged user can read the shadow file. Which category of finding is this?

- A. Supply chain
- B. Privilege escalation
- C. Denial of service
- D. Cross-site scripting

**Jawaban:** B
**Pembahasan:** Akses ke file sensitif seperti `/etc/shadow` memungkinkan pengguna biasa menaikkan hak (misalnya crack hash lalu `su`). Ini eskalasi privilege lokal akibat permission yang salah.

## Soal 75
**Objektif:** 4.1
**Tipe:** Skenario
**Soal:** Which wireless setting should be disabled because it allows attackers to brute-force the PIN and join the network?

- A. WPA3
- B. 802.1X
- C. PMF
- D. WPS

**Jawaban:** D
**Pembahasan:** **WPS** PIN rentan brute force (Pixie Dust/offline attack) dan harus dimatikan. WPA3, 802.1X, dan PMF justru meningkatkan keamanan.

## Soal 76
**Objektif:** 4.2
**Tipe:** Skenario
**Soal:** An organization discovers an unauthorized server running in a lab closet, connected to the corporate network. Which control gap does this expose?

- A. Missing full-disk encryption
- B. Insufficient email filtering
- C. Inadequate asset discovery and network access control
- D. Weak password policy

**Jawaban:** C
**Pembahasan:** Server tidak terinventarisasi adalah **shadow asset**; diperlukan **discovery** rutin dan **NAC/802.1X** agar perangkat tak terdaftar tidak dapat terhubung. Ini juga masalah change management.

## Soal 77
**Objektif:** 4.6
**Tipe:** Skenario
**Soal:** Which MFA factor category does a hardware token that generates a time-based code belong to?

- A. Something you have
- B. Something you know
- C. Something you are
- D. Somewhere you are

**Jawaban:** A
**Pembahasan:** Token fisik adalah faktor **possession** (something you have). Password = knowledge, biometrik = inherence, lokasi = location-based (bukan faktor utama dalam MFA klasik).

## Soal 78
**Objektif:** 4.8
**Tipe:** Skenario
**Soal:** During an incident, the team blocks the attacker's IP at the firewall, disables the compromised account, and segments the affected VLAN. Which IR phase is this?

- A. Recovery
- B. Preparation
- C. Containment
- D. Eradication

**Jawaban:** C
**Pembahasan:** **Containment** membatasi dampak dan menghentikan penyebaran. Eradication menghilangkan akar masalah (malware, backdoor), recovery mengembalikan layanan normal.

## Soal 79
**Objektif:** 4.6
**Tipe:** Multi-select
**Soal:** Which TWO are benefits of single sign-on (SSO)? (Select TWO.)

- A. Limits the blast radius of a stolen credential
- B. Removes the need for authorization
- C. Fewer credentials for users to manage
- D. Centralized authentication logging
- E. Eliminates the need for MFA

**Jawaban:** C, D
**Pembahasan:** SSO mengurangi jumlah password dan memusatkan log autentikasi. Namun SSO memperbesar **blast radius** jika kredensial dicuri, tidak menghapus kebutuhan MFA, dan tidak menggantikan otorisasi.

## Soal 80
**Objektif:** 4.4
**Tipe:** Multi-select
**Soal:** Which TWO data sources BEST support detecting data exfiltration? (Select TWO.)

- A. NetFlow volume anomalies
- B. DLP alerts
- C. DHCP lease logs
- D. Asset inventory exports
- E. Password policy compliance reports

**Jawaban:** A, B
**Pembahasan:** **NetFlow** memperlihatkan lonjakan volume keluar per host, dan **DLP** menandai data sensitif yang meninggalkan jaringan. DHCP lease dan inventaris aset tidak menunjukkan isi atau volume transfer.

## Soal 81
**Objektif:** 4.8
**Tipe:** Multi-select
**Soal:** Which TWO actions preserve volatile evidence on a compromised host? (Select TWO.)

- A. Isolating the host from the network
- B. Powering the host off immediately
- C. Reimaging the disk
- D. Deleting temporary files
- E. Capturing memory before shutdown

**Jawaban:** A, E
**Pembahasan:** **Capture memori** harus dilakukan sebelum daya hilang, dan **isolasi jaringan** menghentikan penyebaran tanpa menghapus bukti. Mematikan host, reimage, dan menghapus file justru merusak bukti.

