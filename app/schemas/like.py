from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class LikeCreate(BaseModel):
    post_id : int


class LikeResponce(BaseModel):
    id : int
    user_id : int
    post_id : int
    created_at : datetime

    class config:
        from_attributes = True

