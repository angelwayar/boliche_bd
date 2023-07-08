from fastapi import HTTPException, Depends, status

from app.features.club.api.routes import router
from app.features.club.dependecies import get_delete_use_case
from app.features.club.domain.entities.club_query import ClubRead
from app.features.club.domain.use_cases.delete_club import DeleteClubUseCase


@router.delete(
    '/{id_}',
    response_model=ClubRead,
    status_code=status.HTTP_200_OK
)
def delete_club(
        id_: int,
        delete_club_use_case_: DeleteClubUseCase = Depends(get_delete_use_case)
):
    try:
        club = delete_club_use_case_((id_,))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return club
