from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.features.user.data.models.user import User
from app.features.user.domain.entities.user_entity import UserEntity
from app.features.user.domain.repositories.user_repository import UserRepository


class UserRepositoryImpl(UserRepository):

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_email(self, email: str) -> UserEntity | None:
        statement = select(User).filter_by(email=email)

        try:
            result: User = self.session.execute(statement).scalar_one()
        except Exception as exception:
            return None

        return result.to_entity()

    def create(self, entity: UserEntity) -> UserEntity:
        user = User.from_entity(user=entity)
        self.session.add(user)

        return user.to_entity()

    def find_all(self, entity: UserEntity) -> Sequence[UserEntity]:
        pass

    def find_by_id(self, id_: int) -> UserEntity | None:
        pass

    def update(self, entity: UserEntity) -> UserEntity:
        pass

    def delete_by_id(self, id_: int) -> UserEntity:
        pass
