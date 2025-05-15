from fastapi import FastAPI
from app.api.v1.routes import router
from app.core.config import settings

app = FastAPI(title=settings.app_name, version=settings.version)
app.include_router(router, prefix="/api/v1")
