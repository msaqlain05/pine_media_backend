from sqlalchemy import Integer, String, Column, Boolean, ForeignKey, UniqueConstraint
from app.database import Base
from sqlalchemy.orm import relationship 
from sqlalchemy import DateTime ,func

class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    PostId = Column(Integer, ForeignKey("post.id", ondelete="CASCADE"))
    UserId = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    Content = Column(String(250))
    Ccreated_at = Column(DateTime(timezone=True), server_default=func.now())


    user = relationship("User", back_populates="comment")
    post = relationship("Post" ,back_populates="comment")

