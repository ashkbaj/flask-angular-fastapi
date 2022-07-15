from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_url = 'localhost:5432'
db_name = 'online-exam'
db_usename = 'postgres'
password = 'admin'


engine = create_engine(f'postgresql://{db_usename}:{password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
#print(Session..en)

class Entity():
    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime)
    last_updated = Column(DateTime)
    last_updated_by = Column(String)



    def __int__(self, created_by):
        self.created_date = datetime.now()
        self.last_updated = datetime.now()
        self.last_updated_by = created_by
