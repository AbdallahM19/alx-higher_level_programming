#!/usr/bin/python3
"""
Write a script that lists all
State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def relationship_states_cities(user, password, name):
    """
    Your script should take 3 arguments:
    mysql username
    mysql password
    database name
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            user, password, name
        ), pool_pre_ping=True
    )
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    Sess = Session()
    state = Sess.query(State).order_by(State.id)
    for i in state:
        print("{}: {}".format(i.id, i.name))
        for k in i.cities:
            print("\t{}: {}".format(k.id, k.name))
    Sess.close()
    engine.close()


if __name__ == "__main__":
    if len(argv) == 4:
        username, password, db_name = argv[1], argv[2], argv[3]
        # search = argv[4]
        relationship_states_cities(username, password, db_name)
