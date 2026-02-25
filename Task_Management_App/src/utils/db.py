from sqlalchemy.orm import sessionmaker , declarative_base
from sqlalchemy import create_engine
from src.utils.settings import settings

Base = declarative_base()
engine = create_engine(settings.DB_CONNECTION)
localsession = sessionmaker(bind=engine)

def get_db():
    session = localsession()
    try:
        yield session
    finally:
        session.close()