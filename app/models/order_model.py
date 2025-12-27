from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, UniqueConstraint, text, Index
from app.db.base import Base

class OrderStatusModel(Base):
    
    __tablename__ = 'order_statuses'

    id = Column(Integer,primary_key=True,autoincrement=True)
    status_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class OrderActivityTypeModel(Base):
    
    __tablename__ = 'order_activity_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class OrderModel(Base):
    
    __tablename__ = 'orders'

    id = Column(Integer,primary_key=True,autoincrement=True)
    warehouse_id = Column(Integer,ForeignKey('warehouses.id'),nullable=True)
    client_id = Column(Integer,ForeignKey('clients.id'),nullable=False)
    status_id = Column(Integer,ForeignKey('order_statuses.id'),nullable=False)
    order_document_id = Column(Integer,ForeignKey('order_documents.id'),nullable=False)
    trip_id = Column(Integer,ForeignKey('trips.id'),nullable=True)
    order_no = Column(String(60),nullable=True)
    box_count = Column(Integer,nullable=True)
    order_driver = Column(String(60),nullable=True)
    order_plate = Column(String(16),nullable=True)
    trip_number = Column(String(60),nullable=True)
    delivery_address = Column(String(255),nullable=True)
    order_confirmation_date = Column(DateTime,nullable=True)
    order_plan_confirmation_date = Column(DateTime,nullable=True)
    delivered_at = Column(DateTime,nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)
    in_warehouse = Column(Boolean,server_default=text('true'),nullable=False)
    in_position = Column(Boolean,server_default=text('false'),nullable=False)
    is_active = Column(Boolean,server_default=text('true'),nullable=False)

    __table_args__ = (
        Index('ix_ord_client_id','client_id'),
        Index('ix_ord_status_id','status_id'),
        Index('ix_ord_document_id','order_document_id'),
        Index('ix_ord_order_no','order_no'),
        Index('ix_ord_confirmation_date','order_confirmation_date'),
        Index('ix_ord_plan_confirmation_date','order_plan_confirmation_date'),
        Index('ix_ord_created_at','created_at'),
        Index('ix_ord_is_active','is_active'),
    )

class OrderActivityModel(Base):
    
    __tablename__ = 'order_activities'

    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    order_id = Column(Integer,ForeignKey('orders.id'),nullable=False)
    activity_type_id = Column(Integer,ForeignKey('order_activity_types.id'),nullable=False)
    old_value = Column(String(255),nullable=False)
    new_value = Column(String(255),nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

    __table_args__ = (
        Index('ix_ord_act_user_id','user_id'),
        Index('ix_ord_act_order_id','order_id'),
        Index('ix_ord_act_created_at','created_at'),
    )

