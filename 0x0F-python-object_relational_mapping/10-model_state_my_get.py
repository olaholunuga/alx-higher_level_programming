#!/usr/bin/python3
"""python script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ = "__main__":
    if len(sys.argv) >= 4:
        user = sys.argv[1]
        passwd = sys.argv[2]
        db = sys.argv[3]
        state_name = sys.argv[4]
        database_url = "mysql://{}:{}@localhost:3306/{}".format(user, passwd, db)
        engine = create_engine(database_url)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        result = session.query(state).filter(state.name.like(state_name)).first()
        if result:
            print("{}: {}".format(result.id, result.name))
        else:
            print("Not found")
