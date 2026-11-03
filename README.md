# CompTIA Security+ (SY0-701) — Bank Soal & Latihan

**286 soal pilihan ganda + 12 soal performa (PBQ)**, semuanya dengan pembahasan Bahasa Indonesia. Soal ditulis mengikuti struktur resmi lima domain SY0-701, bukan salinan soal ujian.

## Mulai cepat

| Kalau Anda ingin… | Buka |
|---|---|
| Latihan interaktif dengan timer dan skor | **[`dist/quiz.html`](dist/quiz.html)** — klik dua kali, jalan offline di browser |
| Membaca semua soal + pembahasan | [`dist/bank-soal-lengkap.md`](dist/bank-soal-lengkap.md) |
| Cetak / belajar dari HP | [`dist/Security-Plus-SY0-701-Bank-Soal.pdf`](dist/Security-Plus-SY0-701-Bank-Soal.pdf) |
| Mengedit atau menambah soal | [`bank-soal/`](bank-soal/) |

## Isi bank soal

| Domain | Materi | Bobot ujian | Soal | Objektif yang dicakup |
|---|---|---|---|---|
| 1 | General Security Concepts | 12% | 36 | 1.1 – 1.4 |
| 2 | Threats, Vulnerabilities, and Mitigations | 22% | 74 | 2.1 – 2.5 |
| 3 | Security Architecture | 18% | 48 | 3.1 – 3.4 |
| 4 | Security Operations | 28% | 78 | 4.1 – 4.9 |
| 5 | Security Program Management and Oversight | 20% | 50 | 5.1 – 5.6 |
| — | Performance-based questions (PBQ) | — | 12 | konfigurasi, matching, urutan, analisis |

Total **286 MCQ + 12 PBQ**. Kunci jawaban tersebar merata di A/B/C/D (72/72/71/71) supaya tidak bisa ditebak polanya.

## Mode di `quiz.html`

- **Ujian Simulasi** — 90 soal, 90 menit, komposisi domain sesuai bobot resmi (11/20/16/25/18), skor akhir 100–900 dengan ambang lulus 750.
- **Latihan per Domain** — 20 soal acak dari satu domain, pembahasan langsung muncul setelah menjawab.
- **Latihan Cepat** — 25 soal acak lintas domain tanpa timer.
- **Ulangi yang Salah** — soal yang pernah salah disimpan di browser dan hilang otomatis setelah dijawab benar.

Fitur lain: navigasi grid soal, tanda ragu-ragu, shortcut keyboard (`1`–`4`, `←`/`→`, `F`), rincian skor per domain, pembahasan semua jawaban yang salah, dan riwayat sesi.

> Skor 100–900 adalah simulasi sederhana (persentase benar dipetakan ke skala), bukan penskoran resmi CompTIA. Anggap ≥750 sebagai indikasi siap, bukan jaminan.

## Rencana belajar 4 minggu

| Pekan | Fokus | Target harian |
|---|---|---|
| 1 | Domain 1 + 2 (kontrol, kriptografi, threat actor, vektor, kerentanan) | 25 soal + baca ulang pembahasan yang salah |
| 2 | Domain 3 (arsitektur, cloud, data, resiliensi) | 25 soal + ringkas tabel perbandingan |
| 3 | Domain 4 (hardening, vuln mgmt, monitoring, IAM, IR) | 30 soal, bagi per sub-objektif |
| 4 | Domain 5 + simulasi penuh | 2× Ujian Simulasi + ulangi semua soal salah |

Aturan belajar yang penting:

1. **Jawab dulu, baru buka kunci.** Untuk PDF, kerjakan satu domain lalu periksa bagian kunci.
2. **Baca pembahasan soal yang benar juga** bila jawaban Anda hasil tebakan.
3. **Catat pola salah**, bukan hanya materinya: salah baca kata kunci (`BEST`, `MOST`, `FIRST`, `MINIMAL`), tertukar istilah mirip (IDS/IPS, RADIUS/TACACS+, RTO/RPO), atau tidak hafal angka (CVSS, port, masa retensi).
4. **Ulangi soal salah setelah 2–3 hari.** Di quiz.html gunakan mode *Ulangi yang Salah*.
5. **Seminggu terakhir**: satu simulasi 90 menit setiap 2 hari, lalu bedah soal yang salah.

