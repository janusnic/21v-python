# 21v-python unit 15

## КОМАНДА СОЗДАНИЯ ТАБЛИЦЫ

Таблицы создаются командой CREATE TABLE. Эта команда создает пустую таблицу - таблицу без строк. Значения вводятся с помощью DML команды INSERT. Команда CREATE TABLE в основном определяет им таблицы, в виде описания набора имен столбцов указанных в определенном порядке. Она также определяет типы данных и размеры столбцов. Каждая таблица должна иметь по крайней мере один столбец. 

Синтаксис команды CREATE TABLE:
``` 
    CREATE TABLE <TABLE-NAME> 
         ( <COLUMN name> <DATA type>[(<SIZE>)], 
         <COLUMN name> <DATA type> [(<SIZE>)] ... ); 
```
## ВВОД ЗНАЧЕНИЙ

Все строки в SQL вводятся с использованием команды модификации INSERT. В самой простой форме, INSERT использует следующий синтаксис:
```
INSERT INTO <TABLE name>VALUES ( ,  . . .); 
```
Так, например, чтобы ввести строку в таблицу cities, вы можете использовать следующее условие:
```
insert into cities values (1, "Melksham", "SN12")
```
Команды DML не производят никакого вывода. 

Им таблицы, должно быть предварительно определено, в команде CREATE TABLE, а каждое значение пронумерованное в предложении значений, должно совпадать с типом данных столбца, в который оно вставляется. В ANSI, эти значения не могут составлять выражений, что означает что 3 - это доступно, а выражение 2 + 1 - нет. Значения, конечно же, вводятся в таблицу в поименном порядке, поэтому первое значение с именем, автоматически попадает в столбец 1, второе в столбец 2, на так далее.

## ВСТАВКА ПУСТЫХ УКАЗАТЕЛЕЙ (NULL)

Так как значение NULL - это специальный маркер, а не просто символьное значение, он не включается в одиночные кавычки.

## ИМЕНОВАНИЕ СТОЛБЦА ДЛЯ ВСТАВКИ (INSERT)

Вы можете также указывать столбцы, куда вы хотите вставить значение имени. Это позволяет вам вставлять имена в любом порядке. 

По умолчанию может быть введено или значение NULL или другое значе- ние определяемое как - по умолчанию. Если ограничение запрещает использование значения NULL в данном столбце, и этот столбец не установлен как по умолчанию, этот столбец должен быть обеспечен значением для любой команды INSERT которая относится к таблице.

seed.py
```
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

c.execute("""insert into employee values (1, 2, 1, "Hamilkilo", "Hotel", "Chesterton Road", 15., 40.,11,12)""")
c.execute("""insert into employee values (2, 2, 1, "Arun", "Dell", "Chesterton Road", 60., 70.,100,100)""")
c.execute("""insert into employee values (3, 3, 2, "Crown", "Plaza", "Downing Street", 100., 105.,100,200)""")
c.execute("""insert into employee values (4, 1, 2, "Well", "Manor", "Spa Road", 5., 80.,200,110)""")
c.execute("""insert into employee values (5, 1, 2, "Beechfield", "House", "The Main Road", 26., 110.,200,111)""")

conn.commit()

c.execute ("""select * from cities left join employee on cities.city_id = employee.city_id""")

for row in c:
        print (row)

c.close()

(1, u'Melksham', u'SN12', 4, 1, 2, u'Well', u'Manor', u'Spa Road', 5.0, 80.0, 200, 110)
(1, u'Melksham', u'SN12', 5, 1, 2, u'Beechfield', u'House', u'The Main Road', 26.0, 110.0, 200, 111)
(2, u'Cambridge', u'CB1', 1, 2, 1, u'Hamilkilo', u'Hotel', u'Chesterton Road', 15.0, 40.0, 11, 12)
(2, u'Cambridge', u'CB1', 2, 2, 1, u'Arun', u'Dell', u'Chesterton Road', 60.0, 70.0, 100, 100)
(3, u'Foxkilo', u'CB22', 3, 3, 2, u'Crown', u'Plaza', u'Downing Street', 100.0, 105.0, 100, 200)

```
## SQL LEFT JOIN Syntax
```
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name=table2.column_name;

SELECT column_name(s)
FROM table1
LEFT OUTER JOIN table2
ON table1.column_name=table2.column_name;
```
Запрос вернет объединенные данные, которые пересекаются по условию, указанному в LEFT JOIN <..> ON. 
В нашем случае условие <таблица_employee>.<идентификатор_city_id> должен совпадать с <таблица_cities>.<идентификатор>

