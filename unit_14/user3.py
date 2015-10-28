# -*- coding: utf-8 -*- 
import sqlite3

con = sqlite3.connect('users.db')

with con:
    cur = con.cursor()
    cur.execute('SELECT * FROM users')
    data = cur.fetchone()
    print data[0]
con.close()