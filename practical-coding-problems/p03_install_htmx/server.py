from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from lab.helpers import mount_problem_static

FOLDER = Path(__file__).resolve().parent
app = FastAPI()


@app.get("/ping", response_class=HTMLResponse)
def ping() -> str:
    return '<p class="ping">pong — htmx issued this request</p>'


mount_problem_static(app, FOLDER)
