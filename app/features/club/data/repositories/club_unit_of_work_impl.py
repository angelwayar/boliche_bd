from sqlalchemy.orm import Session

from app.features.club.domain.repositories.club_repository import ClubRepository
from app.features.club.domain.repositories.club_unit_of_work import ClubUnitOfWork


class ClubUnitOfWorkImpl(ClubUnitOfWork):
    def __init__(self, session: Session, club_repository: ClubRepository):
        self.session: Session = session
        self.repository: ClubRepository = club_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
