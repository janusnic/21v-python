import sqlite3

conn = sqlite3.connect('staff.db')

c = conn.cursor()

c.execute("""drop table if exists cities""")
c.execute("""drop table if exists deps""")
c.execute("""drop table if exists employee""")

conn.commit()

c.execute("""create table cities (
        city_id INTEGER  primary key AUTOINCREMENT UNIQUE not NULL ,
        name    text CHECK( LENGTH(name) <= 100 ) NOT NULL DEFAULT '',
        postcode varchar(10) NOT NULL DEFAULT '0001')""")

c.execute("""create table deps (
        dep_id  INTEGER     primary key AUTOINCREMENT UNIQUE not NULL ,
        name    text CHECK( LENGTH(name) <= 100 ) NOT NULL DEFAULT '',
        location varchar(50) NOT NULL DEFAULT '',
        description    text)""")


c.execute("""create table employee (
        id   INTEGER  primary key AUTOINCREMENT UNIQUE NOT NULL ,
        city_id     INTEGER,
        dep_id      INTEGER,
        first_name   varchar(20),
        last_name    varchar(20),
        sex    varchar(1) CHECK( sex IN ('M','W') ) NOT NULL DEFAULT 'M',
        address text NOT NULL DEFAULT '',
        pid   float NOT NULL DEFAULT 0.0,
        title varchar(10) NOT NULL DEFAULT '',
        salary float NOT NULL DEFAULT 0,
        shift    int NOT NULL DEFAULT 0,
        hours    int NOT NULL DEFAULT 0
        )""")

c.execute("""insert into cities values (1,"Longon", "SN12")""")
c.execute("""insert into cities values (2,"Cambridge", "CB1")""")
c.execute("""insert into cities values (3,"Kiev", "CB22")""")

c.execute("""insert into deps values (1,"IBM",'NYC', "Computing sys")""")
c.execute("""insert into deps values (2,"MS", 'LA',  "Ms Computing sys")""")

c.execute("""insert into employee values (1,2, 1,"Hamilkilo", "Mark",'W', "Chesterton Road",'SEO', 15., 40.,1,12)""")
c.execute("""insert into employee values (2,2, 1,"Arun", "Della",'M', "Chesterton Road", 60.,'Accouter', 70.,1,100)""")
c.execute("""insert into employee values (3,3, 2,"Crown", "Poll",'M', "Downing Street", 100.,'Security', 105.,1,200)""")
c.execute("""insert into employee values (4,1, 2,"Well", "John",'M', "Spa Road", 5.,'Developer', 80.,2,110)""")

c.execute("""insert into employee values (5,3, 1,'Jane', 'Smith','W',"Milk Road", 27.,'Sale Manager', 210.,1,111)""")
c.execute("""insert into employee values (6,3, 1,'Rita', 'Patel','W',"Flower Road", 28.,'DBA', 410.,3,111)""")

conn.commit()

c.execute ("""select * from cities left join employee on cities.city_id = employee.city_id""")

for row in c:
        print (row)

c.close()