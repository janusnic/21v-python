# -*- coding: utf-8 -*- 
import sqlite3

con = sqlite3.connect('users.db')
cur = con.cursor()
cur.execute('SELECT * FROM users')
print cur.fetchall()

cur.execute('SELECT * FROM users')
for row in cur:
    print '-'*10
    print 'ID:', row[0]
    print 'First name:', row[1]
    print 'Second name:', row[2]
    print '-'*10
con.close()