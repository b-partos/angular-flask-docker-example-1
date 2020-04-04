# coding=utf-8
"""
ORM entity classes for the application.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

db_url = 'database:5432'
db_name = 'knowledge'
db_user = 'learner'
db_password = 'password'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')

Base = declarative_base()

class Definition(Base):
    __tablename__ = "definition"

    id = Column(Integer, primary_key=True)
    subject = Column(String)
    definition = Column(String)



