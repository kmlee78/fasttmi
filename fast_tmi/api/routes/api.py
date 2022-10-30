from fastapi import APIRouter

from fast_tmi.api.routes.user import router as user_api

router = APIRouter()

router.include_router(user_api, tags=["user"])
