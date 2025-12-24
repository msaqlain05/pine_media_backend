from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, index=True)
    password_hash = Column(String(200), nullable=False)
    bio = Column(String(200))
    profile_picture = Column(String(250))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Posts, Comments, Likes relationships
    posts = relationship(
        "Post",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    comments = relationship(
        "Comment",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    likes = relationship(
        "Like",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    # FOLLOW SYSTEM (self-referential)
    followers = relationship(
        "Followers",
        foreign_keys="Followers.followee_id",
        back_populates="followee",
        cascade="all, delete-orphan"
    )
    following = relationship(
        "Followers",
        foreign_keys="Followers.follower_id",
        back_populates="follower",
        cascade="all, delete-orphan"
    )
