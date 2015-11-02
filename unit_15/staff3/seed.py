import sqlite3

conn = sqlite3.connect('staff.db')

c = conn.cursor()

c.execute("""drop table if exists cities""")
c.execute("""drop table if exists deps""")
c.execute("""drop table if exists employee""")

conn.commit()

c.execute("""create table cities (
        city_id     int     primary key not NULL ,
        name    text CHECK( LENGTH(name) <= 100 ) NOT NULL DEFAULT '',
        postcode varchar(10) NOT NULL DEFAULT '0001')""")

c.execute("""create table deps (
        dep_id     int     primary key not NULL ,
        name    text CHECK( LENGTH(name) <= 100 ) NOT NULL DEFAULT '',
        location varchar(50) NOT NULL DEFAULT '',
        description    text)""")


c.execute("""create table employee (
        emp_id      int     primary key not NULL ,
        city_id     int,
        dep_id      int,
        sex    varchar(1) CHECK( sex IN ('M','W') ) NOT NULL DEFAULT 'M',
        first_name   varchar(20),
        last_name    varchar(20),
        address text NOT NULL DEFAULT '',
        id   float NOT NULL DEFAULT 0.0,
        base_pay float NOT NULL DEFAULT 0,
        shift    int NOT NULL DEFAULT 0,
        hours    int NOT NULL DEFAULT 0,
        title varchar(10) NOT NULL DEFAULT '')""")

c.execute("""insert into cities values (1, "Melksham", "SN12")""")
c.execute("""insert into cities values (2, "Cambridge", "CB1")""")
c.execute("""insert into cities values (3, "Foxkilo", "CB22")""")

c.execute("""insert into deps values (1, "IBM",'NYC', "Computing sys")""")
c.execute("""insert into deps values (2, "MS", 'LA',  "Ms Computing sys")""")

c.execute("""insert into employee values (1, 2, 1,'W',"Hamilkilo", "Mark", "Chesterton Road", 15., 40.,1,12,'SEO')""")
c.execute("""insert into employee values (2, 2, 1,'M',"Arun", "Della", "Chesterton Road", 60., 70.,1,100,'Accouter')""")
c.execute("""insert into employee values (3, 3, 2,'M',"Crown", "Poll", "Downing Street", 100., 105.,1,200,'Security')""")
c.execute("""insert into employee values (4, 1, 2,'M',"Well", "John", "Spa Road", 5., 80.,2,110,'Developer')""")
c.execute("""insert into employee values (5, 1, 2,'W',"Beechfield", "Ann", "The Main Road", 26., 110.,2,111,'Admin')""")
c.execute("""insert into employee values (6, 3, 1,'W','Jane', 'Smith',"Milk Road", 27., 210.,1,111,'Sale Manager')""")
c.execute("""insert into employee values (7, 3, 1,'W','Rita', 'Patel',"Flower Road", 28., 410.,3,111,'DBA')""")

conn.commit()

c.execute ("""select * from cities left join employee on cities.city_id = employee.city_id""")

for row in c:
        print (row)

c.close()