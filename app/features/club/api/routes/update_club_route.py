from fastapi import Depends, HTTPException, status

from app.features.club.api.routes import router
from app.features.club.dependecies import get_update_club_use_case
from app.features.club.domain.entities.club_command import ClubUpdate
from app.features.club.domain.entities.club_query import ClubRead
from app.features.club.domain.use_cases.update_club import UpdateClubUseCase


@router.put(
    '/{id_}',
    response_model=ClubRead,
    status_code=status.HTTP_200_OK,
)
async def update_club(
        id_: int,
        data: ClubUpdate,
        update_club_use_case_: UpdateClubUseCase = Depends(get_update_club_use_case)
):
    try:
        club = update_club_use_case_((id_, data))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return club
