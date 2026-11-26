from fastapi import APIRouter
from app.services.health_service import HealthService
from app.schemas.health import HealthResponse

router = APIRouter()
health_service = HealthService()


@router.get("/health/live", summary="Liveness Probe")
async def liveness():
    """
    Kubernetes-style liveness probe.
    Returns 200 OK if the application is running.
    """
    return {"status": "alive"}


@router.get("/health/ready", summary="Readiness Probe")
async def readiness():
    """
    Kubernetes-style readiness probe.
    Returns 200 OK if the application is ready to serve traffic.
    """
    return await health_service.get_readiness()


@router.get("/health", response_model=HealthResponse, summary="Health Check")
async def health_check():
    """
    Perform a health check on the application.

    Returns the current status, version, and environment.
    """
    return await health_service.get_health()
