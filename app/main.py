
from fastapi import FastAPI

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