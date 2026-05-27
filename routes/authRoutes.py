from fastapi import APIRouter
from config.database import Session, engine
from schemas.schema import SignUpModel
from models.userModel import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash

 
auth_router = APIRouter(prefix="/auth", tags=["auth"])
session=Session(bind=engine)


@auth_router.get("/hello")
async def get_auth():
    return {"message": "Hello world"}

@auth_router.post("/signup", response_model=SignUpModel,status_code=201)
async def signup(user: SignUpModel):
    
    db_email=session.query(User).filter(User.email==user.email).first()
    if db_email is not None:
        return HTTPException(status_code=400, detail="User with the email alread exists")
    db_username=session.query(User).filter(User.username==user.username).first()
    if db_username is not None:
        return HTTPException(status_code=400, detail="User with the username alread exists")
    
    new_user=User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        is_active=user.is_active,
        is_staff=user.is_staff
    )
    
    session.add(new_user)
    session.commit()
    
    return new_user