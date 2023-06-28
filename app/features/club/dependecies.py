from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database.database import get_session
from app.features.club.data.repositories.club_repository_impl import ClubRepositoryImpl
from app.features.club.data.repositories.club_unit_of_work_impl import ClubUnitOfWorkImpl
from app.features.club.domain.repositories.club_repository import ClubRepository
from app.features.club.domain.repositories.club_unit_of_work import ClubUnitOfWork
from app.features.club.domain.use_cases.create_club import CreateClubUseCase, CreateClubUseCaseImpl


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
