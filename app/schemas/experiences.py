from typing import Optional
from pydantic import BaseModel


# Shared properties
class ExperienceBase(BaseModel):
    nm_year: str = ""
    nm_title: Optional[str] = None
    nm_description: Optional[str] = None
    is_active: Optional[bool] = None
