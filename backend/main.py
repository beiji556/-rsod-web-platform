from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.config import settings
from app.api.detection import router as detection_router
from app.utils.file_utils import ensure_directories

ensure_directories()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="遥感目标检测平台后端API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(detection_router, prefix="/api")


@app.get("/")
async def root():
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "status": "running"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/api/test/connect")
async def test_connect():
    return {"code": 200, "message": "前后端连通成功！"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug
    )
