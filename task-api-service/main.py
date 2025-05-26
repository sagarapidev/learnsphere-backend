from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database.connection import SessionLocal, engine, Base
from app.infrastructure.database.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to Task API"}

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()
