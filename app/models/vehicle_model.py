from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, UniqueConstraint, text, Numeric, Index
from app.db.base import Base

class VehicleTypeModel(Base):
    
    __tablename__ = 'vehicle_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class VehicleActivityTypeModel(Base):
    
    __tablename__ = 'vehicle_activity_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class VehicleModel(Base):
    
    __tablename__ = 'vehicles'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_id = Column(Integer,ForeignKey('vehicles.id'),nullable=False)
    plate = Column(String(16),unique=True,nullable=False)
    brand = Column(String(30),nullable=False)
    model = Column(String(30),nullable=False)
    model_year = Column(String(4),nullable=False)
    capacity = Column(Numeric(10,2),nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)
    is_active = Column(Boolean,server_default=text('true'),nullable=False)

class VehicleActivityModel(Base):
    
    __tablename__ = 'vehicle_activities'

    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    vehicle_id = Column(Integer,ForeignKey('vehicles.id'),nullable=False)
    activity_type_id = Column(Integer,ForeignKey('vehicle_activity_types.id'),nullable=False)
    old_value = Column(String(255),nullable=True)
    new_value = Column(String(255),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

    __table_args__ = (
        Index('ix_veh_act_user_id','user_id'),
        Index('ix_veh_act_vehicle_id','vehicle_id'),
        Index('ix_veh_act_created_at','created_at'),
    )