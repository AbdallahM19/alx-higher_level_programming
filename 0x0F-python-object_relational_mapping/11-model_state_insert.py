#!/usr/bin/python3
"""
Write a script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def model_state_fetch_first(user, password, name):
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
    Louisiana = State(name="Louisiana")
    Sess.add(Louisiana)
    Sess.commit()
    print(Louisiana.id)
    Sess.close()
    engine.close()


if __name__ == "__main__":
    if len(argv) == 4:
        username, password, db_name = argv[1], argv[2], argv[3]
        # search = argv[4]
        model_state_fetch_first(username, password, db_name)
