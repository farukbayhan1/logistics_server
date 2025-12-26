from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, UniqueConstraint, text, Index
from app.db.base import Base

class OrderDocumentStatusModel(Base):
    
    __tablename__ = 'order_document_statuses'

    id = Column(Integer,primary_key=True,autoincrement=True)
    status_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class OrderDocumentActivityTypeModel(Base):
    
    __tablename__ = 'order_document_activity_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class OrderDocumentModel(Base):
    
    __tablename__ = 'order_documents'

    id = Column(Integer,primary_key=True,autoincrement=True)
    status_id = Column(Integer,ForeignKey('order_document_statuses.id'),nullable=False)
    document_number = Column(String(60),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=False)
    is_active = Column(Boolean,server_default=text('true'),nullable=False)

class OrderDocumentActivities(Base):
    
    __tablename__ = 'order_document_activities'

    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    order_document_id = Column(Integer,ForeignKey('order_documents.id'),nullable=False)
    activity_type_id = Column(Integer,ForeignKey('order_document_activity_types.id'),nullable=False)
    old_value = Column(String(255),nullable=True)
    new_value = Column(String(255),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

    __table_args__ = (
        Index('ix_orddoc_act_user_id','user_id'),
        Index('ix_orddoc_act_order_document_id','order_document_id'),
        Index('ix_orddoc_act_created_at','created_at'),
    )
