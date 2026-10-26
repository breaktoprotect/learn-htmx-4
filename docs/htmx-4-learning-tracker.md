# htmx 4 Curriculum and Learning Tracker

Single source of truth for **HTMX Sensei**. The curriculum is a Kumon ladder: every level must be proven before the next unlocks. Granular features come first; composites come after their parts; architecture and process items come last.

The theory itself is not duplicated here. Every granular feature item maps to at least one local page under `.github/skills/htmx-4/references/`; concepts and composites cite the pages they combine. This file tracks ordering, prerequisites, and progress.

## Current position

- **Current level:** 0 — Orientation
- **Current item:** FND-05 — Server-first fragment design
- **Learned items:** 4 (`passed` + `review-due` + `mastered`)
- **Due reviews:** 0
- **Last session:** s01
- **Last learning update:** 2026-10-24

## Session logs

One file per conversation session under `docs/htmx-4-learning-session-logs/`. The `Session` column in each level table stores the last session that changed the item.

| Session | Date       | Items                          | Log                                                                 |
| ------- | ---------- | ------------------------------ | ------------------------------------------------------------------- |
| s01     | 2026-10-24 | FND-01, FND-02, FND-03, FND-04 | [2026-10-24_s01.md](htmx-4-learning-session-logs/2026-10-24_s01.md) |

## Status legend

| Status        | Meaning                                      |
| ------------- | -------------------------------------------- |
| `not-started` | Never assigned                               |
| `learning`    | Lesson delivered or attempt in progress      |
| `needs-work`  | Failed the gate; re-attempt required         |
| `passed`      | Gate cleared; review scheduled               |
| `review-due`  | Review date reached; still counts as learned |
| `mastered`    | Passed plus three successful spaced reviews  |

## Gate rules

1. Level `N+1` unlocks only when every item in Levels `0..N` is `passed`, `review-due`, or `mastered`.
2. An item is eligible only when every ID in its `Prereqs` column is `passed`, `review-due`, or `mastered`.
3. Coding items pass only on: working artifact, all acceptance criteria met, correct verbal explanation, and no v2-only behavior.
4. Concept, architecture, process, and Q&A items pass only on: a completed hands-on observation, mini-lab, or retention artifact, plus correct core concept and tradeoff.
5. A composite requires every listed component to be visibly exercised.
6. Q&A-only is the exception: the session log must record why no lab or retention artifact was useful.

## Review intervals

| Event         | Status       | Rev       | Next review     |
| ------------- | ------------ | --------- | --------------- |
| Assigned      | `learning`   | unchanged | `—`             |
| Fail          | `needs-work` | `0`       | today + 1 day   |
| Pass          | `passed`     | `0`       | today + 3 days  |
| Review pass 1 | `passed`     | `1`       | today + 7 days  |
| Review pass 2 | `passed`     | `2`       | today + 21 days |
| Review pass 3 | `mastered`   | `3`       | `—`             |
| Review fail   | `needs-work` | `0`       | today + 1 day   |

## Hands-on requirement

Every item is hands-on-first. Use the smallest lab that produces an observable result, then ask the one explanation question. Q&A is the assessment layer; it does not replace the lab when a lab is possible.

Lesson order: **teach → hands-on → one assessment question → persist → advance**. One item is active at a time.

| Scale              | Used for                                                 | Output                                                |
| ------------------ | -------------------------------------------------------- | ----------------------------------------------------- |
| Full lab           | Attributes, composites, patterns, extensions, JS API     | Scaffolded problem under `practical-coding-problems/` |
| Mini-lab           | Concepts, architecture, process, config, headers, events | Guided experiment with an observable result           |
| Observation lab    | Mental models, lifecycle, v4 deltas, debugging           | Network, DOM, or event observation                    |
| Retention artifact | Pure tradeoff or teach-back items                        | Diagram, decision note, or live modification          |

Full per-item labs for orientation and architecture items live in `docs/htmx-4-hands-on-map.md`.

## Level 0 — Orientation

| ID     | Item                                                                                                                                               | Type    | Prereqs        | Status      | Rev | Next review | Session |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------- | ----------- | --- | ----------- | ------- |
| FND-01 | Hypermedia mental model: the server returns HTML fragments, not JSON                                                                               | Concept | —              | passed      | 0   | 2026-10-27  | s01     |
| FND-02 | Installing htmx 4: CDN, ESM, npm, vendoring, htmax bundle                                                                                          | Concept | FND-01         | passed      | 0   | 2026-10-27  | s01     |
| FND-03 | The four axes: method, trigger, target, swap                                                                                                       | Concept | FND-01         | passed      | 0   | 2026-10-27  | s01     |
| FND-04 | Request lifecycle: request, response, swap, settle, cleanup                                                                                        | Concept | FND-03         | passed      | 0   | 2026-10-27  | s01     |
| FND-05 | Server-first fragment design: choosing the HTML the server returns                                                                                 | Concept | FND-01, FND-04 | not-started | 0   | —           | —       |
| FND-06 | htmx 4 versus 2.x: explicit `:inherited`, 4xx/5xx swapping, history restore, OOB swap order after main swap, removed `hx-trigger` `queue` modifier | Concept | FND-03         | not-started | 0   | —           | —       |