```
c.execute ("""select * from cities left join employee on cities.city_id = employee.city_id""")

```

## INNER JOIN ON
```
SELECT u.id, u.name, d.name AS d_name
FROM users u
INNER JOIN departments d ON u.d_id = d.id
 ```

Запрос вернет объединенные данные, которые пересекаются по условию, указанному в INNER JOIN ON <..>. 
В нашем случае условие <таблица_пользователей>.<идентификатор_отдела> должен совпадать с <таблица_отделов>.<идентификатор>

Внутреннее объединение INNER JOIN (синоним JOIN, ключевое слово INNER можно опустить). 

Выбираются только совпадающие данные из объединяемых таблиц. Чтобы получить данные, которые не подходят по условию, необходимо использовать 

- внешнее объединение - OUTER JOIN. 

Такое объединение вернет данные из обеих таблиц совпадающими по одному из условий.

Существует два типа внешнего объединения OUTER JOIN - LEFT OUTER JOIN и RIGHT OUTER JOIN. 

Работают они одинаково, разница заключается в том что LEFT - указывает что "внешней" таблицей будет находящаяся слева (в нашем примере это таблица cities). 
Ключевое слово OUTER можно опустить. Запись LEFT JOIN идентична LEFT OUTER JOIN.

``` 
select * from cities left join employee on cities.city_id = employee.city_id
```

# Employee
```
class Employee(object):
    def __init__(self,emp_id,city_id,dep_id,first_name,last_name,address,id,base_pay,shift,hours):
        self.info = {}
        self.info["emp_id"] = emp_id
        self.info["city_id"] = city_id
        self.info["dep_id"] = dep_id
        self.info["first_name"] = first_name
        self.info["last_name"] = last_name
        self.info["address"] = address
        self.info["id"] = id
        self.info["base_pay"] = base_pay
        self.info["shift"] = shift
        self.info["hours"] = hours

        self.SHIFT_2 = 0.05
        self.SHIFT_3 = 0.10
   
   
    def getname(self):
        return self.info["first_name"]+' '+self.info["last_name"]
    
    def show_pay(self):
        if self.info["shift"] == 1:
            return (self.info["base_pay"]*self.info["hours"])
        elif self.info["shift"] == 2:
            return  (self.info["base_pay"] * self.SHIFT_2 + self.info["base_pay"])*self.info["hours"]
        elif self.info["shift"] == 3:
            return (self.info["base_pay"] * self.SHIFT_3 + self.info["base_pay"])*self.info["hours"]

if __name__ == "__main__":
        
    manor = Employee(2,2,1,"Manor","Well","Chesterton Road",80.00,5.,1,8)
    antonia = Employee(1,2,1,"Antonia", "Hourse","Shaw Country Road",45.00,2.,1,12)
    shaw = Employee(1,2,1,"Shaw", "Carry","Antonia Road",44.00,22.,3,6)

    emps = (manor, antonia, shaw)
    for emp in emps:
        print emp.getname(), emp.show_pay()

```

