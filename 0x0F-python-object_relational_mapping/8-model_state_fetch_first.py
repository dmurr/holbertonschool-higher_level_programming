#!/usr/bin/python3
""" Prints the first State object from the database hbtn_0e_6_usa
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
    try:
        state = session.query(State).order_by(State.id.asc()).first()
        print("{}: {}".format(state.id, state.name))
    except:
        print("Nothing\n")

    session.close()
