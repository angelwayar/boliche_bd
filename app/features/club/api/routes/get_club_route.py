from fastapi import Depends, status, HTTPException

from app.features.club.api.routes import router
from app.features.club.dependecies import get_club_use_case
from app.features.club.domain.entities.club_query import ClubRead
from app.features.club.domain.use_cases.get_club import GetClubUseCase


@router.get(
    '/{id_}/',
    response_model=ClubRead,
    status_code=status.HTTP_200_OK
)
def get_club(
        id_: int,
        get_club_use_case_: GetClubUseCase = Depends(get_club_use_case)
):
    try:
        club = get_club_use_case_((id_,))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return club