models.py
```
import sqlite3
import employee 

class Model(object):
    def __init__(self):
        self.conn = sqlite3.connect('staff.db')
        self.result = []
   
    def add_employee(self,row):
        new_emp = employee.Employee(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
        self.result.append(new_emp)

    def make_list(self):
        c = self.conn.cursor()
        c.execute ("select * from employee")
        for row in c:
            self.add_employee(row)
        return self.result

    def fetchemployee(self):
        c = self.conn.cursor()
        c.execute ("select * from employee")
        for row in c:
            self.add_employee(row)
        return self.result

if __name__ == "__main__":
    resource = Model()
    # accoms = resource.fetchemployee()
    accoms = resource.make_list()


    for accom in accoms:
        print (accom.getname(),accom.show_pay())
```
accomlist.py
```
import models

class Accomlist(object):
    def __init__(self):
        resource = models.Model()
        self.accoms = resource.fetchemployee()

    def __str__(self):
        result = ""
        for emp in self.accoms:
            called = emp.getname()
            result += "\n" + called
        return result
```
### Список сотрудников компании
```
import sys
import accomlist

from PyQt4 import QtGui
from PyQt4 import QtCore

class MainWindow(QtGui.QDialog):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        QtGui.QMainWindow.__init__(self)
        self.resize(250,150)
        self.setWindowTitle('Список сотрудников компании')

        self.report = str(accomlist.Accomlist())

        self.feedback = QtGui.QLabel(self.report)
        self.quit = QtGui.QPushButton("Quit",self)

        self.grid = QtGui.QVBoxLayout()
        self.grid.addWidget(self.feedback)
        self.grid.addWidget(self.quit)

        self.setLayout(self.grid)

        self.connect(self.quit, QtCore.SIGNAL("clicked()"), self.dunn)

    def dunn(self):
        sys.exit()

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
```
### Список сотрудников компании
```
# -*- coding:utf-8 -*-
import sys
import accomlist

from PyQt4 import QtGui
from PyQt4 import QtCore

class MainWindow(QtGui.QDialog):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        QtGui.QMainWindow.__init__(self)
        self.resize(550,350)
        self.setWindowTitle(u'Список сотрудников компании')

        self.report = str(accomlist.Accomlist())

        self.feedback = QtGui.QLabel(self.report)
        self.quit = QtGui.QPushButton("Quit",self)

        self.grid = QtGui.QVBoxLayout()
        self.grid.addWidget(self.feedback)
        self.grid.addWidget(self.quit)

        self.setLayout(self.grid)

        self.connect(self.quit, QtCore.SIGNAL("clicked()"), self.dunn)

    def dunn(self):
        rusure.show()

class CheckWindow(QtGui.QDialog):
    def __init__(self,parent=None):
        super(CheckWindow,self).__init__(parent)
        QtGui.QMainWindow.__init__(self)
        self.resize(150,100)
        self.setWindowTitle('R U Sure')

        self.yes = QtGui.QPushButton("Yes",self)
        self.no = QtGui.QPushButton("No",self)

        self.grid = QtGui.QVBoxLayout()
        self.grid.addWidget(self.yes)
        self.grid.addWidget(self.no)

        self.setLayout(self.grid)
        self.connect(self.yes, QtCore.SIGNAL("clicked()"), self.dunn)
        self.connect(self.no, QtCore.SIGNAL("clicked()"), self.undunn)

    def dunn(self):
        sys.exit()
    def undunn(self):
        rusure.close()

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()

rusure = CheckWindow()

app.exec_()
```

### оператор IN
Вы можете использовать подзапросы которые производят любое число строк если вы используете специальный оператор IN ( операторы BETWEEN, LIKE, и IS NULL не могут использоваться с подзапросами ). IN определяет набор значений, одно из которых должно совпадать с другим термином уравнения предиката в порядке, чтобы предикат был верным. Когда вы используете IN с подзапросом, SQL просто формирует этот набор из вывода подзапроса.

### CHECK
```
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
```

### enum
```
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
```
## ALTER TABLE
SQLite версия команды ALTER TABLE позволяет пользователю переименовать или добавить новые поля в существующую таблицу. Нет возможности удалить поле из таблицы.

Синтаксис RENAME TO используется при переименовании таблицы из [database-name.]table-name в new-table-name. Эта команда не может применяться для переноса таблиц между базами данных, только переименование в пределах одной базы.
Если переименованная таблица имеет триггеры или индексы, то они остаются связанными с таблицей и после переименования. Однако, если имеются представления (view) или запросы выполняемые триггерами, ссылаются на переименованную таблицу, то они автоматически не изменяются. Если необходимо то триггеры и представления, должны быть удалены и повторно созданы вручную. 

