# Domain 5 — Security Program Management and Oversight (20%)

Domain ini menguji **tata kelola**, **manajemen risiko**, **risiko pihak ketiga**, **kepatuhan**, **audit**, dan **security awareness**. Banyak istilah mirip (policy vs standard vs procedure, MOU vs MOA vs BPA, controller vs processor) — hafalkan perbedaannya.

## Soal 1
**Objektif:** 5.1
**Tipe:** Perbandingan
**Soal:** Which statement BEST describes the difference between a policy and a procedure?

- A. A policy applies only to executives; a procedure applies only to IT
- B. A policy is a high-level statement of management intent; a procedure is a detailed, step-by-step instruction
- C. A policy is optional guidance; a procedure is a legal requirement
- D. A policy describes technical settings; a procedure describes business goals

**Jawaban:** B
**Pembahasan:** **Policy** menyatakan maksud dan arah manajemen (apa dan mengapa), sedangkan **procedure** menjelaskan langkah operasional (bagaimana). **Standard** berisi persyaratan spesifik yang wajib, **guideline** bersifat rekomendasi.

## Soal 2
**Objektif:** 5.1
**Tipe:** Definisi
**Soal:** Which document defines what employees may and may not do with company computing resources?

- A. Business partnership agreement
- B. Data retention policy
- C. Acceptable use policy
- D. Service level agreement

**Jawaban:** C
**Pembahasan:** **AUP** menetapkan penggunaan yang diizinkan dan larangan, termasuk konsekuensi pelanggaran. SLA mengatur tingkat layanan, BPA mengatur kemitraan bisnis.

## Soal 3
**Objektif:** 5.1
**Tipe:** Skenario
**Soal:** An organization must define how long financial records and email are kept and how they are destroyed afterward. Which policy is required?

- A. Password policy
- B. Wireless policy
- C. Incident response policy
- D. Data retention policy

**Jawaban:** D
**Pembahasan:** **Data retention policy** menetapkan masa simpan berdasarkan kebutuhan bisnis dan regulasi, serta metode penghapusan. Ini juga mendukung e-discovery dan mengurangi risiko penyimpanan berlebih.

## Soal 4
**Objektif:** 5.1
**Tipe:** Skenario
**Soal:** A security team documents who must approve firewall changes, what testing is required, and how to roll back. Which policy governs this?

- A. Data classification policy
- B. Business continuity policy
- C. Change management policy
- D. Acceptable use policy

**Jawaban:** C
**Pembahasan:** **Change management policy** menetapkan proses persetujuan, pengujian, jadwal, dan backout plan. Tujuannya mencegah perubahan tidak terkontrol yang mengganggu keamanan dan ketersediaan.

## Soal 5
**Objektif:** 5.1
**Tipe:** Skenario
**Soal:** A company grants a temporary exception to allow an unsupported application for six months, with a documented risk owner and review date. Which governance element is this?

- A. Guideline
- B. Baseline
- C. Policy exception
- D. Standard

**Jawaban:** C
**Pembahasan:** **Exception** adalah penyimpangan resmi dan terdokumentasi dari kebijakan, dengan pemilik risiko, kontrol kompensasi, dan tanggal kedaluwarsa. Tanpa itu, penyimpangan menjadi pelanggaran tak terkelola.

## Soal 6
**Objektif:** 5.1
**Tipe:** Skenario
**Soal:** Which group is typically responsible for approving security policies and accepting residual risk at the organizational level?

- A. Help desk team
- B. External penetration tester
- C. Individual system administrators
- D. Governance/security steering committee

**Jawaban:** D
**Pembahasan:** **Security steering committee** (dewan tata kelola) menyetujui kebijakan dan menerima risiko residual. Administrator menjalankan kontrol, pen tester menguji, help desk menangani operasional.

## Soal 7
**Objektif:** 5.1
**Tipe:** Perbandingan
**Soal:** Which is an example of a standard rather than a policy?

- A. "The company is committed to protecting customer data"
- B. "If a breach occurs, call the incident hotline"
- C. "Employees should consider using password managers"
- D. "All laptops must use AES-256 full-disk encryption"

**Jawaban:** D
**Pembahasan:** **Standard** bersifat spesifik, terukur, dan wajib (AES-256). Pernyataan komitmen adalah policy, langkah operasional adalah procedure, dan saran adalah guideline.

