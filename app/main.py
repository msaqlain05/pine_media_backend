from fastapi import FastAPI
from app.database import engine ,Base
from app.models import User, Post , Like ,Followers , Comment


app = FastAPI()

Base.metadata.create_all(bind = engine)