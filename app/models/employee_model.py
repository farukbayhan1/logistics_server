from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, UniqueConstraint, text, Numeric, Index
from app.db.base import Base

class GenderModel(Base):

    __tablename__ = 'genders'
    
    id = Column(Integer,primary_key=True,autoincerement=True)
    gender_name = Column(String(30),unique=True,nullable=False)

class EmployeeUnitModel(Base):
    
    __tablename__ = 'employee_units'

    id = Column(Integer,primary_key=True,autoincerement=True)
    unit_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class EmployeePositionModel(Base):
    
    __tablename__ = 'employee_positions'

    id = Column(Integer,primary_key=True,autoincerement=True)
    position_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class EmployeeModel(Base):
    
    __tablename__ = 'employees'

    id = Column(Integer,primary_key=True,autoincerement=True)
    gender_id = Column(Integer,ForeignKey('genders.id'),nullable=False)
    unit_id = Column(Integer,ForeignKey('employee_units.id'),nullable=False)
    position_id = Column(Integer,ForeignKey('employee_positions.id'),nullable=False)
    goverment_id = Column(String(11),unique=True,nullable=False)
    name = Column(String(60),nullable=False)
    surname = Column(String(60),nullable=False)
    started_at = Column(DateTime,nullable=False)
    ended_at = Column(DateTime,nullable=True)
    salary = Column(Numeric(12,2),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)
    is_active = Column(Boolean,server_default=text('true'),nullable=False)

class EmployeeActivityTypeModel(Base):
    
    __tablename__ = 'employee_activity_types'

    id = Column(Integer,primary_key=True,autoincerement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class EmployeeActivityModel(Base):
    
    __tablename__ = 'employee_activities'

    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    employee_id = Column(Integer,ForeignKey('employees.id'),nullable=False)
    activity_type_id = Column(Integer,ForeignKey('employee_activity_types.id'),nullable=False)
    old_value = Column(String(255),nullable=True)
    new_value = Column(String(255),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

    __table_args__ = (
        Index('ix_emp_act_user_id','user_id'),
        Index('ix,emp_act_employee_id','employee_id'),
        Index('ix_emp_act_created_at','created_at'),
    )