from abc import abstractmethod
from typing import Sequence

from app.core.repositories.base_repository import BaseRepository
from app.features.club.domain.entities.club_entity import ClubEntity


class ClubRepository(BaseRepository[ClubEntity]):

    @abstractmethod
    def find_by_owner_id(self, owner_id: int) -> Sequence[ClubEntity]:
        raise NotImplementedError()
