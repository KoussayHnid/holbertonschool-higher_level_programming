#!/usr/bin/python3
'''
script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa
'''
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3],

    )
    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states ORDER BY id"
            .format(argv[4]))
    results=cursor.fetchall()
    for row in results:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
