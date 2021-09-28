from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,TIMESTAMP
from sqlalchemy.dialects.mysql import INTEGER

#class to store the dataset values
Base = declarative_base()
metadata = Base.metadata

class Dataset(Base):
    __tablename__ = 'dataset'
    id = Column(INTEGER,primary_key = True)
    amount = Column(INTEGER)
    date = Column(TIMESTAMP)
    




    