from sqlalchemy import Integer, String, Column, Boolean, ForeignKey, UniqueConstraint
from app.database import Base
from sqlalchemy.orm import relationship 
from sqlalchemy import DateTime ,func

class Like(Base):
    __tablename__ = "Like"

    id = Column(Integer, primary_key=True, index=True)
    PostId = Column(Integer, ForeignKey("post.id", ondelete="CASCADE"))
    UserId = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="like")
    post = relationship("post" , back_populates="like")