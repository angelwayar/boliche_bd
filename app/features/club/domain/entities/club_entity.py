import copy
from datetime import datetime
from typing import Any, Callable

from app.features.club.domain.entities.club_command import ClubUpdate

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

    def update_entity(
            self,
            entity_update_model: 'ClubUpdate',
            get_update_data_fn: Callable[['ClubUpdate'], dict[str, Any]]
    ) -> 'ClubEntity':
        update_data = get_update_data_fn(entity_update_model)
        update_entity = copy.deepcopy(self)

        for attr_name, value in update_data.items():
            update_entity.__setattr__(attr_name, value)

        return update_entity
