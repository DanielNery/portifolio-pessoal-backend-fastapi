from typing import Optional
from pydantic import BaseModel


# Shared properties
class EmailContatoSchema(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    message: Optional[str] = None
    utm: Optional[str] = None
