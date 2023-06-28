from fastapi import Depends, HTTPException, status

from app.features.user.api.routes import router
from app.features.user.dependencies import get_create_user_use_case
from app.features.user.domain.entities.user_query import UserRead
from app.features.user.domain.entities.user_command import UserCreate
from app.features.user.domain.use_cases.create_user import CreateUserUseCase


@router.post(
    '/',
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED
)
def create_user(
        data: UserCreate,
        create_user_use_case: CreateUserUseCase = Depends(get_create_user_use_case)
):
    try:
        user = create_user_use_case((data,))
    except Exception as _exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return user
