from typing import Optional
from pydantic import BaseModel


# Shared properties
class KnowledgesBase(BaseModel):
    nm_title: Optional[str] = None
    nm_description: Optional[str] = None
    nm_image: Optional[str] = None
    nm_certificado: Optional[str] = None
    is_active: Optional[bool] = None
