import json
from fastapi import APIRouter, Request
from app.documents.health.health import HealthCreateDocument

health_router = APIRouter()


@health_router.post("/", status_code=201)
async def create_health(health: HealthCreateDocument, request: Request):
    health.ip_client = request.client[0]
    health.port_client = request.client[1]
    health.headers_client = [
        {info[0].decode("ascii"): info[1].decode("ascii")}
        for info in request.headers.raw
    ]

    new_health = await health.create()
    return new_health
