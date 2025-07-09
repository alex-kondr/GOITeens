import logging

from fastapi import APIRouter, Request, Response, Depends

test_route = APIRouter(prefix="/route")
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("Route log")

async def test_route_middleware(request: Request):
    log.info("Старт тестової middleware")
    return "Тестова middleware відпрацювала"

@test_route.get("/")
async def start_test_route(msg = Depends(test_route_middleware)):
    return dict(msg=msg)