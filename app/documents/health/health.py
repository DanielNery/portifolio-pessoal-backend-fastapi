from datetime import datetime
from beanie import Document
from pydantic import Field


class HealthCreateDocument(Document):
    ip_client: str = ""
    port_client: str = ""
    headers_client: list = []
    date_created: datetime = datetime.now()

    class Settings:
        name = "health"
