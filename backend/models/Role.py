from typing import List

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from database.database import Base
#from models.User import association_table
#from models.User import User



class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String, index=False)

    # roles: Mapped[List[User]] = relationship(
    #     secondary=association_table, back_populates="roles"
    # )
#users : Mapped[List[User]] = relationship('User', secondary=association_table, back_populates='roles')