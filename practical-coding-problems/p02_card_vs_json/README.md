# P02 — Card vs JSON record

- **Curriculum ID:** FND-01 variant — Hypermedia mental model: the server returns HTML fragments, not JSON
- **Scale:** Observation lab
- **Ownership:** `index.html` is student-owned. `server.py`, `README.md`, and `__init__.py` are sensei-owned.

## Goal

Send an HTML `card` and a JSON `record` into the same target and compare the rendered result.

## Requirements

1. In `index.html`, add a button that requests `card` into `#result`.
2. Add a second button that requests `record` into the same `#result`.
3. Click both and inspect each response's `Content-Type` in the Network panel.
4. Record what `#result` displays after each click.

## Acceptance criteria

- [ ] Both buttons target `#result`; no other target id is used.
- [ ] The `card` request renders as an `<article>` inside `#result`.
- [ ] The `record` request shows the JSON text literally inside `#result`.
- [ ] The Network panel shows `text/html` for `card` and `application/json` for `record`.

## Run

```bash
uv run uvicorn lab.main:app --reload
```

Open <http://127.0.0.1:8000/p/p02_card_vs_json/>.

## Constraints

- No bespoke JavaScript and no `hx-on`; use htmx attributes only.
- Both requests must use the same existing `#result` element as the target.
- Do not change `server.py`.

## Attempt rule

Attempt the lab first. Ask for a hint only after a real attempt.
