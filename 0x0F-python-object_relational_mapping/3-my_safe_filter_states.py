#!/usr/bin/python3
"""
write a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
But this time, write one that is safe from MySQL injections!
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Your script should take 4 arguments:
    mysql username
    mysql password
    database name
    state name searched
    (no argument validation needed)
    """
    args_cur = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        data=sys.argv[3]
    )
    cur = args_cur.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE \
        BINARY %(name)s ORDER BY states.id ASC", \
        {'name': sys.argv[4]}
    )
    row = cur.fetchall()
    for i in row:
        print(i)