## Soal 8
**Objektif:** 5.1
**Tipe:** Skenario
**Soal:** After a merger, two companies have conflicting security requirements. Which approach BEST resolves the conflict?

- A. Perform a gap analysis and update policies through the governance process
- B. Let each department keep its own rules indefinitely
- C. Apply the stricter rule only to the acquired company
- D. Suspend all security controls until integration finishes

**Jawaban:** A
**Pembahasan:** **Gap analysis** memetakan perbedaan kontrol, lalu kebijakan diselaraskan melalui proses tata kelola dengan persetujuan manajemen. Membiarkan aturan ganda menciptakan celah dan kebingungan audit.

## Soal 9
**Objektif:** 5.1
**Tipe:** Skenario
**Soal:** Which metric BEST indicates whether security awareness training is changing behavior?

- A. Number of training videos available
- B. Total training hours delivered
- C. Number of employees who completed onboarding
- D. Phishing simulation click rate trending downward over time

**Jawaban:** D
**Pembahasan:** **Click rate** dan **reporting rate** pada simulasi phishing menunjukkan perilaku nyata, bukan sekadar kehadiran. Metrik input (jam pelatihan) tidak membuktikan efektivitas.

## Soal 10
**Objektif:** 5.2
**Tipe:** Definisi
**Soal:** Which term describes the risk that remains after controls have been implemented?

- A. Risk appetite
- B. Risk transfer
- C. Inherent risk
- D. Residual risk

**Jawaban:** D
**Pembahasan:** **Residual risk** adalah sisa risiko setelah kontrol diterapkan. **Inherent risk** adalah risiko sebelum kontrol; manajemen harus menyetujui residual risk yang tersisa.

## Soal 11
**Objektif:** 5.2
**Tipe:** Perhitungan
**Soal:** An asset is valued at $200,000. A threat would destroy 25% of its value, and such an event is expected once every two years. What are the SLE and ALE?

- A. SLE = $200,000; ALE = $100,000
- B. SLE = $50,000; ALE = $100,000
- C. SLE = $50,000; ALE = $25,000
- D. SLE = $25,000; ALE = $50,000

**Jawaban:** C
**Pembahasan:** **SLE = Asset Value × Exposure Factor = $200,000 × 0.25 = $50,000**. **ALE = SLE × ARO = $50,000 × 0.5 = $25,000** (ARO 0,5 karena sekali per dua tahun).

## Soal 12
**Objektif:** 5.2
**Tipe:** Skenario
**Soal:** A company buys cyber insurance to cover the financial impact of a breach. Which risk response is this?

- A. Transfer
- B. Avoid
- C. Mitigate
- D. Accept

**Jawaban:** A
**Pembahasan:** **Transfer** memindahkan dampak finansial ke pihak lain (asuransi, kontrak). Risiko operasional dan reputasi tetap ada, sehingga kontrol teknis tidak boleh dihapus.

## Soal 13
**Objektif:** 5.2
**Tipe:** Skenario
**Soal:** A company stops offering a risky legacy service entirely rather than securing it. Which risk response is this?

- A. Avoid
- B. Accept
- C. Transfer
- D. Mitigate

**Jawaban:** A
**Pembahasan:** **Avoidance** menghilangkan aktivitas yang menimbulkan risiko. Ini berbeda dari mitigation yang mengurangi kemungkinan/dampak, dan acceptance yang menerima risiko.

## Soal 14
**Objektif:** 5.2
**Tipe:** Skenario
**Soal:** Management decides that a low-impact risk is acceptable because the cost of the control exceeds the potential loss. Which concept is applied?

- A. Risk avoidance
- B. Risk transference
- C. Risk elimination
- D. Risk acceptance based on cost-benefit analysis

**Jawaban:** D
**Pembahasan:** **Risk acceptance** dipilih ketika biaya kontrol lebih besar dari dampak yang diperkirakan, dan keputusan itu harus terdokumentasi. Ini bukan kelalaian selama ada analisis dan persetujuan.

## Soal 15
**Objektif:** 5.2
**Tipe:** Definisi
**Soal:** Which document records identified risks, owners, likelihood, impact, and treatment status?

- A. Risk register
- B. Incident log
- C. Asset inventory
- D. Statement of work

