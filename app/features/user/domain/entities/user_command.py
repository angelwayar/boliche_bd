from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    email: str = Field(example='test@test.com')
    password: str = Field(example='password')
