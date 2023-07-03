from fastapi import Depends, status, HTTPException

from app.features.club.api.routes import router
from app.features.club.dependecies import get_clubs_use_case
from app.features.club.domain.entities.club_query import ClubRead
from app.features.club.domain.use_cases.get_clubs import GetClubsUseCase


@router.get(
    '/',
    response_model=list[ClubRead],
    status_code=status.HTTP_200_OK
)
def get_clubs(
        get_clubs_use_case_: GetClubsUseCase = Depends(get_clubs_use_case)
):
    try:
        clubs = get_clubs_use_case_(None)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if not clubs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return clubs