**Jawaban:** A
**Pembahasan:** **Risk register** adalah catatan hidup berisi risiko, pemilik, skor, dan rencana penanganan. Dokumen ini menjadi dasar pelaporan ke manajemen dan audit.

## Soal 16
**Objektif:** 5.2
**Tipe:** Skenario
**Soal:** A risk assessment uses categories such as "low, medium, high" based on expert judgment rather than monetary values. Which type of analysis is this?

- A. Monte Carlo
- B. Qualitative
- C. Quantitative
- D. ALE-based

**Jawaban:** B
**Pembahasan:** **Qualitative** memakai skala subjektif (low/medium/high) dan cepat diterapkan. **Quantitative** memakai nilai moneter seperti SLE/ALE dan membutuhkan data lebih banyak.

## Soal 17
**Objektif:** 5.2
**Tipe:** Skenario
**Soal:** Which statement BEST describes risk appetite?

- A. The amount of risk an organization is willing to accept in pursuit of its objectives
- B. The maximum downtime a system can tolerate
- C. The list of risks identified during an assessment
- D. The cost of implementing security controls

**Jawaban:** A
**Pembahasan:** **Risk appetite** adalah tingkat risiko yang bersedia diambil organisasi; **risk tolerance** adalah variasi yang dapat diterima di sekitar appetite tersebut. RTO berkaitan dengan ketersediaan, bukan selera risiko.

## Soal 18
**Objektif:** 5.2
**Tipe:** Skenario
**Soal:** A KRI shows the number of unpatched critical vulnerabilities rising for three consecutive months. What is the PRIMARY purpose of this metric?

- A. Replacing the need for vulnerability scans
- B. Early warning that risk exposure is increasing, prompting action
- C. Calculating the annual security budget
- D. Meeting the requirement to publish a security report

**Jawaban:** B
**Pembahasan:** **KRI** (Key Risk Indicator) memberi peringatan dini tentang memburuknya risiko sehingga tindakan dapat diambil sebelum menjadi insiden. Ini berbeda dari KPI yang mengukur kinerja.

## Soal 19
**Objektif:** 5.2
**Tipe:** Skenario
**Soal:** Which risk assessment approach is MOST appropriate for a rapidly changing cloud environment?

- A. Ad hoc assessment after an incident only
- B. Continuous assessment with automated monitoring
- C. One-time assessment at project start
- D. Annual assessment only

**Jawaban:** B
**Pembahasan:** Lingkungan yang berubah cepat membutuhkan **continuous risk assessment** agar risiko baru (konfigurasi berubah, aset baru) segera terdeteksi. Penilaian tahunan saja akan tertinggal.

## Soal 20
**Objektif:** 5.2
**Tipe:** Skenario
**Soal:** A risk matrix plots likelihood against impact. A risk with high likelihood and high impact should be treated how?

- A. Deferred to the next budget cycle
- B. Prioritized for immediate mitigation or avoidance
- C. Accepted without further action
- D. Transferred without notifying management

**Jawaban:** B
**Pembahasan:** Risiko di kuadran likelihood tinggi/impact tinggi menjadi prioritas utama. Keputusan tetap harus melibatkan pemilik risiko, tetapi menunda tanpa alasan kuat tidak dapat diterima.

## Soal 21
**Objektif:** 5.3
**Tipe:** Skenario
**Soal:** Before signing a contract with a new cloud vendor, a company sends a detailed security questionnaire and reviews the vendor's SOC 2 report. Which process is this?

- A. Penetration testing
- B. Internal audit
- C. Incident response
- D. Vendor due diligence

**Jawaban:** D
**Pembahasan:** **Due diligence** menilai risiko vendor sebelum kontrak melalui kuesioner, sertifikasi, dan laporan audit. Hasilnya menentukan apakah kontrol tambahan atau klausul kontrak diperlukan.

## Soal 22
**Objektif:** 5.3
**Tipe:** Skenario
**Soal:** Which contract clause allows a company to inspect a vendor's security controls and records?

- A. Non-disclosure
- B. Service level
- C. Indemnification
- D. Right-to-audit

**Jawaban:** D
**Pembahasan:** **Right-to-audit** memberi hak untuk mengaudit atau meminta bukti kepatuhan vendor. NDA mengatur kerahasiaan, SLA mengatur tingkat layanan, indemnification mengatur ganti rugi.

