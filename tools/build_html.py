#!/usr/bin/env python3
"""Build a self-contained interactive study app (dist/quiz.html) from dist/questions.json."""
from __future__ import annotations

import html as html_lib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
BANK = ROOT / "bank-soal"

DOMAINS = [
    {"id": 1, "name": "General Security Concepts", "weight": 12},
    {"id": 2, "name": "Threats, Vulnerabilities, and Mitigations", "weight": 22},
    {"id": 3, "name": "Security Architecture", "weight": 18},
    {"id": 4, "name": "Security Operations", "weight": 28},
    {"id": 5, "name": "Security Program Management and Oversight", "weight": 20},
]

PBQ_RE = re.compile(r"(?ms)^## PBQ (\d+) — (.+?)\s*$(.*?)(?=^## PBQ \d+ — |\Z)")


def inline_md(text: str) -> str:
    text = html_lib.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    return text


def md_html(text: str) -> str:
    """Small Markdown subset -> HTML for the PBQ section."""
    lines = text.splitlines()
    out: list[str] = []
    list_open: str | None = None

    def close_list() -> None:
        nonlocal list_open
        if list_open:
            out.append(f"</{list_open}>")
            list_open = None

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            close_list()
            i += 1
            continue
        if line.startswith("|") and i + 1 < len(lines):
            sep = lines[i + 1].replace("|", "").strip()
            if sep and set(sep) <= set("-: "):
                close_list()
                rows = []
                while i < len(lines) and lines[i].startswith("|"):
                    rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                    i += 1
                rows = [r for r in rows if not (r and set("".join(r)) <= set("-: "))]
                if rows:
                    head, *body = rows
                    out.append('<table class="tbl"><thead><tr>')
                    out.extend(f"<th>{inline_md(c)}</th>" for c in head)
                    out.append("</tr></thead><tbody>")
                    for r in body:
                        out.append("<tr>" + "".join(f"<td>{inline_md(c)}</td>" for c in r) + "</tr>")
                    out.append("</tbody></table>")
                continue
        if line.startswith("- "):
            if list_open != "ul":
                close_list()
                out.append("<ul>")
                list_open = "ul"
            out.append(f"<li>{inline_md(line[2:])}</li>")
            i += 1
            continue
        if re.match(r"^\d+\.\s", line):
            if list_open != "ol":
                close_list()
                out.append("<ol>")
                list_open = "ol"
            out.append(f"<li>{inline_md(re.sub(r'^\d+\.\s', '', line))}</li>")
            i += 1
            continue
        if line.startswith("### "):
            close_list()
            out.append(f"<h4>{inline_md(line[4:])}</h4>")
            i += 1
            continue
        if line.startswith("## "):
            close_list()
            out.append(f"<h3>{inline_md(line[3:])}</h3>")
            i += 1
            continue
        if line.startswith("> "):
            close_list()
            out.append(f"<blockquote>{inline_md(line[2:])}</blockquote>")
            i += 1
            continue
        close_list()
        out.append(f"<p>{inline_md(line)}</p>")
        i += 1
    close_list()
    return "\n".join(out)


def parse_pbq() -> list[dict]:
    text = (BANK / "06-performance-based.md").read_text(encoding="utf-8")
    items = []
    for m in PBQ_RE.finditer(text):
        num, title, body = m.group(1), m.group(2), m.group(3)
        marker = re.search(r"\*\*Jawaban model:\*\*", body)
        if marker:
            prompt = body[: marker.start()]
            answer = body[marker.start():].replace("**Jawaban model:**", "", 1)
        else:
            prompt, answer = body, ""
        items.append(
            {
                "id": f"PBQ {num}",
                "title": title.strip(),
                "prompt": md_html(prompt.strip()),
                "answer": md_html(answer.strip()),
            }
        )
    return items


