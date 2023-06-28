from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from app.core.models.base_model import Base
from app.features.club.domain.entities.club_entity import ClubEntity


class Club(Base):
    __tablename__ = 'clubs'

    owner_id: Mapped[int] = Column(Integer, ForeignKey('users.id_'))
    name: Mapped[str] = Column(String)
    long: Mapped[str | None]
    lat: Mapped[str | None]

    owner: Mapped['User'] = relationship('User', back_populates='clubs', uselist=False)

    def to_entity(self) -> ClubEntity:
        return ClubEntity(
            id_=self.id_,
            name=self.name,
            long=self.long,
            lat=self.lat,
            owner_id=self.owner_id,
            updated_at=self.updated_at,
            created_at=self.created_at
        )

    @staticmethod
    def from_entity(club: ClubEntity) -> 'Club':
        return Club(
            id_=club.id_,
            name=club.name,
            long=club.long,
            lat=club.lat,
            owner_id=club.owner_id,
            updated_at=club.updated_at,
            created_at=club.created_at
        )
