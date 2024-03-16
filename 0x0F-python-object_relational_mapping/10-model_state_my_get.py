#!/usr/bin/python3
"""
Write a script that prints the
State object with the name passed as
argument from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def model_state_fetch_first(user, password, name, search):
    """
    prints the State object
    Your script should take 4 arguments:
    mysql username
    mysql password
    database name
    state name to search
    (SQL injection free)
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, password, name),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    Sess = Session()
    state = Sess.query(State)
    state = state.filter(State.name == search).first()
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")
    Sess.close()
    engine.close()


if __name__ == "__main__":
    if len(argv) == 5:
        username, password, db_name = argv[1], argv[2], argv[3]
        search = argv[4]
        model_state_fetch_first(username, password, db_name, search)
