#!/usr/bin/env python3
"""Parse bank soal Markdown -> dist/questions.json (single source of truth)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANK = ROOT / "bank-soal"
DIST = ROOT / "dist"

DOMAINS = [
    (1, "General Security Concepts", 12, "01-general-security-concepts.md"),
    (2, "Threats, Vulnerabilities, and Mitigations", 22, "02-threats-vulnerabilities-mitigations.md"),
    (3, "Security Architecture", 18, "03-security-architecture.md"),
    (4, "Security Operations", 28, "04-security-operations.md"),
    (5, "Security Program Management and Oversight", 20, "05-security-program-management.md"),
]

BLOCK_RE = re.compile(r"^## Soal (\d+)\s*$", re.MULTILINE)
OPT_RE = re.compile(r"^- ([A-E])\. (.+)$", re.MULTILINE)


def parse_file(path: Path, domain_id: int) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    marks = list(BLOCK_RE.finditer(text))
    if not marks:
        raise SystemExit(f"No questions found in {path}")

    questions = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        block = text[m.end():end]
        number = int(m.group(1))

        objective = re.search(r"\*\*Objektif:\*\*\s*([0-9.]+)", block)
        qtype = re.search(r"\*\*Tipe:\*\*\s*(.+)", block)
        stem_m = re.search(r"\*\*Soal:\*\*\s*(.+?)(?=\n- [A-E]\.)", block, re.DOTALL)
        answer = re.search(r"\*\*Jawaban:\*\*\s*([A-E])", block)
        expl = re.search(r"\*\*Pembahasan:\*\*\s*(.+)", block, re.DOTALL)
        options = [{"key": k, "text": t.strip()} for k, t in OPT_RE.findall(block)]

        missing = [
            name
            for name, value in (
                ("Objektif", objective),
                ("Tipe", qtype),
                ("Soal", stem_m),
                ("Jawaban", answer),
                ("Pembahasan", expl),
            )
            if value is None
        ]
        if missing:
            raise SystemExit(f"{path.name} Soal {number}: missing {', '.join(missing)}")
        if len(options) < 4:
            raise SystemExit(f"{path.name} Soal {number}: only {len(options)} options")
        keys = [o["key"] for o in options]
        if keys != sorted(keys) or len(set(keys)) != len(keys):
            raise SystemExit(f"{path.name} Soal {number}: option keys out of order {keys}")
        if answer.group(1) not in keys:
            raise SystemExit(f"{path.name} Soal {number}: answer not among options")

        questions.append(
            {
                "id": f"D{domain_id}-{number:02d}",
                "number": number,
                "domain": domain_id,
                "objective": objective.group(1),
                "type": qtype.group(1).strip(),
                "stem": " ".join(stem_m.group(1).split()),
                "options": options,
                "answer": answer.group(1),
                "explanation": " ".join(expl.group(1).split()),
            }
        )

    numbers = [q["number"] for q in questions]
    if numbers != list(range(1, len(numbers) + 1)):
        raise SystemExit(f"{path.name}: question numbers are not sequential: {numbers}")
    return questions


def main() -> None:
    data = {"exam": "SY0-701", "title": "CompTIA Security+ (SY0-701)", "domains": []}
    total = 0
    for domain_id, name, weight, filename in DOMAINS:
        path = BANK / filename
        if not path.exists():
            print(f"skip (not written yet): {filename}")
            continue
        qs = parse_file(path, domain_id)
        total += len(qs)
        data["domains"].append(
            {"id": domain_id, "name": name, "weight": weight, "questions": qs}
        )
        print(f"Domain {domain_id}: {len(qs):3d} soal  ({name})")

    DIST.mkdir(exist_ok=True)
    out = DIST / "questions.json"
    out.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"TOTAL: {total} soal -> {out.relative_to(ROOT)}")

    # quick stats per objective
    from collections import Counter

    for d in data["domains"]:
        c = Counter(q["objective"] for q in d["questions"])
        print(f"  D{d['id']} objektif: " + ", ".join(f"{k}={v}" for k, v in sorted(c.items())))


if __name__ == "__main__":
    sys.exit(main())
