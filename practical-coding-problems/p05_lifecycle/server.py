from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from lab.helpers import mount_problem_static

FOLDER = Path(__file__).resolve().parent
app = FastAPI()


@app.get("/step", response_class=HTMLResponse)
def step() -> str:
    return '<p class="step">request complete</p>'


mount_problem_static(app, FOLDER)
