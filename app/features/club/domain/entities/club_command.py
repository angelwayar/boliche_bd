from pydantic import BaseModel


class ClubCreate(BaseModel):
    owner_id: int
    name: str
    long: str | None
    lat: str | None
