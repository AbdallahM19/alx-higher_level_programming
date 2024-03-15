#!/usr/bin/python3
"""
Write a script that takes in an argument
displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Your script should take 4 arguments:
    mysql username
    mysql password
    database name and state name searched
    (no argument validation needed)
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
        "SELECT * FROM states WHERE name LIKE BINARY '{}' \
        ORDER BY states.id ASC", (sys.argv[4],)
    )
    row = cur.fetchall()
    for i in row:
        print(i)
