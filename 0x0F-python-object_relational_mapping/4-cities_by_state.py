#!/usr/bin/python3
"""
Write a script that lists all
cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Your script should take 3 arguments:
    mysql username
    mysql password
    database name
    """
    args_cur = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cur = args_cur.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC"
    )
    row = cur.fetchall()
    for i in row:
        print(i)
    cur.close()
    args_cur.close()
