#!/usr/bin/python3
""" Lists all states with name starting with N from hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[1],
        password=args[2],
        db=args[3]
        )

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")

    for row in cur.fetchall():
        print("({}, '{}')".format(row[0], row[1]))
    cur.close()
    db.close()