### Синтаксис ADD [COLUMN]
Синтаксис ADD [COLUMN] используется для добавления нового поля в существующую таблицу. Новый столбец всегда добавляется в конец списка полей. Описание добавляемого столбца должен соответствовать формату, разрешенному в CREATE TABLE, со следующими ограничениями: 
- Столбец не может иметь ограничений PRIMARY KEY или UNIQUE.
- Столбец не может иметь значений по умолчанию CURRENT_TIME, CURRENT_DATE или CURRENT_TIMESTAMP.
- Если наложено ограничение NOT NULL, столбец должен иметь значение по умолчанию, отличное от NULL.
Время выполнения команды ALTER TABLE не зависит от количества данных в таблице. ALTER TABLE работает также быстро на таблице с 10 миллионами записей, как и на таблице с 1 записью. 
После выполнения ADD COLUMN, база данных не будет читаться SQLite версии 3.1.3 и ниже, до применения команды VACUUM.

Добавим к нашей таблице employee column updatedon. 

```
sqlite> alter table employee add column updatedon date;
```

sqlite> .schema employee
```
CREATE TABLE employee (
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
        title varchar(10) NOT NULL DEFAULT '', updatedon date);

```

## CREATE TRIGGER Триггеры в SQLite 
Триггеры в SQLite – это функции, которые выполняются по какому-то событию. Например, вставка строки в базу, удаление строки, обновление поля. Причем триггеры могут срабатывать как до выполнения действий по некоторому событию, так и после. 
#### create trigger

employee_update_trg.sql
```
create trigger employee_update_trg after update on employee
begin
  update employee set updatedon = datetime('NOW') where emp_id = new.emp_id;
end;
```
create trigger
```
sqlite3 staff.db   < employee_update_trg.sql
```
Тестируем триггер. 

```
sqlite> .schema employee

CREATE TABLE employee (
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
        title varchar(10) NOT NULL DEFAULT '', updatedon date);
CREATE TRIGGER employee_update_trg after update on employee
begin
  update employee set updatedon = datetime('NOW') where emp_id = new.emp_id;
end;

```
Тестируем триггер. update employee
```
sqlite> update employee set title='Sales Manager' where emp_id=4;

```

Тестируем триггер.  sqlite> select * from employee;
```
1|2|1|W|Hamilkilo|Mark|Chesterton Road|15.0|40.0|1|12|SEO|
2|2|1|M|Arun|Della|Chesterton Road|60.0|70.0|1|100|Accouter|
3|3|2|M|Crown|Poll|Downing Street|100.0|105.0|1|200|Security|
4|1|2|M|Well|John|Spa Road|5.0|80.0|2|110|Sales Manager|2015-11-02 13:24:36
5|1|2|W|Beechfield|Ann|The Main Road|26.0|110.0|2|111|Admin|
6|3|1|W|Jane|Smith|Milk Road|27.0|210.0|1|111|Sale Manager|
7|3|1|W|Rita|Patel|Flower Road|28.0|410.0|3|111|DBA|

```

### UPDATE
```
UPDATE [ OR conflict-algorithm ] [database-name .] table-name
SET column1=expression1, column2=expression2, ... 
[WHERE expr]
assignment ::=
column-name = expr
```
Оператор UPDATE используется для изменения значения столбцов в выбранных записях таблицы. Каждое присваивание в UPDATE определяется именем колонки слева от знака равенства и вычисляемым выражением в правой. Выражение может использовать значения других полей. Все выражения вычисляются перед выполнением присваивания (например, в MySQL это не так) Оператор WHERE может использоваться для задания обновляемых записей.
Опциональный оператор конфликта, позволяет определить правила альтернативного алгоритма разрешения конфликтных ситуаций, которые будут применяться при выполнении команды, смотрите ON CONFLICT.

## Представление (VIEW)
Представление (VIEW) - объект данных который не содержит никаких данных его владельца. Это - тип таблицы, чье содержание выбирается из других таблиц с помощью выполнения запроса. Поскольку значения в этих таблицах меняются, то авто- матически, их значения могут быть показаны представлением. В этой главе, вы узнаете что такое представления, как они создаются, и не- много об их возможностях и ограничениях. Использование представлений основанных на улучшенных средствах запросов, таких как объединение и под- запрос, разработанных очень тщательно, в некоторых случаях даст больший выигрыш по сравнению с запросами.

### ЧТО ТАКОЕ ПРЕДСТАВЛЕНИЕ ?

