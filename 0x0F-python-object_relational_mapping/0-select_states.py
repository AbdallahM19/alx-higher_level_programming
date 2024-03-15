#!/usr/bin/python3
"""
Write a script that lists all states
from the database 'hbtn_0e_0_usa':
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Your script should take 3 arguments:
    mysql username
    mysql password
    database name (no argument validation needed)
    """
    args = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        name=sys.argv[3],
    )
    cur = args.cursor()
    cur.execute("SELECT * FROM states")
    row = cur.fetchall()
    for i in row:
        print(i)
