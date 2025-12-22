from sqlalchemy import Integer, String, Column, Boolean, ForeignKey, UniqueConstraint
from app.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta 
from sqlalchemy import DateTime ,func


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    User_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    ContentURL = Column(String(100) , nullable= False)
    Caption = Column(String(250))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="post")
    comments = relationship("Comment", back_populates="post")  
    likes = relationship("Like", back_populates="post")