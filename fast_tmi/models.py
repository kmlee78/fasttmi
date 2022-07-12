from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from fast_tmi.database import Base


class Master(Base):
    __tablename__ = "masters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    slaves = relationship("Slave", back_populates="owner")


class Slave(Base):
    __tablename__ = "slaves"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    owner_id = Column(Integer, ForeignKey("masters.id"))

    owner = relationship("Master", back_populates="slaves")
