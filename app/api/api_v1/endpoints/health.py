import json
from fastapi import APIRouter, Request
from app.documents.health.health import HealthCreateDocument

health_router = APIRouter()


@health_router.post("", status_code=201)
async def create_health(health: HealthCreateDocument, request: Request):
    forwarded_for = request.headers.get("x-forwarded-for")
    if forwarded_for:
        health.ip_client = forwarded_for.split(",")[0].strip()
    elif request.client:
        health.ip_client = request.client.host
        health.port_client = str(request.client.port)

    health.headers_client = [
        {info[0].decode("ascii"): info[1].decode("ascii")}
        for info in request.headers.raw
    ]

    new_health = await health.create()
    return new_health