## Level 1 — First requests

| ID     | Item                                                                             | Type      | Prereqs                        | Status      | Rev | Next review | Session |
| ------ | -------------------------------------------------------------------------------- | --------- | ------------------------------ | ----------- | --- | ----------- | ------- |
| ATT-01 | `hx-get`: issue a GET request to a URL                                           | Attribute | FND-04                         | not-started | 0   | —           | —       |
| ATT-02 | `hx-post`: issue a POST request to a URL                                         | Attribute | FND-04                         | not-started | 0   | —           | —       |
| ATT-03 | `hx-trigger`: default events and basic trigger selection                         | Attribute | FND-03                         | not-started | 0   | —           | —       |
| ATT-04 | `hx-target`: default target rules (`this`) and CSS selectors                     | Attribute | FND-03                         | not-started | 0   | —           | —       |
| ATT-05 | `hx-swap`: basic styles, including `innerHTML`, `outerHTML`, `beforeend`, `none` | Attribute | FND-03                         | not-started | 0   | —           | —       |
| ATT-06 | `hx-select`: pick only part of the response to swap                              | Attribute | ATT-05                         | not-started | 0   | —           | —       |
| CMP-01 | Button loads a fragment                                                          | Composite | ATT-01, ATT-03, ATT-04, ATT-05 | not-started | 0   | —           | —       |
| CMP-02 | Form submits and swaps the result                                                | Composite | ATT-02, ATT-03, ATT-04, ATT-05 | not-started | 0   | —           | —       |
| CMP-03 | Extract one region from a full-page response                                     | Composite | ATT-01, ATT-06                 | not-started | 0   | —           | —       |
| CMP-04 | Level 1 mastery: server-rendered list app                                        | Composite | CMP-01, CMP-02, CMP-03         | not-started | 0   | —           | —       |

## Level 2 — Methods, triggers, and timing

| ID     | Item                                                                                                                                                     | Type      | Prereqs                                                | Status      | Rev | Next review | Session |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------ | ----------- | --- | ----------- | ------- |
| ATT-07 | `hx-put`: issue a PUT request                                                                                                                            | Attribute | ATT-02                                                 | not-started | 0   | —           | —       |
| ATT-08 | `hx-patch`: issue a PATCH request                                                                                                                        | Attribute | ATT-02                                                 | not-started | 0   | —           | —       |
| ATT-09 | `hx-delete`: issue a DELETE request                                                                                                                      | Attribute | ATT-02                                                 | not-started | 0   | —           | —       |
| ATT-10 | `hx-query`: issue a safe, idempotent QUERY request with a body                                                                                           | Attribute | ATT-02                                                 | not-started | 0   | —           | —       |
| ATT-11 | `hx-action`: URL source with progressive enhancement                                                                                                     | Attribute | ATT-01, ATT-02                                         | not-started | 0   | —           | —       |
| ATT-12 | `hx-method`: choose the method when using `hx-action`                                                                                                    | Attribute | ATT-11                                                 | not-started | 0   | —           | —       |
| MOD-01 | HCON syntax: the `key:value` mini-language used by structured attributes                                                                                 | Modifier  | ATT-03                                                 | not-started | 0   | —           | —       |
| ATT-13 | `hx-trigger` modifiers: `once`, `changed`, `delay:`, `throttle:`, `from:`, `target:`, `prevent`, `stop`/`consume`, `halt`, `capture`, `passive`, filters | Attribute | ATT-03, MOD-01                                         | not-started | 0   | —           | —       |
| ATT-14 | `hx-sync`: synchronize requests between elements; replaces the removed `hx-trigger` `queue` modifier                                                     | Attribute | ATT-13                                                 | not-started | 0   | —           | —       |
| EVT-01 | `load` trigger                                                                                                                                           | Event     | ATT-03                                                 | not-started | 0   | —           | —       |
| EVT-02 | `intersect` trigger                                                                                                                                      | Event     | ATT-03                                                 | not-started | 0   | —           | —       |
| EVT-03 | `every` trigger                                                                                                                                          | Event     | ATT-03                                                 | not-started | 0   | —           | —       |
| EVT-32 | `revealed` trigger: fire when the element scrolls into the viewport (documented in `hx-trigger.md`)                                                      | Event     | ATT-03                                                 | not-started | 0   | —           | —       |
| CMP-05 | Active search with debounce                                                                                                                              | Composite | ATT-01, ATT-13                                         | not-started | 0   | —           | —       |
| CMP-06 | Lazy-load panel on scroll                                                                                                                                | Composite | EVT-02, ATT-01, ATT-04, ATT-05                         | not-started | 0   | —           | —       |
| CMP-07 | Polling widget                                                                                                                                           | Composite | EVT-03, ATT-01, ATT-05                                 | not-started | 0   | —           | —       |
| CMP-08 | Level 2 mastery: multi-method CRUD table                                                                                                                 | Composite | ATT-07, ATT-08, ATT-09, ATT-10, ATT-11, ATT-12, ATT-14 | not-started | 0   | —           | —       |

