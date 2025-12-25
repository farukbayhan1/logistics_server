from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, UniqueConstraint, Index, text
from app.db.base import Base

class PhoneNumberTypeModel(Base):
    __tablename__ = 'phone_number_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class PhoneNumberActivityTypeModel(Base):
    __tablename__ = 'phone_number_activity_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class PhoneNumberModel(Base):
    __tablename__ = 'phone_numbers'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_id = Column(Integer,ForeignKey('phone_number_types.id'),nullable=False)
    phone_number = Column(String(16),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)
    is_active = Column(Boolean,server_default=text('true'),nullable=False)

class PhoneNumberActivityModel(Base):
    __tablename__ = 'phone_number_activities'

    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    phone_number_id = Column(Integer,ForeignKey('phone_numbers.id'),nullable=False)
    activity_type_id = Column(Integer,ForeignKey('number_number_activity_types.id'),nullable=False)
    old_value = Column(String(255),nullable=True)
    new_value = Column(String(255),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

    __table_args__ = (
        Index('ix_phn_act_user_id','user_id'),
        Index('ix_phn_act_phone_id','phone_number_id'),
        Index('ix_phn_act_created_at','created_at'),
    )

class PhoneNumberEntityModel(Base):
    __tablename__ = 'phone_number_entities'

    entity_name = Column(String(255),primary_key=True,nullable=False)
    entity_id = Column(Integer,primary_key=True,nullable=False)
    phone_number_id = Column(Integer,ForeignKey('phone_numbers.id'),primary_key=True,nullable=False)

    __table_args__ = (
        UniqueConstraint('entity_name','entity_id','phone_number_id',name='uq_phone_number_entity'),
    )