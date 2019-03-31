#!/usr/bin/python3
""" Lists all State objects that contain the letter a
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                        argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    for state in session.query(State).\
        filter(State.name.ilike('%a%')).order_by(State.id.asc()):
        print("{}: {}".format(state.id, state.name))

    session.close()
