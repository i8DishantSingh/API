from pydantic import BaseModel
from typing import Optional
class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]

    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                'username':'dishant',
                'email':'example@gmail.com',
                'password':'12345',
                'is_active':True,
                'is_staff':False
            }
        }
    