## Level 3 — Response shaping: targeting, swaps, OOB, partials, morphing

| ID     | Item                                                                                                                                                                                                                                                            | Type      | Prereqs                | Status      | Rev | Next review | Session |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ---------------------- | ----------- | --- | ----------- | ------- |
| ATT-15 | `hx-target` advanced selectors: `this`, `closest`, `find`, `findAll`, `next`, `previous`, CSS selectors                                                                                                                                                         | Attribute | ATT-04                 | not-started | 0   | —           | —       |
| ATT-16 | `hx-swap` full style set: `innerHTML`, `outerHTML`, `textContent`, `beforebegin`/`before`, `afterbegin`/`prepend`, `beforeend`/`append`, `afterend`/`after`, `innerMorph`, `outerMorph`, `outerSync`, `delete`, `none`; `upsert` is taught separately in EXT-04 | Attribute | ATT-05                 | not-started | 0   | —           | —       |
| ATT-17 | `hx-swap` modifiers: `transition:`, `swap:`, `settle:`, `ignoreTitle:`, `scroll:`, `scrollTarget:`, `show:`, `showTarget:`, `focusScroll:`, `target:`, `strip:`, `swapEmpty:`                                                                                   | Attribute | ATT-16, MOD-01         | not-started | 0   | —           | —       |
| ATT-18 | `hx-swap-oob`: out-of-band swaps by id                                                                                                                                                                                                                          | Attribute | ATT-05                 | not-started | 0   | —           | —       |
| ATT-19 | `hx-select-oob`: pick out-of-band content from the response                                                                                                                                                                                                     | Attribute | ATT-06, ATT-18         | not-started | 0   | —           | —       |
| ATT-20 | `hx-morph-skip`: skip an element's attributes and children during a morph swap                                                                                                                                                                                  | Attribute | ATT-16                 | not-started | 0   | —           | —       |
| ATT-21 | `hx-morph-skip-children`: morph attributes but keep children                                                                                                                                                                                                    | Attribute | ATT-16                 | not-started | 0   | —           | —       |
| TAG-01 | `<hx-partial>`: arbitrary partial responses                                                                                                                                                                                                                     | Tag       | ATT-05                 | not-started | 0   | —           | —       |
| CMP-09 | Multi-region update with OOB swaps                                                                                                                                                                                                                              | Composite | ATT-18, ATT-19         | not-started | 0   | —           | —       |
| CMP-10 | Multi-fragment response with `<hx-partial>`                                                                                                                                                                                                                     | Composite | TAG-01                 | not-started | 0   | —           | —       |
| CMP-11 | Morph refresh that preserves widget state                                                                                                                                                                                                                       | Composite | ATT-16, ATT-20, ATT-21 | not-started | 0   | —           | —       |
| CMP-12 | Level 3 mastery: dashboard with OOB and morphing                                                                                                                                                                                                                | Composite | CMP-09, CMP-10, CMP-11 | not-started | 0   | —           | —       |

## Level 4 — Request payloads, parameters, and headers

| ID     | Item                                                           | Type      | Prereqs                | Status      | Rev | Next review | Session |
| ------ | -------------------------------------------------------------- | --------- | ---------------------- | ----------- | --- | ----------- | ------- |
| ATT-22 | `hx-include`: include additional element values in the request | Attribute | ATT-02                 | not-started | 0   | —           | —       |
| ATT-23 | `hx-vals`: add values to request parameters                    | Attribute | ATT-02                 | not-started | 0   | —           | —       |
| ATT-24 | `hx-headers`: add custom request headers                       | Attribute | ATT-02                 | not-started | 0   | —           | —       |
| ATT-25 | `hx-encoding`: set the request encoding type                   | Attribute | ATT-02                 | not-started | 0   | —           | —       |
| ATT-26 | `hx-config`: per-element request configuration                 | Attribute | MOD-01                 | not-started | 0   | —           | —       |
| MOD-02 | `:inherited` modifier: explicit attribute inheritance          | Modifier  | FND-06                 | not-started | 0   | —           | —       |
| MOD-03 | `:merge` modifier: keep parent selector values and add more    | Modifier  | MOD-02                 | not-started | 0   | —           | —       |
| HDR-01 | `HX-Request` request header                                    | Header    | ATT-01                 | not-started | 0   | —           | —       |
| HDR-02 | `HX-Request-Type` request header: `partial` versus `full`      | Header    | HDR-01                 | not-started | 0   | —           | —       |
| HDR-03 | `HX-Current-URL` request header                                | Header    | HDR-01                 | not-started | 0   | —           | —       |
| HDR-04 | `HX-Source` request header                                     | Header    | HDR-01                 | not-started | 0   | —           | —       |
| HDR-05 | `HX-Target` request header                                     | Header    | HDR-01                 | not-started | 0   | —           | —       |
| CMP-13 | Inherited CSRF header on the body                              | Composite | ATT-24, MOD-02         | not-started | 0   | —           | —       |
| CMP-14 | Extra values from outside the form                             | Composite | ATT-22, ATT-23         | not-started | 0   | —           | —       |
| CMP-15 | File upload with multipart encoding                            | Composite | ATT-25                 | not-started | 0   | —           | —       |
| CMP-16 | Level 4 mastery: multipart form with an inherited auth header  | Composite | CMP-13, CMP-14, CMP-15 | not-started | 0   | —           | —       |

