from fastapi import APIRouter
from fastapi.params import Depends

from app.auth.auth import get_current_active_user
from app.schemas.courses import CoursesBase
from app.documents.courses.courses import (
    CoursesDocument,
    CoursesCreateDocument,
)
from app.documents.users.user import UsersDocument

from typing import List
from beanie import PydanticObjectId

course_router = APIRouter()


@course_router.post("/", status_code=201)
async def create_course(
    course: CoursesCreateDocument,
) -> CoursesBase:
    new_esperience = await course.create()
    return new_esperience


@course_router.get("/", status_code=200)
async def retrieve_courses(
    current_user: UsersDocument = Depends(get_current_active_user),
) -> List[CoursesDocument]:
    courses = await CoursesDocument.find_all(limit=1000).to_list()
    return courses


@course_router.get("/{course_id}", status_code=200)
async def retrieve_course(course_id: PydanticObjectId) -> CoursesBase:
    course = await CoursesDocument.get(course_id)
    return course


@course_router.delete("/{course_id}", status_code=204)
async def delete_course(course_id: PydanticObjectId):
    course = await CoursesDocument.get(course_id)
    await course.delete()
    # Não retorna nada


# @course_router.put("/{course_id}", status_code=200)
# async def update_course(
#     course: CoursesCreateDocument, course_id: PydanticObjectId
# ) -> CoursesDocument:
#     course_to_update = await UsersDocument.get(course_id)
#     if not course_to_update:
#         raise HTTPException(status_code=404, detail="Resource not found")

#     course_to_update.nm_email = user.nm_email
#     course_to_update.nm_name = user.nm_name
#     await user_to_update.save()
#     return user_to_update
