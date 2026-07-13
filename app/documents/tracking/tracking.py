from datetime import datetime
from typing import Optional
from beanie import Document


class TrackingDocument(Document):
    ip_client: str = ""
    user_agent: str = ""
    referrer: str = ""
    language: str = ""
    screen: str = ""
    utm: str = ""
    utm_source: str = ""
    utm_medium: str = ""
    utm_campaign: str = ""
    utm_content: str = ""
    utm_term: str = ""
    date_created: datetime = datetime.now()

    class Settings:
        name = "tracking"
