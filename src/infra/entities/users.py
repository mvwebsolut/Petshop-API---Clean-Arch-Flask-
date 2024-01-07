from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.infra.database import Base

class Users(Base):
    """user entity"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    id_pet = relationship("Pets")

    def __repr__(self):
        return f"User [name={self.name}]"

    


