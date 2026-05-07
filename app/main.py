from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import engine
from app.models import Base
from app.routers import router

# Create FastAPI app
app = FastAPI(title="TaskFlow RBAC")

# Create database tables
Base.metadata.create_all(bind=engine)

# Register all routes
app.include_router(router)

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home():
    return {
        "message": "TaskFlow RBAC API Running Successfully"
    }