## Soal 23
**Objektif:** 5.3
**Tipe:** Perbandingan
**Soal:** Which document is used to define a preliminary understanding between two parties before a formal contract, often non-binding?

- A. MOU
- B. SLA
- C. BPA
- D. SOW

**Jawaban:** A
**Pembahasan:** **MOU** (Memorandum of Understanding) menyatakan niat dan pemahaman bersama, umumnya tidak mengikat secara hukum. **MOA** lebih formal dan spesifik; **BPA** mengatur kemitraan bisnis; **SOW** merinci pekerjaan.

## Soal 24
**Objektif:** 5.3
**Tipe:** Skenario
**Soal:** An organization relies on a single SaaS provider for a critical function, and migrating would require rewriting integrations. Which risk is this?

- A. Supply chain diversification
- B. Vendor lock-in
- C. Data sovereignty
- D. Shadow IT

**Jawaban:** B
**Pembahasan:** **Vendor lock-in** membuat organisasi sulit berpindah penyedia, sehingga posisi negosiasi dan ketahanan melemah. Mitigasi: standar data terbuka, exit plan, dan multi-vendor untuk fungsi kritis.

## Soal 25
**Objektif:** 5.3
**Tipe:** Skenario
**Soal:** A vendor subcontracts part of its service to another company without informing the customer. Which risk is MOST directly introduced?

- A. Decreased licensing cost
- B. Unassessed fourth-party risk in the supply chain
- C. Increased network latency
- D. Loss of data sovereignty only

**Jawaban:** B
**Pembahasan:** **Subcontractor/fourth-party** memperluas rantai pasok tanpa penilaian, sehingga kontrol dan kepatuhan tidak diketahui. Kontrak harus mewajibkan persetujuan dan pengungkapan subkontraktor.

## Soal 26
**Objektif:** 5.3
**Tipe:** Skenario
**Soal:** Which activity provides the MOST reliable evidence of a vendor's actual security posture over time?

- A. Independent audit report covering a period (SOC 2 Type II)
- B. Vendor's marketing brochure
- C. A single phone interview with sales
- D. Vendor's self-assessment completed in one day

**Jawaban:** A
**Pembahasan:** **SOC 2 Type II** menilai efektivitas kontrol selama periode tertentu oleh auditor independen. Self-assessment dan materi pemasaran tidak membuktikan operasi kontrol sehari-hari.

## Soal 27
**Objektif:** 5.3
**Tipe:** Skenario
**Soal:** A company requires its cloud provider to notify it within 24 hours of any breach involving its data. Which document should contain this requirement?

- A. Risk register
- B. Asset inventory
- C. Service level agreement or contract with security terms
- D. Acceptable use policy

**Jawaban:** C
**Pembahasan:** Kewajiban notifikasi insiden harus tertulis dalam **kontrak/SLA** (sering sebagai security addendum) agar dapat ditegakkan. AUP mengatur pengguna internal, bukan vendor.

## Soal 28
**Objektif:** 5.3
**Tipe:** Skenario
**Soal:** A vendor's product is critical, but the vendor refuses any audit rights and provides no independent certifications. What is the MOST appropriate action?

- A. Rely on the vendor's verbal assurance
- B. Document the risk and require compensating controls or choose another vendor
- C. Accept the contract without conditions
- D. Ignore the issue because the product is popular

**Jawaban:** B
**Pembahasan:** Risiko harus didokumentasikan dan diputuskan oleh pemilik risiko; kontrol kompensasi (segmentasi, monitoring, enkripsi) atau vendor alternatif dapat dipertimbangkan. Jaminan lisan bukan bukti.

## Soal 29
**Objektif:** 5.3
**Tipe:** Skenario
**Soal:** Which agreement is specifically used when two organizations exchange data and defines how that data may be processed and protected?

- A. MOU
- B. SOW
- C. Data processing agreement
- D. NDA

**Jawaban:** C
**Pembahasan:** **DPA** mengatur pemrosesan data pribadi antara controller dan processor, termasuk tujuan, keamanan, dan subprocessor. NDA hanya mengatur kerahasiaan informasi.

## Soal 30
**Objektif:** 5.4
**Tipe:** Definisi
**Soal:** Under GDPR, which party determines the purposes and means of processing personal data?

- A. Data subject
- B. Supervisory authority
- C. Data controller
- D. Data processor

