# -*- encoding: utf-8 -*- 
import sqlite3,sys 

def mystr(input): 
    # здесь можно сделать все что угодно 
    return unicode(input,'u8').encode('cp866') 
# подготавливаем данные 
data=['Россия'.decode('u8'),'England'] 

# создаем таблицу, вносим данные 
con = sqlite3.connect(":memory:") 
cur = con.cursor() 
cur.execute("create table country(name text)") 
for i in data: 
    cur.execute('insert into country values (?)',(i,)) 

print u'По умолчанию все объекты возвращаются типом Unicode' 
cur.execute('select * from country') 
for i in cur.fetchall(): 
    print i[0],type(i[0]) 

print '-'*10 
print u'Выходные данный типа str ' 
con.text_factory=str 
cur.execute('select * from country') 
for i in cur.fetchall(): 
    print i[0],type(i[0]) 

print '-'*10 
print u'Использование преобразующей функции mystr' 
con.text_factory=mystr 
cur.execute('select * from country') 
for i in cur.fetchall(): 
    print i[0],type(i[0]) 

print '-'*10 
print u'Использование OptimizedUnicode ' 
con.text_factory=sqlite3.OptimizedUnicode 
cur.execute('select * from country') 
for i in cur.fetchall(): 
    print i[0],type(i[0])