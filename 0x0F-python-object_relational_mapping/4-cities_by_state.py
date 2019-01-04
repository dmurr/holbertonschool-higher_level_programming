#!/usr/bin/python3
""" A script that lists all cities in the database hbtn_0e_4_usa """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities JOIN states ON state_id = states.id "
                "ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print ("{}".format(row))
    cur.close()
    db.close()
