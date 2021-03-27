import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    fullName = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    hair_color = Column(String(50))
    eye_color = Column(String(50))
    gender = Column(String(50))
    photoUrl = Column(String(500))
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    population = Column(String(50))
    terrain = Column(String(50))
    weather = Column(String(50))
    photoUrl = Column(String(500))

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_favorite = Column(Integer,ForeignKey(Planets.id,Characters.id) )
    id_type = Column(Integer)
    users = relationship(Users)
    characters = relationship(Characters)
    planets = relationship(Planets)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
