// Minimal DOM harness to smoke-test the quiz logic in Node (no browser available).
import fs from "node:fs";

class El {
  constructor(tag = "div", id = "") {
    this.tag = tag; this.id = id;
    this._classes = new Set(); this.dataset = {}; this.children = [];
    this._listeners = {}; this._html = ""; this._text = ""; this.disabled = false;
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

const ids = ["bankCount", "wrongTag", "histBody", "home", "quiz", "result", "modeLabel", "timer", "counter",
  "pbar", "qDomain", "qObjective", "qType", "stem", "opts", "fb", "prevBtn", "nextBtn", "flagBtn", "grid",
  "scoreRing", "scoreNum", "resTitle", "resSub", "resPill", "kOk", "kBad", "kSkip", "kTime", "domres",
  "review", "retryWrongBtn", "domlist", "quitBtn", "homeBtn", "againBtn"];
const els = new Map(ids.map(id => [id, new El("div", id)]));
const modes = ["exam", "domain", "quick", "wrong"].map(m => { const e = new El("button"); e.dataset.mode = m; return e; });

const document = {
  getElementById: id => els.get(id) || null,
  querySelectorAll: sel => (sel === ".mode" ? modes : []),
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

const $ = id => els.get(id);
const assert = (cond, msg) => { if (!cond) { console.error("FAIL:", msg); process.exitCode = 1; } else console.log("ok:", msg); };

const expected = JSON.parse(fs.readFileSync("dist/questions.json", "utf8")).domains
  .reduce((sum, d) => sum + d.questions.length, 0);
assert($("bankCount").textContent === String(expected), "bank count rendered = " + expected);

// -- practice / quick mode --
modes.find(m => m.dataset.mode === "quick").click();
assert($("quiz").className.includes("hide") === false, "quick mode opens quiz screen");
assert($("counter").textContent === "1 / 25", "quick mode has 25 questions");
const opts = $("opts").children;
assert(opts.length === 4, "question renders 4 options");
assert(opts.every(o => o._text.includes(".") || o._text.length > 1), "options have text");
assert(!$("opts")._html.includes("undefined"), "no undefined rendered in options");
assert(!$("stem")._text.includes("undefined"), "stem has text");
opts[0].click();
assert($("fb").classList.contains("show"), "feedback shown after answering in practice mode");
const fbHtml = $("fb")._html;
assert(fbHtml.includes("Benar") || fbHtml.includes("Belum tepat"), "feedback shows a verdict");
assert(!fbHtml.includes("undefined"), "feedback has no undefined values");
if (fbHtml.includes("Belum tepat")) {
  assert(fbHtml.includes("Jawaban benar"), "feedback reveals correct answer when wrong");
}
assert($("opts").children[0].disabled === true, "options locked after answering");

// answer every question then finish
for (let i = 0; i < 25; i++) {
  const o = $("opts").children;
  if (o.length && !o[0].disabled) o[0].click();
  $("nextBtn").click();
}
assert($("quiz").className.includes("hide"), "quiz screen hidden after finishing");
assert($("result").className.includes("hide") === false, "result screen shown");
const ok = +$("kOk").textContent, bad = +$("kBad").textContent, skip = +$("kSkip").textContent;
assert(ok + bad + skip === 25, "result counts add up to 25");
const scaled = +$("scoreNum").textContent;
assert(scaled >= 100 && scaled <= 900, "scaled score within 100-900 (" + scaled + ")");
assert($("review")._html.includes("Pembahasan soal yang belum benar"), "review section rendered");

// -- exam mode --
modes.find(m => m.dataset.mode === "exam").click();
assert($("counter").textContent === "1 / 90", "exam mode has 90 questions");
let guard = 0;
while (!$("quiz").className.includes("hide") && guard++ < 120) {
  $("nextBtn").click();
}
assert($("quiz").className.includes("hide"), "exam ends");
const eok = +$("kOk").textContent, ebad = +$("kBad").textContent, eskip = +$("kSkip").textContent;
assert(eok + ebad + eskip === 90, "exam counts add up to 90");
assert(eskip === 90, "unanswered exam counts as skipped");

// -- wrong retry bank persisted --
const wrong = JSON.parse(globalThis.localStorage.store["sp701_wrong_v1"] || "[]");
assert(Array.isArray(wrong) && wrong.length > 0, "wrong answers persisted (" + wrong.length + ")");

console.log("SMOKE TEST DONE");
