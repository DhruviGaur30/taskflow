# TaskFlow RBAC API

## Project Overview

TaskFlow RBAC is a backend task management system built using FastAPI and PostgreSQL. The application enables users to authenticate securely using JWT tokens, create and manage projects, assign tasks, and monitor task progress through dashboard APIs. The system implements Role-Based Access Control (RBAC) to manage Admin and Member permissions effectively.

The project demonstrates backend API development, database integration, authentication, authorization, and deployment practices using modern Python frameworks and tools.

---

# Features

## Authentication & Authorization
- User Signup
- User Login
- JWT Token Authentication
- OAuth2 Password Bearer Flow
- Password Hashing using bcrypt
- Protected API Routes

## Role-Based Access Control (RBAC)
- Admin Role
- Member Role
- Authorization-based API Access

## Project Management
- Create Projects
- Retrieve Projects

## Task Management
- Create Tasks
- Assign Tasks to Users
- Task Status Tracking
- Task Relationship with Projects and Users

## Dashboard APIs
- Total Tasks Count
- Pending Tasks Count
- Completed Tasks Count

---

# Tech Stack

| Technology | Purpose |
|---|---|
| FastAPI | Backend Framework |
| PostgreSQL | Relational Database |
| SQLAlchemy | ORM |
| JWT | Authentication |
| OAuth2 | Secure Authorization |
| Passlib + bcrypt | Password Hashing |
| Uvicorn | ASGI Server |
| Swagger UI | API Documentation |

---

# Database Schema

## Users Table
| Column | Type |
|---|---|
| id | Integer |
| name | String |
| email | String |
| password | String |
| role | String |
| created_at | Timestamp |

## Projects Table
| Column | Type |
|---|---|
| id | Integer |
| name | String |
| description | String |
| created_at | Timestamp |

## Tasks Table
| Column | Type |
|---|---|
| id | Integer |
| title | String |
| description | String |
| status | String |
| project_id | Integer |
| assigned_to | Integer |
| created_at | Timestamp |

---

# Project Structure

```bash
app/
│
├── main.py
├── auth.py
├── config.py
├── database.py
├── models.py
├── schemas.py
├── routers.py
│
├── static/
│
└── templates/
```

---

# Installation & Setup

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

## 2. Navigate to Project Folder

```bash
cd YOUR_PROJECT_FOLDER
```

## 3. Create Virtual Environment

```bash
python -m venv .venv
```

## 4. Activate Virtual Environment

### Windows
```bash
.venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Required Dependencies

```txt
fastapi
uvicorn
sqlalchemy
psycopg2-binary
python-jose
passlib[bcrypt]
python-multipart
jinja2
```

---

# PostgreSQL Configuration

Create a PostgreSQL database and configure the connection string.

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost/taskmanager
SECRET_KEY=taskflowsecretkey
ALGORITHM=HS256
```

---

# Run Application

```bash
uvicorn app.main:app --reload
```

---

# Application URLs

## API Base URL

```text
http://127.0.0.1:8000
```

## Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

# Authentication Flow

## Step 1 — Signup User

Endpoint:

```http
POST /signup
```

Example Request:

```json
{
  "name": "Dhruvi",
  "email": "dhruvi@example.com",
  "password": "password123"
}
```

---

## Step 2 — Login User

Endpoint:

```http
POST /login
```

Use:

```text
grant_type=password
username=dhruvi@example.com
password=password123
```

---

## Step 3 — Authorize in Swagger

1. Click "Authorize"
2. Enter:
   - Username → User Email
   - Password → User Password
3. Click "Authorize"

---

# API Endpoints

## Authentication APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | /signup | Register User |
| POST | /login | Login User |

---

## Project APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | /projects | Get All Projects |
| POST | /projects | Create Project |

---

## Task APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | /tasks | Get All Tasks |
| POST | /tasks | Create Task |

---

## Dashboard APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | /dashboard | Task Statistics Dashboard |

---

# Sample API Usage

## Create Project

```json
{
  "name": "TaskFlow Platform",
  "description": "Role based task manager"
}
```

---

## Create Task

```json
{
  "title": "Build Backend APIs",
  "description": "Create authentication and task APIs",
  "status": "pending",
  "project_id": 1,
  "assigned_to": 1
}
```

---

# Sample Dashboard Response

```json
{
  "total_tasks": 1,
  "pending_tasks": 1,
  "completed_tasks": 0
}
```

---

# Deployment

The application is deployed using Railway with PostgreSQL integration.

## Deployment Platform
- Railway

## Deployment Features
- Cloud Hosting
- PostgreSQL Database Integration
- Public API Access
- Automatic Deployments from GitHub

---

# Railway Deployment Steps

## 1. Push Code to GitHub

```bash
git add .
git commit -m "Final TaskFlow RBAC submission"
git push origin main
```

---

## 2. Deploy on Railway

1. Login to Railway
2. Create New Project
3. Deploy from GitHub Repository
4. Add PostgreSQL Service
5. Configure Environment Variables
6. Deploy Application

---

# Environment Variables

```env
DATABASE_URL=your_database_url
SECRET_KEY=taskflowsecretkey
ALGORITHM=HS256
```

---

# Start Command

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

# Testing

The application was tested using:
- Swagger UI
- PostgreSQL
- JWT Authentication
- Protected Routes
- CRUD Operations

---

# Future Improvements

- Frontend Integration
- Task Deadlines
- File Uploads
- Email Notifications
- Advanced RBAC Permissions
- Real-time Dashboard Analytics

---

# Author

## Dhruvi Gaur
dhruvigaur30@gmail.com 

---
