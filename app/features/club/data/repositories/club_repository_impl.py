from typing import Sequence

from sqlalchemy import select, update, delete
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
        result: Club | None = self.session.get(Club, id_)

        if result is None:
            return None

        return result.to_entity()

    def update(self, entity: ClubEntity) -> ClubEntity:
        club = Club.from_entity(entity)
        update_data = club.to_dict()

        # for key in [Club.updated_at.key, Club.created_at.key, Club.updated_at.key]:
        for key in [Club.updated_at.key, Club.created_at.key]:
            update_data.pop(key)

        statement = update(
            Club
        ).filter_by(
            id_=club.id_
        ).values(
            update_data
        ).returning(
            Club
        )

        club_mapping: Club | None = self.session.execute(statement=statement).fetchone()
        if club_mapping is None:
            raise

        result, = club_mapping

        return result.to_entity()

    def delete_by_id(self, id_: int) -> ClubEntity:
        statement = delete(Club).filter_by(id_=id_).returning(*Club.__table__.columns)

        result: Club = self.session.execute(statement=statement).scalar_one()

        return result.to_entity()

    def find_by_owner_id(self, owner_id: int) -> Sequence[ClubEntity]:
        statement = select(Club).filter_by(owner_id=owner_id).order_by(Club.created_at.desc())

        try:
            result: Sequence[Club] = self.session.execute(statement).scalars().all()
        except Exception as _e:
            return []

        return [club.to_entity() for club in result]
