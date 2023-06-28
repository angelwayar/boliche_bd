from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database.database import get_session
from app.features.user.data.repository.repository_impl import UserRepositoryImpl
from app.features.user.data.repository.unit_of_work_impl import UserUnitOfWorkImpl
from app.features.user.domain.repositories.user_repository import UserRepository
from app.features.user.domain.repositories.user_unit_of_work import UserUnitOfWork
from app.features.user.domain.use_cases.create_user import CreateUserUseCase, CreateUserUseCaseImpl


def get_user_repository(session: Session = Depends(get_session)) -> UserRepository:
    return UserRepositoryImpl(session=session)


def get_user_unit_of_work(
        session: Session = Depends(get_session),
        user_repository: UserRepository = Depends(get_user_repository)
) -> UserUnitOfWork:
    return UserUnitOfWorkImpl(session=session, user_repository=user_repository)


def get_create_user_use_case(
        unit_of_work: UserUnitOfWork = Depends(get_user_unit_of_work)
) -> CreateUserUseCase:
    return CreateUserUseCaseImpl(unit_of_work=unit_of_work)
