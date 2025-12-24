from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PostBase(BaseModel):
    content : str
    caption : Optional[str] = None

class PostResponce(PostBase):
    id : int
    user_id : int
    created_at : datetime

    class Config:
        from_attributes = True
