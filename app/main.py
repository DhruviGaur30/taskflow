from fastapi import FastAPI
from fastapi import Request

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import engine
from app.models import Base
from app.routes import router

app = FastAPI(
    title="TaskFlow RBAC",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
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

# HOME PAGE
@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )