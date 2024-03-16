#!/usr/bin/python3
"""
Write a Python file similar to
model_state.py named model_city.py
that contains the class definition of a City.
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    inherits from Base (imported from model_state)
    links to the MySQL table cities
    class attribute id
    class attribute name
    class attribute state_id
    """
    __tablename__ = 'cities'

    id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False
    )
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer, ForeignKey('states.id'), nullable=False
    )
