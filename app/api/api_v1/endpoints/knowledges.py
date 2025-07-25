from fastapi import APIRouter
from fastapi.params import Depends

from app.auth.auth import get_current_active_user
from app.schemas.knowledges import KnowledgesBase
from app.documents.knowledges.knowledges import (
    KnowledgesDocument,
    KnowledgesCreateDocument,
)
from app.documents.users.user import UsersDocument

from typing import List
from beanie import PydanticObjectId

knowledge_router = APIRouter()


@knowledge_router.post("/", status_code=201)
async def create_knowledge(
    knowledge: KnowledgesCreateDocument,
) -> KnowledgesBase:
    new_esperience = await knowledge.create()
    return new_esperience


@knowledge_router.get("/", status_code=200)
async def retrieve_knowledges() -> List[KnowledgesDocument]:
    knowledges = await KnowledgesDocument.find_all(limit=1000).to_list()
    return knowledges


@knowledge_router.get("/{knowledge_id}", status_code=200)
async def retrieve_knowledge(knowledge_id: PydanticObjectId) -> KnowledgesBase:
    knowledge = await KnowledgesDocument.get(knowledge_id)
    return knowledge


@knowledge_router.delete("/{knowledge_id}", status_code=200)
async def delete_knowledge(knowledge_id: PydanticObjectId) -> KnowledgesBase:
    knowledge = await KnowledgesDocument.get(knowledge_id)
    await knowledge.delete()
    return knowledge


# @knowledge_router.put("/{knowledge_id}", status_code=200)
# async def update_knowledge(
#     knowledge: KnowledgesCreateDocument, knowledge_id: PydanticObjectId
# ) -> KnowledgesDocument:
#     knowledge_to_update = await UsersDocument.get(knowledge_id)
#     if not knowledge_to_update:
#         raise HTTPException(status_code=404, detail="Resource not found")

#     knowledge_to_update.nm_email = user.nm_email
#     knowledge_to_update.nm_name = user.nm_name
#     await user_to_update.save()
#     return user_to_update
