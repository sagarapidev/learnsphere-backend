from app.core.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# This code defines a dependency for FastAPI that provides a database session for each request.
# It uses SQLAlchemy's SessionLocal to create a new session and ensures that the session is closed after the request is completed.