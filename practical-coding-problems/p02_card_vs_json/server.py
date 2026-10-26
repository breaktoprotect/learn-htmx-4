from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

from lab.helpers import mount_problem_static

FOLDER = Path(__file__).resolve().parent
app = FastAPI()


@app.get("/card", response_class=HTMLResponse)
def card() -> str:
    return (
        '<article class="card">'
        "<h2>Ada Lovelace</h2>"
        "<p>Role: Engineer</p>"
        "</article>"
    )


@app.get("/record", response_class=JSONResponse)
def record() -> dict[str, str]:
    return {"name": "Ada Lovelace", "role": "Engineer"}


mount_problem_static(app, FOLDER)
