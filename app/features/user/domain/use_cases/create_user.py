from abc import abstractmethod
from typing import cast, Tuple

from app.core.use_cases.base_use_case import BaseUseCase
from app.features.user.domain.entities.user_command import UserCreate
from app.features.user.domain.entities.user_entity import UserEntity
from app.features.user.domain.entities.user_query import UserRead
from app.features.user.domain.repositories.user_unit_of_work import UserUnitOfWork


class CreateUserUseCase(BaseUseCase[Tuple[UserCreate], UserRead]):
    unit_of_work: UserUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[UserCreate]) -> UserRead:
        raise NotImplementedError()


class CreateUserUseCaseImpl(CreateUserUseCase):

    def __init__(self, unit_of_work: UserUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[UserCreate]) -> UserRead:
        data, = args
        user = UserEntity(
            id_=None,
            **data.dict()
        )

        existing_user = self.unit_of_work.repository.find_by_email(email=data.email)

        if existing_user is not None:
            # TODO: Se deben de agregar el error de useralreadyexist
            raise

        try:
            self.unit_of_work.repository.create(entity=user)
        except Exception as _e:
            self.unit_of_work.rollback()
            raise

        self.unit_of_work.commit()

        created_user = self.unit_of_work.repository.find_by_email(email=data.email)

        return UserRead.from_entity(entity=cast(UserEntity, created_user))