TEMPLATE = r"""<!DOCTYPE html>
<html lang="id" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Latihan SY0-701 — CompTIA Security+</title>
<style>
:root{
  --bg:#0a1120; --bg2:#0e1729; --card:#121e33; --card2:#17253d;
  --line:#24344f; --txt:#e7eefc; --muted:#93a4c3;
  --accent:#38bdf8; --accent2:#22d3ee; --ok:#34d399; --bad:#fb7185; --warn:#fbbf24;
  --shadow:0 18px 50px rgba(0,0,0,.45);
}
html[data-theme="light"]{
  --bg:#f4f7fc; --bg2:#e9eff8; --card:#ffffff; --card2:#f1f5fb;
  --line:#d5dfee; --txt:#12213a; --muted:#5a6b88;
  --accent:#0b74d1; --accent2:#0891b2; --ok:#0e7c5a; --bad:#c02c45; --warn:#a16207;
  --shadow:0 18px 40px rgba(20,40,80,.12);
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{
  background:radial-gradient(1200px 700px at 15% -10%,#12304d 0%,transparent 55%),
             radial-gradient(900px 600px at 100% 0%,#1b2140 0%,transparent 50%),
             var(--bg);
  color:var(--txt);
  font-family:"Segoe UI",system-ui,-apple-system,Roboto,Helvetica,Arial,sans-serif;
  min-height:100vh; line-height:1.55;
}
html[data-theme="light"] body{
  background:radial-gradient(1000px 600px at 10% -10%,#dbeafe 0%,transparent 55%),
             radial-gradient(800px 500px at 100% 0%,#e0e7ff 0%,transparent 50%),
             var(--bg);
}
.wrap{max-width:1000px;margin:0 auto;padding:22px 18px 70px}
.brand{display:flex;align-items:center;gap:12px;font-weight:700;letter-spacing:.2px}
.logo{width:38px;height:38px;border-radius:11px;display:grid;place-items:center;
  background:linear-gradient(135deg,var(--accent),#6366f1);color:#04121f;font-size:19px}
.brand small{display:block;font-weight:500;color:var(--muted);font-size:12px;letter-spacing:.3px}
.topbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px}
.tools{display:flex;gap:8px;align-items:center}
.hero{margin:6px 0 22px}
.hero h1{font-size:clamp(26px,4vw,38px);margin:0 0 8px;line-height:1.2}
.hero p{color:var(--muted);margin:0;max-width:720px}
.hero .hl{color:var(--accent)}
.stats{display:flex;gap:10px;flex-wrap:wrap;margin:16px 0 6px}
.chip{background:var(--card);border:1px solid var(--line);border-radius:999px;
  padding:6px 12px;font-size:12.5px;color:var(--muted)}
.chip b{color:var(--txt)}
.tabs{display:flex;gap:6px;background:var(--card);border:1px solid var(--line);
  padding:5px;border-radius:14px;margin:0 0 20px;width:max-content;max-width:100%}
.tab{background:transparent;border:0;color:var(--muted);padding:8px 16px;border-radius:10px;
  cursor:pointer;font:inherit;font-size:14px;font-weight:600}
.tab.active{background:var(--card2);color:var(--txt);box-shadow:inset 0 0 0 1px var(--line)}
.modes{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:14px}
.mode{background:linear-gradient(180deg,var(--card),var(--bg2));border:1px solid var(--line);
  border-radius:16px;padding:18px;cursor:pointer;transition:.18s transform,.18s border-color,.18s box-shadow;
  display:flex;flex-direction:column;gap:6px;text-align:left;color:inherit;font:inherit}
.mode:hover{transform:translateY(-2px);border-color:var(--accent);box-shadow:var(--shadow)}
.mode .ic{font-size:22px}
.mode h3{margin:2px 0 0;font-size:16px}
.mode p{margin:0;color:var(--muted);font-size:13px}
.mode .tag{margin-top:6px;font-size:12px;color:var(--accent)}
.panel{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin-top:18px}
.panel h3{margin:0 0 4px;font-size:15px}
.panel p{margin:0 0 10px;color:var(--muted);font-size:13px}
.objrow{display:flex;gap:10px;flex-wrap:wrap}
select{background:var(--card2);color:var(--txt);border:1px solid var(--line);
  border-radius:10px;padding:9px 12px;font:inherit;font-size:13.5px;min-width:260px;flex:1}
.domlist{display:none;gap:8px;flex-wrap:wrap;margin-top:14px}
.domlist.show{display:flex}
.dombtn{background:var(--card2);border:1px solid var(--line);color:var(--txt);
  padding:8px 12px;border-radius:10px;cursor:pointer;font-size:13px;text-align:left}
.dombtn:hover{border-color:var(--accent)}
.hist{margin-top:22px;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 18px;overflow-x:auto}
.hist table{min-width:640px}
.hist h3{margin:0 0 8px;font-size:15px}
table{width:100%;border-collapse:collapse;font-size:13px}
td,th{text-align:left;padding:7px 6px;border-bottom:1px solid var(--line);color:var(--muted)}
th{color:var(--txt);font-weight:600;font-size:12px;text-transform:uppercase;letter-spacing:.4px}
tr:last-child td{border-bottom:0}
.pill{display:inline-block;padding:2px 9px;border-radius:999px;font-size:11.5px;font-weight:700}
.pill.pass{background:rgba(52,211,153,.14);color:var(--ok)}
.pill.fail{background:rgba(251,113,133,.14);color:var(--bad)}
.hide{display:none !important}

.btn{background:var(--card2);border:1px solid var(--line);color:var(--txt);padding:9px 15px;
  border-radius:11px;cursor:pointer;font:inherit;font-size:13.5px;transition:.15s}
.btn:hover{border-color:var(--accent)}
.btn.primary{background:linear-gradient(135deg,var(--accent),#6366f1);color:#05121f;font-weight:700;border:0}
.btn.primary:hover{filter:brightness(1.07)}
.btn.ghost{background:transparent}
.btn:disabled{opacity:.45;cursor:not-allowed}
.btn.warn{border-color:rgba(251,191,36,.45);color:var(--warn)}
.btn.flag-on{border-color:rgba(251,191,36,.7);color:var(--warn);background:rgba(251,191,36,.08)}
.quizhead{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:10px}
.timer{font-variant-numeric:tabular-nums;background:var(--card);border:1px solid var(--line);
  padding:7px 13px;border-radius:11px;font-weight:700;letter-spacing:.4px}
.timer.low{color:var(--bad);border-color:rgba(251,113,133,.5)}
.pbar{height:7px;background:var(--card2);border-radius:99px;overflow:hidden;border:1px solid var(--line);margin-bottom:18px}
.pbar i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--accent2),var(--accent));transition:width .25s}
.card{background:linear-gradient(180deg,var(--card),var(--bg2));border:1px solid var(--line);
  border-radius:18px;padding:24px;box-shadow:var(--shadow)}
.meta{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:14px}
.badge{background:rgba(56,189,248,.12);color:var(--accent);border:1px solid rgba(56,189,248,.25);
  padding:3px 10px;border-radius:999px;font-size:11.5px;font-weight:600;letter-spacing:.3px}
.badge.ghost{background:transparent;color:var(--muted);border-color:var(--line)}
.badge.gold{background:rgba(251,191,36,.12);color:var(--warn);border-color:rgba(251,191,36,.3)}
.stem{font-size:clamp(17px,2.2vw,20px);line-height:1.55;margin:0 0 8px;font-weight:600}
.hint{color:var(--muted);font-size:12.5px;margin:0 0 16px}
.opts{display:grid;gap:10px}
.opt{display:flex;gap:12px;align-items:flex-start;text-align:left;background:var(--card2);
  border:1px solid var(--line);border-radius:13px;padding:13px 15px;cursor:pointer;color:inherit;
  font:inherit;font-size:15px;transition:.14s}
.opt:hover:not(:disabled){border-color:var(--accent)}
.opt .k{flex:0 0 28px;height:28px;border-radius:9px;display:grid;place-items:center;
  background:var(--bg2);border:1px solid var(--line);font-weight:700;font-size:13px;color:var(--accent)}
.opts.multi .opt .k{border-radius:6px}
.opt.sel{border-color:var(--accent);background:rgba(56,189,248,.09)}
.opt.sel .k{background:rgba(56,189,248,.22);border-color:rgba(56,189,248,.5);color:var(--accent)}
.opt.correct{border-color:rgba(52,211,153,.65);background:rgba(52,211,153,.09)}
.opt.correct .k{background:rgba(52,211,153,.2);border-color:rgba(52,211,153,.5);color:var(--ok)}
.opt.wrong{border-color:rgba(251,113,133,.6);background:rgba(251,113,133,.08)}
.opt.wrong .k{background:rgba(251,113,133,.2);border-color:rgba(251,113,133,.5);color:var(--bad)}
.opt:disabled{cursor:default;opacity:1}
.opt.dim{opacity:.5}
.checkrow{margin-top:14px;display:flex;justify-content:flex-end}
.fb{margin-top:18px;border-radius:13px;padding:14px 16px;border:1px solid var(--line);background:var(--card2);display:none}
.fb.show{display:block;animation:pop .18s ease-out}
@keyframes pop{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
.fb .verdict{font-weight:700;margin-bottom:6px;display:flex;gap:8px;align-items:center}
.fb.ok{border-color:rgba(52,211,153,.4)}
.fb.ok .verdict{color:var(--ok)}
.fb.bad{border-color:rgba(251,113,133,.4)}
.fb.bad .verdict{color:var(--bad)}
.fb .ans{color:var(--muted);font-size:13px;margin-bottom:6px}
.fb p{margin:0;font-size:14.5px;color:var(--txt)}
.fb code,.pbq code{background:var(--bg2);border:1px solid var(--line);border-radius:5px;padding:1px 5px;font-size:.9em}
.nav{display:flex;justify-content:space-between;gap:10px;margin-top:22px;flex-wrap:wrap}
.nav .right{display:flex;gap:10px;margin-left:auto}
.qnav{display:grid;grid-template-columns:1fr auto 1fr;gap:10px;align-items:center;margin-top:22px}
.qnav #prevBtn{justify-self:start}
.qnav #nextBtn{justify-self:end}
.qnav .flagbtn{justify-self:center;border-color:rgba(251,191,36,.5);color:var(--warn);background:rgba(251,191,36,.07)}
.qnav .flagbtn.flag-on{background:var(--warn);color:#2a1d00;border-color:var(--warn);font-weight:700}
@media (max-width:560px){.qnav{grid-template-columns:1fr 1fr 1fr}.qnav .btn{padding:9px 8px;font-size:12px}}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(34px,1fr));gap:6px;margin-top:18px}
.dot{aspect-ratio:1;border-radius:8px;border:1px solid rgba(56,189,248,.3);background:rgba(56,189,248,.1);color:var(--accent);
  font-size:12px;cursor:pointer;display:grid;place-items:center}
.dot.cur{outline:2px solid var(--accent);color:var(--txt)}
.dot.done{background:rgba(52,211,153,.18);color:var(--ok);border-color:rgba(52,211,153,.55)}
.dot.flag{background:rgba(251,191,36,.18);color:var(--warn);border-color:rgba(251,191,36,.65)}
.dot.ok{background:rgba(52,211,153,.2);border-color:rgba(52,211,153,.6);color:var(--ok)}
.dot.no{background:rgba(251,113,133,.18);border-color:rgba(251,113,133,.6);color:var(--bad)}
.dot.skip{border-style:dashed;opacity:.55}
.legend{display:flex;gap:14px;flex-wrap:wrap;margin-top:10px;font-size:12px;color:var(--muted)}
.legend span{display:flex;align-items:center;gap:6px}
.legend i{width:12px;height:12px;border-radius:3px;display:inline-block;border:1px solid var(--line)}
.legend i.ok{background:rgba(52,211,153,.35);border-color:var(--ok)}
.legend i.no{background:rgba(251,113,133,.35);border-color:var(--bad)}
.legend i.skip{background:transparent;border-style:dashed}
.legend i.flag{border-color:var(--warn)}
.legend i.blue{background:rgba(56,189,248,.3);border-color:var(--accent)}
.mark{display:inline-grid;place-items:center;width:20px;height:20px;border-radius:6px;font-size:11px;flex:0 0 auto}
.mark.ok{background:rgba(52,211,153,.2);color:var(--ok)}
.mark.no{background:rgba(251,113,133,.2);color:var(--bad)}
.mark.skip{background:var(--card2);color:var(--muted)}
.chart{display:flex;align-items:flex-end;justify-content:center;gap:10px;height:150px;padding:8px 4px 0;border-bottom:1px solid var(--line);margin:8px 0 4px}
.chart .bar{flex:0 0 54px;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;gap:5px;height:100%}
.chart .bar b{font-size:10.5px;color:var(--muted);font-weight:600}
.chart .bar i{width:100%;max-width:40px;border-radius:6px 6px 0 0;min-height:3px;background:linear-gradient(180deg,var(--accent),#6366f1)}
.chart .bar.pass i{background:linear-gradient(180deg,var(--ok),#0f766e)}
.chart .bar.fail i{background:linear-gradient(180deg,var(--bad),#9f1239)}
.chart .bar .lbl{font-size:10px;color:var(--muted)}
.btn.on{border-color:var(--ok);color:var(--ok);background:rgba(52,211,153,.08)}
.btn.on-no{border-color:var(--bad);color:var(--bad);background:rgba(251,113,133,.08)}
.objrow2{display:flex;align-items:center;gap:8px}
.objrow2 .btn{padding:5px 10px;font-size:12px}

.score{width:150px;height:150px;border-radius:50%;display:grid;place-items:center;
  background:conic-gradient(var(--accent) var(--deg,0deg),var(--card2) 0);position:relative;flex:0 0 auto}
.score::after{content:"";position:absolute;inset:9px;border-radius:50%;background:var(--card)}
.score .in{position:relative;z-index:1;text-align:center}
.score .num{font-size:34px;font-weight:800;line-height:1}
.score .lbl{font-size:11px;color:var(--muted);letter-spacing:.6px;text-transform:uppercase}
.reshead{display:flex;gap:22px;align-items:center;flex-wrap:wrap;margin-bottom:8px}
.resmeta h2{margin:0 0 4px;font-size:23px}
.resmeta p{margin:0;color:var(--muted);font-size:14px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px;margin:18px 0 4px}
.kpi{background:var(--card2);border:1px solid var(--line);border-radius:13px;padding:12px 14px}
.kpi .v{font-size:20px;font-weight:800}
.kpi .l{font-size:11.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.4px}
.kpi.ok .v{color:var(--ok)} .kpi.bad .v{color:var(--bad)} .kpi.warn .v{color:var(--warn)}
.domres{margin-top:22px;display:grid;gap:12px}
.dombar{display:grid;grid-template-columns:1fr auto;gap:6px 12px;align-items:center}
.dombar .name{font-size:13.5px}
.dombar .val{font-size:12.5px;color:var(--muted)}
.dombar .track{grid-column:1/-1;height:8px;border-radius:99px;background:var(--card2);overflow:hidden}
.dombar .track i{display:block;height:100%;border-radius:99px}
.review{margin-top:26px}
.review h3{margin:0 0 10px;font-size:16px}
.ritem{border:1px solid var(--line);border-radius:13px;margin-bottom:10px;overflow:hidden;background:var(--card2)}
.ritem summary{cursor:pointer;padding:13px 15px;font-size:14px;font-weight:600;list-style:none;display:flex;gap:9px;align-items:flex-start}
.ritem summary::-webkit-details-marker{display:none}
.ritem .body{padding:0 15px 15px;font-size:14px;color:var(--txt)}
.ritem .body .o{padding:7px 10px;border-radius:8px;background:var(--card);border:1px solid var(--line);font-size:13.5px;margin:5px 0}
.ritem .body .o.a{border-color:rgba(52,211,153,.45)}
.ritem .body .o.mine{border-color:rgba(251,113,133,.45)}
.note{color:var(--muted);font-size:13px}
.footer{margin-top:34px;color:var(--muted);font-size:12px;text-align:center;opacity:.8}

/* PBQ */
.pbq{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px 22px;margin-bottom:16px}
.pbq-head{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:6px}
.pbq-head h3{margin:0;font-size:17px}
.pbq .md{font-size:14.5px}
.pbq .md p{margin:8px 0}
.pbq .md ul,.pbq .md ol{margin:8px 0 8px 20px;padding:0}
.pbq .md li{margin:3px 0}
.pbq .md blockquote{margin:10px 0;padding:8px 12px;border-left:3px solid var(--accent);
  background:var(--card2);border-radius:0 8px 8px 0;color:var(--muted)}
.pbq .md table{margin:10px 0;font-size:13px}
.pbq .md th,.pbq .md td{border:1px solid var(--line);padding:6px 8px;color:var(--txt)}
.pbq .md th{background:var(--card2)}
.pbq textarea{width:100%;min-height:90px;margin-top:12px;background:var(--card2);color:var(--txt);
  border:1px solid var(--line);border-radius:11px;padding:11px 13px;font:inherit;font-size:14px;resize:vertical}
.pbq-actions{display:flex;gap:10px;align-items:center;margin-top:10px;flex-wrap:wrap}
.pbq-answer{margin-top:14px;border-top:1px dashed var(--line);padding-top:12px}

/* stats */
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px}
.meter{height:9px;border-radius:99px;background:var(--card2);overflow:hidden;border:1px solid var(--line)}
.meter i{display:block;height:100%;border-radius:99px;background:linear-gradient(90deg,var(--accent2),var(--accent))}
.weak{display:flex;justify-content:space-between;gap:10px;padding:9px 0;border-bottom:1px solid var(--line);font-size:13.5px}
.weak:last-child{border-bottom:0}

/* modal */
.modal{position:fixed;inset:0;background:rgba(3,10,22,.65);display:grid;place-items:center;z-index:50;padding:18px}
.modal-card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px;max-width:440px;width:100%;box-shadow:var(--shadow)}
.modal-card h3{margin:0 0 8px}
.modal-card p{color:var(--muted);font-size:14px;margin:0 0 16px}

@media (max-width:560px){
  .card{padding:18px}
  .score{width:120px;height:120px}
  .score .num{font-size:27px}
  .nav .right{width:100%;margin-left:0}
  .nav .right .btn{flex:1}
  .tabs{width:100%;justify-content:space-between}
  .tab{flex:1;padding:8px 6px}
}
</style>
</head>
<body>
<div class="wrap">

  <div class="topbar" id="topbar">
    <div class="brand">
      <div class="logo">🛡️</div>
      <div>Security+ SY0-701<small>Latihan soal interaktif · Bahasa Indonesia</small></div>
    </div>
    <div class="tools">
      <span class="chip"><b id="bankCount">0</b> soal</span>
      <button class="btn ghost" id="themeBtn" title="Ganti tema">🌙</button>
    </div>
  </div>

  <nav class="tabs" id="tabbar">
    <button class="tab active" data-tab="practice">Latihan</button>
    <button class="tab" data-tab="pbq">PBQ</button>
    <button class="tab" data-tab="stats">Statistik</button>
    <button class="tab" data-tab="guide">Panduan</button>
  </nav>

  <!-- PRACTICE -->
  <section id="tab-practice">
    <div class="hero">
      <h1>Latihan <span class="hl">SY0-701</span>, siap hadapi ujian Security+</h1>
      <p>Soal bergaya ujian dengan pembahasan Bahasa Indonesia. Simulasi memakai komposisi domain sesuai bobot resmi, campuran pilihan tunggal dan multi-select, ditambah latihan PBQ dan pelacakan progres.</p>
      <div class="stats">
        <span class="chip">5 domain</span>
        <span class="chip">Passing <b>750/900</b></span>
        <span class="chip">Pembahasan tiap soal</span>
        <span class="chip">Progres tersimpan</span>
      </div>
    </div>

    <div class="modes">
      <button class="mode" data-mode="exam">
        <span class="ic">⏱️</span>
        <h3>Ujian Simulasi</h3>
        <p>90 soal campuran sesuai bobot domain, 90 menit, skor 100–900 seperti ujian asli.</p>
        <span class="tag">Mulai ujian →</span>
      </button>
      <button class="mode" data-mode="domain">
        <span class="ic">📚</span>
        <h3>Latihan per Domain</h3>
        <p>Pilih satu dari 5 domain. 20 soal acak, pembahasan langsung muncul.</p>
        <span class="tag">Pilih domain →</span>
      </button>
      <button class="mode" data-mode="quick">
        <span class="ic">⚡</span>
        <h3>Latihan Cepat</h3>
        <p>25 soal acak dari semua domain, tanpa timer. Cocok untuk sesi singkat.</p>
        <span class="tag">Mulai latihan →</span>
      </button>
      <button class="mode" data-mode="wrong">
        <span class="ic">🔁</span>
        <h3>Ulangi yang Salah</h3>
        <p>Kerjakan kembali soal yang pernah salah. Hilang otomatis saat dijawab benar.</p>
        <span class="tag" id="wrongTag">Belum ada data →</span>
      </button>
    </div>

    <div class="domlist" id="domlist"></div>

    <div class="panel">
      <h3>Format ujian yang disimulasikan</h3>
      <p><b>90 soal · 90 menit · skor 100–900 (lulus 750).</b> Pilihan ganda 4 opsi, multi-select 5 opsi (pilih 2–3 jawaban), dan PBQ bergaya simulasi. Tidak ada soal esai. PBQ di ujian asli muncul paling awal.</p>
    </div>

    <div class="panel">
      <h3>Latihan per objektif</h3>
      <p>Fokus ke satu sub-objektif, misalnya 4.6 Identity and Access Management atau 3.3 Data Protection.</p>
      <div class="objrow">
        <select id="objSelect"></select>
        <button class="btn primary" id="objStart">Mulai objektif</button>
      </div>
    </div>

    <div class="hist" id="histBox">
      <h3>Riwayat latihan</h3>
      <div id="histBody" class="note">Belum ada riwayat. Selesaikan satu sesi untuk melihat statistik.</div>
    </div>
  </section>

  <!-- PBQ -->
  <section id="tab-pbq" class="hide">
    <div class="hero">
      <h1>Soal Performa <span class="hl">(PBQ)</span></h1>
      <p>Di ujian asli, 3–5 PBQ muncul paling awal. Tulis jawaban Anda dulu, lalu buka jawaban model. Catatan tersimpan otomatis di browser.</p>
    </div>
    <div id="pbqList"></div>
  </section>

  <!-- STATS -->
  <section id="tab-stats" class="hide">
    <div class="hero">
      <h1>Statistik <span class="hl">belajar</span></h1>
      <p>Dihitung dari jawaban yang Anda kerjakan di browser ini. Gunakan untuk menemukan domain dan objektif terlemah.</p>
    </div>
    <div id="statsBody"></div>
  </section>

  <!-- GUIDE -->
  <section id="tab-guide" class="hide">
    <div class="hero">
      <h1>Jenis soal & <span class="hl">penilaian</span></h1>
      <p>Ringkasan format SY0-701 dan aturan penilaian yang dipakai simulasi ini.</p>
    </div>
    <div class="panel">
      <h3>1. Pilihan ganda satu jawaban</h3>
      <p>Umumnya empat opsi (A–D). Satu jawaban benar, bernilai penuh. Jawaban bisa diubah sebelum sesi diselesaikan. Mesin simulasi mendukung sampai enam opsi (A–F), jadi soal 5–6 opsi tetap tampil benar. Di ujian asli, sebagian besar soal berbentuk ini.</p>
    </div>
    <div class="panel">
      <h3>2. Multi-select (checkbox)</h3>
      <p>Lima opsi (A–E), pilih dua atau tiga jawaban. Penilaian bersifat <b>all-or-nothing</b>: satu pilihan salah atau ada yang kurang berarti 0 poin. Tidak ada nilai parsial untuk multi-select.</p>
    </div>
    <div class="panel">
      <h3>3. Performance-based question (PBQ)</h3>
      <p>Simulasi: menempatkan perangkat, menyusun aturan firewall, membaca log, konfigurasi SSID, atau memilih algoritma. Di ujian asli PBQ muncul di awal dan <b>dapat bernilai parsial</b> per komponen. CompTIA tidak mempublikasikan bobot pastinya.</p>
    </div>
    <div class="panel">
      <h3>4. Essay?</h3>
      <p><b>Tidak ada soal esai</b> di SY0-701. Jika suatu ujian memakai esai, penilaiannya manual memakai rubrik (bukan otomatis), dan biasanya tidak ada satu jawaban benar tunggal.</p>
    </div>
    <div class="panel">
      <h3>Cara skor dihitung</h3>
      <p>Simulasi: <b>skor = 100 + 8 × persentase benar</b> (maksimal 900). Lulus bila ≥ <b>750</b>, setara ±81% benar. Ujian asli memakai <i>scaled score</i> 100–900 dengan komposisi bobot yang tidak dipublikasikan, jadi angka ini hanya pendekatan.</p>
      <p>Ujian asli: maksimal 90 soal, 90 menit. Saat waktu habis, jawaban otomatis dikumpulkan.</p>
    </div>
    <div class="panel">
      <h3>Aturan simulasi ini</h3>
      <ul>
        <li>Benar/salah <b>tidak ditampilkan</b> selama sesi berlangsung; semua pembahasan muncul setelah selesai.</li>
        <li>Jawaban <b>bisa diubah</b> kapan saja sebelum submit.</li>
        <li>Soal yang ditandai <b>ragu-ragu harus dihapus tandanya</b> sebelum bisa submit.</li>
        <li>Timer habis → <b>auto-submit</b>, termasuk jawaban kosong.</li>
        <li>Peta soal: biru = belum dijawab, hijau = sudah dijawab, kuning = ragu-ragu.</li>
      </ul>
    </div>
  </section>

  <!-- QUIZ -->
  <section id="quiz" class="hide">
    <div class="quizhead">
      <div class="brand"><div class="logo" style="width:32px;height:32px;font-size:16px">🛡️</div>
        <div style="font-size:14px">SY0-701<small id="modeLabel">Latihan</small></div></div>
      <div style="display:flex;gap:8px;align-items:center">
        <div class="chip hide" id="liveScore">✓ 0 · ✗ 0</div>
        <div class="chip" id="counter">1 / 1</div>
        <div class="timer" id="timer">—</div>
        <button class="btn ghost" id="quitBtn">Keluar</button>
      </div>
    </div>
    <div class="pbar"><i id="pbar"></i></div>

    <div class="card">
      <div class="meta">
        <span class="badge" id="qDomain">Domain</span>
        <span class="badge ghost" id="qObjective">Objektif</span>
        <span class="badge ghost" id="qType">Tipe</span>
      </div>
      <h2 class="stem" id="stem"></h2>
      <p class="hint" id="hint"></p>
      <div class="opts" id="opts"></div>
      <div class="fb" id="fb"></div>
      <div class="qnav">
        <button class="btn" id="prevBtn">← Sebelumnya</button>
        <button class="btn flagbtn" id="flagBtn">⚑ Ragu-ragu</button>
        <button class="btn primary" id="nextBtn">Berikutnya →</button>
      </div>
    </div>

    <div class="grid" id="grid"></div>
    <div class="legend">
      <span><i class="blue"></i>Belum dijawab</span>
      <span><i class="ok"></i>Sudah dijawab</span>
      <span><i class="flag"></i>Ragu-ragu</span>
      <span id="gridNote" class="note">Benar/salah baru terlihat setelah sesi selesai.</span>
    </div>
    <p class="note" style="margin-top:14px">Shortcut: <b>1–6</b> pilih/toggle jawaban · <b>←</b>/<b>→</b> navigasi · <b>F</b> ragu-ragu.</p>
  </section>

  <!-- RESULT -->
  <section id="result" class="hide">
    <div class="quizhead" style="margin-bottom:12px">
      <div class="brand"><div class="logo" style="width:32px;height:32px;font-size:16px">🛡️</div>
        <div style="font-size:14px">Hasil sesi<small id="resMode">Latihan</small></div></div>
      <button class="btn" id="homeBtnTop">← Beranda</button>
    </div>
    <div class="card">
      <div class="reshead">
        <div class="score" id="scoreRing"><div class="in"><div class="num" id="scoreNum">0</div><div class="lbl">dari 900</div></div></div>
        <div class="resmeta">
          <h2 id="resTitle">Hasil</h2>
          <p id="resSub"></p>
          <p style="margin-top:8px"><span class="pill" id="resPill">—</span></p>
          <p class="note" style="margin-top:6px">Ambang 750 setara ±81% jawaban benar. Skor ini simulasi, bukan penskoran resmi CompTIA.</p>
        </div>
      </div>
      <div class="kpis">
        <div class="kpi ok"><div class="v" id="kOk">0</div><div class="l">Benar</div></div>
        <div class="kpi bad"><div class="v" id="kBad">0</div><div class="l">Salah</div></div>
        <div class="kpi warn"><div class="v" id="kSkip">0</div><div class="l">Kosong</div></div>
        <div class="kpi"><div class="v" id="kTime">0:00</div><div class="l">Waktu</div></div>
      </div>
      <div class="panel" style="margin-top:18px">
        <h3 style="margin:0 0 4px">Peta jawaban</h3>
        <p class="note" style="margin:0 0 10px">Klik nomor untuk membuka pembahasan soal tersebut.</p>
        <div class="grid" id="resultMap"></div>
        <div class="legend">
          <span><i class="ok"></i>Benar</span>
          <span><i class="no"></i>Salah</span>
          <span><i class="skip"></i>Kosong</span>
        </div>
      </div>
      <div class="panel">
        <h3 style="margin:0 0 4px">Hasil per objektif</h3>
        <p class="note" style="margin:0 0 10px">10 objektif dengan persentase terendah perlu diulang lebih dulu.</p>
        <div id="objRes"></div>
      </div>
      <div class="domres" id="domres"></div>
      <div class="review" id="review"></div>
      <div class="nav" style="margin-top:24px">
        <button class="btn" id="homeBtn">← Beranda</button>
        <div class="right">
          <button class="btn" id="retryWrongBtn">Ulangi yang salah</button>
          <button class="btn primary" id="againBtn">Sesi baru</button>
        </div>
      </div>
    </div>
  </section>

  <div class="footer">Latihan mandiri · bukan produk resmi CompTIA · disusun dengan bantuan AI DeepSeek</div>
</div>

<div class="modal hide" id="modal">
  <div class="modal-card">
    <h3>Selesaikan sesi?</h3>
    <p id="modalText"></p>
    <div class="nav">
      <button class="btn" id="modalBack">Kembali</button>
      <div class="right">
        <button class="btn warn hide" id="modalClear">Hapus semua tanda</button>
        <button class="btn primary" id="modalSubmit">Selesai</button>
      </div>
    </div>
  </div>
</div>

<script>
const BANK = __QUESTIONS__;
const PBQ = __PBQ__;
const DOMAINS = __DOMAINS__;
const EXAM_PLAN = __PLAN__;
const PASS_SCALED = 750;
const LS_WRONG = "sp701_wrong_v1";
const LS_HIST = "sp701_history_v1";
const LS_RESULTS = "sp701_results_v1";
const LS_PBQ = "sp701_pbq_v1";
const LS_PBQ_STATUS = "sp701_pbq_status_v1";
const LS_THEME = "sp701_theme";

/* ---------- helpers ---------- */
const $ = (id) => document.getElementById(id);
const escapeHtml = (s) => String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const md = (s) => escapeHtml(s)
  .replace(/`([^`]+)`/g, "<code>$1</code>")
  .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
const shuffle = (arr) => {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
};
const loadJSON = (k, fb) => { try { const v = JSON.parse(localStorage.getItem(k)); return v ?? fb; } catch { return fb; } };
const saveJSON = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} };
const fmtTime = (s) => {
  s = Math.max(0, Math.floor(s));
  return Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0");
};
const domName = (id) => (DOMAINS.find(d => d.id === id) || {}).name || "";
const hasAnswer = (q) => (S.sel[q.id] || []).length > 0;
const isCorrect = (q) => {
  const sel = (S.sel[q.id] || []).slice().sort();
  const ans = q.a.slice().sort();
  return sel.length === ans.length && sel.every((v, i) => v === ans[i]);
};

/* ---------- state ---------- */
const S = {
  mode: null, domain: null, list: [], idx: 0, sel: {}, flags: new Set(),
  start: 0, remain: 0, timer: null, finished: false, autoSubmit: false,
  fromHistory: false, durationOverride: null
};

/* ---------- tabs ---------- */
function showTab(name) {
  $("topbar").classList.remove("hide");
  ["practice", "pbq", "stats", "guide"].forEach(t => $("tab-" + t).classList.toggle("hide", t !== name));
  document.querySelectorAll(".tab").forEach(b => b.classList.toggle("active", b.dataset.tab === name));
  if (name === "stats") renderStats();
  window.scrollTo({ top: 0, behavior: "smooth" });
}
document.querySelectorAll(".tab").forEach(b => b.addEventListener("click", () => showTab(b.dataset.tab)));

/* ---------- theme ---------- */
function applyTheme(t) {
  document.documentElement.dataset.theme = t;
  $("themeBtn").textContent = t === "dark" ? "🌙" : "☀️";
  try { localStorage.setItem(LS_THEME, t); } catch {}
}
$("themeBtn").addEventListener("click", () => {
  applyTheme(document.documentElement.dataset.theme === "dark" ? "light" : "dark");
});

/* ---------- persistence ---------- */
function wrongIds() { return loadJSON(LS_WRONG, []); }
function results() { return loadJSON(LS_RESULTS, {}); }
function recordResult(id, ok) {
  const r = results();
  const cur = r[id] || { r: 0, w: 0 };
  if (ok) cur.r += 1; else cur.w += 1;
  r[id] = cur;
  saveJSON(LS_RESULTS, r);
}

/* ---------- home ---------- */
function refreshHome() {
  $("bankCount").textContent = BANK.length;
  const w = wrongIds().length;
  $("wrongTag").textContent = w ? (w + " soal menunggu →") : "Belum ada data →";

  const hist = loadJSON(LS_HIST, []);
  if (!hist.length) {
    $("histBody").innerHTML = 'Belum ada riwayat. Selesaikan satu sesi untuk melihat statistik.';
    return;
  }
  const best = Math.max(...hist.map(h => h.scaled));
  const avg = Math.round(hist.reduce((s, h) => s + h.scaled, 0) / hist.length);
  const rows = hist.slice(-6).reverse().map(h => {
    const d = new Date(h.ts);
    const when = d.toLocaleDateString("id-ID", { day: "2-digit", month: "short" }) + " " +
                 d.toLocaleTimeString("id-ID", { hour: "2-digit", minute: "2-digit" });
    return `<tr><td>${when}</td><td>${h.mode}</td><td>${h.total} soal</td>
            <td><b>${h.scaled}</b></td>
            <td><span class="pill ${h.scaled >= PASS_SCALED ? "pass" : "fail"}">${h.scaled >= PASS_SCALED ? "LULUS" : "BELUM"}</span></td>
            <td>${h.ids ? `<button class="btn history-open" data-ts="${h.ts}">Pembahasan</button>` : '<span class="note">tanpa detail</span>'}</td></tr>`;
  }).join("");
  $("histBody").innerHTML = `
    <div class="stats" style="margin:0 0 12px">
      <span class="chip">Sesi: <b>${hist.length}</b></span>
      <span class="chip">Skor terbaik: <b>${best}</b></span>
      <span class="chip">Rata-rata: <b>${avg}</b></span>
      <span class="chip">Soal pernah salah: <b>${w}</b></span>
    </div>
    <table><thead><tr><th>Waktu</th><th>Mode</th><th>Jumlah</th><th>Skor</th><th>Status</th><th>Aksi</th></tr></thead>
    <tbody>${rows}</tbody></table>`;
  $("histBody").querySelectorAll(".history-open").forEach(b => b.addEventListener("click", () => {
    openHistory(+b.dataset.ts);
  }));
}

function openHistory(ts) {
  const h = loadJSON(LS_HIST, []).find(x => x.ts === ts);
  if (!h || !h.ids) return;
  const list = h.ids.map(id => BANK.find(q => q.id === id)).filter(Boolean);
  if (!list.length) return;
  S.mode = h.mode === "Simulasi" ? "exam" : "quick";
  S.domain = null; S.list = list; S.sel = h.sel || {};
  S.flags = new Set(); S.finished = false; S.autoSubmit = !!h.auto;
  S.fromHistory = true; S.durationOverride = h.secs != null ? h.secs : 0;
  S.start = Date.now() - (h.secs || 0) * 1000;
  $("tabbar").classList.add("hide");
  $("topbar").classList.add("hide");
  ["practice", "pbq", "stats", "guide"].forEach(t => $("tab-" + t).classList.add("hide"));
  $("quiz").classList.add("hide");
  finish();
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function buildObjectiveSelect() {
  const map = {};
  BANK.forEach(q => { (map[q.o] = map[q.o] || []).push(q); });
  const opts = Object.keys(map).sort().map(o =>
    `<option value="${o}">${o} · ${map[o].length} soal</option>`).join("");
  $("objSelect").innerHTML = opts;
}

function buildDomainList() {
  $("domlist").innerHTML = DOMAINS.map(d => {
    const n = BANK.filter(q => q.d === d.id).length;
    return `<button class="dombtn" data-d="${d.id}"><b>D${d.id}</b> · ${d.name} <span class="note">(${n} soal · ${d.weight}%)</span></button>`;
  }).join("");
  $("domlist").querySelectorAll(".dombtn").forEach(b => b.addEventListener("click", () => {
    const d = +b.dataset.d;
    const pool = shuffle(BANK.filter(q => q.d === d));
    startSession("domain", pool.slice(0, Math.min(20, pool.length)), d);
  }));
}

/* ---------- stats ---------- */
function calcStreak(hist) {
  const days = new Set(hist.map(h => new Date(h.ts).toDateString()));
  const d = new Date();
  if (!days.has(d.toDateString())) d.setDate(d.getDate() - 1);
  let n = 0;
  while (days.has(d.toDateString())) { n++; d.setDate(d.getDate() - 1); }
  return n;
}

function renderStats() {
  const res = results();
  const answered = Object.keys(res).length;
  const attempts = Object.values(res).reduce((s, v) => s + v.r + v.w, 0);
  const rights = Object.values(res).reduce((s, v) => s + v.r, 0);
  const hist = loadJSON(LS_HIST, []);
  const best = hist.length ? Math.max(...hist.map(h => h.scaled)) : 0;
  const coverage = Math.round(answered / BANK.length * 100);
  const accuracy = attempts ? Math.round(rights / attempts * 100) : 0;
  const streak = calcStreak(hist);
  const timed = hist.filter(h => h.secs);
  const avgTime = timed.length ? Math.round(timed.reduce((s, h) => s + h.secs, 0) / timed.length) : 0;
  const pbqStatus = loadJSON(LS_PBQ_STATUS, {});
  const pbqDone = Object.values(pbqStatus).filter(v => v === "ok").length;

  const chart = hist.slice(-10).map(h => {
    const px = Math.max(6, Math.round(h.scaled / 900 * 110));
    const d = new Date(h.ts);
    return `<div class="bar ${h.scaled >= PASS_SCALED ? "pass" : "fail"}" title="${h.mode} · ${h.total} soal · ${h.scaled}">
      <b>${h.scaled}</b><i style="height:${px}px"></i><span class="lbl">${d.getDate()}/${d.getMonth() + 1}</span></div>`;
  }).join("");

  const domRows = DOMAINS.map(d => {
    const qs = BANK.filter(q => q.d === d.id);
    let r = 0, w = 0;
    qs.forEach(q => { const v = res[q.id]; if (v) { r += v.r; w += v.w; } });
    const pct = (r + w) ? Math.round(r / (r + w) * 100) : 0;
    const col = pct >= 75 ? "var(--ok)" : pct >= 50 ? "var(--warn)" : "var(--bad)";
    return `<div class="dombar">
      <span class="name">D${d.id} · ${d.name}</span>
      <span class="val">${r + w ? pct + "% (" + (r + w) + " jawaban)" : "belum ada data"}</span>
      <span class="track"><i style="width:${pct}%;background:${col}"></i></span></div>`;
  }).join("");

  const objMap = {};
  BANK.forEach(q => {
    const v = res[q.id];
    if (!v) return;
    const o = objMap[q.o] = objMap[q.o] || { r: 0, w: 0 };
    o.r += v.r; o.w += v.w;
  });
  const weak = Object.entries(objMap)
    .map(([o, v]) => ({ o, pct: Math.round(v.r / (v.r + v.w) * 100), n: v.r + v.w }))
    .filter(x => x.n >= 3 && x.pct < 75)
    .sort((a, b) => a.pct - b.pct)
    .slice(0, 8);

  $("statsBody").innerHTML = `
    <div class="grid2">
      <div class="kpi"><div class="v">${coverage}%</div><div class="l">Cakupan bank (${answered}/${BANK.length})</div></div>
      <div class="kpi ${accuracy >= 75 ? "ok" : accuracy >= 50 ? "warn" : "bad"}"><div class="v">${accuracy}%</div><div class="l">Akurasi (${attempts} jawaban)</div></div>
      <div class="kpi ok"><div class="v">${best}</div><div class="l">Skor simulasi terbaik</div></div>
      <div class="kpi"><div class="v">${hist.length}</div><div class="l">Sesi selesai</div></div>
      <div class="kpi warn"><div class="v">${streak}</div><div class="l">Streak hari</div></div>
      <div class="kpi"><div class="v">${avgTime ? fmtTime(avgTime) : "–"}</div><div class="l">Rata-rata durasi sesi</div></div>
    </div>
    <div class="panel" style="margin-top:18px">
      <h3>Perkembangan skor</h3>
      <p>Sepuluh sesi terakhir. Hijau = lulus ambang 750, merah = belum.</p>
      ${chart ? `<div class="chart">${chart}</div>` : '<p class="note">Belum ada sesi.</p>'}
    </div>
    <div class="panel">
      <h3>Penguasaan per domain</h3>
      <p>Persentase jawaban benar dari semua percobaan Anda.</p>
      <div class="domres">${domRows}</div>
    </div>
    <div class="panel">
      <h3>Objektif yang perlu diulang</h3>
      <p>Objektif dengan akurasi di bawah 75% (minimal 3 jawaban).</p>
      ${weak.length ? weak.map(x => `<div class="weak">
        <span><b>${x.o}</b> · ${x.n} jawaban · <span style="color:var(--bad)">${x.pct}%</span></span>
        <span class="objrow2"><button class="btn" data-obj="${x.o}">Latih</button></span></div>`).join("") : '<p class="note">Belum cukup data. Kerjakan latihan per objektif untuk mengisi statistik.</p>'}
    </div>
    <div class="panel">
      <h3>Latihan PBQ</h3>
      <p>PBQ yang Anda tandai sudah dipahami: <b>${pbqDone}/${PBQ.length}</b></p>
      <div class="meter"><i style="width:${(pbqDone / PBQ.length * 100).toFixed(1)}%"></i></div>
    </div>
    <div class="panel">
      <h3>Reset progres</h3>
      <p>Menghapus riwayat sesi, daftar soal salah, statistik per soal, dan status PBQ di browser ini.</p>
      <button class="btn" id="resetStats">Hapus semua progres</button>
    </div>`;

  $("statsBody").querySelectorAll("[data-obj]").forEach(b => b.addEventListener("click", () => {
    const o = b.dataset.obj;
    const pool = shuffle(BANK.filter(q => q.o === o));
    if (pool.length) startSession("objective", pool.slice(0, Math.min(20, pool.length)));
  }));

  $("resetStats").addEventListener("click", () => {
    if (!confirm("Hapus semua progres belajar di browser ini?")) return;
    [LS_WRONG, LS_HIST, LS_RESULTS, LS_PBQ_STATUS].forEach(k => { try { localStorage.removeItem(k); } catch {} });
    refreshHome(); renderStats();
  });
}

/* ---------- start session ---------- */
function startSession(mode, list, domain) {
  if (!list.length) return;
  S.mode = mode; S.domain = domain || null; S.list = list; S.idx = 0;
  S.sel = {}; S.flags = new Set();
  S.finished = false; S.autoSubmit = false; S.fromHistory = false; S.durationOverride = null;
  S.start = Date.now(); S.remain = mode === "exam" ? 90 * 60 : 0;

  $("tabbar").classList.add("hide");
  $("topbar").classList.add("hide");
  ["practice", "pbq", "stats", "guide"].forEach(t => $("tab-" + t).classList.add("hide"));
  $("result").classList.add("hide");
  $("quiz").classList.remove("hide");
  $("modeLabel").textContent = mode === "exam" ? "Ujian simulasi · 90 menit" :
    mode === "domain" ? "Latihan per domain" : mode === "objective" ? "Latihan per objektif" :
    mode === "wrong" ? "Ulangi yang salah" : "Latihan cepat";

  clearInterval(S.timer);
  if (mode === "exam") {
    $("timer").classList.remove("hide");
    tickTimer();
    S.timer = setInterval(tickTimer, 1000);
  } else {
    $("timer").classList.add("hide");
  }
  buildGrid();
  render();
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function tickTimer() {
  const elapsed = Math.floor((Date.now() - S.start) / 1000);
  S.remain = Math.max(0, 90 * 60 - elapsed);
  const t = $("timer");
  t.textContent = "⏱ " + fmtTime(S.remain);
  t.classList.toggle("low", S.remain <= 300);
  if (S.remain <= 0 && !S.finished) { clearInterval(S.timer); S.autoSubmit = true; finish(); }
}

function pickExam() {
  let out = [];
  for (const d of [1, 2, 3, 4, 5]) {
    const pool = shuffle(BANK.filter(q => q.d === d));
    out = out.concat(pool.slice(0, EXAM_PLAN[d]));
  }
  return shuffle(out);
}

/* ---------- render ---------- */
function buildGrid() {
  $("grid").innerHTML = S.list.map((q, i) =>
    `<button class="dot" data-i="${i}" title="Soal ${i + 1}">${i + 1}</button>`).join("");
  $("grid").querySelectorAll(".dot").forEach(b =>
    b.addEventListener("click", () => { S.idx = +b.dataset.i; render(); }));
  paintGrid();
}

function paintGrid() {
  let answeredCount = 0;
  $("grid").querySelectorAll(".dot").forEach((b, i) => {
    const q = S.list[i];
    const answered = hasAnswer(q);
    const flagged = S.flags.has(q.id);
    b.classList.toggle("cur", i === S.idx);
    b.classList.toggle("done", answered);
    b.classList.toggle("flag", flagged);
    b.classList.remove("ok", "no", "skip");
    if (answered) answeredCount++;
  });
  $("liveScore").classList.remove("hide");
  $("liveScore").textContent = "Terjawab " + answeredCount + " / " + S.list.length;
  $("gridNote").textContent = "Biru = belum dijawab · hijau = sudah dijawab · kuning = ragu-ragu. Benar/salah baru terlihat setelah selesai.";
}

function render() {
  const q = S.list[S.idx];
  const sel = S.sel[q.id] || [];
  const multi = q.a.length > 1;

  $("qDomain").textContent = "D" + q.d + " · " + domName(q.d);
  $("qObjective").textContent = "Objektif " + q.o;
  $("qType").textContent = q.t;
  $("stem").textContent = q.q;
  $("hint").textContent = (multi
    ? "Pilih " + q.a.length + " jawaban. "
    : "") + "Jawaban bisa diubah sebelum sesi diselesaikan.";

  $("opts").className = "opts" + (multi ? " multi" : "");
  $("opts").innerHTML = q.opts.map(o => {
    const on = sel.includes(o.k);
    return `<button class="opt${on ? " sel" : ""}" data-k="${o.k}">
       <span class="k">${o.k}</span><span>${escapeHtml(o.v)}</span></button>`;
  }).join("");
  $("opts").querySelectorAll(".opt").forEach(b =>
    b.addEventListener("click", () => choose(b.dataset.k)));

  $("fb").className = "fb";
  $("fb").innerHTML = "";

  $("pbar").style.width = ((S.idx + 1) / S.list.length * 100) + "%";
  $("counter").textContent = (S.idx + 1) + " / " + S.list.length;
  $("prevBtn").disabled = S.idx === 0;
  $("nextBtn").textContent = S.idx === S.list.length - 1 ? "Selesai ✓" : "Berikutnya →";
  $("flagBtn").classList.toggle("flag-on", S.flags.has(q.id));
  $("flagBtn").textContent = S.flags.has(q.id) ? "⚑ Ditandai" : "⚑ Ragu-ragu";
  paintGrid();
}

function choose(k) {
  const q = S.list[S.idx];
  const multi = q.a.length > 1;
  const cur = (S.sel[q.id] || []).slice();
  if (multi) {
    const i = cur.indexOf(k);
    if (i >= 0) cur.splice(i, 1); else cur.push(k);
    S.sel[q.id] = cur;
  } else {
    S.sel[q.id] = [k];
  }
  renderOptions();
  paintGrid();
}

function renderOptions() {
  const q = S.list[S.idx];
  const sel = S.sel[q.id] || [];
  $("opts").querySelectorAll(".opt").forEach(b => {
    b.classList.toggle("sel", sel.includes(b.dataset.k));
  });
}

function updateWrongList(q) {
  const wrong = wrongIds();
  const ok = isCorrect(q);
  if (ok && wrong.includes(q.id)) saveJSON(LS_WRONG, wrong.filter(id => id !== q.id));
  if (!ok && !wrong.includes(q.id)) saveJSON(LS_WRONG, wrong.concat(q.id));
}

/* ---------- navigation / finish ---------- */
function move(d) {
  const n = S.idx + d;
  if (n < 0) return;
  if (n >= S.list.length) { askFinish(); return; }
  S.idx = n; render(); window.scrollTo({ top: 0, behavior: "smooth" });
}

function askFinish() {
  const unanswered = S.list.filter(q => !hasAnswer(q)).length;
  const flagged = S.flags.size;
  const submit = $("modalSubmit");
  const clear = $("modalClear");
  if (flagged) {
    $("modalText").textContent = "Masih ada " + flagged + " soal ditandai ragu-ragu. Hapus semua tanda tersebut sebelum menyelesaikan sesi.";
    submit.classList.add("hide");
    clear.classList.remove("hide");
  } else {
    $("modalText").textContent = unanswered
      ? "Masih ada " + unanswered + " soal kosong. Soal kosong dihitung salah. Selesaikan sesi sekarang?"
      : "Semua soal sudah dijawab. Selesaikan sesi dan lihat hasilnya?";
    submit.classList.remove("hide");
    clear.classList.add("hide");
  }
  $("modal").classList.remove("hide");
}

function closeModal() { $("modal").classList.add("hide"); }

function finish() {
  if (S.finished) return;
  S.finished = true;
  clearInterval(S.timer);
  closeModal();
  $("quiz").classList.add("hide");
  $("tabbar").classList.add("hide");
  $("result").classList.remove("hide");
  window.scrollTo({ top: 0, behavior: "smooth" });

  const total = S.list.length;
  let ok = 0, bad = 0, skip = 0;
  const perDom = {};
  for (const q of S.list) {
    perDom[q.d] = perDom[q.d] || { ok: 0, total: 0 };
    perDom[q.d].total++;
    if (!hasAnswer(q)) { skip++; continue; }
    const good = isCorrect(q);
    if (!S.fromHistory) {
      recordResult(q.id, good);
      updateWrongList(q);
    }
    if (good) { ok++; perDom[q.d].ok++; } else bad++;
  }
  const pct = Math.round(ok / total * 100);
  const scaled = 100 + Math.round(pct * 8);
  const pass = scaled >= PASS_SCALED;
  const secs = S.durationOverride != null ? S.durationOverride : Math.round((Date.now() - S.start) / 1000);

  $("scoreNum").textContent = scaled;
  $("scoreRing").style.setProperty("--deg", (scaled / 900 * 360) + "deg");
  $("resTitle").textContent = pass ? "Lulus ambang batas 🎉" : "Belum mencapai ambang batas";
  $("resSub").textContent = `${ok} dari ${total} soal benar (${pct}%) · ${S.mode === "exam" ? "ujian simulasi" : "latihan"}${S.autoSubmit ? " · waktu habis, jawaban dikumpulkan otomatis" : ""}`;
  $("resMode").textContent = S.mode === "exam" ? "Ujian simulasi" : "Latihan";
  const pill = $("resPill");
  pill.className = "pill " + (pass ? "pass" : "fail");
  pill.textContent = pass ? "LULUS (≥750)" : "BELUM LULUS (<750)";
  $("kOk").textContent = ok; $("kBad").textContent = bad; $("kSkip").textContent = skip;
  $("kTime").textContent = fmtTime(secs);

  const names = { 1: "Fundamental", 2: "Threats & Vuln", 3: "Arsitektur", 4: "Operasi", 5: "Tata kelola" };
  $("domres").innerHTML = [1, 2, 3, 4, 5].filter(d => perDom[d]).map(d => {
    const p = perDom[d], r = Math.round(p.ok / p.total * 100);
    const col = r >= 75 ? "var(--ok)" : r >= 50 ? "var(--warn)" : "var(--bad)";
    return `<div class="dombar">
      <span class="name">D${d} · ${names[d]} <span class="note">(${p.total} soal)</span></span>
      <span class="val">${p.ok}/${p.total} · ${r}%</span>
      <span class="track"><i style="width:${r}%;background:${col}"></i></span></div>`;
  }).join("");

  $("resultMap").innerHTML = S.list.map((q, i) => {
    const answered = hasAnswer(q);
    const cls = !answered ? "skip" : isCorrect(q) ? "ok" : "no";
    return `<button class="dot ${cls}" data-i="${i}" title="Soal ${i + 1}">${i + 1}</button>`;
  }).join("");
  $("resultMap").querySelectorAll(".dot").forEach(b => b.addEventListener("click", () => {
    const el = $("rev-" + b.dataset.i);
    if (el) { el.open = true; el.scrollIntoView({ behavior: "smooth", block: "center" }); }
  }));

  const perObj = {};
  S.list.forEach(q => {
    const o = perObj[q.o] = perObj[q.o] || { ok: 0, total: 0 };
    o.total++;
    if (hasAnswer(q) && isCorrect(q)) o.ok++;
  });
  const objRows = Object.entries(perObj)
    .sort((a, b) => a[1].ok / a[1].total - b[1].ok / b[1].total)
    .slice(0, 10)
    .map(([o, v]) => {
      const r = Math.round(v.ok / v.total * 100);
      const col = r >= 75 ? "var(--ok)" : r >= 50 ? "var(--warn)" : "var(--bad)";
      return `<div class="dombar">
        <span class="name">Objektif ${o}</span>
        <span class="val">${v.ok}/${v.total} · ${r}%</span>
        <span class="track"><i style="width:${r}%;background:${col}"></i></span></div>`;
    }).join("");
  $("objRes").innerHTML = objRows || '<p class="note">Tidak ada data.</p>';

  const miss = S.list.filter(q => !isCorrect(q));
  $("review").innerHTML = `<h3>Pembahasan semua soal (${miss.length} belum benar dari ${total})</h3>` +
    S.list.map((q, i) => {
      const answered = hasAnswer(q);
      const good = answered && isCorrect(q);
      const mark = good ? "✓" : answered ? "✗" : "–";
      const cls = good ? "ok" : answered ? "no" : "skip";
      return `<details class="ritem" id="rev-${i}">
      <summary><span class="mark ${cls}">${mark}</span><span>${i + 1}. ${escapeHtml(q.q)}</span></summary>
      <div class="body">
        ${q.opts.map(o => `<div class="o ${q.a.includes(o.k) ? "a" : ""} ${(S.sel[q.id] || []).includes(o.k) && !q.a.includes(o.k) ? "mine" : ""}">
          <b>${o.k}.</b> ${escapeHtml(o.v)}</div>`).join("")}
        <p class="note">Jawaban Anda: <b>${(S.sel[q.id] || []).join(", ") || "kosong"}</b> · Jawaban benar: <b>${q.a.join(", ")}</b> · Objektif ${q.o}</p>
        <p>${md(q.e)}</p>
      </div></details>`;
    }).join("");

  if (!S.fromHistory) {
    const hist = loadJSON(LS_HIST, []);
    hist.push({
      ts: Date.now(), mode: S.mode === "exam" ? "Simulasi" : "Latihan",
      total, ok, comp: pct, scaled, secs, auto: S.autoSubmit,
      ids: S.list.map(q => q.id), sel: S.sel
    });
    saveJSON(LS_HIST, hist.slice(-30));
  }

  $("retryWrongBtn").classList.toggle("hide", !miss.length);
  refreshHome();
}

/* ---------- events ---------- */
document.querySelectorAll(".mode").forEach(el => el.addEventListener("click", () => {
  const mode = el.dataset.mode;
  if (mode === "exam") return startSession("exam", pickExam());
  if (mode === "quick") return startSession("quick", shuffle(BANK).slice(0, 25));
  if (mode === "wrong") {
    const ids = wrongIds();
    const list = shuffle(BANK.filter(q => ids.includes(q.id))).slice(0, 50);
    if (!list.length) { alert("Belum ada soal yang pernah salah. Kerjakan latihan dulu, ya!"); return; }
    return startSession("wrong", list);
  }
  if (mode === "domain") {
    $("domlist").classList.toggle("show");
    if (!$("domlist").dataset.built) { buildDomainList(); $("domlist").dataset.built = "1"; }
  }
}));

$("objStart").addEventListener("click", () => {
  const o = $("objSelect").value;
  const pool = shuffle(BANK.filter(q => q.o === o));
  if (pool.length) startSession("objective", pool.slice(0, Math.min(20, pool.length)));
});

$("prevBtn").addEventListener("click", () => move(-1));
$("nextBtn").addEventListener("click", () => move(1));
$("flagBtn").addEventListener("click", () => {
  const q = S.list[S.idx];
  if (S.flags.has(q.id)) S.flags.delete(q.id); else S.flags.add(q.id);
  render();
});
$("quitBtn").addEventListener("click", () => {
  if (confirm("Keluar dari sesi ini? Progres sesi akan hilang.")) {
    clearInterval(S.timer); S.finished = true;
    $("quiz").classList.add("hide");
    $("tabbar").classList.remove("hide");
    showTab("practice");
    refreshHome();
  }
});
function goHome() {
  $("result").classList.add("hide");
  $("tabbar").classList.remove("hide");
  showTab("practice");
}
$("homeBtn").addEventListener("click", goHome);
$("homeBtnTop").addEventListener("click", goHome);
$("againBtn").addEventListener("click", () => {
  if (S.mode === "exam") return startSession("exam", pickExam());
  if (S.mode === "domain" && S.domain) {
    const pool = shuffle(BANK.filter(q => q.d === S.domain));
    return startSession("domain", pool.slice(0, Math.min(20, pool.length)), S.domain);
  }
  if (S.mode === "objective") {
    const o = S.list[0].o;
    const pool = shuffle(BANK.filter(q => q.o === o));
    return startSession("objective", pool.slice(0, Math.min(20, pool.length)));
  }
  startSession(S.mode === "wrong" ? "quick" : S.mode, shuffle(BANK).slice(0, S.list.length));
});
$("retryWrongBtn").addEventListener("click", () => {
  const ids = wrongIds();
  const list = shuffle(BANK.filter(q => ids.includes(q.id))).slice(0, 50);
  if (list.length) startSession("wrong", list);
});
$("modalBack").addEventListener("click", closeModal);
$("modalSubmit").addEventListener("click", finish);
$("modalClear").addEventListener("click", () => {
  S.flags.clear();
  paintGrid();
  render();
  askFinish();
});

document.addEventListener("keydown", (e) => {
  if (!$("modal").classList.contains("hide")) {
    if (e.key === "Escape") closeModal();
    return;
  }
  if ($("quiz").classList.contains("hide")) return;
  const q = S.list[S.idx];
  if (!q) return;
  if (["1", "2", "3", "4", "5", "6"].includes(e.key)) {
    const opt = q.opts[+e.key - 1];
    if (opt) { e.preventDefault(); choose(opt.k); }
  } else if (e.key === "ArrowRight") { e.preventDefault(); move(1); }
  else if (e.key === "ArrowLeft") { e.preventDefault(); move(-1); }
  else if (e.key.toLowerCase() === "f") { e.preventDefault(); $("flagBtn").click(); }
});

/* ---------- PBQ ---------- */
function renderPBQ() {
  const notes = loadJSON(LS_PBQ, {});
  const st = loadJSON(LS_PBQ_STATUS, {});
  $("pbqList").innerHTML = PBQ.map(p => `
    <article class="pbq" data-id="${p.id}">
      <div class="pbq-head"><span class="badge gold">${p.id}</span><h3>${escapeHtml(p.title)}</h3></div>
      <div class="md">${p.prompt}</div>
      <textarea data-note="${p.id}" placeholder="Tulis jawaban Anda di sini (tersimpan otomatis)...">${escapeHtml(notes[p.id] || "")}</textarea>
      <div class="pbq-actions">
        <button class="btn" data-reveal="${p.id}">Lihat jawaban model</button>
        <button class="btn ${st[p.id] === "ok" ? "on" : ""}" data-status="ok" data-id="${p.id}">✓ Paham</button>
        <button class="btn ${st[p.id] === "no" ? "on-no" : ""}" data-status="no" data-id="${p.id}">✗ Belum paham</button>
      </div>
      <div class="md pbq-answer hide" data-answer="${p.id}">${p.answer}</div>
    </article>`).join("");
  $("pbqList").querySelectorAll("textarea").forEach(t => t.addEventListener("input", () => {
    const n = loadJSON(LS_PBQ, {});
    n[t.dataset.note] = t.value;
    saveJSON(LS_PBQ, n);
  }));
  $("pbqList").querySelectorAll("[data-reveal]").forEach(b => b.addEventListener("click", () => {
    const id = b.dataset.reveal;
    const ans = $("pbqList").querySelector(`[data-answer="${id}"]`);
    const hidden = ans.classList.toggle("hide");
    b.textContent = hidden ? "Lihat jawaban model" : "Sembunyikan jawaban";
  }));
  $("pbqList").querySelectorAll("[data-status]").forEach(b => b.addEventListener("click", () => {
    const st2 = loadJSON(LS_PBQ_STATUS, {});
    const id = b.dataset.id, v = b.dataset.status;
    if (st2[id] === v) delete st2[id]; else st2[id] = v;
    saveJSON(LS_PBQ_STATUS, st2);
    paintPbqStatus();
  }));
  paintPbqStatus();
}

function paintPbqStatus() {
  const st = loadJSON(LS_PBQ_STATUS, {});
  $("pbqList").querySelectorAll("[data-status]").forEach(b => {
    const on = st[b.dataset.id] === b.dataset.status;
    b.classList.toggle("on", on && b.dataset.status === "ok");
    b.classList.toggle("on-no", on && b.dataset.status === "no");
  });
}

/* ---------- boot ---------- */
applyTheme(localStorage.getItem(LS_THEME) || "dark");
try { buildObjectiveSelect(); } catch (e) { console.error(e); }
refreshHome();
renderPBQ();
</script>
</body>
</html>
"""


