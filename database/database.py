from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://romanus:L3c4tDtn5ztwn20QTj28S4o0VPfgPCBY@dpg-csjqad9u0jms73b4ds9g-a.oregon-postgres.render.com/marketplace_shop"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
