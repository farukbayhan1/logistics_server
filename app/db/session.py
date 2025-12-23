from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from app.config import Config

engine = create_engine(Config.database_url(),echo=True)

SessionLocal = sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine
	)