from fastapi import FastAPI
from app.database import engine ,Base
from app.models import User, Post , Like ,Followers , Comment
from app.routes import user


app = FastAPI()

Base.metadata.create_all(bind = engine)

app.include_router(user.router, prefix="/user", tags=["User"])