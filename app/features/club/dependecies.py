from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database.database import get_session
from app.features.club.data.repositories.club_repository_impl import ClubRepositoryImpl
from app.features.club.data.repositories.club_unit_of_work_impl import ClubUnitOfWorkImpl
from app.features.club.data.services.club_query_service_impl import ClubQueryServiceImpl
from app.features.club.domain.repositories.club_repository import ClubRepository
from app.features.club.domain.repositories.club_unit_of_work import ClubUnitOfWork
from app.features.club.domain.service.club_query_service import ClubQueryService
from app.features.club.domain.use_cases.create_club import CreateClubUseCase, CreateClubUseCaseImpl
from app.features.club.domain.use_cases.get_club import GetClubUseCase, GetClubUseCaseImpl
from app.features.club.domain.use_cases.get_clubs import GetClubsUseCase, GetClubsUseCaseImpl


def get_club_query_service(session: Session = Depends(get_session)) -> ClubQueryService:
    return ClubQueryServiceImpl(session)


def get_club_repository(session: Session = Depends(get_session)) -> ClubRepository:
    return ClubRepositoryImpl(session=session)


def get_club_unit_of_work(
        session: Session = Depends(get_session),
        club_repository: ClubRepository = Depends(get_club_repository)
) -> ClubUnitOfWork:
    return ClubUnitOfWorkImpl(session=session, club_repository=club_repository)


def get_create_club_use_case(
        unit_of_work: ClubUnitOfWork = Depends(get_club_unit_of_work)
) -> CreateClubUseCase:
    return CreateClubUseCaseImpl(unit_of_work=unit_of_work)


def get_clubs_use_case(
        club_query_service: ClubQueryService = Depends(get_club_query_service)
) -> GetClubsUseCase:
    return GetClubsUseCaseImpl(club_query_service)


def get_club_use_case(
        club_query_service: ClubQueryService = Depends(get_club_query_service)
) -> GetClubUseCase:
    return GetClubUseCaseImpl(club_query_service)