**Jawaban:** C
**Pembahasan:** **Controller** menentukan tujuan dan cara pemrosesan; **processor** memproses atas nama controller; **data subject** adalah individu yang datanya diproses. Kewajiban utama kepatuhan berada pada controller.

## Soal 31
**Objektif:** 5.4
**Tipe:** Skenario
**Soal:** A US healthcare provider must protect patient records and ensure only authorized staff can access them. Which regulation applies?

- A. PCI DSS
- B. SOX
- C. FERPA
- D. HIPAA

**Jawaban:** D
**Pembahasan:** **HIPAA** mengatur perlindungan **PHI** (protected health information) di sektor kesehatan AS. PCI DSS untuk data kartu pembayaran, SOX untuk pelaporan keuangan, FERPA untuk data pendidikan.

## Soal 32
**Objektif:** 5.4
**Tipe:** Skenario
**Soal:** A retailer accepts credit cards and must comply with requirements for storing and transmitting cardholder data. Which standard applies?

- A. GDPR
- B. ISO 27001
- C. PCI DSS
- D. HIPAA

**Jawaban:** C
**Pembahasan:** **PCI DSS** menetapkan persyaratan untuk organisasi yang menangani data kartu pembayaran. ISO 27001 adalah standar sistem manajemen keamanan informasi, bukan khusus kartu.

## Soal 33
**Objektif:** 5.4
**Tipe:** Skenario
**Soal:** A company wants to demonstrate to customers that its security controls are designed appropriately at a specific point in time. Which report is MOST appropriate?

- A. SOC 2 Type I
- B. SOC 2 Type II
- C. Penetration test report
- D. Risk assessment

**Jawaban:** A
**Pembahasan:** **SOC 2 Type I** menilai desain kontrol pada satu titik waktu; **Type II** menilai efektivitas operasi selama periode. Pen test menguji eksploitabilitas, bukan kepatuhan kontrol.

## Soal 34
**Objektif:** 5.4
**Tipe:** Skenario
**Soal:** Which framework provides a voluntary, risk-based set of cybersecurity practices organized into functions such as Identify, Protect, Detect, Respond, and Recover?

- A. HIPAA Security Rule
- B. SOX
- C. NIST Cybersecurity Framework
- D. PCI DSS

**Jawaban:** C
**Pembahasan:** **NIST CSF** mengorganisasi praktik keamanan ke dalam fungsi Identify, Protect, Detect, Respond, Recover (dan Govern pada versi 2.0). Regulasi seperti HIPAA/PCI bersifat wajib untuk cakupan tertentu.

## Soal 35
**Objektif:** 5.4
**Tipe:** Skenario
**Soal:** A customer asks for written confirmation that a vendor's controls meet agreed requirements. Which document satisfies this?

- A. Asset inventory
- B. Attestation/acknowledgement letter
- C. Risk register
- D. Incident report

**Jawaban:** B
**Pembahasan:** **Attestation** adalah pernyataan resmi bahwa kontrol memenuhi persyaratan, sering didukung audit. Ini berbeda dari acknowledgment yang hanya menandakan penerimaan dokumen.

## Soal 36
**Objektif:** 5.4
**Tipe:** Skenario
**Soal:** Which is a potential consequence of non-compliance with a regulatory framework?

- A. Fines, sanctions, reputational damage, and loss of license
- B. Increased bandwidth
- C. Faster incident response
- D. Reduced need for audits

**Jawaban:** A
**Pembahasan:** Konsekuensi ketidakpatuhan mencakup **denda, sanksi, kerusakan reputasi, kehilangan lisensi, dan dampak kontrak**. Kepatuhan bukan jaminan keamanan, tetapi pelanggaran membawa risiko hukum dan bisnis.

## Soal 37
**Objektif:** 5.4
**Tipe:** Skenario
**Soal:** A company processes EU residents' data and must respond to requests to access or delete personal data. Which concept is this?

- A. Right-to-audit
- B. Data subject rights
- C. Data sovereignty
- D. Data minimization

**Jawaban:** B
**Pembahasan:** **Data subject rights** (akses, koreksi, penghapusan, portabilitas) mengharuskan organisasi memiliki proses untuk menemukan dan menghapus data pribadi. Ini memerlukan inventaris data yang baik.

## Soal 38
**Objektif:** 5.5
**Tipe:** Perbandingan
**Soal:** Which statement BEST distinguishes an audit from an assessment?

