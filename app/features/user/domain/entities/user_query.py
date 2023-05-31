from datetime import datetime

from pydantic import BaseModel, Field

from app.features.user.domain.entities.user_entity import UserEntity


class UserRead(BaseModel):
    id_: int = Field(example=1)
    email: str = Field(example='test@test.com')
    created_at = datetime
    updated_at = datetime
    is_deleted: bool = Field(example=False)

    @staticmethod
    def from_entity(entity: UserEntity) -> 'UserRead':
        return UserRead(
            id_=entity.id_,
            email=entity.email,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            is_deleted=entity.is_deleted,
        )