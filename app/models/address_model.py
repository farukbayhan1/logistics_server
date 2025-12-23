from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, UniqueConstraint
from app.db.base import Base

class Province(Base):
    __tablename__ = 'provinces'

    id = Column(Integer,primary_key=True,autoincrement=True)
    province_name = Column(String(60),unique=True,nullable=False)

class District(Base):
    __tablename__ = 'districts'

    id = Column(Integer,primary_key=True,autoincrement=True)
    province_id = Column(Integer,ForeignKey('provinces.id'),nullable=False)
    district_name = Column(String(60),nullable=False)

    __table_args__ = (UniqueConstraint('province_id','district_name'),)

class AddressTypeModel(Base):
    __tablename__ = 'address_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class AdressActivityTypeModel(Base):
    __tablename__ = 'address_activity_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=False)

class AddressModel(Base):
    __tablename__ = 'addresses'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_id = Column(Integer,ForeignKey('address_types.id'),nullable=False)
    province_id = Column(Integer,ForeignKey('provinces.id'),nullable=False)
    district_id = Column(Integer,ForeignKey('districts.id'),nullable=False)
    address_text = Column(String(255),nullable=False)
    location = Column(String(255),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)
    is_active = Column(Boolean,server_default='true',nullable=False)

    __table_args__ = (UniqueConstraint('type_id','province_id','district_id','address_text'),)

class AddressActivityModel(Base):
    __tablename__ = 'address_activities'

    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    activity_type_id = Column(Integer,ForeignKey('address_activity_types.id'),nullable=False)
    old_value = Column(String(255),nullable=True)
    new_value = Column(String(255),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class AddressEntityModel(Base):
    __tablename__ = 'address_entities'

    entity_name = Column(String(255),nullable=False)
    entity_id = Column(Integer,nullable=False)
    address_id = Column(ForeignKey('addresses.id'),nullable=False)

    __table_args__ = (UniqueConstraint('entity_name','entity_id','address_id'),)