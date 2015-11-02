import sqlite3

conn = sqlite3.connect('staff.db')

c = conn.cursor()

c.execute("""drop table if exists cities""")
c.execute("""drop table if exists deps""")
c.execute("""drop table if exists employee""")

conn.commit()

c.execute("""create table cities (
        city_id     int     primary key not NULL ,
        name    text,
        postcode        text)""")

c.execute("""create table deps (
        dep_id     int     primary key not NULL ,
        name    text,
        description    text)""")


c.execute("""create table employee (
        emp_id      int     primary key not NULL ,
        city_id     int,
        dep_id      int,
        first_name    text,
        last_name    text,
        address text,
        id   float,
        base_pay    float,
        shift    int,
        hours    int)""")

c.execute("""insert into cities values (1, "Melksham", "SN12")""")
c.execute("""insert into cities values (2, "Cambridge", "CB1")""")
c.execute("""insert into cities values (3, "Foxkilo", "CB22")""")

c.execute("""insert into deps values (1, "IBM", "Computing sys")""")
c.execute("""insert into deps values (2, "MS", "Ms Computing sys")""")

c.execute("""insert into employee values (1, 2, 1, "Hamilkilo", "Hotel", "Chesterton Road", 15., 40.,1,12)""")
c.execute("""insert into employee values (2, 2, 1, "Arun", "Dell", "Chesterton Road", 60., 70.,1,100)""")
c.execute("""insert into employee values (3, 3, 2, "Crown", "Plaza", "Downing Street", 100., 105.,1,200)""")
c.execute("""insert into employee values (4, 1, 2, "Well", "Manor", "Spa Road", 5., 80.,2,110)""")
c.execute("""insert into employee values (5, 1, 2, "Beechfield", "House", "The Main Road", 26., 110.,2,111)""")

conn.commit()

c.execute ("""select * from cities left join employee on cities.city_id = employee.city_id""")

for row in c:
        print (row)

c.close()