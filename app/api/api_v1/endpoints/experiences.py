from fastapi import APIRouter
from fastapi.params import Depends

from app.auth.auth import get_current_active_user
from app.schemas.experiences import ExperienceBase
from app.documents.experiences.experiences import (
    ExperiencesDocument,
    ExperiencesCreateDocument,
)
from app.documents.users.user import UsersDocument

from typing import List
from beanie import PydanticObjectId

experience_router = APIRouter()


@experience_router.post("/", status_code=201)
async def create_experience(
    experience: ExperiencesCreateDocument,
) -> ExperienceBase:
    new_esperience = await experience.create()
    return new_esperience


@experience_router.get("/", status_code=200)
async def retrieve_experiences() -> List[ExperiencesDocument]:
    experiences = await ExperiencesDocument.find_all(limit=1000).to_list()
    return experiences


@experience_router.get("/{experience_id}", status_code=200)
async def retrieve_experience(experience_id: PydanticObjectId) -> ExperienceBase:
    experience = await ExperiencesDocument.get(experience_id)
    return experience


@experience_router.delete("/{experience_id}", status_code=204)
async def delete_experience(experience_id: PydanticObjectId):
    experience = await ExperiencesDocument.get(experience_id)
    await experience.delete()
    # Não retorna nada


# @experience_router.put("/{experience_id}", status_code=200)
# async def update_experience(
#     experience: ExperiencesCreateDocument, experience_id: PydanticObjectId
# ) -> ExperiencesDocument:
#     experience_to_update = await UsersDocument.get(experience_id)
#     if not experience_to_update:
#         raise HTTPException(status_code=404, detail="Resource not found")

#     experience_to_update.nm_email = user.nm_email
#     experience_to_update.nm_name = user.nm_name
#     await user_to_update.save()
#     return user_to_update
