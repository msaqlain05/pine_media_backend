from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.models import user_model
from app.schemas.user import UserCreate
from app.database import get_db
from app.utils.password_hashing import hash_password


router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/register", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    # 1. Check if user already exists
    if db.query(user_model.User).filter(
        user_model.User.email == user.email
    ).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    # 2. Hash password (schema -> model translation)
    password_hash = hash_password(user.password)

    # 3. Create ORM user (NO `password` field here)
    db_user = user_model.User(
        username=user.username,
        email=user.email,
        password_hash=password_hash,
        bio=user.bio,
        profile_picture=user.profile_picture
    )

    # 4. Persist
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # 5. Response (never return password/hash)
    return {
        "message": "User created successfully",
        "user": {
            "id": db_user.id,
            "username": db_user.username,
            "email": db_user.email,
            "bio": db_user.bio,
            "profile_picture": db_user.profile_picture
        }
    }
