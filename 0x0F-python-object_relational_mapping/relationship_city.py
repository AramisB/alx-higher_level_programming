#!/usr/bin/python3
"""
Contains City class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Class representing a State table in MySQL database
    """
    __tablename__ = 'cities'
    id = Column(
        Integer, unique=True, primary_key=True,
        nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
