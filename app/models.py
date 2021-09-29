from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,TIMESTAMP
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.sql.sqltypes import String

#class to store the dataset values
Base = declarative_base()
metadata = Base.metadata

class Dataset(Base):
    __tablename__ = 'dataset'
    id = Column(INTEGER,primary_key = True)
    amount = Column(String(16))
    amount_one = Column(String(16))
    amount_two = Column(String(16))
    amount_three = Column(String(16))
    amount_four = Column(String(16))
    date = Column(String(16))
    




    