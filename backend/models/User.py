from typing import List

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import Mapped, relationship

from database.database import Base
from models.Role import Role


# association_table2 = Table(
#     "user_has_review",
#     Base.metadata,
#     Column("reviewee_id", ForeignKey("user.id")),
#     Column("reviewer_id", ForeignKey("user.id")),
#     Column("review_id", ForeignKey("review.id"), primary_key=True)
# )


association_table = Table(
    "user_has_role",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("role_id", ForeignKey("role.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=False)
    password = Column(String, index=False)
    name = Column(String, index=False)
    lastname = Column(String, index=False)
    email = Column(String, index=False)
    phone = Column(String, index=False)
    photo = Column(String, index=False)
    verified_status = Column(Boolean, index=False)
    user_created = Column(DateTime, index=False)

    roles: Mapped[List[Role]] = relationship(secondary=association_table, lazy="joined")#, back_populates="users")


