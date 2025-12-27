from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, UniqueConstraint, text, Index
from app.db.base import Base

class TripStatusModel(Base):
    
    __tablename__ = 'trip_statuses'

    id = Column(Integer,primary_key=True,autoincrement=True)
    status_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class TripActivityTypeModel(Base):
    
    __tablename__ = 'trip_activity_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class TripModel(Base):
    
    __tablename__ = 'trips'

    id = Column(Integer,primary_key=True,autoincrement=True)
    status_id = Column(Integer,ForeignKey('trip_statuses.id'),nullable=False)
    vehicle_id = Column(Integer,ForeignKey('vehicles.id'),nullable=False)
    driver_id = Column(Integer,ForeignKey('employees.id'),nullable=False)
    courier_id = Column(Integer,ForeignKey('employees.id'),nullable=False)
    loaded_province_id = Column(Integer,ForeignKey('provinces.id'),nullable=False)
    loaded_district_id = Column(Integer,ForeignKey('districts.id'),nullable=False)
    destination_province_id = Column(Integer,ForeignKey('provinces.id'),nullable=False)
    destination_district_id = Column(Integer,ForeignKey('districts.id'),nullable=False)
    started_at = Column(DateTime,nullable=True)
    ended_at = Column(DateTime,nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)
    is_active = Column(Boolean,server_default=text('true'),nullable=False)

class TripActivityModel(Base):
    
    __tablename__ = 'trip_activities'

    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    trip_id = Column(Integer,ForeignKey('trips.id'),nullable=False)
    activity_type_id = Column(Integer,ForeignKey('trip_activity_types.id'),nullable=False)
    old_value = Column(String(255),nullable=True)
    new_value = Column(String(255),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

    __table_args__ = (
        Index('ix_trp_act_user_id','user_id'),
        Index('ix_trp_act_trip_id','trip_id'),
        Index('ix_trp_act_created_at','created_at'),
    )


