from fastapi import FastAPI
from app.routes.health import router as health_router
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description=(
        "⚠️ **Under Deployment — Not a Stable Release.** "
        "APIs and features are subject to breaking changes without notice.\n\n"
        "LLMs often struggle with mathematical problems because they rely on probabilistic "
        "text generation rather than reliable computation. **MathKit** bridges this gap by "
        "providing a computational layer that helps LLMs solve complex equations, perform "
        "calculations, and verify results — instead of relying solely on generated responses."
    ),
)

app.include_router(health_router, prefix="/api/v1", tags=["health"])


@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.app_name}"}
