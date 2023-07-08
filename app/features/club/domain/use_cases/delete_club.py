from abc import abstractmethod
from typing import cast, Tuple

from app.core.use_cases.base_use_case import BaseUseCase
from app.features.club.domain.entities.club_entity import ClubEntity
from app.features.club.domain.entities.club_query import ClubRead
from app.features.club.domain.repositories.club_unit_of_work import ClubUnitOfWork


class DeleteClubUseCase(BaseUseCase):
    unit_of_work: ClubUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> ClubRead:
        raise NotImplementedError()


class DeleteClubUseCaseImpl(DeleteClubUseCase):

    def __init__(self, unit_of_work: ClubUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[int]) -> ClubRead:
        id_, = args

        existing_club = self.unit_of_work.repository.find_by_id(id_)

        if existing_club is None:
            raise

        marked_club = existing_club.mark_entity_as_deleted()

        try:
            deleted_club = self.unit_of_work.repository.update(marked_club)
            self.unit_of_work.commit()
        except Exception:
            self.unit_of_work.rollback()
            raise

        return ClubRead.from_entity(cast(ClubEntity, deleted_club))
