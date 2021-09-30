from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,TIMESTAMP
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.sql.sqltypes import String

#class to store the dataset values
Base = declarative_base()
metadata = Base.metadata

class Dataset(Base):
    __tablename__ = 'amount'
    id = Column(INTEGER,primary_key = True)
    amount = Column(String(16))
    amount_one = Column(String(16))
    amount_two = Column(String(16))
    amount_three = Column(String(16))
    amount_four = Column(String(16))
    
class Dates(Base):
    __tablename__ = 'dates'
    id = Column(INTEGER,primary_key = True)
    date = Column(String(16))
    date_one = Column(String(16))
    date_two = Column(String(16))
    date_three = Column(String(16))
    date_four = Column(String(16))
    



    