from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, Index
from app.db.base import Base

class UserTypeModel(Base):
    __tablename__ = 'user_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class UserActivityTypeModel(Base):
    __tablename__ = 'user_activity_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(255),unique=True,nullable=False)
    password = Column(String(255),nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)
    is_active = Column(Boolean,server_default='true',nullable=False)

class UserActivityModel(Base):
    __tablename__ = 'user_activities'

    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    activity_type_id = Column(Integer,ForeignKey('user_activity_types.id'),nullable=False)
    old_value = Column(String(255),nullable=True)
    new_value = Column(String(255),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    description = Column(String(255),nullable=True)

    __table_args__ = (
        Index('ix_usr_act_user_id','user_id'),
        Index('ix_usr_act_created','created_at'),
        Index('ix_usr_act_activity_type','activity_type_id'),
    )

class UserSessionModel(Base):
    __tablename__ = 'user_sessions'
    
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    session_id = Column(String(255),unique=True,nullable=False)
    ip_addr = Column(String(45),nullable=True)
    user_agent = Column(String(255),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    expires_at = Column(DateTime(timezone=True),nullable=False)
    is_active = Column(Boolean,server_default='true',nullable=False)
    
    __table_args__ = (
        Index('ix_usr_sess_user_id','user_id'),
        Index('ix_usr_sess_created_at','created_at'),
    )