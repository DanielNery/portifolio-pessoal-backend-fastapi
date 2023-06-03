from fastapi import APIRouter

from app.api.api_v1.endpoints import (
    login,
    users,
    experiences,
    courses,
    bootcamps,
    hackathons,
    knowledges,
    projects,
)

api_router = APIRouter()
api_router.include_router(login.login_router, tags=["login"])
api_router.include_router(users.user_router, prefix="/users", tags=["users"])

api_router.include_router(
    experiences.experience_router, prefix="/experiences", tags=["experiences"]
)

api_router.include_router(
    bootcamps.bootcamp_router, prefix="/bootcamps", tags=["bootcamps"]
)

api_router.include_router(courses.course_router, prefix="/courses", tags=["courses"])

api_router.include_router(
    hackathons.hackathon_router, prefix="/hackathons", tags=["hackathons"]
)
api_router.include_router(
    projects.project_router, prefix="/projects", tags=["projects"]
)

api_router.include_router(
    knowledges.knowledge_router, prefix="/knowledge", tags=["knowledges"]
)
