from datetime import datetime
from beanie import Document
from pydantic import Field


class ExperiencesDocument(Document):
    nm_year: str = ""
    nm_title: str = ""
    nm_description: str = ""
    is_active: bool = False
    date_created: datetime = datetime.now()

    class Settings:
        name = "experiences"

    class Config:
        schema_extra = {
            "nm_year": "2023",
            "nm_title": "A sample content",
            "nm_description": "A sample content",
            "is_active": True,
            "date_created": datetime.now(),
        }


class ExperiencesCreateDocument(Document):
    nm_year: str = Field()
    nm_title: str = Field()
    nm_description: str = Field()
    is_active: bool = False
    date_created: datetime = datetime.now()

    class Settings:
        name = "experiences"

    class Config:
        schema_extra = {
            "nm_year": "2023",
            "nm_title": "A sample content",
            "nm_description": "A sample content",
            "is_active": True,
            "date_created": datetime.now(),
        }
