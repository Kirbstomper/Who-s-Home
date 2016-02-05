#!/usr/bin/python

##############################
########  Create DB   ########
##############################

import sqlite3

conn = sqlite3.connect('Client.db')
print( "Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS devices
       (id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT,
       ip TEXT,
       online TEXT,
       time TEXT,
       mac TEXT,
       owner TEXT,
       FOREIGN KEY(owner) REFERENCES clients(name));''')
print("Created Devices Table")

conn.execute('''CREATE TABLE IF NOT EXISTS client
(id INTEGER,
name TEXT PRIMARY KEY,
online TEXT,
time TEXT);''')

print ("Tables created successfully")
conn.close()
