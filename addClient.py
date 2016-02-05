#!/usr/bin/python

##############################
########  Add Client  ########
##############################

import sqlite3

print("Please fill the following entries")

name = raw_input("Name: ")


conn = sqlite3.connect('Client.db')
cur = conn.cursor()

cur.execute('''INSERT INTO client (id, name, online, time) VALUES (?, ?, ?, ?)''',
            (1, name, "N/A", "n/a"))

conn.commit()
conn.close()
