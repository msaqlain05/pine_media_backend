from sqlalchemy import Integer, String, Column, Boolean, ForeignKey, UniqueConstraint
from app.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta 
from sqlalchemy import DateTime ,func


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    Username = Column(String(50) ,nullable= False )
    Email = Column(String(50), unique=True, index=True)
    PasswordHash = Column(String(200) , nullable=False)
    Bio = Column(String(200))
    ProfilePicture = Column(String(250))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    
    # Relationships
    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")
    likes = relationship("Like", back_populates="user")
    followers = relationship("Followers" ,back_populates="user")
