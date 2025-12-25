from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, UniqueConstraint, text
from app.db.base import Base

class VehicleTypeModel(Base):
    pass

class VehicleActivityTypeModel(Base):
    pass

class VehicleModel(Base):
    pass

class VehicleActivityModel(Base):
    pass
