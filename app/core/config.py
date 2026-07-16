import os
import secrets

from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, EmailStr, field_validator, validator
from typing import List, Optional, Dict, Any


def get_optional_env(name: str) -> Optional[str]:
    value = os.environ.get(name)
    return value or None


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SERVER_HOST: AnyHttpUrl = "http://localhost"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "Daniel Pontes Nery"
    FIRST_SUPERUSER: EmailStr = "danielpontesnery@gmail.com"
    FIRST_SUPERUSER_PASSWORD: str = "admin"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # Set to enviroment
    SECRET_KEY: str = secrets.token_urlsafe(32)
    MONGODB_URL: str = os.environ.get("MONGODB_URL", "mongodb://localhost:27017")

    SMTP_TLS: bool = False
    SMTP_SSL: bool = False
    SMTP_PORT: Optional[int] = get_optional_env("SMTP_PORT")
    SMTP_HOST: Optional[str] = get_optional_env("SMTP_HOST")
    SMTP_USER: Optional[str] = get_optional_env("SMTP_USER")
    SMTP_PASSWORD: Optional[str] = get_optional_env("SMTP_PASSWORD")
    EMAILS_FROM_EMAIL: Optional[EmailStr] = "grapedev.schools@gmail.com"
    EMAILS_FROM_NAME: Optional[str] = "Grape"

    @validator("EMAILS_FROM_NAME")
    def get_project_name(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if not v:
            return values["PROJECT_NAME"]
        return v

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = get_optional_env("EMAIL_TEMPLATES_PATH") or "app/email/templates"
    EMAILS_ENABLED: bool = False

    @field_validator(
        "SMTP_PORT",
        "SMTP_HOST",
        "SMTP_USER",
        "SMTP_PASSWORD",
        mode="before",
    )
    @classmethod
    def empty_string_to_none(cls, v: Any) -> Any:
        if v == "":
            return None
        return v

    @validator("EMAILS_ENABLED", pre=True)
    def get_emails_enabled(cls, v: bool, values: Dict[str, Any]) -> bool:
        return bool(
            values.get("SMTP_HOST")
            and values.get("SMTP_PORT")
            and values.get("EMAILS_FROM_EMAIL")
        )

    class Config:
        case_sensitive = True


settings = Settings()
