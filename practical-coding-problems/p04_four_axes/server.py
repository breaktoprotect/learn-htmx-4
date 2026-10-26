from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from lab.helpers import mount_problem_static

FOLDER = Path(__file__).resolve().parent
app = FastAPI()


@app.get("/probe", response_class=HTMLResponse)
def probe_get() -> str:
    return '<p class="probe">method: GET</p>'


@app.post("/probe", response_class=HTMLResponse)
def probe_post() -> str:
    return '<p class="probe">method: POST</p>'


mount_problem_static(app, FOLDER)
