from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr
    bio: Optional[str] = None
    profile_picture: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email : EmailStr
    password :str



class UserUpdate(BaseModel):
    username: Optional[str] = None
    bio: Optional[str] = None
    profile_picture: Optional[str] = None



class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  



