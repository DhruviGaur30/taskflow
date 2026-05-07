# TaskFlow RBAC

Full-stack team task management system built with FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, Role-Based Access Control (RBAC), and Jinja2 templates.

## Features

- User Signup & Login
- JWT Authentication
- Role-Based Access Control (Admin / Member)
- Project Management
- Task Creation & Assignment
- Dashboard Analytics
- PostgreSQL Database Integration
- Protected Routes
- Server-Side Rendered Frontend
- Swagger API Documentation

---

# Tech Stack

## Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication
- Pydantic

## Frontend
- Jinja2 Templates
- HTML
- Tailwind CSS

## Deployment
- Railway

---

# System Architecture

```text
Browser
   ↓
Jinja2 Frontend
   ↓
FastAPI Backend
   ↓
SQLAlchemy ORM
   ↓
PostgreSQL Database
```
Project Structure
```
taskflow-rbac/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── dependencies.py
│   ├── routers.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   └── dashboard.html
│   │
│   └── static/
│
├── requirements.txt
├── .env
└── README.md
```
## Installation & Setup
# 1. Clone Repository
```
git clone https://github.com/YOUR_USERNAME/taskflow-rbac.git
cd taskflow-rbac
```
# 2. Create Virtual Environment

```Windows
python -m venv venv
venv\Scripts\activate
```
# 3. Install Dependencies
```
pip install -r requirements.txt
```
# 4. Configure Environment Variables
Create .env file in root directory:
```
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost/taskflow
SECRET_KEY=mysecretkey
ALGORITHM=HS256
```
# 5. Create PostgreSQL Database

Create database named:
```
taskflow
```

# 6. Run Application
```
uvicorn app.main:app --reload
```
Access Application
API
```
http://127.0.0.1:8000
```
Swagger Documentation
```
http://127.0.0.1:8000/docs
```
Dashboard
```
http://127.0.0.1:8000/dashboard
```
# Authentication Flow
```
Signup
→ Login
→ JWT Token Generated
→ Protected Routes Access
```

# Role-Based Access
```
Admin
-Create Projects
-Assign Tasks
-Manage Projects

Member
-View Tasks
-Update Assigned Work
```
# Database Models
User
id
name
email
password
role
Project
id
name
description
Task
id
title
description
status
priority
project_id
assigned_to
API Endpoints
Authentication
Method	Endpoint
POST	/signup
POST	/login
Projects
Method	Endpoint
POST	/projects
GET	/projects
Tasks
Method	Endpoint
POST	/tasks
GET	/tasks
Deployment

Backend and PostgreSQL deployed using Railway.

Future Improvements
Task Status Updates
Project Member Management
Overdue Task Tracking
Docker Support
Alembic Migrations
Enhanced Dashboard UI
Author

Dhruvi Gaur
