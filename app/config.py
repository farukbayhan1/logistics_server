import os
from dotenv import load_dotenv

load_dotenv()
class Config:
	DB_HOST=os.getenv("DB_HOST")
	DB_PORT=os.getenv("DB_PORT")
	DB_NAME=os.getenv("DB_NAME")
	DB_USER=os.getenv("DB_USER")
	DB_PASSWORD=os.getenv("DB_PASSWORD")

	@classmethod
	def database_url(cls):
		return (
			f"postgresql+psycopg2://"
			f"{cls.DB_USER}:{cls.DB_PASSWORD}"
			f"@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"
			)
			