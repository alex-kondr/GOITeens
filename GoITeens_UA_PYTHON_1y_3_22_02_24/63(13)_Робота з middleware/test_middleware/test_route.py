import logging

from fastapi import APIRouter, Request, Response, Depends


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("router")


async def test_route_middleware(request: Request, response: Response) -> Response:
    logger.info("Повідомлення від роутера")
    logger.info(f"Тип запиту - {request.method}\nЗапит - {request.url}")
    response.headers["New-header"] = "Header by router"


router = APIRouter(prefix="/users", dependencies=[Depends(test_route_middleware)])


@router.get("/")
async def get_user():
    return dict(users="users")
