#!/usr/bin/python3
"""
Write a script that lists all State objects
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            argv[1], argv[2], argv[3]
        ), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    Sess = Session()
    for _ in Sess.query(State).order_by(State.id):
        print("{}: {}".format(_.id, _.name))
    Sess.close()
