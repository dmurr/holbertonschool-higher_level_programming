#!/usr/bin/python3
""" Lists all states with name starting with N from hbtn_0e_0_usa
"""

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

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")

    for row in cur.fetchall():
        print("({}, '{}')".format(row[0], row[1]))
    cur.close()
    db.close()
