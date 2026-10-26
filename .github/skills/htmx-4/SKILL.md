---
name: htmx-4
description: "Use when: building, extending, or debugging an htmx 4 front-end — writing hx- attributes, choosing triggers/swaps/targeting, wiring out-of-band or partial updates, handling htmx events and headers, configuring htmx, adding extensions, migrating htmx 2.x code, or answering any htmx 4 question. Triggers: 'htmx', 'hx-get', 'hx-post', 'hx-trigger', 'hx-swap', 'hx-target', 'hx-boost', 'hx-partial', 'hypermedia', 'AJAX without JavaScript', 'htmx 4'."
---

# HTMX 4 Application Development

Build htmx 4 front-ends the way the library intends: server returns **HTML fragments**, the client swaps them into the DOM. Everything in this skill is version-4 specific.

## Non-Negotiable Mental Model

- htmx expects **HTML** from the server, **not JSON**. (`docs.md` → "installing htmx expects HTML")
- Attributes start with `hx-`. A second prefix `data-hx-` is active by default (`htmx.config.prefix`).
- Four axes control every request: **method** (`hx-get`/`hx-post`/…), **trigger** (`hx-trigger`), **target** (`hx-target`), **swap strategy** (`hx-swap`).
- Attribute inheritance is **explicit** in v4 — use the `:inherited` modifier. In v2 it was implicit.
- `hx-swap` adds built-in **`innerMorph`** / **`outerMorph`** in v4 (no Idiomorph extension needed). Targeting and swap options live in [hx-target](./references/reference/attributes/hx-target.md) and [hx-swap](./references/reference/attributes/hx-swap.md).
- This is **version 4**. Do not apply htmx 2.x habits without checking [whats-new-in-htmx-4](./references/docs/whats-new-in-htmx-4.md) and [the migration guide](./references/docs/extension-htmx-4-migration-guide.md).

## Version 4 Breaking Changes (memorize these)

| Change                | v2 behavior                     | v4 behavior                   | How to restore v2                               |
| --------------------- | ------------------------------- | ----------------------------- | ----------------------------------------------- |
| Attribute inheritance | implicit                        | **explicit** via `:inherited` | `htmx.config.implicitInheritance = true`        |
| `400`/`500` responses | not swapped                     | **swapped**                   | `htmx.config.noSwap = [204, 304, '4xx', '5xx']` |
| History restore       | local `sessionStorage` snapshot | full server request           | `hx-history-cache` extension                    |

See [whats-new-in-htmx-4](./references/docs/whats-new-in-htmx-4.md). To port large codebases: `npx htmx.org@4.0.0 upgrade-check -- ./project`.

## Workflow

1. **Find the page** in the map below; read the local file. Everything is offline.
2. **Server-first**: decide which HTML fragment the server returns. htmx expects HTML, not JSON.
3. **Compose the four axes**: method (`hx-get`/`hx-post`/…), trigger (`hx-trigger`), target (`hx-target`), swap (`hx-swap`).
4. **Multiple regions in one response**: `hx-swap-oob` (by id) or `<hx-partial>` (arbitrary content).
5. **Harden**: escape untrusted content; CSP via `hx-csp`; CSRF via `hx-headers:inherited` on `<body>`.
6. **Debug**: `htmx.config.logAll = true`, or `monitorEvents(htmx.find("#el"))`.

## Where to Look (mirror map)

Every path is inside this skill folder and works offline.

| Need                                                                                     | Read                                                                                                                                                                                             |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| The full narrative manual (one file)                                                     | [references/docs.md](./references/docs.md)                                                                                                                                                       |
| Installing htmx (CDN, ESM, npm, vendoring, htmax)                                        | [references/docs.md](./references/docs.md)                                                                                                                                                       |
| What changed in v4 / migration from 2.x                                                  | [references/docs/whats-new-in-htmx-4.md](./references/docs/whats-new-in-htmx-4.md), [references/docs/extension-htmx-4-migration-guide.md](./references/docs/extension-htmx-4-migration-guide.md) |
| Every `hx-*` attribute (36)                                                              | [references/reference/attributes/](./references/reference/attributes/)                                                                                                                           |
| Every request/response header (16)                                                       | [references/reference/headers/](./references/reference/headers/)                                                                                                                                 |
| Every `htmx:*` event (30)                                                                | [references/reference/events/](./references/reference/events/)                                                                                                                                   |
| Global config (24)                                                                       | [references/reference/config/](./references/reference/config/)                                                                                                                                   |
| JS API (`htmx.ajax`, `htmx.swap`, …)                                                     | [references/reference/methods/](./references/reference/methods/)                                                                                                                                 |
| `<hx-partial>` tag                                                                       | [references/reference/tags/hx-partial.md](./references/reference/tags/hx-partial.md)                                                                                                             |
| Recipes (search, dialogs, infinite scroll, file upload…)                                 | [references/patterns/](./references/patterns/)                                                                                                                                                   |
| Bundled extensions (SSE, WS, preload, CSP…)                                              | [references/extensions/](./references/extensions/)                                                                                                                                               |
| Deep dives: events, morphing, `hx-live`, extension authoring, HCON, quirks, editor setup | [references/docs/](./references/docs/)                                                                                                                                                           |
| Index of every page with a description                                                   | [references/llms.txt](./references/llms.txt)                                                                                                                                                     |
| The list of pages the mirror covers                                                      | [references/SOURCES.txt](./references/SOURCES.txt)                                                                                                                                               |

## Hard Rules

- **Escape all user content.** Never inject untrusted HTML; wrap untrusted regions in `hx-ignore` if you must.
- **Prefer `hx-*` over bespoke JavaScript.** Reach for `hx-on:*`, Alpine, or `hx-live` only when attributes fall short.
- **Check v4 defaults** before copying snippets from the web — most htmx examples target 2.x.
- **Pair with the `frontend` skill.** This skill owns *architecture and coding*; `frontend` owns *look and feel* (design tokens, motion, icons, layout). Load both when building UI.

## Project Architecture (project-tango-november)

This skill defines *how* the frontend talks to the backend. The *shape* of the endpoints in this repo:

- Templates live under `app/htmx/templates/` and `app/htmx/pages/`; static assets under `app/htmx/static/`.
- Endpoints live under `app/api/v1/`. Respond with **HTML fragments** for htmx requests.
- Templates never import Python — everything crosses the HTTP boundary → API layer → service layer.
- HTML fragments and JSON payloads can coexist on the same API layer: HTML for htmx-driven UI, JSON for non-UI consumers (MCP server, agentic RAG, integrations).

## Fetching a Page That Isn't Here

Everything under `references/` is already a mirror of `four.htmx.org/docs`, so normally you just read the local file. Only if a page is genuinely absent or stale:

```bash
# from .github/skills/htmx-4/
bash scripts/fetch_docs.sh /reference/attributes/hx-swap   # one page
bash scripts/fetch_docs.sh                                 # refresh everything
```

Fetch it, **then** read the local copy — don't answer from an ad-hoc web fetch. The next reader gets the local file for free. This requires terminal access; if you don't have it, say the page isn't cached locally rather than answering from an uncached web fetch.
