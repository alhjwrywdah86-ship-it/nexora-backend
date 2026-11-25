from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.router import api_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

if settings.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"]
    )

app.include_router(api_router)


@app.get("/")
def root():

    return {
        "message": "Welcome to NEXORA AI"
    }
