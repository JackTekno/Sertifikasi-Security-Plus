// Minimal DOM harness to smoke-test the quiz logic in Node (no browser available).
import fs from "node:fs";

class El {
  constructor(tag = "div", id = "") {
    this.tag = tag; this.id = id;
    this._classes = new Set(); this.dataset = {}; this.children = [];
    this._listeners = {}; this._html = ""; this._text = ""; this.disabled = false;
    this.value = "";
    this.style = { setProperty() {} };
    const self = this;
    this.classList = {
      add: (...c) => c.forEach(x => self._classes.add(x)),
      remove: (...c) => c.forEach(x => self._classes.delete(x)),
      toggle: (c, f) => { const on = f === undefined ? !self._classes.has(c) : !!f; on ? self._classes.add(c) : self._classes.delete(c); return on; },
      contains: c => self._classes.has(c),
    };
  }
  set className(v) { this._classes = new Set(String(v).split(/\s+/).filter(Boolean)); }
  get className() { return [...this._classes].join(" "); }
  set innerHTML(v) {
    this._html = String(v);
    this.children = [];
    const re = /<button class="([^"]*)"([^>]*)>([\s\S]*?)<\/button>/g;
    let m;
    while ((m = re.exec(this._html))) {
      const el = new El("button");
      m[1].split(/\s+/).filter(Boolean).forEach(c => el._classes.add(c));
      const attrRe = /data-([\w-]+)="([^"]*)"/g;
      let a;
      while ((a = attrRe.exec(m[2]))) el.dataset[a[1]] = a[2];
      el._text = m[3].replace(/<[^>]*>/g, "").trim();
      el.parent = this;
      this.children.push(el);
    }
  }
  get innerHTML() { return this._html; }
  set textContent(v) { this._text = String(v); }
  get textContent() { return this._text; }
  addEventListener(t, fn) { (this._listeners[t] ||= []).push(fn); }
  click() { (this._listeners.click || []).forEach(f => f({ preventDefault() {}, target: this })); }
  focus() {}
  scrollIntoView() {}
  querySelectorAll(sel) {
    if (sel.startsWith(".")) {
      const cls = sel.slice(1);
      return this.children.filter(c => c._classes.has(cls));
    }
    return [];
  }
  querySelector(sel) {
    const m = /^\.([\w-]+)\[data-([\w-]+)="([^"]*)"\]$/.exec(sel);
    if (m) return this.querySelectorAll("." + m[1]).find(c => c.dataset[m[2]] === m[3]) || null;
    return this.querySelectorAll(sel)[0] || null;
  }
}

const els = new Map();
const document = {
  documentElement: { dataset: { theme: "dark" } },
  getElementById: id => {
    if (!els.has(id)) els.set(id, new El("div", id));
    return els.get(id);
  },
  querySelectorAll: sel => {
    if (sel === ".mode") return modes;
    if (sel === ".tab") return tabs;
    return [];
  },
  addEventListener() {},
};
const modes = ["exam", "domain", "quick", "wrong"].map(m => { const e = new El("button"); e.dataset.mode = m; return e; });
const tabs = ["practice", "pbq", "stats"].map(t => { const e = new El("button"); e.dataset.tab = t; return e; });

globalThis.document = document;
globalThis.window = { scrollTo() {} };
globalThis.localStorage = {
  store: {},
  getItem(k) { return Object.hasOwn(this.store, k) ? this.store[k] : null; },
  setItem(k, v) { this.store[k] = String(v); },
};
globalThis.confirm = () => true;
globalThis.alert = () => {};
globalThis.setInterval = () => 1;
globalThis.clearInterval = () => {};

const html = fs.readFileSync("dist/quiz.html", "utf8");
const script = /<script>([\s\S]*?)<\/script>/.exec(html);
if (!script) throw new Error("no inline script found in dist/quiz.html");
new Function(script[1])();

const $ = id => document.getElementById(id);
let failures = 0;
const assert = (cond, msg) => {
  if (!cond) { console.error("FAIL:", msg); failures++; } else console.log("ok:", msg);
};

const bank = JSON.parse(fs.readFileSync("dist/questions.json", "utf8"));
const total = bank.domains.reduce((s, d) => s + d.questions.length, 0);
const multiCount = bank.domains.reduce((s, d) => s + d.questions.filter(q => q.answers.length > 1).length, 0);

assert($("bankCount").textContent === String(total), "bank count rendered = " + total);
assert(globalThis.localStorage.store["sp701_pbq_v1"] === undefined, "pbq notes empty at start");
assert($("pbqList").innerHTML.includes("PBQ 1"), "PBQ cards rendered");
assert($("pbqList").innerHTML.includes("Lihat jawaban model"), "PBQ reveal buttons rendered");

// theme toggle
document.getElementById("themeBtn").click();
assert(document.documentElement.dataset.theme === "light", "theme toggles to light");

