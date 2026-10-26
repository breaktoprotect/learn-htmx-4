# P01 — HTML fragment vs JSON payload

- **Curriculum ID:** FND-01 — Hypermedia mental model: the server returns HTML fragments, not JSON
- **Scale:** Observation lab
- **Ownership:** `index.html` is student-owned. `server.py`, `README.md`, and `__init__.py` are sensei-owned.

## Goal

Send two requests through htmx into the same target — one that returns an HTML fragment and one that returns JSON — and observe the difference between rendered HTML and literal JSON text.

## Requirements

1. In `index.html`, add one button that requests `fragment` into `#output` using htmx attributes only.
2. Add a second button that requests `payload` into the same `#output`.
3. Click both and inspect the Network panel for each response's `Content-Type`.
4. Record what `#output` displays after each click.

## Acceptance criteria

- [ ] The fragment request renders as HTML inside `#output`.
- [ ] The payload request shows the JSON text literally inside `#output`.
- [ ] The Network panel shows `text/html` for `fragment` and `application/json` for `payload`.

## Run

```bash
uv run uvicorn lab.main:app --reload
```

Open <http://127.0.0.1:8000/p/p01_fragments_vs_json/>.

## Constraints

- No bespoke JavaScript and no `hx-on`; use htmx attributes only.
- Do not change `server.py`.

## Attempt rule

Attempt the lab first. Ask for a hint only after a real attempt.