Типы таблиц, с которыми вы имели дело до сих пор, назывались - базовыми таблицами. Это - таблицы, которые содержат данные. Однако имеется другой вид таблиц: - представления. Представления - это таблицы чье содержание выбирается или получается из других таблиц. Они работают в запросах и операторах DML точно также как и основные таблицы, но не содержат ника- ких собственных данных. Представления - подобны окнам, через которые вы просматриваете информа- цию( как она есть, или в другой форме, как вы потом увидите ), которая фактически хранится в базовой таблице. Представление - это фактически запрос, который выполняется всякий раз, когда представление становится темой ко- манды. Вывод запроса при этом в каждый момент становится содержанием представления.

### КОМАНДА CREATE VIEW

Вы создаете представление командой CREATE VIEW. Она состоит из слов CREATE VIEW (СОЗДАТЬ ПРЕДСТАВЛЕНИЕ), имени представления которое нужно создать, слова AS (КАК), и далее запроса, как в следующем примере:
  
```
create view empdept as select emp_id, e.first_name, title, d.name, d.location from employee e, deps d where e.dep_id = d.dep_id;
```

## create view
```
sqlite> create view empdept as select emp_id, e.first_name, title, d.name, d.location from employee e, deps d where e.dep_id = d.dep_id;
```
Теперь Вы имеете представление, называемое empdept. Вы можете использовать это представление точно так же как и любую другую таблицу. Она может быть запрошена, модифицирована, вставлена в, удалена из, и соединена с, другими таблицами и представлениями. 

```
sqlite> select * from empdept;
1|Hamilkilo|SEO|IBM|NYC
2|Arun|Accouter|IBM|NYC
3|Crown|Security|MS|LA
4|Well|Sales Manager|MS|LA
5|Beechfield|Admin|MS|LA
6|Jane|Sale Manager|IBM|NYC
7|Rita|DBA|IBM|NYC
```
## ПРЕДСТАВЛЕНИЯ И ОБЪЕДИНЕНИЯ

Представления не требуют чтобы их вывод осуществлялся из одной базовой таблицы. Так как почти любой допустимый запрос SQL может быть использован в представлении, он может выводить информацию из любого числа базовых таблиц, или из других представлений. 
```
create view empdept as select emp_id, e.first_name, title, d.name, d.location from employee e, deps d where e.dep_id = d.dep_id;
```

# Employee
```
class Employee(object):
    def __init__(self,emp_id,sex,city_id,dep_id,first_name,last_name,address,id,base_pay,shift,hours,title,updatedon):
        self.info = {}
        self.info["emp_id"] = emp_id
        self.info["city_id"] = city_id
        self.info["dep_id"] = dep_id
        self.info["first_name"] = first_name
        self.info["last_name"] = last_name
        self.info["address"] = address
        self.info["id"] = id
        self.info["base_pay"] = base_pay
        self.info["shift"] = shift
        self.info["hours"] = hours
        self.info["updatedon"] = updatedon
        self.info["title"] = title
        self.info["sex"] = sex

        self.SHIFT_2 = 0.05
        self.SHIFT_3 = 0.10
    
    
    def getname(self):
        return self.info["first_name"]+' '+self.info["last_name"]
    
    def show_pay(self):
        if self.info["shift"] == 1:
            return (self.info["base_pay"]*self.info["hours"])
        elif self.info["shift"] == 2:
            return  (self.info["base_pay"] * self.SHIFT_2 + self.info["base_pay"])*self.info["hours"]
        elif self.info["shift"] == 3:
            return (self.info["base_pay"] * self.SHIFT_3 + self.info["base_pay"])*self.info["hours"]


if __name__ == "__main__":
        
    manor = Employee(2,2,1,"Manor","Well","Chesterton Road",80.00,5.,1,8)
    antonia = Employee(1,2,1,"Antonia", "Hourse","Shaw Country Road",45.00,2.,1,12)
    shaw = Employee(1,2,1,"Shaw", "Carry","Antonia Road",44.00,22.,3,6)

    emps = (manor, antonia, shaw)
    for emp in emps:
        print emp.getname(), emp.show_pay()
```

