from abc import abstractmethod
from typing import Tuple

from app.core.use_cases.base_use_case import BaseUseCase
from app.features.club.domain.entities.club_query import ClubRead
from app.features.club.domain.service.club_query_service import ClubQueryService


class GetClubUseCase(BaseUseCase[Tuple[int], ClubRead]):
    service: ClubQueryService

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> ClubRead:
        raise NotImplementedError()


class GetClubUseCaseImpl(GetClubUseCase):
    def __init__(self, service: ClubQueryService):
        self.service: ClubQueryService = service

    def __call__(self, args: Tuple[int]) -> ClubRead:
        id_, = args
        try:
            club = self.service.find_by_id(id_)
            if club is None:
                raise
        except Exception:
            raise
        return club
