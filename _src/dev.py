#!/usr/bin/env python3
"""
Live editing server for the WEL website.

    python _src/dev.py

Opens http://localhost:8000, watches _src/ and assets/, rebuilds the site the
moment you save a file, and refreshes the browser by itself.  Your scroll
position is kept.  If a build fails, the error appears as a red banner in the
browser instead of a broken page.

Stop it with Ctrl+C.  Nothing here affects the published site - it only injects
the reload script into pages it serves live.
"""
import os
import subprocess
import sys
import threading
import time
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BUILD = os.path.join(HERE, "build.py")
PORT = int(os.environ.get("WEL_PORT", "8000"))

# Files and folders that should trigger a rebuild when they change.
WATCH_DIRS = [HERE, os.path.join(ROOT, "assets", "css"), os.path.join(ROOT, "assets", "js")]
WATCH_EXTS = (".py", ".json", ".css", ".js")

state = {"version": 0, "error": "", "building": False}

RELOAD_JS = """
<script>
(function () {
  var known = null, banner = null;
  function showBanner(msg) {
    if (!banner) {
      banner = document.createElement('pre');
      banner.style.cssText = 'position:fixed;left:0;right:0;bottom:0;z-index:99999;margin:0;' +
        'max-height:45vh;overflow:auto;background:#7f1020;color:#ffe9ec;padding:14px 18px;' +
        'font:12px/1.5 ui-monospace,Consolas,monospace;white-space:pre-wrap;' +
        'box-shadow:0 -6px 24px rgba(0,0,0,.35);border-top:3px solid #ff5566';
      document.body.appendChild(banner);
    }
    banner.textContent = 'Build failed - the page below is the last good version.\\n\\n' + msg;
  }
  function clearBanner() { if (banner) { banner.remove(); banner = null; } }
  if (sessionStorage.getItem('welScrollY')) {
    window.addEventListener('load', function () {
      window.scrollTo(0, parseInt(sessionStorage.getItem('welScrollY'), 10) || 0);
      sessionStorage.removeItem('welScrollY');
    });
  }
  setInterval(function () {
    fetch('/__reload', { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (d) {
      if (d.error) { showBanner(d.error); return; }
      clearBanner();
      if (known === null) { known = d.version; return; }
      if (d.version !== known) {
        sessionStorage.setItem('welScrollY', String(window.scrollY));
        location.reload();
      }
    }).catch(function () {});
  }, 500);
})();
</script>
"""


def snapshot():
    """mtime of every watched file, so we can tell when something changed."""
    stamps = {}
    for d in WATCH_DIRS:
        if not os.path.isdir(d):
            continue
        for name in os.listdir(d):
            if name.endswith(WATCH_EXTS):
                path = os.path.join(d, name)
                try:
                    stamps[path] = os.path.getmtime(path)
                except OSError:
                    pass
    return stamps


def rebuild(reason=""):
    state["building"] = True
    started = time.time()
    proc = subprocess.run([sys.executable, BUILD], cwd=ROOT,
                          capture_output=True, text=True)
    state["building"] = False
    if proc.returncode != 0:
        state["error"] = (proc.stderr or proc.stdout).strip()[-4000:]
        print("\n  BUILD FAILED %s\n%s\n" % (reason, state["error"]))
        return
    state["error"] = ""
    state["version"] += 1
    tail = [l for l in proc.stdout.splitlines() if l.strip()]
    warn = "" if "All internal links resolve." in proc.stdout else "  (check link warnings)"
    print("  rebuilt in %.1fs %s%s" % (time.time() - started, reason, warn))
    if warn:
        for line in tail[-6:]:
            if "->" in line:
                print("   ", line.strip())


def watcher():
    last = snapshot()
    while True:
        time.sleep(0.4)
        now = snapshot()
        if now != last:
            changed = [os.path.basename(p) for p in now
                       if p not in last or last.get(p) != now[p]]
            last = now
            time.sleep(0.15)          # let the editor finish writing
            rebuild("(%s)" % ", ".join(sorted(set(changed))[:3]))


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def log_message(self, fmt, *args):
        pass                          # keep the console focused on builds

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()

    def do_GET(self):
        if self.path.startswith("/__reload"):
            import json
            payload = json.dumps({"version": state["version"], "error": state["error"]}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return

        path = self.translate_path(self.path)
        if os.path.isdir(path):
            path = os.path.join(path, "index.html")
        if path.endswith(".html") and os.path.exists(path):
            with open(path, "rb") as fh:
                body = fh.read()
            if b"</body>" in body:
                body = body.replace(b"</body>", RELOAD_JS.encode() + b"</body>", 1)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        super().do_GET()


def main():
    print("\n  Wadhwani Electronics Laboratory - live editing server")
    print("  " + "-" * 52)
    rebuild("(initial)")
    threading.Thread(target=watcher, daemon=True).start()

    url = "http://localhost:%d/" % PORT
    print("  serving   %s" % url)
    print("  watching  _src/*.py, assets/css, assets/js")
    print("  edit a file, save, and the browser refreshes itself")
    print("  Ctrl+C to stop\n")

    if os.environ.get("WEL_OPEN", "1") == "1":
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()

    try:
        ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\n  stopped\n")


if __name__ == "__main__":
    main()
