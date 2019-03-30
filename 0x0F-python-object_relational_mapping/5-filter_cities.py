#!/usr/bin/python3
""" Takes name of state as parameter and lists all cities of that state
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

    cur.execute("SELECT cities.name FROM cities \
    LEFT JOIN states ON cities.state_id = states.id \
    WHERE states.name = '{}' ORDER BY cities.id ASC".format(argv[4]))

    print(', '.join([row[0] for row in cur.fetchall()]))
    cur.close()
    db.close()
