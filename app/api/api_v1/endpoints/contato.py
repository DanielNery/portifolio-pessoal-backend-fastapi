from fastapi import APIRouter
from app.schemas.email import EmailContatoSchema

from typing import Any

from app.utils import (
    send_contact_email,
)

contato_router = APIRouter()


@contato_router.post(
    "/{email_to}",
)
def contact_form(email_contato: EmailContatoSchema, email_to: str) -> Any:
    send_contact_email(
        email_to=email_to, name=email_contato.name, message=email_contato.message
    )
    return {
        "msg": "Email de contato enviado com sucesso, retornarei no prazo de 48 horas!"
    }
