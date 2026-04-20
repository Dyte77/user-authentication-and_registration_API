from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import logging
import os

# Load environment variables
load_dotenv()

from app.database import engine, Base
from app.routes import auth, users

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Authentication API",
    description="RESTful API for user registration, authentication, and management",
    version="1.0.0",
    docs_url="/api/docs",           # Swagger UI at /api/docs
    redoc_url="/api/redoc",         # ReDoc at /api/redoc
    openapi_url="/api/openapi.json" # OpenAPI schema at /api/openapi.json
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "message": str(exc)}
    )

# Include routers
app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to User Authentication API",
        "version": "1.0.0",
        "endpoints": {
            "auth": "/api/auth/register, /api/auth/login",
            "users": "/api/users, /api/users/{id}, /api/profile/me"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}