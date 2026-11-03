#!/usr/bin/env python3
"""Build dist/bank-soal-lengkap.md — one readable file with questions, answers and PBQs."""
from __future__ import annotations

import json
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
BANK = ROOT / "bank-soal"


def main() -> None:
    data = json.loads((DIST / "questions.json").read_text(encoding="utf-8"))
    total = sum(len(d["questions"]) for d in data["domains"])
    multi = sum(1 for d in data["domains"] for q in d["questions"] if len(q["answers"]) > 1)

    lines: list[str] = []
    add = lines.append
    add("# Bank Soal CompTIA Security+ (SY0-701)")
    add("")
    add(
        f"**{total} soal pilihan ganda (termasuk {multi} multi-select) + 12 soal performa (PBQ), "
        "lengkap dengan pembahasan Bahasa Indonesia.**"
    )
    add("")
    add(f"Disusun: {date.today().strftime('%d %B %Y')} · Sumber soal: latihan mandiri, bukan soal resmi CompTIA.")
    add("")
    add("Bank soal ini disusun dengan bantuan kecerdasan buatan (AI) DeepSeek, lalu ditinjau untuk konsistensi.")
    add("")
    add("## Format ujian")
    add("")
    add("- Maksimal **90 soal**, **90 menit**, skor **100–900**, lulus **750**.")
    add("- Tipe soal: pilihan ganda, sesekali **multi-select**, dan **3–5 PBQ** (simulasi). Tidak ada esai.")
    add("- PBQ muncul di awal dan dapat bernilai parsial — tandai, lanjut, kembali bila ada waktu.")
    add("")
    add("## Cara pakai")
    add("")
    add("1. Kerjakan satu domain per sesi; jangan melihat kunci sebelum menjawab.")
    add("2. Tandai soal yang ragu, lalu baca pembahasan sampai paham *mengapa* jawaban lain salah.")
    add("3. Ulangi domain dengan skor terendah setelah 2–3 hari (spaced repetition).")
    add("4. Seminggu sebelum ujian, kerjakan **Ujian Simulasi** di `quiz.html` (90 soal, 90 menit).")
    add("")
    add("## Bobot domain ujian")
    add("")
    add("| Domain | Nama | Bobot | Jumlah soal di bank |")
    add("|---|---|---|---|")
    for d in data["domains"]:
        add(f"| {d['id']} | {d['name']} | {d['weight']}% | {len(d['questions'])} |")
    add(f"| | **Total** | **100%** | **{total}** |")
    add("")
    add("---")
    add("")

    for d in data["domains"]:
        add(f"# Domain {d['id']} — {d['name']} ({d['weight']}%)")
        add("")
        c = Counter(q["objective"] for q in d["questions"])
        add("Objektif yang dicakup: " + ", ".join(f"**{k}** ({v} soal)" for k, v in sorted(c.items())) + ".")
        add("")
        for q in d["questions"]:
            add(f"## Soal {q['number']} · Objektif {q['objective']} · {q['type']}")
            add("")
            add(q["stem"])
            add("")
            for o in q["options"]:
                add(f"- **{o['key']}.** {o['text']}")
            add("")
            add(f"**Jawaban: {q['answer']}**")
            add("")
            add(f"> {q['explanation']}")
            add("")

    # PBQ section
    pbq = (BANK / "06-performance-based.md").read_text(encoding="utf-8")
    # demote headings by one level so the file stays a single H1 document
    pbq = pbq.replace("\n## ", "\n### ").replace("\n# ", "\n## ")
    add("---")
    add("")
    add(pbq)
    add("")

    out = DIST / "bank-soal-lengkap.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)} ({out.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    main()
