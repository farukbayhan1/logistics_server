from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, UniqueConstraint, Index
from app.db.base import Base

class AuthActivityType(Base):
    __tablename__ = 'auth_activity_types'

    id = Column(Integer,primary_key=True,autoincrement=True)
    type_name = Column(String(30),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    description = Column(String(255),nullable=True)

class AuthActivity(Base):
    __tablename__ = 'auth_activities'

    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    activity_type_id = Column(Integer,ForeignKey('auth_activity_types.id'),nullable=False)
    ip_addr = Column(String(45),nullable=True)
    session_id = Column(String(255),ForeignKey('user_sessions.session_id'),nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)

    __table_args__ = (
        Index('ix_auth_activity_user','user_id'),
        Index('ix_auth_activity_session','session_id'),
    )

class RefreshToken(Base):
    __tablename__ = 'refresh_tokens'

    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    token = Column(String(500),unique=True,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    expires_at = Column(DateTime(timezone=True),nullable=False)
    revoked = Column(Boolean,server_default='false',nullable=False)
    user_agent = Column(String(255),nullable=True)
    session_id = Column(String(255),ForeignKey('user_sessions.session_id'),nullable=False)

    __table_args__ = (
        Index('ix_refresh_token_user_session','user_id','session_id'),
    )

