from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse

from app.core.openapi import add_custom_openapi_schema
from app.routes import authentication_route

app = FastAPI()

app.include_router(authentication_route.router)

add_custom_openapi_schema(app)


@app.get("/")
def root(response: Response) -> RedirectResponse:
    """
    Uma função que serve como o caminho raiz da aplicação.

    Args:
        response: Uma instância da classe Response que representa
            a resposta à requisição do cliente.

    Returns:
        Um objeto RedirectResponse que redireciona o cliente para
            o caminho "/docs".
    """

    response = RedirectResponse(url="/docs")
    return response
