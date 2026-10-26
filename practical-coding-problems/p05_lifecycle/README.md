# P05 — Request lifecycle

- **Curriculum ID:** FND-04 — Request lifecycle: request, response, swap, settle, cleanup
- **Scale:** Observation lab
- **Ownership:** `index.html` is student-owned. `server.py`, `README.md`, and `__init__.py` are sensei-owned.

## Goal

Capture one request's event order with `htmx.config.logAll` and map the events to the request, response, swap, settle, and cleanup phases.

## Requirements

1. Open the page and the DevTools console.
2. Run `htmx.config.logAll = true` in the console.
3. Clear the console, then click **Start request** exactly once.
4. Capture the event order from the console output.
5. Map each phase to at least one event name and note where the `finally` events fire.

## Acceptance criteria

- [ ] `logAll` output captured for exactly one request.
- [ ] Request phase identified: `htmx:config:request`, `htmx:before:request`, `htmx:before:response`, `htmx:after:request`.
- [ ] Swap phase identified: `htmx:before:swap`, `htmx:after:swap`.
- [ ] Settle phase identified: `htmx:before:settle`, `htmx:after:settle`.
- [ ] Cleanup phase identified: `htmx:before:cleanup`, `htmx:after:cleanup`.
- [ ] Finalization identified: `htmx:finally:request`, `htmx:finally:swap`.

## Run

```bash
uv run uvicorn lab.main:app --reload
```

Open <http://127.0.0.1:8000/p/p05_lifecycle/>.

## Constraints

- Do not add JavaScript to the page; use the console only to enable `logAll`.
- Do not change `server.py`.

## Attempt rule

Attempt the lab first. Ask for a hint only after a real attempt.
