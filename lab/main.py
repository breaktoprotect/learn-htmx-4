"""One shared FastAPI server for every practical problem.

Every folder under ``practical-coding-problems/`` that contains ``server.py``
is imported as a package and mounted at ``/p/<folder>``. The problem's
``server.py`` serves its own ``index.html`` at the sub-app root, so relative
URLs such as ``hx-get="fragment"`` resolve against the problem base.
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "practical-coding-problems"

app = FastAPI(title="htmx 4 Sensei Lab")


def _discover() -> list[str]:
    """Import every problem package and mount its FastAPI sub-app."""
    if not PROBLEMS_DIR.is_dir():
        return []

    problems_path = str(PROBLEMS_DIR)
    if problems_path not in sys.path:
        sys.path.insert(0, problems_path)

    mounted: list[str] = []
    for folder in sorted(p for p in PROBLEMS_DIR.iterdir() if p.is_dir()):
        if not (folder / "server.py").is_file():
            continue
        module = importlib.import_module(f"{folder.name}.server")
        sub_app = getattr(module, "app", None)
        if sub_app is None:
            continue
        app.mount(f"/p/{folder.name}", sub_app, name=f"p_{folder.name}")
        mounted.append(folder.name)
    return mounted


MOUNTED = _discover()


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    links = "\n".join(
        f'<li><a href="/p/{name}/">{name.replace("_", " ")}</a></li>'
        for name in MOUNTED
    )
    if not links:
        links = "<li>No problems scaffolded yet. Start a session with HTMX Sensei.</li>"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>htmx 4 Sensei Lab</title>
</head>
<body>
  <h1>htmx 4 Sensei Lab</h1>
  <ul>{links}</ul>
  <p>Curriculum: <code>docs/htmx-4-learning-tracker.md</code></p>
</body>
</html>"""


@app.get("/health")
def health() -> dict[str, str | int]:
    return {"status": "ok", "problems": len(MOUNTED)}
