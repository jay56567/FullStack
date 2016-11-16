'''
database setup
'''
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'Shelter'

    id      = Column(Integer, primary_key = True)
    name    = Column(String(25), nullable = False)
    address = Column(String(100), nullable = False)
    city    = Column(String(20), nullable = False)
    state   = Column(String(10), nullable = False)
    zipCode = Column(String(5), nullable = False)
    wesite  = Column(String(30), nullable = False)

class Puppy(Base):
    __tablename__ = 'Puppy'

    name        = Column(String(25), primary_key = True)
    dateOfBirth = Column(String(10))
    gender      = Column(String(6), nullable = False)
    weight      = Column(String(3), nullable = False)
    shelter_id  = Column(Integer, ForeignKey('Shelter.id'))
    Puppy       = relationship(Shelter)

engine = create_engine('sqlite:///shelterpuppy.db')
Base.metadata.create_all(engine)
