from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.features.club.data.models.club import Club
from app.features.club.domain.entities.club_query import ClubRead
from app.features.club.domain.service.club_query_service import ClubQueryService


class ClubQueryServiceImpl(ClubQueryService):
    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id_: int) -> ClubRead | None:
        result: Club | None = self.session.get(Club, id_)

        if result is None:
            return None

        return result.to_read_model()

    def find_all(self) -> Sequence[ClubRead]:
        statement = select(Club)

        result = self.session.execute(statement).scalars().all()

        if len(result) == 0:
            return []

        return [club.to_read_model() for club in result]
