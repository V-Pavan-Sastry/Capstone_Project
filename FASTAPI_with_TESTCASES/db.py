from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from fastapi import Depends

# DB URL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Pass%40123@localhost:3306/capstone"

# Engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Optional connection check
def check_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SHOW TABLES"))
            print("Tables in the database:")
            for table in result.fetchall():
                print(table[0])
    except SQLAlchemyError as e:
        print("Error connecting to the database:", e)

# Run check if needed
# check_connection()
