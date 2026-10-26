"""Helpers for building one FastAPI sub-app per practical problem."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


def problem_app() -> FastAPI:
    """Create the FastAPI sub-app for one exercise folder."""
    return FastAPI()


def mount_problem_static(app: FastAPI, folder: Path) -> None:
    """Serve the exercise folder (index.html and assets) at the sub-app root.

    Call this AFTER declaring all API routes. Starlette matches routes in the
    order they were added, so a root static mount declared first would shadow
    the exercise endpoints.
    """
    app.mount("/", StaticFiles(directory=folder, html=True), name="static")
