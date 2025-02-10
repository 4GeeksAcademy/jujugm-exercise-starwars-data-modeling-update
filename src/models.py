import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, ForeignKey, Integer
from eralchemy2 import render_er
from typing import List


Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped [str] = mapped_column(nullable=False)
    email: Mapped [str] = mapped_column(nullable=False, unique=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    favorites: Mapped[List["Favorites"]] = relationship()

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    hair__color: Mapped[str]= mapped_column(nullable=False)
    skin_color: Mapped[str] = mapped_column(nullable=False)
    gender: Mapped[str] 
    favorites: Mapped[List["Favorites"]] = relationship()

class Planets(Base):
    __tablename__ = 'planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    climate: Mapped[str]= mapped_column(nullable=False)
    terrain: Mapped[str] = mapped_column(nullable=False)
    population: Mapped[str] 
    favorites: Mapped[List["Favorites"]] = relationship()

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column (ForeignKey("users.id"))
    planet_id: Mapped[str]= mapped_column (ForeignKey("planets.id"))
    people_id: Mapped[str] = mapped_column (ForeignKey("people.id"))
    item: Mapped[str] =  mapped_column (nullable=False)
    type: Mapped[str] = mapped_column (nullable=False)
    users = relationship('Users', back_populates='favorites') 
    planets  = relationship ('Planets', back_populates='favorites')
    people  = relationship ('People', back_populates='favorites')
    # aqui le digo que un usuario puede tener muchos favoritos

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
