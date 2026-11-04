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
const modes = ["exam", "domain", "quick", "wrong"].map(m => { const e = new El("button"); e.dataset.mode = m; return e; });
const tabs = ["practice", "pbq", "stats", "guide"].map(t => { const e = new El("button"); e.dataset.tab = t; return e; });

const document = {
  documentElement: { dataset: { theme: "dark" } },
  getElementById: id => {
    if (!els.has(id)) els.set(id, new El("div", id));
    return els.get(id);
  },
  querySelectorAll: sel => (sel === ".mode" ? modes : sel === ".tab" ? tabs : []),
  addEventListener() {},
};

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
assert($("pbqList").innerHTML.includes("PBQ 1"), "PBQ cards rendered");
assert($("pbqList").innerHTML.includes("Paham"), "PBQ self-assessment rendered");

// theme
document.getElementById("themeBtn").click();
assert(document.documentElement.dataset.theme === "light", "theme toggles to light");

// tabs
tabs.find(t => t.dataset.tab === "stats").click();
assert($("statsBody").innerHTML.includes("Penguasaan per domain"), "stats tab renders");
tabs.find(t => t.dataset.tab === "guide").click();
assert(html.includes("Multi-select (checkbox)") && html.includes("Cara skor dihitung"), "guide tab content present");
tabs.find(t => t.dataset.tab === "practice").click();
assert($("objSelect").innerHTML.includes("1.1"), "objective select populated");

// start quick session
modes.find(m => m.dataset.mode === "quick").click();
assert(!$("quiz").className.includes("hide"), "quick mode opens quiz");
assert($("counter").textContent === "1 / 25", "quick mode has 25 questions");
assert($("opts").children.length >= 4, "options rendered");

// answering shows no correctness and can be changed
const opts = $("opts").children;
opts[0].click();
assert(opts[0].classList.contains("sel"), "first option selected");
assert(!$("fb").classList.contains("show"), "no feedback during session");
assert($("grid").children[0].classList.contains("done"), "answered question marked on grid");
assert($("liveScore").textContent.includes("Terjawab"), "live answered counter shown");
opts[1].click();
assert($("opts").children[1].classList.contains("sel"), "answer can be changed");
assert(!$("opts").children[0].classList.contains("sel"), "old answer deselected");
assert(!$("opts").innerHTML.includes("undefined"), "no undefined in options");

// flag blocks submit
$("flagBtn").click();
assert($("grid").children[0].classList.contains("flag"), "flagged question marked yellow");
$("grid").children[24].click();
$("nextBtn").click();
assert(!$("modal").classList.contains("hide"), "finish modal opens");
assert($("modalSubmit").classList.contains("hide"), "submit blocked while flagged");
assert(!$("modalClear").classList.contains("hide"), "clear-flags button shown");
$("modalClear").click();
assert(!$("grid").children[0].classList.contains("flag"), "flags cleared");
assert(!$("modalSubmit").classList.contains("hide"), "submit allowed after clearing flags");
$("modalSubmit").click();

assert(!$("result").className.includes("hide"), "result screen shown");
const ok = +$("kOk").textContent, bad = +$("kBad").textContent, skip = +$("kSkip").textContent;
assert(ok + bad + skip === 25, "result counts add up to 25");
const scaled = +$("scoreNum").textContent;
assert(scaled >= 100 && scaled <= 900, "scaled score within 100-900 (" + scaled + ")");
assert($("review").innerHTML.includes("Pembahasan semua soal"), "review shows all questions");
assert($("review").innerHTML.includes("<strong>"), "review renders bold markdown");
assert($("review").innerHTML.includes('id="rev-0"'), "review items have ids for answer map");
assert($("resultMap").children.length === 25, "result map has 25 dots");
assert($("resultMap").children.some(d => d.classList.contains("ok") || d.classList.contains("no")), "result map shows correctness");
assert(html.includes('class="qnav"') && html.includes("flagbtn"), "question nav uses centered flag layout");

// history detail can be reopened
const openBtns = $("histBody").querySelectorAll(".history-open");
assert(openBtns.length === 1, "history entry has review button");
openBtns[0].click();
assert(!$("result").className.includes("hide"), "history review opens result screen");
assert($("review").innerHTML.includes("Pembahasan semua soal"), "history review shows explanations");
const histCount = JSON.parse(globalThis.localStorage.store["sp701_history_v1"]).length;
assert(histCount === 1, "opening history does not add a session (" + histCount + ")");

// multi-select flow via objective drill
$("homeBtn").click();
$("objSelect").value = "1.1";
$("objStart").click();
let sawMulti = false;
for (let i = 0; i < 10; i++) {
  if ($("hint").textContent.includes("Pilih")) {
    sawMulti = true;
    const o = $("opts").children;
    o[0].click();
    o[1].click();
    assert(o[0].classList.contains("sel") && o[1].classList.contains("sel"), "multi-select toggles two options");
    assert(!$("fb").classList.contains("show"), "multi-select hides feedback during session");
    assert($("liveScore").textContent.includes("Terjawab"), "multi-select updates answered count");
    break;
  }
  $("nextBtn").click();
}
assert(sawMulti, "found a multi-select question in objective 1.1");
$("quitBtn").click();

// exam mode: 90 questions, finish without answering
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
assert(Array.isArray(wrong), "wrong list stored");
const res = JSON.parse(globalThis.localStorage.store["sp701_results_v1"] || "{}");
assert(Object.keys(res).length > 0, "per-question results persisted (" + Object.keys(res).length + ")");

console.log("multi-select in bank:", multiCount);
console.log(failures ? "SMOKE TEST FAILED: " + failures : "SMOKE TEST DONE");
process.exitCode = failures ? 1 : 0;
