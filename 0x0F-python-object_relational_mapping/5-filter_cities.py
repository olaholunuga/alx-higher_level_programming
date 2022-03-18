#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

state_name = sys.argv[4]

if __name__ == "__main__":
    if len(sys.argv) >= 5:
        db_connection = MySQLdb.connect(
                host="localhost", port=3306,
                user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
                )
        c = db_connection.cursor()
        c.execute("SELECT c.name FROM cities as c INNER JOIN states as s ON c.state_id = s.id WHERE s.name LIKE %s ORDER  BY c.id;", (state_name,))
        results = c.fetchall()
        for result in results:
            print(result[0])
        db_connection.close
