# P04 — The four axes

- **Curriculum ID:** FND-03 — The four axes: method, trigger, target, swap
- **Scale:** Mini-lab
- **Ownership:** `index.html` is student-owned. `server.py`, `README.md`, and `__init__.py` are sensei-owned.

## Goal

Change one axis at a time on the demo button and record the observable difference each change makes.

## Requirements

1. Baseline: click **Probe** and record the method shown, where the fragment lands, and whether `#out` survives.
2. Method axis: change `hx-get` to `hx-post`, click, and record the method shown.
3. Trigger axis: restore GET, change the trigger to `mouseenter`, and record when the request fires.
4. Target axis: restore click, add a second element with a different id, point `hx-target` at it, and record where the fragment lands.
5. Swap axis: restore `#out` as the target, change `hx-swap` to `outerHTML`, and record what disappears from the DOM.
6. Record all four observations.

## Acceptance criteria

- [ ] Baseline: click fires, method is GET, the fragment lands inside `#out`, and `#out` still exists.
- [ ] Method change: the response says POST.
- [ ] Trigger change: hovering fires the request without a click.
- [ ] Target change: the fragment lands in the second element, not `#out`.
- [ ] Swap change: `#out` itself is replaced and no longer exists after the request.
- [ ] All four observations are recorded.

## Run

```bash
uv run uvicorn lab.main:app --reload
```

Open <http://127.0.0.1:8000/p/p04_four_axes/>.

## Constraints

- Use only the method, trigger, target, and swap attributes shown; no bespoke JavaScript.
- Do not change `server.py`.

## Attempt rule

Attempt the lab first. Ask for a hint only after a real attempt.