- A. An assessment results in certification; an audit does not
- B. They are identical activities with different names
- C. An audit provides independent, formal verification against criteria; an assessment is often an internal evaluation of controls or maturity
- D. An audit is always performed by employees; an assessment by regulators

**Jawaban:** C
**Pembahasan:** **Audit** bersifat formal, independen, dan berbasis bukti terhadap kriteria (misalnya ISO 27001, SOC 2). **Assessment** bisa internal dan lebih fleksibel untuk mengukur maturity atau kesiapan.

## Soal 39
**Objektif:** 5.5
**Tipe:** Skenario
**Soal:** An internal audit finds that 30% of servers are missing critical patches. What should happen NEXT?

- A. Document the finding, assign an owner, and track remediation to closure
- B. Delete the finding to protect the team
- C. Immediately fire the administrators
- D. Wait for the external audit to confirm

**Jawaban:** A
**Pembahasan:** Temuan audit harus dicatat dengan bukti, ditindaklanjuti pemilik yang jelas, dan diverifikasi ulang. Menghapus temuan adalah pelanggaran integritas audit.

## Soal 40
**Objektif:** 5.5
**Tipe:** Skenario
**Soal:** Before an external audit, a company reviews its own controls and evidence. Which activity is this?

- A. Penetration test
- B. Tabletop exercise
- C. Threat hunt
- D. Internal audit/readiness assessment

**Jawaban:** D
**Pembahasan:** **Internal audit/readiness assessment** menemukan kekurangan sebelum auditor eksternal datang, memberi waktu perbaikan. Pen test menguji keamanan teknis, bukan kesiapan bukti kepatuhan.

## Soal 41
**Objektif:** 5.6
**Tipe:** Skenario
**Soal:** A company runs monthly phishing simulations and tracks how many users report suspicious emails. Which metric BEST demonstrates program improvement?

- A. Number of emails sent
- B. Number of employees trained once
- C. Total budget spent
- D. Increased reporting rate and decreased click rate

**Jawaban:** D
**Pembahasan:** **Reporting rate naik** dan **click rate turun** menunjukkan pengguna semakin waspada dan mau melaporkan. Mengukur jumlah email terkirim tidak menunjukkan perubahan perilaku.

## Soal 42
**Objektif:** 5.6
**Tipe:** Skenario
**Soal:** An attacker holds the door open for an employee carrying boxes and enters the building without a badge. Which social engineering technique is this?

- A. Shoulder surfing
- B. Pretexting
- C. Phishing
- D. Tailgating

**Jawaban:** D
**Pembahasan:** **Tailgating** (piggybacking) adalah mengikuti orang berwenang masuk tanpa otorisasi. Mitigasi: access control vestibule, pelatihan, dan kebijakan menantang orang tak dikenal.

## Soal 43
**Objektif:** 5.6
**Tipe:** Skenario
**Soal:** Which training is MOST important for the finance department to prevent business email compromise?

- A. Server hardening
- B. Verifying payment changes through a separate known phone number
- C. Learning to create strong passwords only
- D. Physical security awareness

**Jawaban:** B
**Pembahasan:** BEC mengeksploitasi urgensi dan otoritas; kontrol kuncinya adalah **verifikasi out-of-band** sebelum mengubah data pembayaran. Password kuat tidak mencegah transfer yang salah.

## Soal 44
**Objektif:** 5.6
**Tipe:** Skenario
**Soal:** A company wants to increase engagement in security training using points, badges, and leaderboards. Which technique is this?

- A. Phishing simulation
- B. Tabletop exercise
- C. Role-based training
- D. Gamification

**Jawaban:** D
**Pembahasan:** **Gamification** meningkatkan partisipasi melalui elemen permainan. Simulasi phishing melatih deteksi, role-based training menyesuaikan materi dengan pekerjaan.

## Soal 45
**Objektif:** 5.6
**Tipe:** Skenario
**Soal:** An employee finds a suspicious email and forwards it to the security team instead of clicking. Which behavior is being reinforced?

- A. Separation of duties
- B. Incident reporting culture
- C. Clean desk policy
- D. Least privilege

**Jawaban:** B
**Pembahasan:** **Reporting culture** memungkinkan deteksi dini dan respons cepat. Program awareness harus mempermudah pelaporan (tombol report) dan memberi umpan balik positif, bukan menghukum kesalahan.

