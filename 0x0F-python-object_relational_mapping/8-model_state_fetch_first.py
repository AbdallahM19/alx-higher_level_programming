#!/usr/bin/python3
"""
Write a script that prints the first
State object from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def model_state_fetch_first(user, password, name):
    """
    prints the first State
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            user, password, name
        ), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    Sess = Session()
    state = Sess.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    Sess.close()


if __name__ == "__main__":
    if len(argv) == 4:
        username, password, db_name = argv[1], argv[2], argv[3]
        model_state_fetch_first(username, password, db_name)
