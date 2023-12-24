from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import recognition

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(prefix="/api/v1.0",router=recognition.router)