## Level 5 — Form UX, validation, and feedback

| ID     | Item                                                                           | Type      | Prereqs                | Status      | Rev | Next review | Session |
| ------ | ------------------------------------------------------------------------------ | --------- | ---------------------- | ----------- | --- | ----------- | ------- |
| ATT-27 | `hx-validate`: validate before submitting the request                          | Attribute | ATT-02                 | not-started | 0   | —           | —       |
| ATT-28 | `hx-confirm`: show a confirmation dialog before the request                    | Attribute | ATT-03                 | not-started | 0   | —           | —       |
| ATT-29 | `hx-disable`: disable selected elements during requests                        | Attribute | ATT-02                 | not-started | 0   | —           | —       |
| ATT-30 | `hx-indicator`: designate a loading indicator element                          | Attribute | ATT-02                 | not-started | 0   | —           | —       |
| ATT-31 | `hx-status`: override target, swap, selection, and URL behavior by status code | Attribute | ATT-05, ATT-15         | not-started | 0   | —           | —       |
| EVT-04 | `htmx:confirm` event                                                           | Event     | ATT-28                 | not-started | 0   | —           | —       |
| EVT-05 | `htmx:error` event                                                             | Event     | FND-04                 | not-started | 0   | —           | —       |
| EVT-06 | `htmx:response:error` event                                                    | Event     | EVT-05                 | not-started | 0   | —           | —       |
| EVT-07 | `htmx:abort` event                                                             | Event     | FND-04                 | not-started | 0   | —           | —       |
| CMP-17 | Confirm, disable, and indicator delete flow                                    | Composite | ATT-28, ATT-29, ATT-30 | not-started | 0   | —           | —       |
| CMP-18 | Inline validation rendered from a 422 response                                 | Composite | ATT-31, EVT-06         | not-started | 0   | —           | —       |
| CMP-19 | Request-state feedback without the pending extension                           | Composite | ATT-29, ATT-30         | not-started | 0   | —           | —       |
| CMP-20 | Level 5 mastery: safe destructive action flow                                  | Composite | CMP-17, CMP-18, CMP-19 | not-started | 0   | —           | —       |

## Level 6 — Navigation, history, and URL state

| ID     | Item                                                                     | Type      | Prereqs                                                        | Status      | Rev | Next review | Session |
| ------ | ------------------------------------------------------------------------ | --------- | -------------------------------------------------------------- | ----------- | --- | ----------- | ------- |
| ATT-32 | `hx-boost`: convert links and forms to AJAX navigation                   | Attribute | ATT-01, ATT-02                                                 | not-started | 0   | —           | —       |
| ATT-33 | `hx-push-url`: push a URL into browser history                           | Attribute | ATT-32                                                         | not-started | 0   | —           | —       |
| ATT-34 | `hx-replace-url`: replace the current URL in browser history             | Attribute | ATT-33                                                         | not-started | 0   | —           | —       |
| ATT-35 | `hx-history-elt`: mark the element swapped on history restore            | Attribute | ATT-33                                                         | not-started | 0   | —           | —       |
| HDR-06 | `HX-Boosted` request header                                              | Header    | ATT-32                                                         | not-started | 0   | —           | —       |
| HDR-07 | `HX-History-Restore-Request` request header                              | Header    | ATT-35                                                         | not-started | 0   | —           | —       |
| HDR-08 | `HX-Push-Url` response header                                            | Header    | ATT-33                                                         | not-started | 0   | —           | —       |
| HDR-09 | `HX-Replace-Url` response header                                         | Header    | ATT-34                                                         | not-started | 0   | —           | —       |
| HDR-10 | `HX-Location` response header: redirect without a full page load         | Header    | ATT-33                                                         | not-started | 0   | —           | —       |
| HDR-11 | `HX-Redirect` response header: full-page redirect                        | Header    | HDR-10                                                         | not-started | 0   | —           | —       |
| HDR-12 | `HX-Refresh` response header: full page reload                           | Header    | HDR-11                                                         | not-started | 0   | —           | —       |
| HDR-13 | `HX-Retarget` response header: override the swap target                  | Header    | ATT-15                                                         | not-started | 0   | —           | —       |
| HDR-14 | `HX-Reswap` response header: override the swap style                     | Header    | ATT-16                                                         | not-started | 0   | —           | —       |
| HDR-15 | `HX-Reselect` response header: override content selection                | Header    | ATT-06                                                         | not-started | 0   | —           | —       |
| HDR-16 | `HX-Trigger` response header: fire client-side events                    | Header    | EVT-05                                                         | not-started | 0   | —           | —       |
| EVT-08 | `htmx:before:history:update` event                                       | Event     | ATT-33                                                         | not-started | 0   | —           | —       |
| EVT-09 | `htmx:after:history:update` event                                        | Event     | EVT-08                                                         | not-started | 0   | —           | —       |
| EVT-10 | `htmx:after:history:push` event                                          | Event     | EVT-09                                                         | not-started | 0   | —           | —       |
| EVT-11 | `htmx:after:history:replace` event                                       | Event     | EVT-09                                                         | not-started | 0   | —           | —       |
| EVT-12 | `htmx:before:history:restore` event                                      | Event     | ATT-35                                                         | not-started | 0   | —           | —       |
| CMP-21 | Boosted navigation with correct history behavior                         | Composite | ATT-32, ATT-33, ATT-35                                         | not-started | 0   | —           | —       |
| CMP-22 | Server-driven navigation choice: location versus redirect versus refresh | Composite | HDR-10, HDR-11, HDR-12                                         | not-started | 0   | —           | —       |
| CMP-23 | Response-triggered toast through `HX-Trigger`                            | Composite | HDR-16                                                         | not-started | 0   | —           | —       |
| CMP-24 | Level 6 mastery: deep-linkable tabs with back and forward                | Composite | CMP-21, CMP-22, CMP-23, HDR-08, HDR-09, HDR-13, HDR-14, HDR-15 | not-started | 0   | —           | —       |

