from fastapi import FastAPI
from app.router.api import router as api_router

app = FastAPI()

# API 라우터 확장
app.include_router(api_router)


