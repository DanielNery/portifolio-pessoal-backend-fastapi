from datetime import datetime
from beanie import Document
from pydantic import Field


class BootcampsDocument(Document):
    nm_title: str = ""
    nm_description: str = ""
    nm_certificado: str = ""
    is_active: bool = False
    nm_image: str = ""
    date_created: datetime = datetime.now()

    class Settings:
        name = "bootcamps"

    class Config:
        schema_extra = {
            "nm_certificado": "teste",
            "nm_title": "A sample content",
            "nm_description": "A sample content",
            "nm_image": "A sample content",
            "is_active": True,
            "date_created": datetime.now(),
        }


class BootcampsCreateDocument(Document):
    nm_title: str = Field()
    nm_description: str = Field()
    nm_certificado: str = Field()
    is_active: bool = False
    nm_image: str = Field()
    date_created: datetime = datetime.now()

    class Settings:
        name = "bootcamps"

    class Config:
        schema_extra = {
            "nm_certificado": "teste",
            "nm_title": "A sample content",
            "nm_description": "A sample content",
            "nm_image": "A sample content",
            "is_active": True,
            "date_created": datetime.now(),
        }
