from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import engine


app = FastAPI(
    title="MonitorX API",
    description="Website Monitoring & Alerting Platform",
    version="1.0.0",
)


@app.get("/api/health")
def health_check():
    return {
        "success": True,
        "message": "MonitorX API is running.",
    }


@app.get("/api/health/database")
def database_health_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "success": True,
        "message": "Database connection is working.",
    }
