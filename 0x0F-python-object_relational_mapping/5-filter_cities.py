#!/usr/bin/python3
"""
Write a script that takes in the name of a state as
an argument and lists all cities of that state
using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Your script should take 4 arguments:
    mysql username
    mysql password
    database name
    state name
    """
    args_cur = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = args_cur.cursor()
    cur.execute(
        "SELECT cities.id, cities.name FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name LIKE BINARY %(name)s \
        ORDER BY cities.id ASC", {'name': sys.argv[4]}
    )
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        print(row)
        if i != len(cur) - 1:
            print(", ")
    cur.close()
    args_cur.close()
