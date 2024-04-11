#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
safe for MySQL injection
"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            port=3306
            )
    cursor = db.cursor()
    match = sys.argv[4]
    query = ("""SELECT cities.name
    FROM states INNER JOIN cities
    ON states.id = cities.state_id
    WHERE states.name LIKE %s
    ORDER BY states.id ASC""")
    cursor.execute(query, (match, ))
    rows = cursor.fetchall()
    city_names = ", ".join(row[0] for row in rows)
    print(city_names)
    cursor.close()
    db.close()
