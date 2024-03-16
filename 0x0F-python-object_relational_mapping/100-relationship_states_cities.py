#!/usr/bin/python3
"""
Write a script that creates the State “California”
with the City “San Francisco” from
the database hbtn_0e_100_usa:
(100-relationship_states_cities.py)
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
        )
    )
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    Sess = Session()
    state_California = State(name="California")
    city_San_Francisco = City(name="San Francisco")
    state_California.cities.append(city_San_Francisco)
    Sess.add(state_California)
    Sess.commit()
    Sess.close()
    engine.close()


if __name__ == "__main__":
    if len(argv) == 4:
        username, password, db_name = argv[1], argv[2], argv[3]
        # search = argv[4]
        relationship_states_cities(username, password, db_name)
