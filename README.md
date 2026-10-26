# learn-htmx-4

Kumon-style, mastery-gated htmx 4 curriculum taught by the **HTMX Sensei** agent.

## Layout

| Path                                  | Purpose                          |
| ------------------------------------- | -------------------------------- |
| `.github/agents/htmx-sensei.agent.md` | The teacher agent                |
| `.github/skills/htmx-4/`              | Offline htmx 4 knowledge base    |
| `docs/htmx-4-learning-tracker.md`     | High-level curriculum and status |
| `docs/htmx-4-learning-session-logs/`  | Per-session detailed logs        |
| `practical-coding-problems/`          | One folder per exercise          |
| `lab/`                                | Shared FastAPI lab server        |

## Run the lab

```bash
uv sync
uv run uvicorn lab.main:app --reload
```

Open <http://127.0.0.1:8000/> for the problem index and
<http://127.0.0.1:8000/health> for a health check.

Each problem lives at `http://127.0.0.1:8000/p/<folder>/`. Relative URLs in
`index.html` resolve against that base, so `hx-get="fragment"` calls
`/p/<folder>/fragment`.

## Start learning

Open Copilot Chat, select **HTMX Sensei**, and say `start`. Use `status`,
`review`, or name a topic at any time.
