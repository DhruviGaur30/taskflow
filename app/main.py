from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import engine
from app.models import Base
from app.routes import router

# Create FastAPI app
app = FastAPI(
    title="TaskFlow RBAC",
    version="1.0.0"
)

# Create DB tables
Base.metadata.create_all(bind=engine)

# Include API routes
app.include_router(router)

# Static files
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

# Templates
templates = Jinja2Templates(
    directory="app/templates"
)

# Home Page
@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )