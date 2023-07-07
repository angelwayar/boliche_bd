from abc import abstractmethod
from typing import cast, Tuple

from app.core.use_cases.base_use_case import BaseUseCase
from app.features.club.domain.entities.club_command import ClubUpdate
from app.features.club.domain.entities.club_entity import ClubEntity
from app.features.club.domain.entities.club_query import ClubRead
from app.features.club.domain.repositories.club_unit_of_work import ClubUnitOfWork


class UpdateClubUseCase(BaseUseCase[Tuple[int, ClubUpdate], ClubRead]):
    club_unit_of_work: ClubUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int, ClubUpdate]) -> ClubRead:
        raise NotImplementedError()


class UpdateClubUseCaseImpl(UpdateClubUseCase):
    def __init__(self, unit_of_work: ClubUnitOfWork):
        self.club_unit_of_work = unit_of_work

    def __call__(self, args: Tuple[int, ClubUpdate]) -> ClubRead:
        id_, update_data = args
        existing_club = self.club_unit_of_work.repository.find_by_id(id_)

        if existing_club is None:
            raise

        update_entity = existing_club.update_entity(
            update_data,
            get_update_data_fn=lambda club_data: club_data.dict(exclude_unset=True)
        )

        try:
            updated_club = self.club_unit_of_work.repository.update(update_entity)
            self.club_unit_of_work.commit()
        except Exception:
            self.club_unit_of_work.rollback()
            raise

        return ClubRead.from_entity(cast(ClubEntity, updated_club))
