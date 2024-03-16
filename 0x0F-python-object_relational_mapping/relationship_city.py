#!/usr/bin/python3
"""
Improve the files model_city.py
model_state.py
save them as
relationship_city.py
relationship_state.py
"""
from relationship_state import Base, State
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

    id = Column(Integer, primary_key=True)
    state_id = Column(
        Integer, ForeignKey('states.id'), nullable=False
    )
    name = Column(String(128), nullable=False)
