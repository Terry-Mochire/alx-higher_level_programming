#!/usr/bin/python3
"""
this script takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
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
    )

    # Create a cursor object
    cur = db.cursor()

    # Execute a query
    query = "SELECT * FROM states WHERE name = %s "
    cur.execute(query, (sys.argv[4],))

    # Fetch all the rows in a list of lists
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close all cursors
    cur.close()

    # Close all databases
    db.close()
