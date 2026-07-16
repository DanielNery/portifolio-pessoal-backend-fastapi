import beanie
import motor
import motor.motor_asyncio
from app.documents.users.user import UsersDocument, UserCreateDocument

from app.documents.experiences.experiences import (
    ExperiencesDocument,
    ExperiencesCreateDocument,
)

from app.documents.courses.courses import CoursesCreateDocument, CoursesDocument
from app.documents.bootcamps.bootcamps import BootcampsCreateDocument, BootcampsDocument
from app.documents.hackathons.hackathons import (
    HackathonsDocument,
    HackathonsCreateDocument,
)
from app.documents.knowledges.knowledges import (
    KnowledgesCreateDocument,
    KnowledgesDocument,
)
from app.documents.projects.projects import ProjectsCreateDocument, ProjectsDocument
from app.documents.health.health import HealthCreateDocument
from app.documents.tracking.tracking import TrackingDocument

from app.core.config import settings

documents = [
    UsersDocument,
    UserCreateDocument,
    ExperiencesDocument,
    ExperiencesCreateDocument,
    CoursesCreateDocument,
    CoursesDocument,
    BootcampsCreateDocument,
    BootcampsDocument,
    HackathonsDocument,
    HackathonsCreateDocument,
    KnowledgesCreateDocument,
    KnowledgesDocument,
    ProjectsCreateDocument,
    ProjectsDocument,
    HealthCreateDocument,
    TrackingDocument,
]


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        settings.MONGODB_URL,
        serverSelectionTimeoutMS=5000,
    )
    await beanie.init_beanie(database=client.portifolio, document_models=documents)
