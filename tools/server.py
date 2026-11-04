#!/usr/bin/env python3
"""Local SQLite-backed history server for the Security+ quiz.

Usage:
    python tools/server.py [--port 8000]
    open http://127.0.0.1:8000

The page still works by double-clicking dist/quiz.html (browser storage).
When served from this server it detects /api/health and mirrors history into
data/history.db so the data survives browser cleanup and is shared across
browsers on the same machine.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
DB = ROOT / "data" / "history.db"
MAX_SESSIONS = 200


def connect() -> sqlite3.Connection:
    DB.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB, timeout=5)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS sessions (
            ts INTEGER PRIMARY KEY,
            mode TEXT,
            total INTEGER,
            ok INTEGER,
            scaled INTEGER,
            secs INTEGER,
            payload TEXT NOT NULL,
            created_at TEXT NOT NULL
        )"""
    )
    conn.commit()
    return conn


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIST), **kwargs)

    def log_message(self, fmt, *args):  # keep the console quiet
        pass

    def _json(self, obj, status: int = 200) -> None:
        data = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path == "/api/health":
            return self._json({"ok": True, "db": str(DB.relative_to(ROOT))})
        if path == "/api/history":
            conn = connect()
            try:
                rows = conn.execute(
                    "SELECT payload FROM sessions ORDER BY ts DESC LIMIT ?", (MAX_SESSIONS,)
                ).fetchall()
            finally:
                conn.close()
            sessions = []
            for (payload,) in rows:
                try:
                    sessions.append(json.loads(payload))
                except json.JSONDecodeError:
                    continue
            sessions.reverse()
            return self._json({"sessions": sessions})
        if path == "/":
            self.send_response(302)
            self.send_header("Location", "/quiz.html")
            self.end_headers()
            return
        return super().do_GET()

    def do_POST(self) -> None:
        if urlparse(self.path).path != "/api/history":
            return self._json({"error": "not found"}, 404)
        try:
            length = int(self.headers.get("Content-Length", "0"))
            rec = json.loads(self.rfile.read(length) or b"{}")
            ts = int(rec["ts"])
        except (ValueError, KeyError, json.JSONDecodeError):
            return self._json({"error": "invalid payload"}, 400)
        conn = connect()
        try:
            conn.execute(
                """INSERT INTO sessions (ts, mode, total, ok, scaled, secs, payload, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                   ON CONFLICT(ts) DO UPDATE SET
                     mode=excluded.mode, total=excluded.total, ok=excluded.ok,
                     scaled=excluded.scaled, secs=excluded.secs, payload=excluded.payload""",
                (
                    ts,
                    str(rec.get("mode", "")),
                    int(rec.get("total", 0)),
                    int(rec.get("ok", 0)),
                    int(rec.get("scaled", 0)),
                    int(rec.get("secs", 0) or 0),
                    json.dumps(rec, ensure_ascii=False),
                    datetime.now(timezone.utc).isoformat(),
                ),
            )
            conn.commit()
        finally:
            conn.close()
        return self._json({"ok": True})

    def do_DELETE(self) -> None:
        if urlparse(self.path).path != "/api/history":
            return self._json({"error": "not found"}, 404)
        conn = connect()
        try:
            conn.execute("DELETE FROM sessions")
            conn.commit()
        finally:
            conn.close()
        return self._json({"ok": True})


def main() -> None:
    parser = argparse.ArgumentParser(description="Security+ quiz history server")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--host", default="127.0.0.1")
    args = parser.parse_args()

    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Serving {DIST} on http://{args.host}:{args.port}")
    print(f"SQLite database: {DB}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
