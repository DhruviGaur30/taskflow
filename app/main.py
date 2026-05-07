from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import engine
from app.models import Base
from app.routes import router

# Create FastAPI application
app = FastAPI(
    title="TaskFlow RBAC",
    version="1.0.0"
)

# Create database tables automatically
Base.metadata.create_all(bind=engine)

# Register all API routes
app.include_router(router)

# Static files (CSS, JS, images)
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

# HTML templates
templates = Jinja2Templates(
    directory="app/templates/dashboard.html"
)


# Root route
@app.get("/")
def home():
    return {
        "message": "TaskFlow RBAC API Running Successfully"
    }