def main() -> None:
    data = json.loads((DIST / "questions.json").read_text(encoding="utf-8"))
    bank = []
    for d in data["domains"]:
        for q in d["questions"]:
            bank.append(
                {
                    "id": q["id"],
                    "d": q["domain"],
                    "o": q["objective"],
                    "t": q["type"],
                    "q": q["stem"],
                    "opts": [{"k": o["key"], "v": o["text"]} for o in q["options"]],
                    "a": q["answers"],
                    "e": q["explanation"],
                }
            )
    plan = {1: 11, 2: 20, 3: 16, 4: 25, 5: 18}
    assert sum(plan.values()) == 90
    for d, n in plan.items():
        have = sum(1 for q in bank if q["d"] == d)
        if have < n:
            raise SystemExit(f"Domain {d} only has {have} questions, need {n} for exam plan")

    pbq = parse_pbq()
    if not pbq:
        raise SystemExit("No PBQ items parsed")

    def js(obj) -> str:
        return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    html = (
        TEMPLATE.replace("__QUESTIONS__", js(bank))
        .replace("__PBQ__", js(pbq))
        .replace("__DOMAINS__", json.dumps(DOMAINS, ensure_ascii=False))
        .replace("__PLAN__", json.dumps(plan))
    )
    out = DIST / "quiz.html"
    out.write_text(html, encoding="utf-8")
    multi = sum(1 for q in bank if len(q["a"]) > 1)
    print(f"Wrote {out.relative_to(ROOT)} ({out.stat().st_size/1024:.0f} KB, {len(bank)} soal, {multi} multi-select, {len(pbq)} PBQ)")


if __name__ == "__main__":
    main()
