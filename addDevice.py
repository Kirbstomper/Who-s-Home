#!/usr/bin/python

##############################
########  Add Device  ########
##############################

import sqlite3

print("Please fill the following entries")

name = raw_input("DeviceName: ")
ip = raw_input("IP-address: ")
mac = raw_input("MAC-address: ")
owner = raw_input("Owner: ")

conn = sqlite3.connect('Client.db')
cur = conn.cursor()

cur.execute('''INSERT INTO devices (name, ip, online, time, mac, owner) VALUES (?, ?, ?, ?, ?, ?)''',
            (name, ip, "No", "N/A", mac, owner))

conn.commit()
conn.close()
