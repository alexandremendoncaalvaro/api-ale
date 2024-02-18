from fastapi import APIRouter

router = APIRouter()


@router.get("/me")
def get_current_user() -> dict:
    """
    Obtém o usuário atual.

    Retorna:
        dict: Um dicionário contendo as informações do usuário.
    """
    return {"user": "user"}
