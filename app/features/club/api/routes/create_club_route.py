from fastapi import Depends, HTTPException, status

from app.features.club.api.routes import router
from app.features.club.dependecies import get_create_club_use_case
from app.features.club.domain.entities.club_command import ClubCreate
from app.features.club.domain.entities.club_query import ClubRead
from app.features.club.domain.use_cases.create_club import CreateClubUseCase


@router.post(
    '/',
    response_model=ClubRead,
    status_code=status.HTTP_201_CREATED
)
def create_club(
        data: ClubCreate,
        create_club_use_case: CreateClubUseCase = Depends(get_create_club_use_case)
):
    try:
        club = create_club_use_case((data,))
    except Exception as _e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return club