## Level 7 — Events and the JavaScript API

| ID     | Item                                                            | Type      | Prereqs                                                                                                                                                                                        | Status      | Rev | Next review | Session |
| ------ | --------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | --- | ----------- | ------- |
| ATT-36 | `hx-on`: run inline JavaScript when an event fires              | Attribute | EVT-05                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-13 | `htmx:config:request` event                                     | Event     | FND-04                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-14 | `htmx:before:request` event                                     | Event     | EVT-13                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-15 | `htmx:before:response` event                                    | Event     | EVT-14                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-16 | `htmx:after:request` event                                      | Event     | EVT-15                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-17 | `htmx:finally:request` event                                    | Event     | EVT-16                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-18 | `htmx:before:swap` event                                        | Event     | EVT-16                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-19 | `htmx:after:swap` event                                         | Event     | EVT-18                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-20 | `htmx:before:settle` event                                      | Event     | EVT-19                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-21 | `htmx:after:settle` event                                       | Event     | EVT-20                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-22 | `htmx:finally:swap` event                                       | Event     | EVT-21                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-23 | `htmx:before:cleanup` event                                     | Event     | EVT-19                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-24 | `htmx:after:cleanup` event                                      | Event     | EVT-23                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-25 | `htmx:before:init` event                                        | Event     | FND-04                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-26 | `htmx:after:init` event                                         | Event     | EVT-25                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-27 | `htmx:before:process` event                                     | Event     | EVT-25                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-28 | `htmx:after:process` event                                      | Event     | EVT-27                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-29 | `htmx:before:on:init` event                                     | Event     | ATT-36                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-30 | `htmx:before:viewTransition` event                              | Event     | EVT-19                                                                                                                                                                                         | not-started | 0   | —           | —       |
| EVT-31 | `htmx:after:viewTransition` event                               | Event     | EVT-30                                                                                                                                                                                         | not-started | 0   | —           | —       |
| API-01 | `htmx.ajax()`                                                   | JS API    | ATT-01, ATT-02                                                                                                                                                                                 | not-started | 0   | —           | —       |
| API-02 | `htmx.find()`                                                   | JS API    | FND-04                                                                                                                                                                                         | not-started | 0   | —           | —       |
| API-03 | `htmx.findAll()`                                                | JS API    | API-02                                                                                                                                                                                         | not-started | 0   | —           | —       |
| API-04 | `htmx.swap()`                                                   | JS API    | ATT-16                                                                                                                                                                                         | not-started | 0   | —           | —       |
| API-05 | `htmx.trigger()`                                                | JS API    | EVT-05                                                                                                                                                                                         | not-started | 0   | —           | —       |
| API-06 | `htmx.on()`                                                     | JS API    | EVT-05                                                                                                                                                                                         | not-started | 0   | —           | —       |
| API-07 | `htmx.onLoad()`                                                 | JS API    | API-06                                                                                                                                                                                         | not-started | 0   | —           | —       |
| API-08 | `htmx.process()`                                                | JS API    | EVT-27                                                                                                                                                                                         | not-started | 0   | —           | —       |
| API-09 | `htmx.initialize()`                                             | JS API    | API-08                                                                                                                                                                                         | not-started | 0   | —           | —       |
| API-10 | `htmx.timeout()`                                                | JS API    | FND-04                                                                                                                                                                                         | not-started | 0   | —           | —       |
| API-11 | `htmx.parseInterval()`                                          | JS API    | MOD-01                                                                                                                                                                                         | not-started | 0   | —           | —       |
| API-12 | `htmx.registerExtension()`                                      | JS API    | FND-02, API-06                                                                                                                                                                                 | not-started | 0   | —           | —       |
| CMP-25 | Global 401 handler with `htmx:response:error` and `htmx.ajax()` | Composite | EVT-06, API-01                                                                                                                                                                                 | not-started | 0   | —           | —       |
| CMP-26 | Custom confirm dialog with `htmx:confirm`                       | Composite | EVT-04                                                                                                                                                                                         | not-started | 0   | —           | —       |
| CMP-27 | Programmatic request and swap                                   | Composite | API-01, API-04                                                                                                                                                                                 | not-started | 0   | —           | —       |
| CMP-28 | Widget cleanup on swap                                          | Composite | EVT-23, EVT-24                                                                                                                                                                                 | not-started | 0   | —           | —       |
| CMP-29 | Level 7 mastery: lifecycle instrumentation                      | Composite | ATT-36, EVT-13, EVT-14, EVT-15, EVT-16, EVT-17, EVT-18, EVT-19, EVT-20, EVT-21, EVT-22, EVT-23, EVT-24, EVT-25, EVT-26, EVT-27, EVT-28, EVT-29, EVT-30, EVT-31, CMP-25, CMP-26, CMP-27, CMP-28 | not-started | 0   | —           | —       |

