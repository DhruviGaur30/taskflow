TaskFlow RBAC API

Tech Stack:
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- OAuth2
- Swagger UI

Features:
- User Signup/Login
- JWT Authentication
- Role Based Access Control
- Project Management
- Task Management
- Dashboard APIs

Run Locally:

1. Create virtual environment
2. Install dependencies

pip install -r requirements.txt

3. Start PostgreSQL

4. Run server

uvicorn app.main:app --reload

API Docs:
http://127.0.0.1:8000/docs

Default Test User:
email: dhruvi@example.com
password: password123