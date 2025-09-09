from fastapi import APIRouter, HTTPException, Query

from src.models.user import User, UserListResponse
from src.services import user_service

router = APIRouter()


@router.get('/', response_model=UserListResponse)
def get_user(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
    q: str | None = None,
    role: str | None = None,
    is_active: str | None = None,
):
    return user_service.get_users(page, page_size, q, role, is_active)


@router.get("/{user_id}", response_model=User)
def get_user_by_id(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user