## Level 8 — Inheritance, scoping, and preservation

| ID     | Item                                                                 | Type      | Prereqs                | Status      | Rev | Next review | Session |
| ------ | -------------------------------------------------------------------- | --------- | ---------------------- | ----------- | --- | ----------- | ------- |
| ATT-37 | `hx-ignore`: disable htmx processing for an element and its children | Attribute | FND-06                 | not-started | 0   | —           | —       |
| ATT-38 | `hx-preserve`: preserve an element across swaps                      | Attribute | ATT-05                 | not-started | 0   | —           | —       |
| CMP-30 | Layout defaults with `:inherited`                                    | Composite | MOD-02, ATT-24         | not-started | 0   | —           | —       |
| CMP-31 | Preserve widget state across a swap                                  | Composite | ATT-38                 | not-started | 0   | —           | —       |
| CMP-32 | Ignore a third-party or untrusted subtree                            | Composite | ATT-37                 | not-started | 0   | —           | —       |
| CMP-33 | Level 8 mastery: component shell with scoped defaults                | Composite | CMP-30, CMP-31, CMP-32 | not-started | 0   | —           | —       |

## Level 9 — Global configuration

| ID     | Item                                             | Type      | Prereqs                | Status      | Rev | Next review | Session |
| ------ | ------------------------------------------------ | --------- | ---------------------- | ----------- | --- | ----------- | ------- |
| CFG-01 | `htmx.config`: the global configuration object   | Config    | FND-02                 | not-started | 0   | —           | —       |
| CFG-02 | `htmx.config.prefix`                             | Config    | CFG-01                 | not-started | 0   | —           | —       |
| CFG-03 | `htmx.config.metaCharacter`                      | Config    | CFG-01                 | not-started | 0   | —           | —       |
| CFG-04 | `htmx.config.implicitInheritance`                | Config    | MOD-02                 | not-started | 0   | —           | —       |
| CFG-05 | `htmx.config.defaultSwap`                        | Config    | CFG-01                 | not-started | 0   | —           | —       |
| CFG-06 | `htmx.config.defaultSettleDelay`                 | Config    | CFG-01                 | not-started | 0   | —           | —       |
| CFG-07 | `htmx.config.defaultTimeout`                     | Config    | CFG-01                 | not-started | 0   | —           | —       |
| CFG-08 | `htmx.config.noSwap`                             | Config    | CFG-01                 | not-started | 0   | —           | —       |
| CFG-09 | `htmx.config.history`                            | Config    | CFG-01, ATT-33         | not-started | 0   | —           | —       |
| CFG-10 | `htmx.config.transitions`                        | Config    | CFG-01                 | not-started | 0   | —           | —       |
| CFG-11 | `htmx.config.requestClass`                       | Config    | CFG-01                 | not-started | 0   | —           | —       |
| CFG-12 | `htmx.config.indicatorClass`                     | Config    | CFG-01                 | not-started | 0   | —           | —       |
| CFG-13 | `htmx.config.includeIndicatorCSS`                | Config    | CFG-12                 | not-started | 0   | —           | —       |
| CFG-14 | `htmx.config.defaultFocusScroll`                 | Config    | CFG-01                 | not-started | 0   | —           | —       |
| CFG-15 | `htmx.config.logAll`                             | Config    | CFG-01                 | not-started | 0   | —           | —       |
| CFG-16 | `htmx.config.extensions`                         | Config    | CFG-01                 | not-started | 0   | —           | —       |
| CFG-17 | `htmx.config.mode`                               | Config    | CFG-01                 | not-started | 0   | —           | —       |
| CFG-18 | `htmx.config.inlineScriptNonce`                  | Config    | CFG-01                 | not-started | 0   | —           | —       |
| CFG-19 | `htmx.config.morphIgnore`                        | Config    | ATT-20                 | not-started | 0   | —           | —       |
| CFG-20 | `htmx.config.morphSkip`                          | Config    | ATT-20                 | not-started | 0   | —           | —       |
| CFG-21 | `htmx.config.morphSkipChildren`                  | Config    | ATT-21                 | not-started | 0   | —           | —       |
| CFG-22 | `htmx.config.morphScanLimit`                     | Config    | ATT-20                 | not-started | 0   | —           | —       |
| CFG-23 | `htmx.config.allowEmptySwapAfterOOB`             | Config    | ATT-18                 | not-started | 0   | —           | —       |
| CFG-24 | `htmx.version`: read-only current version string | Config    | CFG-01                 | not-started | 0   | —           | —       |
| CMP-34 | Debugging setup with `logAll` and `requestClass` | Composite | CFG-15, CFG-11         | not-started | 0   | —           | —       |
| CMP-35 | Hardened production configuration                | Composite | CFG-08, CFG-18, CFG-02 | not-started | 0   | —           | —       |
| CMP-36 | htmx 2 compatibility configuration               | Composite | CFG-04, CFG-08, CFG-09 | not-started | 0   | —           | —       |
| CMP-37 | Level 9 mastery: configuration audit             | Composite | CMP-34, CMP-35, CMP-36 | not-started | 0   | —           | —       |

