from fastapi import FastAPI
from app.controller import task_controller
from app.config.db_config import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(task_controller.router)
# Add CORS middleware
from fastapi.middleware.cors import CORSMiddleware