from fastapi import APIRouter

from fast_tmi.api.routes.root import router as root_api

router = APIRouter()

router.include_router(root_api, tags=["root"])
