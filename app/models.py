from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


# =========================
# USER MODEL
# =========================

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    password = Column(String, nullable=False)

    role = Column(String, default="member")

    created_at = Column(DateTime, default=datetime.utcnow)

    tasks = relationship("Task", back_populates="assigned_user")


# =========================
# PROJECT MODEL
# =========================
class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    description = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

    tasks = relationship("Task", back_populates="project")


# =========================
# TASK MODEL
# =========================
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(String)

    status = Column(String, default="TODO")

    priority = Column(String, default="MEDIUM")

    created_at = Column(DateTime, default=datetime.utcnow)

    project_id = Column(Integer, ForeignKey("projects.id"))

    assigned_to = Column(Integer, ForeignKey("users.id"))

    project = relationship("Project", back_populates="tasks")

    assigned_user = relationship("User", back_populates="tasks")