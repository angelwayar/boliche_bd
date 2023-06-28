from datetime import datetime


class ClubEntity:
    def __init__(
            self,
            id_: int | None,
            name: str,
            long: str | None,
            lat: str | None,
            owner_id: int,
            created_at: datetime | None = None,
            updated_at: datetime | None = None,
            is_deleted: bool | None = False,
    ):
        self.id_ = id_
        self.owner_id = owner_id
        self.name = name
        self.long = long
        self.lat = lat
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_deleted = is_deleted
