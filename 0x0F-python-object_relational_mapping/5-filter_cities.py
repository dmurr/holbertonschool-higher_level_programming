#!/usr/bin/python3
""" Takes name of state as parameter and lists all cities of that state
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

    cur.execute("SELECT cities.name FROM cities \
    LEFT JOIN states ON cities.state_id = states.id \
    WHERE states.name = '{}' ORDER BY cities.id ASC".format(args[4]))

    print(', '.join([row[0] for row in cur.fetchall()]))
    cur.close()
    db.close()
