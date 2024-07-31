import uuid
import re

from pydantic import BaseModel, EmailStr
from fastapi import HTTPException


# LETTER_MATCH_PATTERN = re.compile(r'^[а-яА-Яa-zA-Z\-]+$]')


class TunedModel(BaseModel):    
    class Config:
        from_attributes = True


class ShowUser(TunedModel):
    user_id: uuid.UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool


class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr

    # @field_validator("name")
    # def validate_name(cls, value) -> str:
    #     if not LETTER_MATCH_PATTERN.match(value):
    #         raise HTTPException(
    #             status_code=422, detail="Name must contain only letters"
    #         )
    #     return value
    #
    # @field_validator("surname")
    # def validate_name(cls, value):
    #     if not LETTER_MATCH_PATTERN.match(value):
    #         raise HTTPException(
    #             status_code=422, detail="Surname must contain only letters"
    #         )
    #     return value