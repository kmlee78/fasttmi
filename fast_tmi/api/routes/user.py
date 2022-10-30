from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/users/")
async def get_root_api(token: str = Depends(oauth2_scheme)):
    return {"token": token}
