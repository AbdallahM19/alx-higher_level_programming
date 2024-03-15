#!/usr/bin/python3
"""
Write a python file that contains the class
definition of a State and an instance
Base = declarative_base():
"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    inherits from Base Tips
    links to the MySQL table states
    class attribute id
    class attribute name
    """

    __tablename__ = "some_table"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
