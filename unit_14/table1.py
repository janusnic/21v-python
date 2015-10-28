#!/usr/bin/python
import sqlite3

db = sqlite3.connect('test.db')
cur = db.cursor()
cur.execute('CREATE TABLE table1 (id INTEGER PRIMARY KEY, f TEXT, l TEXT)')
db.commit()
cur.execute('INSERT INTO table1 (id, f, l) VALUES(NULL, "john", "smith")')
db.commit()
cur.execute('SELECT * FROM table1')
print cur.fetchall()
