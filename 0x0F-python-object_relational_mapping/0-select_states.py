#!/usr/bin/python3
"""
 A script that lists all states from the database hbtn_0e_0_usa
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
    query = ("SELECT * FROM states ORDER BY states.id ASC")
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
