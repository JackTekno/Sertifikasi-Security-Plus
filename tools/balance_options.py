#!/usr/bin/env python3
"""Rebalance answer positions in bank-soal/*.md.

The authored bank placed the correct option first far too often (72% "A"), which
teaches the wrong pattern. This rotates each question's options deterministically
so the answer letters are evenly distributed, then rewrites the source files.
Explanations never reference option letters, so only option order and the
`**Jawaban:**` letter change.
"""
from __future__ import annotations

import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANK = ROOT / "bank-soal"
FILES = [
    "01-general-security-concepts.md",
    "02-threats-vulnerabilities-mitigations.md",
    "03-security-architecture.md",
    "04-security-operations.md",
    "05-security-program-management.md",
]
BLOCK = re.compile(r"(?ms)^## Soal (\d+)\s*$(.*?)(?=^## Soal \d+\s*$|\Z)")
OPT = re.compile(r"^- ([A-E])\. (.+)$", re.MULTILINE)
ANS = re.compile(r"\*\*Jawaban:\*\*\s*([A-E](?:\s*,\s*[A-E])*)")


def main() -> None:
    blocks = []
    for name in FILES:
        path = BANK / name
        text = path.read_text(encoding="utf-8")
        items = []
        for m in BLOCK.finditer(text):
            body = m.group(2)
            opts = OPT.findall(body)
            ans = ANS.search(body)
            if not opts or not ans:
                raise SystemExit(f"{name} Soal {m.group(1)}: cannot parse options/answer")
            answer = ans.group(1).strip()
            items.append(
                (m.start(2), m.end(2), body, [t for _, t in opts], answer, "," in answer)
            )
        blocks.append((path, text, items))

    total = sum(1 for _, _, items in blocks for it in items if not it[5])
    quota = [total // 4] * 4
    for i in range(total % 4):
        quota[i] += 1
    letters = [ch for ch, n in zip("ABCD", quota) for _ in range(n)]
    random.Random(701).shuffle(letters)

    idx = 0
    midx = 0
    for path, text, items in blocks:
        out = []
        last = 0
        for start, end, body, texts, answer, multi in items:
            n = len(texts)
            if multi:
                shift = midx % 4
                midx += 1
                new_texts = texts[shift:] + texts[:shift]
                shifted = sorted(
                    "ABCDE"[("ABCDE".index(a) - shift) % n] for a in answer.split(", ")
                )
                new_answer = ", ".join(shifted)
            else:
                ai = "ABCDE".index(answer)
                target = "ABCDE".index(letters[idx])
                idx += 1
                if n == 4:
                    rotate = (ai - target) % 4
                    new_texts = texts[rotate:] + texts[:rotate]
                else:
                    # keep 5-option single-answer questions as-is (none in this bank)
                    new_texts = texts
                    target = ai
                new_answer = "ABCDE"[target]
            new_opts = "\n".join(f"- {'ABCDE'[i]}. {t}" for i, t in enumerate(new_texts))
            old_opts = "\n".join(f"- {'ABCDE'[i]}. {t}" for i, t in enumerate(texts))
            if old_opts not in body:
                raise SystemExit(f"{path.name}: option block mismatch")
            new_body = body.replace(old_opts, new_opts, 1)
            new_body = ANS.sub(f"**Jawaban:** {new_answer}", new_body, count=1)
            out.append(text[last:start])
            out.append(new_body)
            last = end
        out.append(text[last:])
        path.write_text("".join(out), encoding="utf-8")
        print(f"balanced {path.name}: {len(items)} soal")

    print("total:", total)


if __name__ == "__main__":
    main()
