from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, UniqueConstraint, Index, text
from app.db.base import Base

class ClientType(Base):

    __tablename__ = 'client_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class ClientActivityType(Base):

    __tablename__ = 'client_activity_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(30),nullable=True)

class Client(Base):

    __tablename__ = 'clients'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_id = Column(Integer,ForeignKey('client_types.id'),nullable=False)
    tax_id = Column(String(11),nullable=True)
    client_name = Column(String(120),nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)
    is_active = Column(Boolean,server_default=text('true'))
    
    __table_args__ = (
        UniqueConstraint('tax_id','client_name',name='uq_client'),
    )

class ClientActivity(Base):
    
    __tablename__ = 'client_activities'

    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    client_id = Column(Integer,ForeignKey('clients.id'),nullable=False)
    activity_type_id = Column(Integer,ForeignKey('client_activity_types.id'),nullable=False)
    old_value = Column(String(255),nullable=True)
    new_value = Column(String(255),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

    __table_args__ = (
        Index('ix_cli_user_id','user_id'),
        Index('ix_cli_client_id','client_id'),
        Index('ix_cli_created','created_at'),
    )
