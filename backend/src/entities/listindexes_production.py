from sqlalchemy import create_engine
from sqlalchemy.engine import reflection
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = '10.2.0.43:3306'
db_name = 'db_grab_prod'
db_usename = 'ashishb'
password = 'admin'


#engine = create_engine(f'postgresql://{db_usename}:{password}@{db_url}/{db_name}')

engine = create_engine(F'mysql://{db_usename}:{password}@{db_url}')
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


engine = create_engine()
