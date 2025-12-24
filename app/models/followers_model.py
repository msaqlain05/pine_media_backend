from sqlalchemy import Column, Integer, ForeignKey, DateTime, UniqueConstraint, func
from sqlalchemy.orm import relationship
from app.database import Base

class Followers(Base):
    __tablename__ = "followers"

    id = Column(Integer, primary_key=True, index=True)
    follower_id = Column(
        Integer,
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False
    )
    followee_id = Column(
        Integer,
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Ensure no duplicate follows
    __table_args__ = (
        UniqueConstraint("follower_id", "followee_id", name="unique_follow"),
    )

    # Relationships (self-referential)
    follower = relationship(
        "User",
        foreign_keys=[follower_id],
        back_populates="following"
    )
    followee = relationship(
        "User",
        foreign_keys=[followee_id],
        back_populates="followers"
    )
