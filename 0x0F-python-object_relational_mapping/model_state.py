#!usr/bin/python3
"""
A python file that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import create_engine, String, Integer, Column, MetaData
from sqlalchemy.ext.declarative import declarative_base
import uuid

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


def gen_unique_uuid():
    return str(uuid.uuid4())


class State(Base):
    """
    Defines a class State that inherits from Base
    """
    __tablename__ = "states"
    id = Column(
            String, primary_key=True,
            default=gen_unique_uuid, nullable=False
            )
    name = Column(String(128), nullable=False)
