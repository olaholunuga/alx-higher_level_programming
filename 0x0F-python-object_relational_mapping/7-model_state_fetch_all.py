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
        database_url = "mysql://{}:{}@localhost:3306/{}".format(user, passwd, db)
        engine = create_engine(database_url)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        results = session.query(state).all()
        for result in results:
            print("{}: {}".format(result.id, result.name))
