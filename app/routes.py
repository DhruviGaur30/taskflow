from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request

from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.database import get_db

from app.models import User
from app.models import Project
from app.models import Task

from app.schemas import UserSignup
from app.schemas import ProjectCreate
from app.schemas import TaskCreate

from app.auth import hash_password
from app.auth import verify_password
from app.auth import create_access_token

from app.dependencies import get_current_user


router = APIRouter()

# Templates folder
templates = Jinja2Templates(directory="app/templates")


# =========================
# SIGNUP
# =========================
@router.post("/signup")
def signup(
    user: UserSignup,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role="member"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User created successfully"
    }


# =========================
# LOGIN
# =========================
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        form_data.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token({
        "user_id": db_user.id,
        "role": db_user.role
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# =========================
# CREATE PROJECT
# =========================
@router.post("/projects")
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # RBAC CHECK
    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Only admin can create projects"
        )

    new_project = Project(
        name=project.name,
        description=project.description
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


# =========================
# GET PROJECTS
# =========================
@router.get("/projects")
def get_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    projects = db.query(Project).all()

    return projects


# =========================
# CREATE TASK
# =========================
@router.post("/tasks")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = db.query(Project).filter(
        Project.id == task.project_id
    ).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    assigned_user = db.query(User).filter(
        User.id == task.assigned_to
    ).first()

    if not assigned_user:
        raise HTTPException(
            status_code=404,
            detail="Assigned user not found"
        )

    new_task = Task(
        title=task.title,
        description=task.description,
        project_id=task.project_id,
        assigned_to=task.assigned_to
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


# =========================
# GET TASKS
# =========================
@router.get("/tasks")
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    tasks = db.query(Task).all()

    return tasks


# =========================
# DASHBOARD PAGE
# =========================

@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):

    total_tasks = db.query(Task).count()

    pending_tasks = db.query(Task).filter(
        Task.status == "pending"
    ).count()

    completed_tasks = db.query(Task).filter(
        Task.status == "completed"
    ).count()

    return JSONResponse({
        "total_tasks": total_tasks,
        "pending_tasks": pending_tasks,
        "completed_tasks": completed_tasks
    })