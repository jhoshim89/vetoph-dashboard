#!/usr/bin/env python3
"""No-cache static server for the VetOph dashboard."""
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class NoCacheHandler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".md": "text/plain; charset=utf-8",
        ".markdown": "text/plain; charset=utf-8",
        ".txt": "text/plain; charset=utf-8",
        ".json": "application/json; charset=utf-8",
    }

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8888
    os.chdir(ROOT)
    print(f"[serve] no-cache server on 0.0.0.0:{port} (root={ROOT})")
    ThreadingHTTPServer(("0.0.0.0", port), NoCacheHandler).serve_forever()
