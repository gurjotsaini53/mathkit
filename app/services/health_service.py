import time
from app.config import settings
from app.schemas.health import HealthResponse

# Record startup time for uptime calculation
_start_time = time.time()


class HealthService:
    async def get_health(self) -> HealthResponse:
        """Return full health status of the application."""
        uptime_seconds = round(time.time() - _start_time, 2)
        return HealthResponse(
            status="healthy",
            version=settings.version,
            environment=settings.environment,
            uptime_seconds=uptime_seconds,
        )

    async def get_readiness(self) -> dict:
        """
        Check if the application is ready to handle requests.
        Extend this method to verify DB connections, caches, etc.
        """
        checks = {
            "app": "ok",
            # "database": await self._check_db(),
        }
        all_ok = all(v == "ok" for v in checks.values())
        return {
            "status": "ready" if all_ok else "not_ready",
            "checks": checks,
        }