## Level 10 — Extensions

| ID     | Item                                                  | Type      | Prereqs                | Status      | Rev | Next review | Session |
| ------ | ----------------------------------------------------- | --------- | ---------------------- | ----------- | --- | ----------- | ------- |
| EXT-01 | `hx-preload` extension                                | Extension | ATT-32                 | not-started | 0   | —           | —       |
| EXT-02 | `hx-pending` extension                                | Extension | ATT-30                 | not-started | 0   | —           | —       |
| EXT-03 | `hx-targets` extension                                | Extension | ATT-15                 | not-started | 0   | —           | —       |
| EXT-04 | `hx-upsert` extension                                 | Extension | ATT-05                 | not-started | 0   | —           | —       |
| EXT-05 | `hx-sse` extension                                    | Extension | EVT-01                 | not-started | 0   | —           | —       |
| EXT-06 | `hx-ws` extension                                     | Extension | EVT-01                 | not-started | 0   | —           | —       |
| EXT-07 | `hx-live` extension                                   | Extension | EXT-05                 | not-started | 0   | —           | —       |
| EXT-08 | `hx-csp` extension                                    | Extension | FND-05                 | not-started | 0   | —           | —       |
| EXT-09 | `hx-download` extension                               | Extension | ATT-05                 | not-started | 0   | —           | —       |
| EXT-10 | `hx-head` extension                                   | Extension | ATT-05                 | not-started | 0   | —           | —       |
| EXT-11 | `hx-prompt` extension                                 | Extension | ATT-23                 | not-started | 0   | —           | —       |
| EXT-12 | `hx-ptag` extension                                   | Extension | TAG-01                 | not-started | 0   | —           | —       |
| EXT-13 | `hx-multipart` extension                              | Extension | CMP-15                 | not-started | 0   | —           | —       |
| EXT-14 | `hx-browser-indicator` extension                      | Extension | ATT-30                 | not-started | 0   | —           | —       |
| EXT-15 | `hx-alpine-compat` extension                          | Extension | ATT-36                 | not-started | 0   | —           | —       |
| EXT-16 | `hx-history-cache` extension                          | Extension | ATT-35                 | not-started | 0   | —           | —       |
| EXT-17 | `htmx-2-compat` extension                             | Extension | FND-06                 | not-started | 0   | —           | —       |
| EXT-18 | Community extensions and extension authoring overview | Extension | API-12, CFG-16         | not-started | 0   | —           | —       |
| CMP-38 | SSE live dashboard                                    | Composite | EXT-05, EXT-03, ATT-30 | not-started | 0   | —           | —       |
| CMP-39 | Streaming response UI                                 | Composite | EXT-05, EXT-07         | not-started | 0   | —           | —       |
| CMP-40 | Preload plus pending navigation                       | Composite | EXT-01, EXT-02         | not-started | 0   | —           | —       |
| CMP-41 | Level 10 mastery: extension composition               | Composite | CMP-38, CMP-39, CMP-40 | not-started | 0   | —           | —       |

## Level 11 — Recipes and patterns

