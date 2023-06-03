from typing import Optional
from pydantic import BaseModel


# Shared properties
class EmailContatoSchema(BaseModel):
    name: Optional[str] = None
    message: Optional[str] = None
