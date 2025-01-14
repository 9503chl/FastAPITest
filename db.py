from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session

user_name = "dbtjq"
user_password = "1234"
db_host = "127.0.0.1"
db_name = "edudb"

#@는 hostName, /는 패스워드
DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    user_password,
    db_host,
    db_name
)

ENGINE = create_engine(DATABASE, echo=True)

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=ENGINE))

Base = declarative_base()
Base.query = session.query_property()


