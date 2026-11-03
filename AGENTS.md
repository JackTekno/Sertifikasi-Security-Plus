# Panduan Repo

## Git

- Setiap perubahan yang sudah selesai dan tervalidasi **wajib di-commit dan di-push** ke `origin main`.
- Penulis dan committer commit hanya pemilik repo. **Jangan** menambahkan trailer `Co-authored-by`, `Generated with`, atau atribusi alat bantu apa pun (Claude, Copilot, dan sejenisnya).
- Pesan commit ringkas, jelaskan isi perubahan; boleh Bahasa Indonesia atau Inggris.

## Struktur

- `bank-soal/` — sumber soal Markdown (satu file per domain, plus PBQ).
- `tools/` — pipeline build: parse → build HTML/Markdown/DOCX → PDF.
- `dist/` — hasil build, ikut di-commit agar bisa langsung dibuka dari GitHub.

## Validasi sebelum commit

```powershell
python tools/parse_bank.py
node tools/test_quiz.mjs
```
