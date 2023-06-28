from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped

from app.core.models.base_model import Base
from app.features.user.domain.entities.user_entity import UserEntity


class User(Base):
    __tablename__ = 'users'

    email: Mapped[str] = Column(String, unique=True, index=True)
    password: Mapped[str] = Column(String)

    def to_entity(self) -> UserEntity:
        return UserEntity(
            id_=self.id_,
            email=self.email,
            password=self.password
        )

    @staticmethod
    def from_entity(user: UserEntity) -> 'User':
        return User(
            id_=user.id_,
            email=user.email,
            password=user.password
        )
