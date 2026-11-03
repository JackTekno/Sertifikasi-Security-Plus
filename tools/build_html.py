#!/usr/bin/env python3
"""Build a self-contained interactive quiz (dist/quiz.html) from dist/questions.json."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"

DOMAINS = [
    {"id": 1, "name": "General Security Concepts", "weight": 12},
    {"id": 2, "name": "Threats, Vulnerabilities, and Mitigations", "weight": 22},
    {"id": 3, "name": "Security Architecture", "weight": 18},
    {"id": 4, "name": "Security Operations", "weight": 28},
    {"id": 5, "name": "Security Program Management and Oversight", "weight": 20},
]

TEMPLATE = r"""<!DOCTYPE html>
<html lang="id">
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
.wrap{max-width:980px;margin:0 auto;padding:24px 18px 64px}
.brand{display:flex;align-items:center;gap:12px;font-weight:700;letter-spacing:.2px}
.logo{width:38px;height:38px;border-radius:11px;display:grid;place-items:center;
  background:linear-gradient(135deg,var(--accent),#6366f1);color:#04121f;font-size:19px}
.brand small{display:block;font-weight:500;color:var(--muted);font-size:12px;letter-spacing:.3px}
.topbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:22px}
.hero{margin:18px 0 26px}
.hero h1{font-size:clamp(26px,4vw,38px);margin:0 0 8px;line-height:1.2}
.hero p{color:var(--muted);margin:0;max-width:720px}
.hero .hl{color:var(--accent)}
.stats{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0 6px}
.chip{background:var(--card);border:1px solid var(--line);border-radius:999px;
  padding:6px 12px;font-size:12.5px;color:var(--muted)}
.chip b{color:var(--txt)}
.modes{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin-top:14px}
.mode{background:linear-gradient(180deg,var(--card),var(--bg2));border:1px solid var(--line);
  border-radius:16px;padding:18px;cursor:pointer;transition:.18s transform,.18s border-color,.18s box-shadow;
  display:flex;flex-direction:column;gap:6px;text-align:left;color:inherit;font:inherit}
.mode:hover{transform:translateY(-2px);border-color:#3d5a85;box-shadow:var(--shadow)}
.mode .ic{font-size:22px}
.mode h3{margin:2px 0 0;font-size:16px}
.mode p{margin:0;color:var(--muted);font-size:13px}
.mode .tag{margin-top:6px;font-size:12px;color:var(--accent)}
.domlist{display:none;gap:8px;flex-wrap:wrap;margin-top:14px}
.domlist.show{display:flex}
.dombtn{background:var(--card2);border:1px solid var(--line);color:var(--txt);
  padding:8px 12px;border-radius:10px;cursor:pointer;font-size:13px;text-align:left}
.dombtn:hover{border-color:var(--accent)}
.hist{margin-top:30px;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 18px}
.hist h3{margin:0 0 8px;font-size:15px}
.hist table{width:100%;border-collapse:collapse;font-size:13px}
.hist td,.hist th{text-align:left;padding:7px 6px;border-bottom:1px solid var(--line);color:var(--muted)}
.hist th{color:var(--txt);font-weight:600;font-size:12px;text-transform:uppercase;letter-spacing:.4px}
.hist tr:last-child td{border-bottom:0}
.pill{display:inline-block;padding:2px 9px;border-radius:999px;font-size:11.5px;font-weight:700}
.pill.pass{background:rgba(52,211,153,.14);color:var(--ok)}
.pill.fail{background:rgba(251,113,133,.14);color:var(--bad)}
.hide{display:none !important}

/* quiz */
.quizhead{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:10px}
.timer{font-variant-numeric:tabular-nums;background:var(--card);border:1px solid var(--line);
  padding:7px 13px;border-radius:11px;font-weight:700;letter-spacing:.4px}
.timer.low{color:var(--bad);border-color:rgba(251,113,133,.5)}
.btn{background:var(--card2);border:1px solid var(--line);color:var(--txt);padding:9px 15px;
  border-radius:11px;cursor:pointer;font:inherit;font-size:13.5px;transition:.15s}
.btn:hover{border-color:#3d5a85}
.btn.primary{background:linear-gradient(135deg,var(--accent),#6366f1);color:#05121f;font-weight:700;border:0}
.btn.primary:hover{filter:brightness(1.07)}
.btn.ghost{background:transparent}
.btn:disabled{opacity:.45;cursor:not-allowed}
.btn.warn{border-color:rgba(251,191,36,.45);color:var(--warn)}
.btn.flag-on{border-color:rgba(251,191,36,.7);color:var(--warn);background:rgba(251,191,36,.08)}
.pbar{height:7px;background:#0c1626;border-radius:99px;overflow:hidden;border:1px solid #1b2a42;margin-bottom:18px}
.pbar i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--accent2),var(--accent));transition:width .25s}
.card{background:linear-gradient(180deg,var(--card),#0f1a2c);border:1px solid var(--line);
  border-radius:18px;padding:24px;box-shadow:var(--shadow)}
.meta{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:14px}
.badge{background:rgba(56,189,248,.12);color:var(--accent);border:1px solid rgba(56,189,248,.25);
  padding:3px 10px;border-radius:999px;font-size:11.5px;font-weight:600;letter-spacing:.3px}
.badge.ghost{background:transparent;color:var(--muted);border-color:var(--line)}
.stem{font-size:clamp(17px,2.2vw,20px);line-height:1.55;margin:0 0 20px;font-weight:600}
.opts{display:grid;gap:10px}
.opt{display:flex;gap:12px;align-items:flex-start;text-align:left;background:#0e192b;
  border:1px solid var(--line);border-radius:13px;padding:13px 15px;cursor:pointer;color:inherit;
  font:inherit;font-size:15px;transition:.14s}
.opt:hover:not(:disabled){border-color:#3d5a85;background:#122036}
.opt .k{flex:0 0 28px;height:28px;border-radius:9px;display:grid;place-items:center;
  background:#182742;border:1px solid #2b3f61;font-weight:700;font-size:13px;color:var(--accent)}
.opt.sel{border-color:var(--accent);background:rgba(56,189,248,.09)}
.opt.sel .k{background:rgba(56,189,248,.22);border-color:rgba(56,189,248,.5);color:var(--accent)}
.opt.correct{border-color:rgba(52,211,153,.65);background:rgba(52,211,153,.09)}
.opt.correct .k{background:rgba(52,211,153,.2);border-color:rgba(52,211,153,.5);color:var(--ok)}
.opt.wrong{border-color:rgba(251,113,133,.6);background:rgba(251,113,133,.08)}
.opt.wrong .k{background:rgba(251,113,133,.2);border-color:rgba(251,113,133,.5);color:var(--bad)}
.opt:disabled{cursor:default;opacity:1}
.opt.dim{opacity:.55}
.fb{margin-top:18px;border-radius:13px;padding:14px 16px;border:1px solid var(--line);background:#0d1728;display:none}
.fb.show{display:block;animation:pop .18s ease-out}
@keyframes pop{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
.fb .verdict{font-weight:700;margin-bottom:6px;display:flex;gap:8px;align-items:center}
.fb.ok{border-color:rgba(52,211,153,.4)}
.fb.ok .verdict{color:var(--ok)}
.fb.bad{border-color:rgba(251,113,133,.4)}
.fb.bad .verdict{color:var(--bad)}
.fb .ans{color:var(--muted);font-size:13px;margin-bottom:6px}
.fb p{margin:0;font-size:14.5px;color:#d6e2f7}
.nav{display:flex;justify-content:space-between;gap:10px;margin-top:22px;flex-wrap:wrap}
.nav .right{display:flex;gap:10px;margin-left:auto}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(34px,1fr));gap:6px;margin-top:18px}
.dot{aspect-ratio:1;border-radius:8px;border:1px solid var(--line);background:#0d1728;color:var(--muted);
  font-size:12px;cursor:pointer;display:grid;place-items:center}
.dot.cur{outline:2px solid var(--accent);color:var(--txt)}
.dot.done{background:rgba(56,189,248,.18);color:var(--accent);border-color:rgba(56,189,248,.35)}
.dot.flag{border-color:rgba(251,191,36,.65);color:var(--warn)}
.dot.done.flag{background:rgba(251,191,36,.12)}

/* result */
.reshead{display:flex;gap:22px;align-items:center;flex-wrap:wrap;margin-bottom:8px}
.score{width:150px;height:150px;border-radius:50%;display:grid;place-items:center;
  background:conic-gradient(var(--accent) var(--deg,0deg),#16243a 0);position:relative;flex:0 0 auto}
.score::after{content:"";position:absolute;inset:9px;border-radius:50%;background:#0d1728}
.score .in{position:relative;z-index:1;text-align:center}
.score .num{font-size:34px;font-weight:800;line-height:1}
.score .lbl{font-size:11px;color:var(--muted);letter-spacing:.6px;text-transform:uppercase}
.resmeta h2{margin:0 0 4px;font-size:23px}
.resmeta p{margin:0;color:var(--muted);font-size:14px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px;margin:18px 0 4px}
.kpi{background:#0e192b;border:1px solid var(--line);border-radius:13px;padding:12px 14px}
.kpi .v{font-size:20px;font-weight:800}
.kpi .l{font-size:11.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.4px}
.kpi.ok .v{color:var(--ok)} .kpi.bad .v{color:var(--bad)} .kpi.warn .v{color:var(--warn)}
.domres{margin-top:22px;display:grid;gap:10px}
.dombar{display:grid;grid-template-columns:1fr auto;gap:6px 12px;align-items:center}
.dombar .name{font-size:13.5px}
.dombar .val{font-size:12.5px;color:var(--muted)}
.dombar .track{grid-column:1/-1;height:8px;border-radius:99px;background:#0c1626;overflow:hidden}
.dombar .track i{display:block;height:100%;border-radius:99px}
.review{margin-top:26px}
.review h3{margin:0 0 10px;font-size:16px}
.ritem{border:1px solid var(--line);border-radius:13px;margin-bottom:10px;overflow:hidden;background:#0e192b}
.ritem summary{cursor:pointer;padding:13px 15px;font-size:14px;font-weight:600;list-style:none;display:flex;gap:9px;align-items:flex-start}
.ritem summary::-webkit-details-marker{display:none}
.ritem .body{padding:0 15px 15px;font-size:14px;color:#cfdcf2}
.ritem .body .opts{display:grid;gap:5px;margin:8px 0}
.ritem .body .o{padding:7px 10px;border-radius:8px;background:#0b1524;border:1px solid var(--line);font-size:13.5px}
.ritem .body .o.a{border-color:rgba(52,211,153,.45)}
.ritem .body .o.mine{border-color:rgba(251,113,133,.45)}
.note{color:var(--muted);font-size:13px}
.footer{margin-top:34px;color:#5b6b88;font-size:12px;text-align:center}
@media (max-width:560px){
  .card{padding:18px}
  .score{width:120px;height:120px}
  .score .num{font-size:27px}
  .nav .right{width:100%;margin-left:0}
  .nav .right .btn{flex:1}
}
</style>
</head>
<body>
<div class="wrap">

  <div class="topbar">
    <div class="brand">
      <div class="logo">🛡️</div>
      <div>Security+ SY0-701<small>Latihan soal interaktif · Bahasa Indonesia</small></div>
    </div>
    <div class="chip"><b id="bankCount">0</b> soal di bank</div>
  </div>

  <!-- HOME -->
  <section id="home">
    <div class="hero">
      <h1>Latihan <span class="hl">SY0-701</span>, siap hadapi ujian Security+</h1>
      <p>Kerjakan soal bergaya ujian dengan pembahasan Bahasa Indonesia. Mode simulasi memakai komposisi domain sesuai bobot resmi dan batas waktu 90 menit.</p>
      <div class="stats">
        <span class="chip">5 domain</span>
        <span class="chip">Passing score <b>750/900</b></span>
        <span class="chip">Pembahasan tiap soal</span>
        <span class="chip">Progres tersimpan di browser</span>
      </div>
    </div>

    <div class="modes">
      <button class="mode" data-mode="exam">
        <span class="ic">⏱️</span>
        <h3>Ujian Simulasi</h3>
        <p>90 soal campuran sesuai bobot domain, 90 menit, nilai akhir seperti ujian asli.</p>
        <span class="tag">Mulai ujian →</span>
      </button>
      <button class="mode" data-mode="domain">
        <span class="ic">📚</span>
        <h3>Latihan per Domain</h3>
        <p>Pilih salah satu dari 5 domain. 20 soal acak, pembahasan langsung muncul.</p>
        <span class="tag">Pilih domain →</span>
      </button>
      <button class="mode" data-mode="quick">
        <span class="ic">⚡</span>
        <h3>Latihan Cepat</h3>
        <p>25 soal acak dari semua domain, tanpa timer. Cocok untuk sesi 20 menit.</p>
        <span class="tag">Mulai latihan →</span>
      </button>
      <button class="mode" data-mode="wrong">
        <span class="ic">🔁</span>
        <h3>Ulangi yang Salah</h3>
        <p>Kerjakan kembali soal yang pernah Anda jawab salah. Hilang otomatis saat benar.</p>
        <span class="tag" id="wrongTag">Belum ada data →</span>
      </button>
    </div>

    <div class="domlist" id="domlist"></div>

    <div class="hist" id="histBox">
      <h3>Riwayat latihan</h3>
      <div id="histBody" class="note">Belum ada riwayat. Selesaikan satu sesi untuk melihat statistik.</div>
    </div>
  </section>

  <!-- QUIZ -->
  <section id="quiz" class="hide">
    <div class="quizhead">
      <div class="brand"><div class="logo" style="width:32px;height:32px;font-size:16px">🛡️</div>
        <div style="font-size:14px">SY0-701<small id="modeLabel">Latihan</small></div></div>
      <div style="display:flex;gap:8px;align-items:center">
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
      <div class="opts" id="opts"></div>
      <div class="fb" id="fb"></div>
      <div class="nav">
        <button class="btn" id="prevBtn">← Sebelumnya</button>
        <div class="right">
          <button class="btn warn" id="flagBtn">⚑ Ragu-ragu</button>
          <button class="btn primary" id="nextBtn">Berikutnya →</button>
        </div>
      </div>
    </div>

    <div class="grid" id="grid"></div>
    <p class="note" style="margin-top:14px">Shortcut: <b>1–4</b> pilih jawaban · <b>←</b>/<b>→</b> navigasi · <b>F</b> tandai ragu-ragu.</p>
  </section>

  <!-- RESULT -->
  <section id="result" class="hide">
    <div class="card">
      <div class="reshead">
        <div class="score" id="scoreRing"><div class="in"><div class="num" id="scoreNum">0</div><div class="lbl">dari 900</div></div></div>
        <div class="resmeta">
          <h2 id="resTitle">Hasil</h2>
          <p id="resSub"></p>
          <p style="margin-top:8px"><span class="pill" id="resPill">—</span></p>
        </div>
      </div>
      <div class="kpis">
        <div class="kpi ok"><div class="v" id="kOk">0</div><div class="l">Benar</div></div>
        <div class="kpi bad"><div class="v" id="kBad">0</div><div class="l">Salah</div></div>
        <div class="kpi warn"><div class="v" id="kSkip">0</div><div class="l">Kosong</div></div>
        <div class="kpi"><div class="v" id="kTime">0:00</div><div class="l">Waktu</div></div>
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

  <div class="footer">Bank soal latihan independen · bukan produk resmi CompTIA · dibuat untuk belajar mandiri</div>
</div>

<script>
const BANK = __QUESTIONS__;
const DOMAINS = __DOMAINS__;
const EXAM_PLAN = __PLAN__;
const PASS_SCALED = 750;
const LS_WRONG = "sp701_wrong_v1";
const LS_HIST = "sp701_history_v1";

/* ---------- helpers ---------- */
const $ = (id) => document.getElementById(id);
const shuffle = (arr) => {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
};
const loadJSON = (k, fb) => { try { return JSON.parse(localStorage.getItem(k)) ?? fb; } catch { return fb; } };
const saveJSON = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} };
const fmtTime = (s) => {
  s = Math.max(0, Math.floor(s));
  const m = Math.floor(s / 60), r = s % 60;
  return m + ":" + String(r).padStart(2, "0");
};
const domName = (id) => (DOMAINS.find(d => d.id === id) || {}).name || "";

/* ---------- state ---------- */
const S = {
  mode: null, domain: null, list: [], idx: 0, answers: {}, flags: new Set(),
  start: 0, remain: 0, timer: null, finished: false, locked: new Set()
};

/* ---------- home ---------- */
function wrongIds() { return loadJSON(LS_WRONG, []); }
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
            <td><span class="pill ${h.scaled >= PASS_SCALED ? "pass" : "fail"}">${h.scaled >= PASS_SCALED ? "LULUS" : "BELUM"}</span></td></tr>`;
  }).join("");
  $("histBody").innerHTML = `
    <div class="stats" style="margin:0 0 12px">
      <span class="chip">Sesi: <b>${hist.length}</b></span>
      <span class="chip">Skor terbaik: <b>${best}</b></span>
      <span class="chip">Rata-rata: <b>${avg}</b></span>
      <span class="chip">Soal pernah salah: <b>${w}</b></span>
    </div>
    <table><thead><tr><th>Waktu</th><th>Mode</th><th>Jumlah</th><th>Skor</th><th>Status</th></tr></thead>
    <tbody>${rows}</tbody></table>`;
}

/* ---------- start session ---------- */
function startSession(mode, list, domain) {
  if (!list.length) return;
  S.mode = mode; S.domain = domain || null; S.list = list; S.idx = 0; S.answers = {}; S.flags = new Set();
  S.locked = new Set(); S.finished = false; S.start = Date.now();
  S.remain = mode === "exam" ? 90 * 60 : 0;

  $("home").classList.add("hide");
  $("result").classList.add("hide");
  $("quiz").classList.remove("hide");
  $("modeLabel").textContent = mode === "exam" ? "Ujian simulasi · 90 menit" :
    mode === "domain" ? "Latihan per domain" : mode === "wrong" ? "Ulangi yang salah" : "Latihan cepat";

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
  if (S.remain <= 0 && !S.finished) { clearInterval(S.timer); finish(); }
}

function pickExam() {
  const plan = EXAM_PLAN;
  let out = [];
  for (const d of [1, 2, 3, 4, 5]) {
    const pool = shuffle(BANK.filter(q => q.d === d));
    out = out.concat(pool.slice(0, plan[d]));
  }
  return shuffle(out);
}

/* ---------- render question ---------- */
function buildGrid() {
  $("grid").innerHTML = S.list.map((q, i) =>
    `<button class="dot" data-i="${i}" title="Soal ${i + 1}">${i + 1}</button>`).join("");
  $("grid").querySelectorAll(".dot").forEach(b =>
    b.addEventListener("click", () => { S.idx = +b.dataset.i; render(); }));
  paintGrid();
}

function paintGrid() {
  $("grid").querySelectorAll(".dot").forEach((b, i) => {
    const q = S.list[i];
    b.classList.toggle("cur", i === S.idx);
    b.classList.toggle("done", !!S.answers[q.id]);
    b.classList.toggle("flag", S.flags.has(q.id));
  });
}

function render() {
  const q = S.list[S.idx];
  const practice = S.mode !== "exam";
  const chosen = S.answers[q.id];
  const locked = S.locked.has(q.id);

  $("qDomain").textContent = "Domain " + q.d + " · " + domName(q.d);
  $("qObjective").textContent = "Objektif " + q.o;
  $("qType").textContent = q.t;
  $("stem").textContent = q.q;

  $("opts").innerHTML = q.opts.map(o =>
    `<button class="opt" data-k="${o.k}" ${(locked || (practice && chosen)) ? "disabled" : ""}>
       <span class="k">${o.k}</span><span>${escapeHtml(o.v)}</span></button>`).join("");

  $("opts").querySelectorAll(".opt").forEach(b =>
    b.addEventListener("click", () => choose(b.dataset.k)));

  if (chosen && !practice) {
    const sel = $("opts").querySelector('.opt[data-k="' + chosen + '"]');
    if (sel) sel.classList.add("sel");
  }

  // feedback / answer state
  const fb = $("fb");
  fb.className = "fb";
  fb.innerHTML = "";
  if (practice && chosen) {
    const ok = chosen === q.a;
    fb.classList.add("show", ok ? "ok" : "bad");
    fb.innerHTML = `<div class="verdict">${ok ? "✅ Benar" : "❌ Belum tepat"}</div>
      ${ok ? "" : `<div class="ans">Jawaban Anda: <b>${chosen}</b> · Jawaban benar: <b>${q.a}</b></div>`}
      <p>${escapeHtml(q.e)}</p>`;
    markOptions(q, chosen, !ok);
  } else if (practice && !chosen) {
    // nothing
  }

  $("pbar").style.width = ((S.idx + 1) / S.list.length * 100) + "%";
  $("counter").textContent = (S.idx + 1) + " / " + S.list.length;
  $("prevBtn").disabled = S.idx === 0;
  $("nextBtn").textContent = S.idx === S.list.length - 1 ? "Selesai ✓" : "Berikutnya →";
  $("flagBtn").classList.toggle("flag-on", S.flags.has(q.id));
  $("flagBtn").textContent = S.flags.has(q.id) ? "⚑ Ditandai" : "⚑ Ragu-ragu";
  paintGrid();
}

function markOptions(q, chosen, revealAll) {
  $("opts").querySelectorAll(".opt").forEach(b => {
    const k = b.dataset.k;
    b.disabled = true;
    if (k === q.a) b.classList.add("correct");
    else if (k === chosen) b.classList.add("wrong");
    else if (revealAll) b.classList.add("dim");
  });
}

function choose(k) {
  const q = S.list[S.idx];
  if (S.locked.has(q.id)) return;
  S.answers[q.id] = k;
  if (S.mode !== "exam") S.locked.add(q.id);

  const wrong = wrongIds();
  const ok = k === q.a;
  if (ok && wrong.includes(q.id)) saveJSON(LS_WRONG, wrong.filter(id => id !== q.id));
  if (!ok && !wrong.includes(q.id)) saveJSON(LS_WRONG, wrong.concat(q.id));

  if (S.mode === "exam") {
    $("opts").querySelectorAll(".opt").forEach(b => b.classList.toggle("sel", b.dataset.k === k));
    paintGrid();
    return;
  }
  render();
  $("fb").scrollIntoView({ block: "nearest", behavior: "smooth" });
}

/* ---------- navigation ---------- */
function move(d) {
  const n = S.idx + d;
  if (n < 0) return;
  if (n >= S.list.length) {
    const unanswered = S.list.filter(q => !S.answers[q.id]).length;
    if (unanswered && !confirm("Masih ada " + unanswered + " soal yang belum dijawab. Selesaikan sesi sekarang?")) return;
    finish();
    return;
  }
  S.idx = n; render(); window.scrollTo({ top: 0, behavior: "smooth" });
}

/* ---------- finish ---------- */
function finish() {
  if (S.finished) return;
  S.finished = true;
  clearInterval(S.timer);
  $("quiz").classList.add("hide");
  $("result").classList.remove("hide");
  window.scrollTo({ top: 0, behavior: "smooth" });

  const total = S.list.length;
  let ok = 0, bad = 0, skip = 0;
  const perDom = {};
  for (const q of S.list) {
    perDom[q.d] = perDom[q.d] || { ok: 0, total: 0 };
    perDom[q.d].total++;
    const a = S.answers[q.id];
    if (!a) skip++;
    else if (a === q.a) { ok++; perDom[q.d].ok++; }
    else bad++;
  }
  const pct = Math.round(ok / total * 100);
  const scaled = 100 + Math.round(pct * 8);
  const pass = scaled >= PASS_SCALED;
  const secs = Math.round((Date.now() - S.start) / 1000);

  $("scoreNum").textContent = scaled;
  $("scoreRing").style.setProperty("--deg", (scaled / 900 * 360) + "deg");
  $("resTitle").textContent = pass ? "Lulus ambang batas 🎉" : "Belum mencapai ambang batas";
  $("resSub").textContent = `${ok} dari ${total} soal benar (${pct}%) · mode ${S.mode === "exam" ? "ujian simulasi" : "latihan"}`;
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

  const miss = S.list.filter(q => S.answers[q.id] !== q.a);
  $("review").innerHTML = miss.length ? `<h3>Pembahasan soal yang belum benar (${miss.length})</h3>` +
    miss.map((q, i) => `<details class="ritem">
      <summary><span>${i + 1}.</span><span>${escapeHtml(q.q)}</span></summary>
      <div class="body">
        <div class="opts">${q.opts.map(o => `<div class="o ${o.k === q.a ? "a" : ""} ${o.k === S.answers[q.id] && o.k !== q.a ? "mine" : ""}">
          <b>${o.k}.</b> ${escapeHtml(o.v)}</div>`).join("")}</div>
        <p class="note">Jawaban Anda: <b>${S.answers[q.id] || "kosong"}</b> · Jawaban benar: <b>${q.a}</b> · Objektif ${q.o}</p>
        <p>${escapeHtml(q.e)}</p>
      </div></details>`).join("") : `<h3>Tidak ada soal yang salah 🎯</h3><p class="note">Semua jawaban benar. Coba mode ujian simulasi untuk mengukur kesiapan.</p>`;

  const hist = loadJSON(LS_HIST, []);
  hist.push({ ts: Date.now(), mode: S.mode === "exam" ? "Simulasi" : "Latihan", total, ok, comp: pct, scaled });
  saveJSON(LS_HIST, hist.slice(-50));

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
    $("quiz").classList.add("hide"); $("home").classList.remove("hide");
    refreshHome(); window.scrollTo(0, 0);
  }
});
$("homeBtn").addEventListener("click", () => {
  $("result").classList.add("hide"); $("home").classList.remove("hide"); refreshHome();
});
$("againBtn").addEventListener("click", () => {
  if (S.mode === "exam") return startSession("exam", pickExam());
  if (S.mode === "domain" && S.domain) {
    const pool = shuffle(BANK.filter(q => q.d === S.domain));
    return startSession("domain", pool.slice(0, Math.min(20, pool.length)), S.domain);
  }
  startSession(S.mode === "wrong" ? "quick" : S.mode, shuffle(BANK).slice(0, S.list.length));
});
$("retryWrongBtn").addEventListener("click", () => {
  const ids = wrongIds();
  const list = shuffle(BANK.filter(q => ids.includes(q.id))).slice(0, 50);
  if (list.length) startSession("wrong", list);
});

document.addEventListener("keydown", (e) => {
  if ($("quiz").classList.contains("hide")) return;
  const q = S.list[S.idx];
  if (!q) return;
  if (["1", "2", "3", "4", "5"].includes(e.key)) {
    const opt = q.opts[+e.key - 1];
    if (opt && !S.locked.has(q.id)) { e.preventDefault(); choose(opt.k); }
  } else if (e.key === "ArrowRight") { e.preventDefault(); move(1); }
  else if (e.key === "ArrowLeft") { e.preventDefault(); move(-1); }
  else if (e.key.toLowerCase() === "f") { e.preventDefault(); $("flagBtn").click(); }
});

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

refreshHome();
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
                    "a": q["answer"],
                    "e": q["explanation"],
                }
            )
    plan = {1: 11, 2: 20, 3: 16, 4: 25, 5: 18}
    assert sum(plan.values()) == 90
    for d, n in plan.items():
        have = sum(1 for q in bank if q["d"] == d)
        if have < n:
            raise SystemExit(f"Domain {d} only has {have} questions, need {n} for exam plan")

    questions_js = json.dumps(bank, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = (
        TEMPLATE.replace("__QUESTIONS__", questions_js)
        .replace("__DOMAINS__", json.dumps(DOMAINS, ensure_ascii=False))
        .replace("__PLAN__", json.dumps(plan))
    )
    out = DIST / "quiz.html"
    out.write_text(html, encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)} ({out.stat().st_size/1024:.0f} KB, {len(bank)} soal)")


if __name__ == "__main__":
    main()
