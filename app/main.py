from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import engine
from app.models import Base
from app.routes import router

app = FastAPI(
    title="TaskFlow RBAC",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(router)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="app/templates"
)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/login-page")
def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )


@app.get("/signup-page")
def signup_page(request: Request):
    return templates.TemplateResponse(
        "signup.html",
        {"request": request}
    )