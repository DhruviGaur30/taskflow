from pydantic import BaseModel, EmailStr


# =========================
# AUTH SCHEMAS
# =========================
class UserSignup(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

# =========================
# PROJECT SCHEMAS
# =========================
class ProjectCreate(BaseModel):
    name: str
    description: str


# =========================
# TASK SCHEMAS
# =========================
class TaskCreate(BaseModel):
    title: str
    description: str
    project_id: int
    assigned_to: int