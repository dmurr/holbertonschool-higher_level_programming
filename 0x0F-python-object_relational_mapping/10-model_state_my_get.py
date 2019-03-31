#!/usr/bin/python3
""" Prints the State object with the name passed as argument from the database
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
        state = session.query(State).filter(State.name == argv[4]).one()
        print("{}".format(state.id))
    except:
        print("Not found")
    finally:
        session.close()
