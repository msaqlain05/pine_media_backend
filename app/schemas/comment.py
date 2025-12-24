from pydantic import BaseModel 
from typing import Optional
from datetime import datetime

class CommentBase(BaseModel) :
    conetent : str


class CommentCreate(CommentBase):
    post_id : str


class CommentResponce(CommentBase):
    id : int
    user_id : int
    post_id : int
    created_at : datetime

    class config:
        from_attribiutes = True