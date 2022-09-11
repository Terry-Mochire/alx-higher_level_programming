#!/usr/bin/python3
"""
this script takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
from email import charset
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to a MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    # Create a cursor object
    cur = db.cursor()

    # Execute a query
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))

    # Fetch all the rows in a list of lists
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        if row[1] == argv[4]:
            print(row)

    # Close all cursors
    cur.close()

    # Close all databases
    db.close()
