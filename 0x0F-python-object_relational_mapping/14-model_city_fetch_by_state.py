#!/usr/bin/python3
"""
Next, write a script 14-model_city_fetch_by_state.py
that prints all City objects
from the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import State
from model_city import City, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def model_city_fetch_first(user, password, name):
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
    Session = sessionmaker(bind=engine)
    Sess = Session()
    citizen = Sess.query(City, State).join(State)
    for state, city in citizen.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    citizen.commit()
    Sess.close()
    engine.close()


if __name__ == "__main__":
    if len(argv) == 4:
        username, password, db_name = argv[1], argv[2], argv[3]
        # search = argv[4]
        model_city_fetch_first(username, password, db_name)