## Materi yang sering keluar dan sering tertukar

- Kategori kontrol (technical/managerial/operational/physical) vs tipe (preventive/deterrent/detective/corrective/compensating/directive)
- Zero trust: policy engine vs policy administrator vs policy enforcement point
- Enkripsi: symmetric vs asymmetric, hashing + salt, tokenization vs masking, HSM vs TPM vs secure enclave
- Serangan: on-path, ARP/DNS poisoning, VLAN hopping, deauth, evil twin, credential stuffing vs password spraying
- Arsitektur: fail-open vs fail-closed, inline vs passive, DMZ, ZTNA vs VPN, SASE
- Data: at rest/in transit/in use, sovereignty, retention, sanitization
- Resiliensi: RTO vs RPO, hot/warm/cold site, 3-2-1 backup, MTTR vs MTBF
- Operasi: SIEM vs SOAR vs EDR vs XDR, FIM, NAC, DLP
- IAM: DAC/MAC/RBAC/ABAC, SAML vs OAuth vs OIDC, RADIUS vs TACACS+, Kerberos, PAM, JIT
- Risiko: SLE/ALE/ARO, risk response (avoid/mitigate/transfer/accept), risk register, residual risk
- Tata kelola: policy vs standard vs procedure vs guideline, MOU/MOA/BPA/NDA/SLA/DPA, SOC 2 Type I vs II

## Struktur repo

```
bank-soal/                    sumber soal (Markdown, mudah diedit)
  01-general-security-concepts.md
  02-threats-vulnerabilities-mitigations.md
  03-security-architecture.md
  04-security-operations.md
  05-security-program-management.md
  06-performance-based.md     PBQ
tools/
  parse_bank.py               Markdown -> dist/questions.json (validasi format)
  balance_options.py          meratakan posisi jawaban A-D
  build_html.py               membuat quiz.html mandiri
  build_md.py                 menggabungkan semua soal + pembahasan
  build_docx.py               membuat DOCX (soal, kunci, PBQ)
  test_quiz.mjs               smoke test logika kuis (Node, tanpa browser)
dist/                         hasil build (jangan diedit manual)
```

### Build ulang

Butuh Python 3 dengan `python-docx`, Node.js, dan LibreOffice Kit (untuk PDF).

```powershell
python tools/parse_bank.py
python tools/build_html.py
python tools/build_md.py
python tools/build_docx.py
node tools/test_quiz.mjs
```

Konversi PDF memakai LibreOffice Kit CLI:

```powershell
node <libreoffice-kit>/lib/cli.js convert `
  --input dist/Security-Plus-SY0-701-Bank-Soal.docx `
  --output dist/Security-Plus-SY0-701-Bank-Soal.pdf
```

Format soal yang dipakai `parse_bank.py`:

```markdown
## Soal 1
**Objektif:** 1.1
**Tipe:** Skenario
**Soal:** Teks pertanyaan…
- A. Opsi pertama
- B. Opsi kedua
- C. Opsi ketiga
- D. Opsi keempat
**Jawaban:** B
**Pembahasan:** Penjelasan dalam Bahasa Indonesia.
```

## Catatan

- Soal dibuat untuk latihan mandiri dan **bukan** soal resmi CompTIA, bukan brain dump, dan tidak berafiliasi dengan CompTIA, Inc.
- Materi mengacu pada objektif SY0-701 v1.0. Selalu cek [situs resmi CompTIA](https://www.comptia.org/certifications/security) untuk detail ujian terbaru (harga, jumlah soal, kebijakan).
- Ujian asli: maksimal 90 soal, 90 menit, skor 100–900, lulus **750**. PBQ muncul di awal ujian.
