from datetime import datetime
from beanie import Document
from pydantic import Field


class HealthCreateDocument(Document):
    date_created: datetime = datetime.now()

    class Settings:
        name = "health"
