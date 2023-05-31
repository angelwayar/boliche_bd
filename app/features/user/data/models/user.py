from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped

from app.core.models.base_model import Base


class User(Base):
    __table__ = 'users'

    email: Mapped[str] = Column(String, unique=True, index=True)
    password: Mapped[str] = Column(String)
   