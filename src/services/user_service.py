from datetime import datetime

from src.repositories import user_repository


def get_users(page: int, page_size: int, q: str = None, role: str = None, is_active: str = None):
    users = user_repository.find_all()

    # Filtro por nome/email
    if q:
        q = q.lower()
        # Verifica se a palavra está contida no email e ou no nome.
        users = [usuario for usuario in users if q in usuario["name"].lower() or q in usuario["email"].lower()]

    # Filtro por role
    if role:
        # Verifica ser a role é igual
        users = [usuario for usuario in users if usuario["role"] == role]

    # Filtro por ativo
    # Verifica se o parametro existe.
    if is_active is not None:
        # Transforma a string is_active em booleano
        active = is_active.lower() == "true"
        users = [usuario for usuario in users if usuario["is_active"] == active]

    # paginação
    total = len(users)
    # lógica de paginação para começar no usuário certo em cada página
    start = (page - 1) * page_size
    end = start + page_size
    users_paginated = [
        {
            "id": u["id"],
            "name": u["name"],
            "email": u["email"],
            "role": u["role"],
            "is_active": u["is_active"],
            "created_at": datetime.fromisoformat(u["created_at"].replace("Z", "+00:00")).isoformat()
        }
        for u in users[start:end]
    ]
    return {
        "data": users_paginated,
        "Pagination": {
            "page": page,
            "page_size": page_size,
            "total": total,
            "total_pages": (total + page_size - 1) // page_size

        }
    }


def get_user_by_id(user_id: int):
    user = user_repository.find_by_id(user_id)
    if not user:
        return None
    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "role": user["role"],
        "is_active": user["is_active"],
        "created_at": datetime.fromisoformat(user["created_at"].replace("Z", "+00:00")).isoformat()
    }
