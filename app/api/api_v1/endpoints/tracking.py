from fastapi import APIRouter, Request
from app.documents.tracking.tracking import TrackingDocument

tracking_router = APIRouter()


def _extract_ip(request: Request) -> str:
    forwarded_for = request.headers.get("x-forwarded-for")
    if forwarded_for:
        return forwarded_for.split(",")[0].strip()
    if request.client:
        return request.client.host
    return ""


@tracking_router.post("/", status_code=201)
async def register_access(payload: TrackingDocument, request: Request):
    payload.ip_client = _extract_ip(request)
    payload.user_agent = request.headers.get("user-agent", payload.user_agent)

    record = await payload.create()
    return record
