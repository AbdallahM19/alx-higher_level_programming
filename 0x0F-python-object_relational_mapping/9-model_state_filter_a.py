#!/usr/bin/python3
"""
Write a script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def model_state_fetch_first(user, password, name):
    """
    lists all State objects
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            user, password, name
        ), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    Sess = Session()
    state = Sess.query(State).filter(State.name.contains('a'))
    state = state.order_by(State.id)
    if state is not None:
        for i in state:
            print("{}: {}".format(i.id, i.name))
    Sess.close()
    engine.close()


if __name__ == "__main__":
    if len(argv) == 4:
        username, password, db_name = argv[1], argv[2], argv[3]
        model_state_fetch_first(username, password, db_name)
