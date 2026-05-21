from fastapi import APIRouter

auth_router = APIRouter(
    prefix="/auth"
)

@auth_router.get("/")
async def get_auth():
    return {"message": "Hello world"}

