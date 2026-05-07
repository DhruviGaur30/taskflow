from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(dotenv_path=".env")

# Get database URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Debugging line
print("DATABASE_URL =", DATABASE_URL)

# Create database engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base model class
Base = declarative_base()


# Database dependency
# Opens DB session
# Closes automatically after request

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()