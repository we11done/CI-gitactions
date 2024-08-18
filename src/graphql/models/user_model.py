from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from . import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)


    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
