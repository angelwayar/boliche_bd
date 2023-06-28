from app.core.unit_of_work.base_unit_of_work import AbstractUnitOfWork
from app.features.club.domain.repositories.club_repository import ClubRepository


class ClubUnitOfWork(AbstractUnitOfWork[ClubRepository]):
    pass
