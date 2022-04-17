from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_root_api():
    return {"message": "It works on localhost"}
