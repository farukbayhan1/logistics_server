from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, UniqueConstraint, text
from app.db.base import Base

class GenderModel(Base):
    pass

class EmployeeUnitModel(Base):
    pass

class EmployeePositionModel(Base):
    pass

class EmployeeModel(Base):
    pass

class EmployeeActivityTypeModel(Base):
    pass

class EmployeeActivityModel(Base):
    pass
