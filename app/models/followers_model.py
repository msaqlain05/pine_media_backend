from sqlalchemy import Integer, String, Column, Boolean, ForeignKey, UniqueConstraint
from app.database import Base
from sqlalchemy.orm import relationship 
from sqlalchemy import DateTime ,func

class Followers(Base):
    __tablename__ = "followers"

    id = Column(Integer, primary_key=True, index=True)
    FollowerId = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    FolloweeId = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())


    user = relationship("User", back_populates="followers")
