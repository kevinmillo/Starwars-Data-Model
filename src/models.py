import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    mail = Column (String(40), nullable=False, unique=True)
    password = Column (String(20), nullable=False)
    favoritospeople = relationship("FavoritosPeople", backref="user")
    favoritosplanets = relationship("FavoritosPlanets", backref="user")
class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    favoritospeople = relationship("FavoritosPeople", backref="people")
    def to_dict(self):
        return {}

class FavoritosPeople(Base):
    __tablename__ = 'favoritospeople'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    people_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    diameter = Column(Float)
    population = Column(Float)
    favoritosplanets = relationship("FavoritosPlanets", backref="planets")
    def to_dict(self):
        return {}

class FavoritosPlanets(Base):
    __tablename__ = 'favoritosplanets'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)
    def to_dict(self):
        return {}

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    model = Column(String(30))
    passengers = Column(Integer)
    favoritosvehicles = relationship("FavoritosVehicles", backref="vehicles")
    def to_dict(self):
        return {}

class FavoritosVehicles(Base):
    __tablename__ = 'favoritosvehicles'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'), primary_key=True)
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')