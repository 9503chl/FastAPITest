from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session

user_name = "root"
user_password = "ehdcns12!"
db_host = "127.0.0.1"
db_name = "edudb"

# @는 hostName, /db 이름
DATABASE = f"mysql+pymysql://{user_name}:{user_password}@{db_host}:3306/{db_name}"

ENGINE = create_engine(DATABASE, echo=True)

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=ENGINE))

Base = declarative_base()
Base.query = session.query_property()
