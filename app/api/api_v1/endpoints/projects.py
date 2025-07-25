from fastapi import APIRouter
from fastapi.params import Depends

from app.auth.auth import get_current_active_user
from app.schemas.projects import ProjectsBase
from app.documents.projects.projects import (
    ProjectsDocument,
    ProjectsCreateDocument,
)
from app.documents.users.user import UsersDocument

from typing import List
from beanie import PydanticObjectId

project_router = APIRouter()


@project_router.post("/", status_code=201)
async def create_project(
    project: ProjectsCreateDocument,
) -> ProjectsBase:
    new_esperience = await project.create()
    return new_esperience


@project_router.get("/", status_code=200)
async def retrieve_projects() -> List[ProjectsDocument]:
    projects = await ProjectsDocument.find_all(limit=1000).to_list()
    return projects


@project_router.get("/{project_id}", status_code=200)
async def retrieve_project(project_id: PydanticObjectId) -> ProjectsBase:
    project = await ProjectsDocument.get(project_id)
    return project


@project_router.delete("/{project_id}", status_code=204)
async def delete_project(project_id: PydanticObjectId):
    project = await ProjectsDocument.get(project_id)
    await project.delete()
    # Não retorna nada


# @project_router.put("/{project_id}", status_code=200)
# async def update_project(
#     project: ProjectsCreateDocument, project_id: PydanticObjectId
# ) -> ProjectsDocument:
#     project_to_update = await UsersDocument.get(project_id)
#     if not project_to_update:
#         raise HTTPException(status_code=404, detail="Resource not found")

#     project_to_update.nm_email = user.nm_email
#     project_to_update.nm_name = user.nm_name
#     await user_to_update.save()
#     return user_to_update
