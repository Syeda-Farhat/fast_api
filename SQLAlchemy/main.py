from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.orm import declarative_base


# db_url = "sqlite:///path/to/mydatabase.db"
db_url = r"sqlite:///C:/Program Files/sqlite/practice_db/mydatabase.db"

engine = create_engine(db_url)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column (Integer, primary_key= True)
    name = Column(String)
    age = Column(Integer)



Base.metadata.create_all(engine)



