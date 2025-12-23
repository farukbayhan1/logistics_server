from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, UniqueConstraint
from app.db.base import Base

class EmailTypeModel(Base):
    __tablename__ = 'email_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class EmailActivityTypeModel(Base):
    __tablename__ = 'email_activity_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class EmailModel(Base):
    __tablename__ = 'emails'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_id = Column(Integer,ForeignKey('email_types.id'),nullable=False)
    email = Column(String(320),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(252),nullable=True)
    is_active = Column(Boolean,server_default=func.now())

class EmailActivityModel(Base):
    __tablename__ = 'email_activity_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    activity_type_id = Column(Integer,ForeignKey('email_activity_types.id'),nullable=False)
    old_value = Column(String(320),nullable=True)
    new_value = Column(String(320),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class EmailEntityModel(Base):
    __tablename__ = 'email_entities'

    entity_name = Column(String(255),nullable=False)
    entity_id = Column(Integer,nullable=False)
    email_id = Column(Integer,ForeignKey('emails.id'),nullable=False)

    __table_args__ = (UniqueConstraint('entity_name','entity_id','email_id'),)