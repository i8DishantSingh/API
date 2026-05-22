from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/signup")
async def get_auth():
    return {"message": "Hello world"}

