# htmx 4 Hands-on Lab Map

Every curriculum item is hands-on-first. Use the smallest lab that produces an observable result, then ask the one explanation question. Q&A is the assessment layer; it does not replace the lab when a lab is possible.

## Lab scales

| Scale              | Used for                                                 | Output                                                |
| ------------------ | -------------------------------------------------------- | ----------------------------------------------------- |
| Full lab           | Attributes, composites, patterns, extensions, JS API     | Scaffolded problem under `practical-coding-problems/` |
| Mini-lab           | Concepts, architecture, process, config, headers, events | Guided experiment with an observable result           |
| Observation lab    | Mental models, lifecycle, v4 deltas, debugging           | Network, DOM, or event observation                    |
| Retention artifact | Pure tradeoff or teach-back items                        | Diagram, decision note, or live modification          |

## Orientation and architecture labs

| ID     | Scale              | Lab                                                                                                                                             |
| ------ | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| FND-01 | Observation        | Serve one HTML fragment and one JSON payload; observe the HTML swap into the DOM and the JSON failing to render as HTML. Record the difference. |
| FND-02 | Mini-lab           | Bootstrap a page with htmx 4; verify `htmx.version`; issue one request and inspect the `HX-Request` header.                                     |
| FND-03 | Mini-lab           | Change one axis at a time on a demo button: method, trigger, target, swap. Record the observable difference for each.                           |
| FND-04 | Observation        | Enable `htmx.config.logAll`; capture one request's event order and map it to request, response, swap, settle, and cleanup.                      |
| FND-05 | Mini-lab           | Build two endpoints, one returning a full page and one a fragment; consume each and decide which the server should return.                      |
| FND-06 | Mini-lab           | Reproduce three v4 deltas: explicit `:inherited`, 4xx/5xx swapping, OOB order, or removed `queue`. Record the v2 versus v4 behavior.            |
| ARC-01 | Mini-lab           | Build list, detail, and create endpoints returning fragments; wire them into one page and verify each swap.                                     |
| ARC-02 | Mini-lab           | Add `hx-boost` and `hx-push-url` to a two-view page; verify deep links and back/forward.                                                        |
| ARC-03 | Mini-lab           | Attempt an XSS payload through an unescaped fragment, fix it with escaping, add `hx-csp`, and verify the CSRF header.                           |
| ARC-04 | Mini-lab           | Measure request count and latency with and without `hx-preload` and settle delays using the network panel.                                      |
| ARC-05 | Mini-lab           | Write a browser-observable acceptance checklist and one server contract test for an endpoint; run both.                                         |
| ARC-06 | Observation        | Break a request, enable `logAll`, inspect events and headers, and fix the failure.                                                              |
| ARC-07 | Mini-lab           | Run the v4 upgrade-check on a small v2 snippet; fix one reported issue and verify.                                                              |
| ARC-08 | Full lab           | Write a minimal extension with `htmx.registerExtension` and observe its hook firing.                                                            |
| ARC-09 | Mini-lab           | Write HCON values in `hx-swap`, `hx-trigger`, and `hx-config`; compare with equivalent JSON and observe.                                        |
| ARC-10 | Observation        | Reproduce three quirks from `quirks.md`; document each workaround.                                                                              |
| ARC-11 | Full lab           | Build a morph demo with `innerMorph`, `outerMorph`, `hx-morph-skip`, and preserved widget state.                                                |
| ARC-12 | Mini-lab           | Configure editor support for htmx attributes; verify completions and diagnostics on a sample page.                                              |
| ARC-13 | Full lab           | Build the capstone hypermedia app with list, detail, create, search, OOB, history, and one extension.                                           |
| ARC-14 | Retention artifact | Live modification exercise plus oral defense: extend the capstone under observation and explain the request and swap decisions.                 |

## Other item types

- **Attribute, Modifier, Tag, JS API, Extension, Composite** — full lab.
- **Pattern** — full lab.
- **Header, Config, Event** — mini-lab or full lab.
- **Concept** — mini-lab or observation lab.
- **Architecture** — mini-lab or full lab.
- **Process** — mini-lab, observation lab, or retention artifact.

If an item genuinely has no useful lab or retention artifact, the session log must record why the item was assessed by Q&A only.