models.py
```
import sqlite3
import employee 

class Model(object):
    def __init__(self):
        self.conn = sqlite3.connect('staff.db')
        self.result = []
   
    def add_employee(self,row):
        new_emp = employee.Employee(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12])
        self.result.append(new_emp)

    def make_list(self):
        c = self.conn.cursor()
        c.execute ("select * from employee")
        for row in c:
            self.add_employee(row)
        return self.result

    def fetchemployee(self):
        c = self.conn.cursor()
        c.execute ("select * from employee")
        for row in c:
            self.add_employee(row)
        return self.result

if __name__ == "__main__":
    resource = Model()
    # accoms = resource.fetchemployee()
    accoms = resource.make_list()


    for accom in accoms:
        print (accom.getname(),accom.show_pay())

```

main1.py

```
# -*- coding:utf-8 -*-
import sys
import accomlist

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

from ext import find, wordcount
from ext import datetime, table

class Main(QtGui.QMainWindow):

    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)

        self.filename = ""

        self.changesSaved = True

        self.initUI()

    def initToolbar(self):

        self.newAction = QtGui.QAction(QtGui.QIcon("icons/new.png"),"New",self)
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.setStatusTip("Create a new document from scratch.")
        self.newAction.triggered.connect(self.new)

        self.openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"),"Open file",self)
        self.openAction.setStatusTip("Open existing document")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)

        self.saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
        self.saveAction.setStatusTip("Save document")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)

        self.printAction = QtGui.QAction(QtGui.QIcon("icons/print.png"),"Print document",self)
        self.printAction.setStatusTip("Print document")
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.triggered.connect(self.printHandler)

        self.previewAction = QtGui.QAction(QtGui.QIcon("icons/preview.png"),"Page view",self)
        self.previewAction.setStatusTip("Preview page before printing")
        self.previewAction.setShortcut("Ctrl+Shift+P")
        self.previewAction.triggered.connect(self.preview)

        self.findAction = QtGui.QAction(QtGui.QIcon("icons/find.png"),"Find and replace",self)
        self.findAction.setStatusTip("Find and replace words in your document")
        self.findAction.setShortcut("Ctrl+F")
        self.findAction.triggered.connect(find.Find(self).show)

        self.cutAction = QtGui.QAction(QtGui.QIcon("icons/cut.png"),"Cut to clipboard",self)
        self.cutAction.setStatusTip("Delete and copy text to clipboard")
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.triggered.connect(self.text.cut)

        self.copyAction = QtGui.QAction(QtGui.QIcon("icons/copy.png"),"Copy to clipboard",self)
        self.copyAction.setStatusTip("Copy text to clipboard")
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.text.copy)

        self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/paste.png"),"Paste from clipboard",self)
        self.pasteAction.setStatusTip("Paste text from clipboard")
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.text.paste)

        self.undoAction = QtGui.QAction(QtGui.QIcon("icons/undo.png"),"Undo last action",self)
        self.undoAction.setStatusTip("Undo last action")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.text.undo)

        self.redoAction = QtGui.QAction(QtGui.QIcon("icons/redo.png"),"Redo last undone thing",self)
        self.redoAction.setStatusTip("Redo last undone thing")
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.text.redo)

        dateTimeAction = QtGui.QAction(QtGui.QIcon("icons/calender.png"),"Insert current date/time",self)
        dateTimeAction.setStatusTip("Insert current date/time")
        dateTimeAction.setShortcut("Ctrl+D")
        dateTimeAction.triggered.connect(datetime.DateTime(self).show)

        wordCountAction = QtGui.QAction(QtGui.QIcon("icons/count.png"),"See word/symbol count",self)
        wordCountAction.setStatusTip("See word/symbol count")
        wordCountAction.setShortcut("Ctrl+W")
        wordCountAction.triggered.connect(self.wordCount)

        self.toolbar = self.addToolBar("Options")

        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.previewAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)
        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.findAction)
        self.toolbar.addAction(dateTimeAction)
        self.toolbar.addAction(wordCountAction)


        self.addToolBarBreak()


    def initMenubar(self):

        menubar = self.menuBar()

        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")

        # Add the most important actions to the menubar

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)
        file.addAction(self.printAction)
        file.addAction(self.previewAction)

        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)
        edit.addAction(self.findAction)

        # Toggling actions for the various bars
        toolbarAction = QtGui.QAction("Toggle Toolbar",self)
        toolbarAction.triggered.connect(self.toggleToolbar)

        statusbarAction = QtGui.QAction("Toggle Statusbar",self)
        statusbarAction.triggered.connect(self.toggleStatusbar)

        view.addAction(toolbarAction)

        view.addAction(statusbarAction)

    def initUI(self):

        self.text = QtGui.QTextEdit(self)

        # Set the tab stop width to around 33 pixels which is
        # more or less 8 spaces
        self.text.setTabStopWidth(33)

        self.initToolbar()

        self.initMenubar()

        self.setCentralWidget(self.text)


        # Initialize a statusbar for the window
        self.statusbar = self.statusBar()

        # If the cursor position changes, call the function that displays
        # the line and column number
        self.text.cursorPositionChanged.connect(self.cursorPosition)


        self.text.textChanged.connect(self.changed)

        self.setGeometry(100,100,1030,800)
        self.setWindowTitle(u'Список сотрудников компании')

        self.setWindowIcon(QtGui.QIcon("icons/icon.png"))

    def changed(self):
        self.changesSaved = False

    def closeEvent(self,event):

        if self.changesSaved:

            event.accept()

        else:
        
            popup = QtGui.QMessageBox(self)

            popup.setIcon(QtGui.QMessageBox.Warning)
            
            popup.setText("The document has been modified")
            
            popup.setInformativeText("Do you want to save your changes?")
            
            popup.setStandardButtons(QtGui.QMessageBox.Save   |
                                      QtGui.QMessageBox.Cancel |
                                      QtGui.QMessageBox.Discard)
            
            popup.setDefaultButton(QtGui.QMessageBox.Save)

            answer = popup.exec_()

            if answer == QtGui.QMessageBox.Save:
                self.save()

            elif answer == QtGui.QMessageBox.Discard:
                event.accept()

            else:
                event.ignore()

    def toggleToolbar(self):

        state = self.toolbar.isVisible()

        # Set the visibility to its inverse
        self.toolbar.setVisible(not state)


    def toggleStatusbar(self):

        state = self.statusbar.isVisible()

        # Set the visibility to its inverse
        self.statusbar.setVisible(not state)

    def new(self):

        spawn = Main()

        spawn.show()

    def open(self):

        # Get filename and show only .writer files
        self.report = str(accomlist.Accomlist())

        #self.feedback = QtGui.QLabel(self.report)
        

        
        # self.grid.addWidget(self.feedback)

        # self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',".","(*.writer)")

        #if self.filename:
        #    with open(self.filename,"rt") as file:
        self.text.setText(self.report)

    def save(self):

        # Only open dialog if there is no filename yet
        if not self.filename:
          self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')

        if self.filename:
            
            # Append extension if not there yet
            if not self.filename.endswith(".writer"):
              self.filename += ".writer"

            # We just store the contents of the text file along with the
            # format in html, which Qt does in a very nice way for us
            with open(self.filename,"wt") as file:
                file.write(self.text.toHtml())

            self.changesSaved = True

    def preview(self):

        # Open preview dialog
        preview = QtGui.QPrintPreviewDialog()

        # If a print is requested, open print dialog
        preview.paintRequested.connect(lambda p: self.text.print_(p))

        preview.exec_()

    def printHandler(self):

        # Open printing dialog
        dialog = QtGui.QPrintDialog()

        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def cursorPosition(self):

        cursor = self.text.textCursor()

        # Mortals like 1-indexed things
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()

        self.statusbar.showMessage("Line: {} | Column: {}".format(line,col))

    def wordCount(self):

        wc = wordcount.WordCount(self)

        wc.getText()

        wc.show()


    def fontColorChanged(self):

        # Get a color from the text dialog
        color = QtGui.QColorDialog.getColor()

        # Set it as the new text color
        self.text.setTextColor(color)

    def highlight(self):

        color = QtGui.QColorDialog.getColor()

        self.text.setTextBackgroundColor(color)

def main():
    app = QtGui.QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
```

### Как изменить кодировку базы данных в utf8:
```
sqlite3 mydb.db ".dump" | iconv -f cp1251 -t utf8 > dump.sql
sqlite3 mydb-utf.db ".read dump.sql"
```

