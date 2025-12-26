from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, UniqueConstraint, text, Index
from app.db.base import Base

class WarehouseTypeModel(Base):
    
    __tablename__ = 'warehouse_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class WarehouseActivityTypeModel(Base):
    
    __tablename__ = 'warehouse_activity_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class WarehouseModel(Base):
    
    __tablename__ = 'warehouses'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_id = Column(ForeignKey('warehouse_types.id'),nullable=False)
    warehouse_name = Column(String(60),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)
    is_active = Column(Boolean,server_default=text('true'),nullable=False)

class WarehouseActivityModel(Base):
    
    __tablename__ = 'warehouse_activities'

    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    warehouse_id = Column(Integer,ForeignKey('warehouses.id'),nullable=False)
    activity_type_id = Column(Integer,ForeignKey('warehouse_activity_types.id'),nullable=False)
    old_value = Column(String(255),nullable=True)
    new_value = Column(String(255),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

    __table_args__ = (
        Index('ix_war_act_user__id','user_id'),
        Index('ix_war_act_warehouse_id','warehouse_id'),
        Index('ix_war_act_created_at','created_at'),
    )
