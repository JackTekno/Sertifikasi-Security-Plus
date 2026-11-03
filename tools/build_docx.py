#!/usr/bin/env python3
"""Build the printable DOCX (questions + answer key + PBQ) from dist/questions.json."""
from __future__ import annotations

import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
BANK = ROOT / "bank-soal"

INK = RGBColor(0x1B, 0x2A, 0x41)
MUTED = RGBColor(0x5B, 0x6B, 0x88)
ACCENT = RGBColor(0x0F, 0x4C, 0x81)
OK = RGBColor(0x0E, 0x7A, 0x5A)


def set_cell_bg(cell, hex_color: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tc_pr.append(shd)


def add_page_field(paragraph) -> None:
    run = paragraph.add_run()
    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = "PAGE"
    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    run._r.append(fld_begin)
    run._r.append(instr)
    run._r.append(fld_end)


def style_doc(doc: Document) -> None:
    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = INK
    normal.paragraph_format.space_after = Pt(4)
    normal.paragraph_format.line_spacing = 1.12

    for name, size, color, before, after in (
        ("Heading 1", 17, ACCENT, 0, 10),
        ("Heading 2", 12.5, ACCENT, 12, 4),
        ("Heading 3", 11.5, INK, 10, 3),
    ):
        st = doc.styles[name]
        st.font.name = "Calibri"
        st.font.size = Pt(size)
        st.font.bold = True
        st.font.color.rgb = color
        st.paragraph_format.space_before = Pt(before)
        st.paragraph_format.space_after = Pt(after)
        st.paragraph_format.keep_with_next = True


def add_runs(paragraph, text: str, bold: bool = False) -> None:
    """Add text with **bold** segments (backticks are stripped)."""
    text = text.replace("`", "")
    for i, part in enumerate(re.split(r"\*\*(.+?)\*\*", text)):
        if not part:
            continue
        run = paragraph.add_run(part)
        run.bold = bold or (i % 2 == 1)


def md_to_docx(doc: Document, text: str, level_offset: int = 1) -> None:
    """Very small Markdown subset -> DOCX (headings, bullets, tables, bold, quotes)."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        if line.startswith("#"):
            m = re.match(r"^(#+)\s+(.*)$", line)
            if m:
                level = min(4, len(m.group(1)) + level_offset)
                doc.add_heading(m.group(2).strip(), level=level)
                i += 1
                continue
        if line.startswith("|") and i + 1 < len(lines) and set(lines[i + 1].replace("|", "").strip()) <= set("-: "):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            rows = [r for r in rows if not set("".join(r)) <= set("-: ")]
            if rows:
                cols = max(len(r) for r in rows)
                table = doc.add_table(rows=len(rows), cols=cols)
                table.style = "Light Grid Accent 1"
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                for r_idx, row in enumerate(rows):
                    for c_idx in range(cols):
                        cell = table.cell(r_idx, c_idx)
                        cell.text = ""
                        p = cell.paragraphs[0]
                        add_runs(p, row[c_idx] if c_idx < len(row) else "", bold=(r_idx == 0))
                        for run in p.runs:
                            run.font.size = Pt(9)
                        if r_idx == 0:
                            set_cell_bg(cell, "DCE9F7")
                doc.add_paragraph()
            continue
        if line.startswith("> "):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.5)
            add_runs(p, line[2:])
            for run in p.runs:
                run.font.color.rgb = MUTED
                run.italic = True
            i += 1
            continue
        if line.startswith(("- ", "* ")):
            p = doc.add_paragraph(style="List Bullet")
            add_runs(p, line[2:])
            i += 1
            continue
        if re.match(r"^\d+\.\s", line):
            p = doc.add_paragraph(style="List Number")
            add_runs(p, re.sub(r"^\d+\.\s", "", line))
            i += 1
            continue
        p = doc.add_paragraph()
        add_runs(p, line)
        i += 1


def build() -> Path:
    data = json.loads((DIST / "questions.json").read_text(encoding="utf-8"))
    domains = data["domains"]
    total = sum(len(d["questions"]) for d in domains)

    doc = Document()
    style_doc(doc)
    section = doc.sections[0]
    section.page_height, section.page_width = Cm(29.7), Cm(21.0)
    for attr in ("top_margin", "bottom_margin"):
        setattr(section, attr, Cm(1.8))
    for attr in ("left_margin", "right_margin"):
        setattr(section, attr, Cm(2.0))

    # header / footer
    header = section.header.paragraphs[0]
    header.text = "CompTIA Security+ SY0-701 · Bank Soal Latihan"
    header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    for run in header.runs:
        run.font.size = Pt(8)
        run.font.color.rgb = MUTED

    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = footer.add_run("Halaman ")
    run.font.size = Pt(8)
    run.font.color.rgb = MUTED
    add_page_field(footer)
    for run in footer.runs:
        run.font.size = Pt(8)
        run.font.color.rgb = MUTED

    # ---------------- cover ----------------
    for _ in range(3):
        doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("BANK SOAL")
    r.font.size = Pt(30)
    r.font.bold = True
    r.font.color.rgb = ACCENT
    r.font.name = "Calibri"

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("CompTIA Security+ (SY0-701)")
    r.font.size = Pt(22)
    r.font.bold = True
    r.font.color.rgb = INK

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(f"{total} soal pilihan ganda + 12 soal performa (PBQ)")
    r.font.size = Pt(13)
    r.font.color.rgb = MUTED

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Dengan kunci jawaban dan pembahasan Bahasa Indonesia")
    r.font.size = Pt(11)
    r.font.italic = True
    r.font.color.rgb = MUTED

    doc.add_paragraph()
    table = doc.add_table(rows=1, cols=3)
    table.style = "Light Grid Accent 1"
    hdr = table.rows[0].cells
    for idx, txt in enumerate(("Domain", "Materi", "Bobot")):
        hdr[idx].text = txt
        set_cell_bg(hdr[idx], "DCE9F7")
        for run in hdr[idx].paragraphs[0].runs:
            run.bold = True
            run.font.size = Pt(9)
    for d in domains:
        cells = table.add_row().cells
        cells[0].text = f"D{d['id']}"
        cells[1].text = d["name"]
        cells[2].text = f"{d['weight']}%"
        for c in cells:
            for run in c.paragraphs[0].runs:
                run.font.size = Pt(9)

    for _ in range(2):
        doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(f"Edisi {date.today().strftime('%d %B %Y')}")
    r.font.size = Pt(10)
    r.font.color.rgb = MUTED
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Materi latihan mandiri — bukan soal resmi CompTIA dan tidak berafiliasi dengan CompTIA, Inc.")
    r.font.size = Pt(8)
    r.font.color.rgb = MUTED
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Bank soal disusun dengan bantuan kecerdasan buatan (AI) DeepSeek.")
    r.font.size = Pt(8)
    r.font.color.rgb = MUTED

    # ---------------- how to use ----------------
    doc.add_page_break()
    doc.add_heading("Format Ujian SY0-701", level=1)
    for line in (
        "Maksimal 90 soal dalam 90 menit, skor berskala 100–900, ambang lulus 750.",
        "Tipe soal: pilihan ganda satu jawaban, sesekali multi-select (pilih dua/tiga), dan 3–5 performance-based questions (PBQ). Tidak ada soal esai.",
        "PBQ muncul di awal ujian dan dapat diberi nilai parsial; tandai lalu lanjut bila macet, kembali lagi jika ada waktu.",
        "PBQ berbentuk simulasi: menempatkan perangkat di zona jaringan, menyusun aturan firewall, membaca log, hardening endpoint, mengatur IAM, memilih algoritma kriptografi, konfigurasi Wi-Fi, dan memprioritaskan kerentanan.",
    ):
        p = doc.add_paragraph(style="List Bullet")
        p.add_run(line)
    p = doc.add_paragraph()
    r = p.add_run("Periksa selalu halaman resmi CompTIA untuk memastikan versi ujian yang berlaku (SY0-701 vs SY0-801) dan ketentuan terbaru.")
    r.font.size = Pt(9)
    r.font.color.rgb = MUTED
    r.italic = True

    doc.add_heading("Cara Menggunakan Bank Soal Ini", level=1)
    for line in (
        "Kerjakan satu domain per sesi. Tutup bagian kunci jawaban sampai semua soal domain tersebut selesai dijawab.",
        "Beri tanda pada soal yang ragu. Setelah selesai, baca pembahasan bukan hanya untuk soal yang salah, tetapi juga yang benar karena kebetulan.",
        "Catat pola kesalahan: apakah karena tidak tahu istilah, salah membaca kata kunci (BEST/MOST/FIRST), atau kurang teliti pada skenario.",
        "Ulangi domain dengan skor terendah setelah 2–3 hari, lalu campur semua domain seminggu sekali.",
        "Seminggu sebelum ujian, gunakan quiz.html: mode Ujian Simulasi (90 soal, 90 menit) untuk melatih stamina dan manajemen waktu.",
        "Untuk PBQ, tulis jawaban di kertas terpisah lalu bandingkan dengan jawaban model. Fokus pada urutan langkah dan justifikasi.",
    ):
        p = doc.add_paragraph(style="List Bullet")
        p.add_run(line)

    doc.add_paragraph()
    p = doc.add_paragraph()
    r = p.add_run("Kata kunci ujian: ")
    r.bold = True
    p.add_run(
        "BEST / MOST likely / FIRST / MINIMAL — empat kata ini sering menentukan pilihan mana yang benar "
        "ketika lebih dari satu opsi tampak masuk akal. Pilih opsi yang paling langsung menjawab skenario, "
        "bukan yang paling canggih."
    )

    # ---------------- part I: questions ----------------
    doc.add_page_break()
    p = doc.add_paragraph()
    r = p.add_run("BAGIAN I — SOAL")
    r.font.size = Pt(26)
    r.bold = True
    r.font.color.rgb = ACCENT
    p = doc.add_paragraph()
    r = p.add_run(f"{total} soal pilihan ganda, dikelompokkan per domain")
    r.font.size = Pt(11)
    r.font.color.rgb = MUTED

    for d in domains:
        h = doc.add_heading(f"Domain {d['id']} — {d['name']} ({d['weight']}%)", level=1)
        h.paragraph_format.page_break_before = True
        c = Counter(q["objective"] for q in d["questions"])
        p = doc.add_paragraph()
        r = p.add_run(f"{len(d['questions'])} soal · objektif: " + ", ".join(sorted(c)))
        r.font.size = Pt(9)
        r.font.color.rgb = MUTED

        for q in d["questions"]:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(9)
            p.paragraph_format.keep_together = True
            p.paragraph_format.keep_with_next = True
            r = p.add_run(f"{q['number']}. ")
            r.bold = True
            r.font.color.rgb = ACCENT
            p.add_run(q["stem"])
            tag = doc.add_paragraph()
            tag.paragraph_format.space_after = Pt(2)
            tag.paragraph_format.keep_with_next = True
            r = tag.add_run(f"Objektif {q['objective']} · {q['type']}")
            r.font.size = Pt(7.5)
            r.font.color.rgb = MUTED
            for o_idx, o in enumerate(q["options"]):
                op = doc.add_paragraph()
                op.paragraph_format.left_indent = Cm(0.7)
                op.paragraph_format.space_after = Pt(1)
                op.paragraph_format.keep_together = True
                op.paragraph_format.keep_with_next = o_idx < len(q["options"]) - 1
                r = op.add_run(f"{o['key']}.  ")
                r.bold = True
                op.add_run(o["text"])

    # ---------------- part II: answer key ----------------
    doc.add_page_break()
    p = doc.add_paragraph()
    r = p.add_run("BAGIAN II — KUNCI JAWABAN & PEMBAHASAN")
    r.font.size = Pt(26)
    r.bold = True
    r.font.color.rgb = ACCENT
    p = doc.add_paragraph()
    r = p.add_run("Periksa jawaban setelah menyelesaikan satu domain penuh.")
    r.font.size = Pt(11)
    r.font.color.rgb = MUTED

    for d in domains:
        h = doc.add_heading(f"Kunci Domain {d['id']} — {d['name']}", level=1)
        h.paragraph_format.page_break_before = True

        qs = d["questions"]
        per_row = 10
        rows = (len(qs) + per_row - 1) // per_row
        table = doc.add_table(rows=rows, cols=per_row)
        table.style = "Table Grid"
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        for idx, q in enumerate(qs):
            cell = table.cell(idx // per_row, idx % per_row)
            cell.text = ""
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(f"{q['number']}. {q['answer'].replace(', ', ',')}")
            r.font.size = Pt(8.5)
            r.bold = True
        doc.add_paragraph()

        for q in qs:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(7)
            r = p.add_run(f"{q['number']}. Jawaban {q['answer']}")
            r.bold = True
            r.font.color.rgb = OK
            r = p.add_run(f"  · Objektif {q['objective']}")
            r.font.size = Pt(8)
            r.font.color.rgb = MUTED
            p2 = doc.add_paragraph()
            add_runs(p2, q["explanation"])

    # ---------------- part III: PBQ ----------------
    doc.add_page_break()
    p = doc.add_paragraph()
    r = p.add_run("BAGIAN III — SOAL PERFORMA (PBQ)")
    r.font.size = Pt(26)
    r.bold = True
    r.font.color.rgb = ACCENT
    md_to_docx(doc, (BANK / "06-performance-based.md").read_text(encoding="utf-8"), level_offset=0)

    out = DIST / "Security-Plus-SY0-701-Bank-Soal.docx"
    doc.save(out)
    print(f"Wrote {out.relative_to(ROOT)} ({out.stat().st_size/1024:.0f} KB)")
    return out


if __name__ == "__main__":
    build()
