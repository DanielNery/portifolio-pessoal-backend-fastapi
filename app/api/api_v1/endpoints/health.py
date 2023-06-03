from fastapi import APIRouter
from app.documents.health.health import HealthCreateDocument

health_router = APIRouter()


@health_router.post("/", status_code=201)
async def create_health(health: HealthCreateDocument):
    new_health = await health.create()
    return new_health
