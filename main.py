from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from mangum import Mangum

from app.api.api_v1.api import api_router
from app.database.session import init_db
from app.core.config import settings

import logging
import tracemalloc
tracemalloc.start()


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def connect():
    try:
        await init_db()
    except Exception:
        logging.exception("Failed to initialize MongoDB connection")
        raise

app.include_router(api_router, prefix=settings.API_V1_STR)

handler = Mangum(app)
