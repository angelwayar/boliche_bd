from datetime import datetime


class UserEntity:
    def __init__(
            self,
            id_: int | None,
            email: str,
            password: str,
            created_at: datetime | None = None,
            updated_at: datetime | None = None,
            is_deleted: bool | None = False

    ):
        self.id_ = id_
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_deleted = is_deleted
