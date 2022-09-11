#!/usr/bin/python3
'''
This script is used to select states from the database hbtn_0e_0_usa
'''
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows in a list of lists
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close all cursors
    cur.close()

    # Close all databases
    db.close()
