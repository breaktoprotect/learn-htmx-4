# P03 — Installing htmx 4

- **Curriculum ID:** FND-02 — Installing htmx 4: CDN, ESM, npm, vendoring, htmax bundle
- **Scale:** Mini-lab
- **Ownership:** `index.html` is student-owned. `server.py`, `README.md`, and `__init__.py` are sensei-owned.

## Goal

Load htmx 4 from the documented CDN, confirm the loaded version, issue one request, and inspect the `HX-Request` request header.

## Requirements

1. Add the htmx 4 CDN script tag from the local docs to `<head>`.
2. Add a button that requests `ping` into `#status`.
3. Open the DevTools console, evaluate `htmx.version`, and record the value.
4. Click the button, inspect the `ping` request in the Network panel, and record the `HX-Request` request header.

## Acceptance criteria

- [ ] `htmx.version` reports `4.0.0`.
- [ ] Clicking the button swaps `<p class="ping">pong — htmx issued this request</p>` into `#status`.
- [ ] The `ping` request carries `HX-Request: true`.
- [ ] You can name the install route you used and one production alternative.

## Run

```bash
uv run uvicorn lab.main:app --reload
```

Open <http://127.0.0.1:8000/p/p03_install_htmx/>.

## Constraints

- Install htmx with the documented CDN tag; do not hand-copy library code.
- Do not change `server.py`.

## Attempt rule

Attempt the lab first. Ask for a hint only after a real attempt.