## Soal 46
**Objektif:** 5.6
**Tipe:** Skenario
**Soal:** Which policy BEST reduces the risk of sensitive documents being photographed or removed from the office?

- A. Password complexity policy
- B. Change management policy
- C. Data retention policy
- D. Clean desk and clear screen policy

**Jawaban:** D
**Pembahasan:** **Clean desk/clear screen** mencegah dokumen dan layar terbuka ditinggal tanpa pengawasan. Ini kontrol operasional sederhana yang sering diuji dalam audit fisik.

## Soal 47
**Objektif:** 5.6
**Tipe:** Skenario
**Soal:** Which awareness topic is MOST relevant for employees who work remotely using personal Wi-Fi?

- A. Risks of unsecured networks and the need for VPN/secure configuration
- B. How to rack servers
- C. Fire suppression procedures
- D. Cable management standards

**Jawaban:** A
**Pembahasan:** Pekerja remote menghadapi risiko jaringan tidak tepercaya (evil twin, sniffing), sehingga perlu VPN, verifikasi jaringan, dan kebijakan perangkat. Topik fisik seperti rack server tidak relevan bagi mereka.

## Soal 48
**Objektif:** 5.6
**Tipe:** Skenario
**Soal:** An insider threat program wants employees to recognize and report unusual behavior such as attempts to bypass controls. Which training element is MOST appropriate?

- A. Scenario-based training with reporting channels
- B. Only annual policy acknowledgement
- C. Technical patch management training
- D. Fire drill training

**Jawaban:** A
**Pembahasan:** **Scenario-based training** melatih karyawan mengenali tanda-tanda dan melapor melalui kanal yang jelas (termasuk anonim). Sekadar menandatangani kebijakan tidak mengubah kemampuan mendeteksi.

## Soal 49
**Objektif:** 5.6
**Tipe:** Skenario
**Soal:** A phishing simulation has a very low click rate, but few users report the simulated emails. What should the program focus on NEXT?

- A. Increasing the difficulty of simulations only
- B. Ending the program because click rate is low
- C. Punishing users who did not report
- D. Encouraging reporting and simplifying the report process

**Jawaban:** D
**Pembahasan:** **Reporting rate** penting karena laporan pengguna mempercepat respons terhadap serangan nyata. Program harus mempermudah pelaporan dan memberi umpan balik, bukan menghukum.

## Soal 50
**Objektif:** 5.1
**Tipe:** Skenario
**Soal:** Which document would a company use to define expected performance and availability of a service provided to a customer?

- A. AUP
- B. SLA
- C. MOU
- D. NDA

**Jawaban:** B
**Pembahasan:** **SLA** menetapkan tingkat layanan terukur (uptime, waktu respons, sanksi). MOU menyatakan niat, NDA kerahasiaan, AUP penggunaan yang dapat diterima.

## Soal 51
**Objektif:** 5.2
**Tipe:** Multi-select
**Soal:** Which TWO inputs are used in quantitative risk analysis? (Select TWO.)

- A. Red/amber/green risk ratings
- B. Delphi expert consensus
- C. Risk matrix colour bands
- D. Single loss expectancy (SLE)
- E. Annualized rate of occurrence (ARO)

**Jawaban:** D, E
**Pembahasan:** Analisis **kuantitatif** memakai angka moneter seperti **SLE** dan **ARO** (ALE = SLE × ARO). Skala RAG, Delphi, dan matriks warna adalah teknik kualitatif.

## Soal 52
**Objektif:** 5.4
**Tipe:** Multi-select
**Soal:** Which TWO are GDPR obligations for an organization processing EU personal data? (Select TWO.)

- A. Publishing the source code of internal applications
- B. Responding to data subject access requests
- C. Notifying the supervisory authority of qualifying breaches within 72 hours
- D. Encrypting all data specifically with AES-256
- E. Retaining personal data indefinitely for audit purposes

**Jawaban:** B, C
**Pembahasan:** GDPR memberi **hak subjek data** (akses, koreksi, penghapusan) dan mewajibkan **notifikasi pelanggaran** ke otoritas dalam 72 jam bila memenuhi kriteria. GDPR tidak menetapkan algoritma tertentu dan melarang penyimpanan tanpa batas.
