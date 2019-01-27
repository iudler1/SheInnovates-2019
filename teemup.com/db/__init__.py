from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=True, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.name

class Event(Base):
    __tablename__ = "Event"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    location = Column(String(80), nullable=False)
    description = Column(String(300), unique = True, nullable=False)
    numberOfPeople = Column(Integer, nullable=False)
    def __repr__(self):
        return '<Event %r>' % self.name

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
