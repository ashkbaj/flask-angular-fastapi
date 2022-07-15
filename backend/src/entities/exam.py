from sqlalchemy import Column, String
from .entity import Entity, Base



class Exam (Entity, Base):

    __tablename__ = 'exams'

    title = Column(String)
    description = Column(String)

    def __int__(self, title, description, created_by):
        self.title = title
        self.description = description
        Entity.__int__(self, created_by)