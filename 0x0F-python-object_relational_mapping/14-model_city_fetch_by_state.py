#!/usr/bin/python3
"""
A script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3])
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = (
        session.query(State.name, City.id, City.name)
        .filter(State.id == City.state_id))
    for instance in query:
        print(instance[0] + ": (" + str(instance[1]) + ")" + instance[2])
