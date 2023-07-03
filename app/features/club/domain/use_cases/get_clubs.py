from abc import abstractmethod
from typing import Sequence

from app.core.use_cases.base_use_case import BaseUseCase
from app.features.club.domain.entities.club_query import ClubRead
from app.features.club.domain.service.club_query_service import ClubQueryService


class GetClubsUseCase(BaseUseCase[None, Sequence[ClubRead]]):
    service: ClubQueryService

    @abstractmethod
    def __call__(self, args: None) -> Sequence[ClubRead]:
        raise NotImplementedError()


class GetClubsUseCaseImpl(GetClubsUseCase):
    def __init__(self, service: ClubQueryService):
        self.service: ClubQueryService = service

    def __call__(self, args: None) -> Sequence[ClubRead]:
        try:
            clubs = self.service.find_all()
        except Exception:
            raise

        return clubs
