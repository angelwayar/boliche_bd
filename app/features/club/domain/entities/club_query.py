from datetime import datetime

from pydantic import BaseModel

from app.features.club.domain.entities.club_entity import ClubEntity


class ClubRead(BaseModel):
    id_: int
    owner_id: int
    name: str
    long: str | None
    lat: str | None
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_entity(cls, entity: ClubEntity) -> 'ClubRead':
        return cls(
            id_=entity.id_,
            owner_id=entity.owner_id,
            name=entity.name,
            long=entity.long,
            lat=entity.lat,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
