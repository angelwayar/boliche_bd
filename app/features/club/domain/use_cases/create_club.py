from abc import abstractmethod
from typing import Tuple

from app.core.use_cases.base_use_case import BaseUseCase
from app.features.club.domain.entities.club_command import ClubCreate
from app.features.club.domain.entities.club_entity import ClubEntity
from app.features.club.domain.entities.club_query import ClubRead
from app.features.club.domain.repositories.club_unit_of_work import ClubUnitOfWork


class CreateClubUseCase(BaseUseCase[Tuple[ClubCreate], ClubRead]):
    unit_of_work: ClubUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[ClubCreate]) -> ClubRead:
        raise NotImplementedError()


class CreateClubUseCaseImpl(CreateClubUseCase):

    def __init__(self, unit_of_work: ClubUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[ClubCreate]) -> ClubRead:
        data, = args
        club = ClubEntity(
            id_=None,
            **data.dict()
        )

        try:
            self.unit_of_work.repository.create(club)
        except Exception as _e:
            self.unit_of_work.rollback()
            raise

        self.unit_of_work.commit()
        create_club = self.unit_of_work.repository.find_by_owner_id(club.owner_id)[0]

        return ClubRead.from_entity(create_club)