// tabs
tabs.find(t => t.dataset.tab === "stats").click();
assert($("statsBody").innerHTML.includes("Penguasaan per domain"), "stats tab renders");
tabs.find(t => t.dataset.tab === "practice").click();

// objective select built
assert($("objSelect").innerHTML.includes("1.1"), "objective select populated");

// practice session
modes.find(m => m.dataset.mode === "quick").click();
assert(!$("quiz").className.includes("hide"), "quick mode opens quiz");
assert($("counter").textContent === "1 / 25", "quick mode has 25 questions");
assert($("opts").children.length >= 4, "options rendered");

const answerCurrent = () => {
  const q = null;
  const check = $("checkBtn");
  const checkVisible = !check.classList.contains("hide");
  const opts = $("opts").children;
  if (checkVisible) {
    opts[0] && opts[0].click();
    opts[1] && opts[1].click();
    check.click();
  } else if (opts.length) {
    opts[0].click();
  }
};

answerCurrent();
assert($("fb").classList.contains("show"), "feedback shown after answering");
assert(!$("opts").innerHTML.includes("undefined"), "no undefined in options");
if ($("fb").innerHTML.includes("Belum tepat")) {
  assert($("fb").innerHTML.includes("Jawaban benar"), "wrong answer shows correct answer");
}
assert($("fb").innerHTML.includes("<strong>"), "feedback renders bold markdown");
assert(!$("fb").innerHTML.includes("**"), "feedback has no raw markdown stars");

// finish the 25-question session
for (let i = 0; i < 40; i++) {
  if (!$("modal").classList.contains("hide")) { $("modalSubmit").click(); break; }
  if (!$("quiz").classList.contains("hide")) {
    const opts = $("opts").children;
    const check = $("checkBtn");
    if (!check.classList.contains("hide")) {
      opts[0] && opts[0].click();
      opts[1] && opts[1].click();
      check.click();
    } else if (opts.length && !opts[0].disabled && !$("opts").innerHTML.includes('class="opt sel"')) {
      opts[0].click();
    }
    $("nextBtn").click();
  } else break;
}
assert($("result").className.includes("hide") === false, "result screen shown");
const ok = +$("kOk").textContent, bad = +$("kBad").textContent, skip = +$("kSkip").textContent;
assert(ok + bad + skip === 25, "result counts add up to 25");
const scaled = +$("scoreNum").textContent;
assert(scaled >= 100 && scaled <= 900, "scaled score within 100-900 (" + scaled + ")");
assert($("review").innerHTML.includes("Pembahasan") || $("review").innerHTML.includes("Tidak ada soal"), "review rendered");

// multi-select flow via objective drill (1.1 contains a multi-select item)
$("homeBtn").click();
$("objSelect").value = "1.1";
$("objStart").click();
let sawMulti = false;
for (let i = 0; i < 10; i++) {
  if ($("hint").textContent.includes("Pilih")) {
    sawMulti = true;
    const opts = $("opts").children;
    opts[0].click();
    opts[1].click();
    assert(!$("checkBtn").classList.contains("hide"), "multi-select shows check button");
    $("checkBtn").click();
    assert($("fb").classList.contains("show"), "multi-select feedback shown");
    assert($("fb").innerHTML.includes("Jawaban benar") || $("fb").innerHTML.includes("Benar"), "multi-select verdict rendered");
    break;
  }
  $("nextBtn").click();
}
assert(sawMulti, "found a multi-select question in objective 1.1");
$("quitBtn").click();

// exam mode: 90 questions, finish without answering
$("homeBtn").click();
modes.find(m => m.dataset.mode === "exam").click();
assert($("counter").textContent === "1 / 90", "exam mode has 90 questions");
for (let i = 0; i < 100; i++) {
  if (!$("modal").classList.contains("hide")) { $("modalSubmit").click(); break; }
  $("nextBtn").click();
}
assert($("quiz").className.includes("hide"), "exam ends");
const eok = +$("kOk").textContent, ebad = +$("kBad").textContent, eskip = +$("kSkip").textContent;
assert(eok + ebad + eskip === 90, "exam counts add up to 90");
assert(eskip === 90, "unanswered exam counts as skipped");

// persistence
const wrong = JSON.parse(globalThis.localStorage.store["sp701_wrong_v1"] || "[]");
assert(Array.isArray(wrong) && wrong.length > 0, "wrong answers persisted (" + wrong.length + ")");
const res = JSON.parse(globalThis.localStorage.store["sp701_results_v1"] || "{}");
assert(Object.keys(res).length > 0, "per-question results persisted (" + Object.keys(res).length + ")");

console.log("multi-select in bank:", multiCount);
console.log(failures ? "SMOKE TEST FAILED: " + failures : "SMOKE TEST DONE");
process.exitCode = failures ? 1 : 0;
