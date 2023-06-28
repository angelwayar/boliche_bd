from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.features.club.data.models.club import Club
from app.features.club.domain.entities.club_entity import ClubEntity
from app.features.club.domain.repositories.club_repository import ClubRepository


class ClubRepositoryImpl(ClubRepository):

    def __init__(self, session: Session):
        self.session: Session = session

    def create(self, entity: ClubEntity) -> ClubEntity:
        club = Club.from_entity(club=entity)
        self.session.add(club)

        return club.to_entity()

    def find_all(self, entity: ClubEntity) -> Sequence[ClubEntity]:
        pass

    def find_by_id(self, id_: int) -> ClubEntity | None:
        pass

    def update(self, entity: ClubEntity) -> ClubEntity:
        pass

    def delete_by_id(self, id_: int) -> ClubEntity:
        pass

    def find_by_owner_id(self, owner_id: int) -> Sequence[ClubEntity]:
        statement = select(Club).filter_by(owner_id=owner_id).order_by(Club.created_at.desc())

        try:
            result: Sequence[Club] = self.session.execute(statement).scalars().all()
        except Exception as _e:
            return []

        return [club.to_entity() for club in result]