| ID     | Item                                   | Type      | Prereqs                                                                                                                                                | Status      | Rev | Next review | Session |
| ------ | -------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | --- | ----------- | ------- |
| PAT-01 | Polling                                | Pattern   | CMP-07                                                                                                                                                 | not-started | 0   | —           | —       |
| PAT-02 | Click to load                          | Pattern   | CMP-06                                                                                                                                                 | not-started | 0   | —           | —       |
| PAT-03 | Lazy load                              | Pattern   | CMP-06                                                                                                                                                 | not-started | 0   | —           | —       |
| PAT-04 | Active search                          | Pattern   | CMP-05                                                                                                                                                 | not-started | 0   | —           | —       |
| PAT-05 | Active validation                      | Pattern   | CMP-18                                                                                                                                                 | not-started | 0   | —           | —       |
| PAT-06 | Linked selects                         | Pattern   | ATT-13, ATT-22, ATT-23                                                                                                                                 | not-started | 0   | —           | —       |
| PAT-07 | Reset on submit                        | Pattern   | CMP-02                                                                                                                                                 | not-started | 0   | —           | —       |
| PAT-08 | Delete in place                        | Pattern   | CMP-17                                                                                                                                                 | not-started | 0   | —           | —       |
| PAT-09 | Edit in place                          | Pattern   | CMP-02, ATT-16                                                                                                                                         | not-started | 0   | —           | —       |
| PAT-10 | Bulk actions                           | Pattern   | ATT-22, ATT-24                                                                                                                                         | not-started | 0   | —           | —       |
| PAT-11 | Dialogs                                | Pattern   | CMP-26                                                                                                                                                 | not-started | 0   | —           | —       |
| PAT-12 | Tabs                                   | Pattern   | CMP-24                                                                                                                                                 | not-started | 0   | —           | —       |
| PAT-13 | Infinite scroll                        | Pattern   | EVT-02, ATT-18                                                                                                                                         | not-started | 0   | —           | —       |
| PAT-14 | Live updates                           | Pattern   | CMP-38                                                                                                                                                 | not-started | 0   | —           | —       |
| PAT-15 | Progress bar                           | Pattern   | ATT-30, EXT-01                                                                                                                                         | not-started | 0   | —           | —       |
| PAT-16 | File upload                            | Pattern   | CMP-15, EXT-13                                                                                                                                         | not-started | 0   | —           | —       |
| PAT-17 | Drag to reorder                        | Pattern   | API-01, ATT-23                                                                                                                                         | not-started | 0   | —           | —       |
| PAT-18 | Keyboard shortcuts                     | Pattern   | ATT-13, ATT-36                                                                                                                                         | not-started | 0   | —           | —       |
| PAT-19 | Streaming LLM response                 | Pattern   | EXT-05, EXT-07                                                                                                                                         | not-started | 0   | —           | —       |
| CMP-42 | Level 11 mastery: combined application | Composite | PAT-01, PAT-02, PAT-03, PAT-04, PAT-05, PAT-06, PAT-07, PAT-08, PAT-09, PAT-10, PAT-11, PAT-12, PAT-13, PAT-14, PAT-15, PAT-16, PAT-17, PAT-18, PAT-19 | not-started | 0   | —           | —       |

## Level 12 — Architecture, process, and expert topics

| ID     | Item                                                            | Type         | Prereqs                                                                                                | Status      | Rev | Next review | Session |
| ------ | --------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------ | ----------- | --- | ----------- | ------- |
| ARC-01 | Server-first fragment architecture: endpoint and partial design | Architecture | FND-05, CMP-42                                                                                         | not-started | 0   | —           | —       |
| ARC-02 | Hypermedia application structure and URL state                  | Architecture | CMP-24                                                                                                 | not-started | 0   | —           | —       |
| ARC-03 | Security: output escaping, CSP, CSRF, and trust boundaries      | Architecture | CMP-13, EXT-08, ATT-37                                                                                 | not-started | 0   | —           | —       |
| ARC-04 | Performance and request budgeting                               | Architecture | EXT-01, CFG-06                                                                                         | not-started | 0   | —           | —       |
| ARC-05 | Testing htmx applications                                       | Process      | CMP-29                                                                                                 | not-started | 0   | —           | —       |
| ARC-06 | Debugging and observability                                     | Process      | CMP-34                                                                                                 | not-started | 0   | —           | —       |
| ARC-07 | Migrating htmx 2.x to 4                                         | Process      | CFG-04, CFG-08, CFG-09, EXT-16, EXT-17                                                                 | not-started | 0   | —           | —       |
| ARC-08 | Extension authoring deep dive                                   | Architecture | API-12, EXT-18                                                                                         | not-started | 0   | —           | —       |
| ARC-09 | HCON deep dive                                                  | Architecture | MOD-01                                                                                                 | not-started | 0   | —           | —       |
| ARC-10 | Quirks and gotchas catalog                                      | Process      | CMP-42                                                                                                 | not-started | 0   | —           | —       |
| ARC-11 | Morphing strategy in production                                 | Architecture | CMP-11, CFG-19, CFG-20, CFG-21, CFG-22                                                                 | not-started | 0   | —           | —       |
| ARC-12 | Editor and tooling support                                      | Process      | FND-02                                                                                                 | not-started | 0   | —           | —       |
| ARC-13 | Capstone: full hypermedia application                           | Architecture | CMP-42, ARC-01, ARC-02, ARC-03, ARC-04, ARC-05, ARC-06, ARC-07, ARC-08, ARC-09, ARC-10, ARC-11, ARC-12 | not-started | 0   | —           | —       |
| ARC-14 | Final teach-back defense                                        | Process      | ARC-13                                                                                                 | not-started | 0   | —           | —       |
