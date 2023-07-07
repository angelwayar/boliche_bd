from pydantic import BaseModel, Field


class ClubCreate(BaseModel):
    owner_id: int
    name: str
    long: str | None
    lat: str | None


class ClubUpdate(BaseModel):
    name: str
    long: str | None
    lat: str | None
    is_deleted: bool = Field(example=False)
