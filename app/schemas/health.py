from pydantic import BaseModel
from typing import Optional


class HealthResponse(BaseModel):
    status: str
    version: str
    environment: str
    uptime_seconds: Optional[float] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": "healthy",
                    "version": "0.1.0",
                    "environment": "development",
                    "uptime_seconds": 42.5,
                }
            ]
        }
    }
