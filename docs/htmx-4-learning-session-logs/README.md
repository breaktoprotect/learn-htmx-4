# htmx 4 Learning Session Logs

One file per conversation session. Logs are **append-only**.

## Naming

`YYYY-MM-DD_sNN.md` uses the session start date and a two-digit sequence.

- First session on 2026-10-21: `2026-10-21_s01.md`
- Second session that same day: `2026-10-21_s02.md`
- A session that runs past midnight keeps its start date and records the end time.

## Why session logs instead of one file per item

A session is the natural teaching unit: it covers several curriculum items, reviews, and the conversation that connects them. One file per FND/ATT item would fragment a single lesson across many files. Each item still gets its own section inside the session log, keyed by its curriculum ID, so item history remains searchable.

The tracker stays high-level:

| Tracker column | Meaning                                              |
| -------------- | ---------------------------------------------------- |
| `Status`       | Current mastery state                                |
| `Rev`          | Successful spaced reviews                            |
| `Next review`  | Next review date                                     |
| `Session`      | Last session that changed the item (`s01`, `s02`, …) |

Detailed prompts, answers, verdicts, gaps, and evidence live here. Each item entry records its hands-on scale (full lab, mini-lab, observation, or retention artifact) and the artifact path or observed behavior.

## Rules

- Append only. Never rewrite a past session log.
- The tracker points here; it does not duplicate the detail.
- Record summaries and file paths, not full student solutions.
- Never record secrets, tokens, or personal data.
- The sensei owns these files; the student may read them.

See `_TEMPLATE.md` for the entry format.
