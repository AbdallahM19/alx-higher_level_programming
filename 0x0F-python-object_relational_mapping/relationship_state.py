#!/usr/bin/python3
"""
Improve the files
model_city.py and model_state.py
and save them as
relationship_city.py and relationship_state.py
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    inherits from Base Tips
    links to the MySQL table states
    class attribute id
    class attribute name 
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
