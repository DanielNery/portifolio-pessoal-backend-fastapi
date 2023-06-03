from fastapi import APIRouter
from fastapi.params import Depends

from app.auth.auth import get_current_active_user
from app.schemas.bootcamps import BootcampsBase
from app.documents.bootcamps.bootcamps import (
    BootcampsDocument,
    BootcampsCreateDocument,
)
from app.documents.users.user import UsersDocument

from typing import List
from beanie import PydanticObjectId

bootcamp_router = APIRouter()


@bootcamp_router.post("/", status_code=201)
async def create_bootcamp(
    bootcamp: BootcampsCreateDocument,
) -> BootcampsBase:
    new_esperience = await bootcamp.create()
    return new_esperience


@bootcamp_router.get("/", status_code=200)
async def retrieve_bootcamps(
    current_user: UsersDocument = Depends(get_current_active_user),
) -> List[BootcampsDocument]:
    bootcamps = await BootcampsDocument.find_all(limit=1000).to_list()
    return bootcamps


@bootcamp_router.get("/{bootcamp_id}", status_code=200)
async def retrieve_bootcamp(bootcamp_id: PydanticObjectId) -> BootcampsBase:
    bootcamp = await BootcampsDocument.get(bootcamp_id)
    return bootcamp


@bootcamp_router.delete("/{bootcamp_id}", status_code=204)
async def delete_bootcamp(bootcamp_id: PydanticObjectId) -> BootcampsBase:
    bootcamp = await BootcampsDocument.get(bootcamp_id)
    await bootcamp.delete()
    return bootcamp


# @bootcamp_router.put("/{bootcamp_id}", status_code=200)
# async def update_bootcamp(
#     bootcamp: BootcampsCreateDocument, bootcamp_id: PydanticObjectId
# ) -> BootcampsDocument:
#     bootcamp_to_update = await UsersDocument.get(bootcamp_id)
#     if not bootcamp_to_update:
#         raise HTTPException(status_code=404, detail="Resource not found")

#     bootcamp_to_update.nm_email = user.nm_email
#     bootcamp_to_update.nm_name = user.nm_name
#     await user_to_update.save()
#     return user_to_update
