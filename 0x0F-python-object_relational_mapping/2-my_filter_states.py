#!/usr/bin/python3
""" Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3]
        )

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = '{:s}' \
    ORDER BY states.id ASC".format(argv[4]))

    for row in cur.fetchall():
        print("{}".format(row))
    cur.close()
    db.close()
