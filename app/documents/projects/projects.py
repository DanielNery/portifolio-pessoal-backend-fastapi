from datetime import datetime
from beanie import Document
from pydantic import Field


class ProjectsDocument(Document):
    nm_title: str = ""
    nm_type: str = ""
    nm_description: str = ""
    nm_image: str = ""
    nm_slug: str = ""
    is_active: bool = False
    date_created: datetime = datetime.now()

    class Settings:
        name = "projects"

    class Config:
        schema_extra = {
            "nm_title": "A sample content",
            "nm_image": "A sample content",
            "nm_description": "A sample content",
            "nm_type": "A sample content",
            "nm_slug": "A sample content",
            "is_active": True,
            "date_created": datetime.now(),
        }


class ProjectsCreateDocument(Document):
    nm_title: str = Field()
    nm_description: str = Field()
    nm_type: str = Field()
    nm_image: str = Field()
    nm_slug: str = Field()
    is_active: bool = False
    date_created: datetime = datetime.now()

    class Settings:
        name = "projects"

    class Config:
        schema_extra = {
            "nm_type": "Teste",
            "nm_title": "A sample content",
            "nm_description": "A sample content",
            "nm_slug": "aaaa",
            "is_active": True,
            "date_created": datetime.now(),
        }
