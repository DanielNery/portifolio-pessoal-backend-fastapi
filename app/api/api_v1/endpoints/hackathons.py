from fastapi import APIRouter
from fastapi.params import Depends

from app.auth.auth import get_current_active_user
from app.schemas.hackathons import HackathonsBase
from app.documents.hackathons.hackathons import (
    HackathonsDocument,
    HackathonsCreateDocument,
)
from app.documents.users.user import UsersDocument

from typing import List
from beanie import PydanticObjectId

hackathon_router = APIRouter()


@hackathon_router.post("/", status_code=201)
async def create_hackathon(
    hackathon: HackathonsCreateDocument,
) -> HackathonsBase:
    new_esperience = await hackathon.create()
    return new_esperience


@hackathon_router.get("/", status_code=200)
async def retrieve_hackathons(
    current_user: UsersDocument = Depends(get_current_active_user),
) -> List[HackathonsDocument]:
    hackathons = await HackathonsDocument.find_all(limit=1000).to_list()
    return hackathons


@hackathon_router.get("/{hackathon_id}", status_code=200)
async def retrieve_hackathon(hackathon_id: PydanticObjectId) -> HackathonsBase:
    hackathon = await HackathonsDocument.get(hackathon_id)
    return hackathon


@hackathon_router.delete("/{hackathon_id}", status_code=204)
async def delete_hackathon(hackathon_id: PydanticObjectId) -> HackathonsBase:
    hackathon = await HackathonsDocument.get(hackathon_id)
    await hackathon.delete()
    return hackathon


# @hackathon_router.put("/{hackathon_id}", status_code=200)
# async def update_hackathon(
#     hackathon: HackathonsCreateDocument, hackathon_id: PydanticObjectId
# ) -> HackathonsDocument:
#     hackathon_to_update = await UsersDocument.get(hackathon_id)
#     if not hackathon_to_update:
#         raise HTTPException(status_code=404, detail="Resource not found")

#     hackathon_to_update.nm_email = user.nm_email
#     hackathon_to_update.nm_name = user.nm_name
#     await user_to_update.save()
#     return user_to_update
