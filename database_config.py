from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


username = "4586599_resturrant"
password = "Jory@100124"
host = "fdb1030.awardspace.net"
database = "4586599_resturrant"
port = "3306"

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://4586599_resturrant:Jory@100124@fdb1030.awardspace.net:3306/4586599_resturrant"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()