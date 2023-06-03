from typing import Optional
from pydantic import BaseModel


# Shared properties
class CoursesBase(BaseModel):
    nm_title: Optional[str] = None
    nm_description: Optional[str] = None
    nm_certificado: Optional[str] = None
    nm_image: Optional[str] = None
    is_active: Optional[bool] = None
