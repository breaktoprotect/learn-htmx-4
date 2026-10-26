from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

from lab.helpers import mount_problem_static

FOLDER = Path(__file__).resolve().parent
app = FastAPI()


@app.get("/fragment", response_class=HTMLResponse)
def fragment() -> str:
    return '<p class="fragment">The server sent <strong>HTML</strong>, and the browser rendered it.</p>'


@app.get("/payload", response_class=JSONResponse)
def payload() -> dict[str, object]:
    return {"count": 3, "kind": "json"}


mount_problem_static(app, FOLDER)
