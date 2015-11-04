# 21v-python unit 16

staff1

main1.py
```
# -*- coding:utf-8 -*-
import os
import sys
from PyQt4.QtCore import (QFile, QString, QVariant, Qt)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtGui import (QApplication, QDialog, QDialogButtonBox, QMenu,
        QMessageBox, QTableView, QVBoxLayout)
from PyQt4.QtSql import (QSqlDatabase, QSqlQuery, QSqlTableModel)


class StaffDataDlg(QDialog):

    def __init__(self, parent=None):
        super(StaffDataDlg, self).__init__(parent)
        self.create_widgets()
        self.layout_widgets()
        
        self.setMinimumWidth(850)
        self.setWindowTitle(u'Список сотрудников компании')


    def create_widgets(self):
        self.model = QSqlTableModel(self)
        

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setSelectionMode(QTableView.SingleSelection)
        self.view.setSelectionBehavior(QTableView.SelectRows)
        
        self.view.resizeColumnsToContents()

        self.buttonBox = QDialogButtonBox()
        self.addButton = self.buttonBox.addButton(u"&Добавить",
                QDialogButtonBox.ActionRole)
        self.deleteButton = self.buttonBox.addButton(u"&Удалить",
                QDialogButtonBox.ActionRole)
        self.sortButton = self.buttonBox.addButton(u"&Сортировать",
                QDialogButtonBox.ActionRole)
        

    def layout_widgets(self):
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)

    form = StaffDataDlg()
    form.show()

    sys.exit(app.exec_())


main()

```

### main.py
#### menu = QMenu(self)

```
# -*- coding:utf-8 -*-
import os
import sys
from PyQt4.QtCore import (QFile, QString, QVariant, Qt)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtGui import (QApplication, QDialog, QDialogButtonBox, QMenu,
        QMessageBox, QTableView, QVBoxLayout)
from PyQt4.QtSql import (QSqlDatabase, QSqlQuery, QSqlTableModel)


class StaffDataDlg(QDialog):

    def __init__(self, parent=None):
        super(StaffDataDlg, self).__init__(parent)
        self.create_widgets()
        self.layout_widgets()

        self.setMinimumWidth(850)
        self.setWindowTitle(u'Список сотрудников компании')


    def create_widgets(self):
        self.model = QSqlTableModel(self)
        

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setSelectionMode(QTableView.SingleSelection)
        self.view.setSelectionBehavior(QTableView.SelectRows)

        self.view.resizeColumnsToContents()

        self.buttonBox = QDialogButtonBox()
        self.addButton = self.buttonBox.addButton(u"&Добавить",
                QDialogButtonBox.ActionRole)
        self.deleteButton = self.buttonBox.addButton(u"&Удалить",
                QDialogButtonBox.ActionRole)
        self.sortButton = self.buttonBox.addButton(u"&Сортировать",
                QDialogButtonBox.ActionRole)
        

        menu = QMenu(self)
        self.sortByCategoryAction = menu.addAction(u"Сортировка по &Имени")
        self.sortByDescriptionAction = menu.addAction(
                u"Сортировка по &Подразделениям")
        self.sortByIDAction = menu.addAction(u"Сортировка по &ID")
        self.sortButton.setMenu(menu)
        self.closeButton = self.buttonBox.addButton(QDialogButtonBox.Close)


    def layout_widgets(self):
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)

    form = StaffDataDlg()
    form.show()

    sys.exit(app.exec_())


main()

```


## staff2

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
        name    text CHECK( LENGTH(name) <= 100 ) NOT NULL DEFAULT '',
        postcode varchar(10) NOT NULL DEFAULT '0001')""")

c.execute("""create table deps (
        dep_id     int     primary key not NULL ,
        name    text CHECK( LENGTH(name) <= 100 ) NOT NULL DEFAULT '',
        location varchar(50) NOT NULL DEFAULT '',
        description    text)""")


c.execute("""create table employee (
        id      int     primary key not NULL ,
        city_id     int,
        dep_id      int,
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

c.execute("""insert into cities values (1, "Melksham", "SN12")""")
c.execute("""insert into cities values (2, "Cambridge", "CB1")""")
c.execute("""insert into cities values (3, "Foxkilo", "CB22")""")

c.execute("""insert into deps values (1, "IBM",'NYC', "Computing sys")""")
c.execute("""insert into deps values (2, "MS", 'LA',  "Ms Computing sys")""")

c.execute("""insert into employee values (1, 2, 1,"Hamilkilo", "Mark",'W', "Chesterton Road",'SEO', 15., 40.,1,12)""")
c.execute("""insert into employee values (2, 2, 1,"Arun", "Della",'M', "Chesterton Road", 60.,'Accouter', 70.,1,100)""")
c.execute("""insert into employee values (3, 3, 2,"Crown", "Poll",'M', "Downing Street", 100.,'Security', 105.,1,200)""")
c.execute("""insert into employee values (4, 1, 2,"Well", "John",'M', "Spa Road", 5.,'Developer', 80.,2,110)""")

c.execute("""insert into employee values (5, 3, 1,'Jane', 'Smith','W',"Milk Road", 27.,'Sale Manager', 210.,1,111)""")
c.execute("""insert into employee values (6, 3, 1,'Rita', 'Patel','W',"Flower Road", 28.,'DBA', 410.,3,111)""")

conn.commit()

c.execute ("""select * from cities left join employee on cities.city_id = employee.city_id""")

for row in c:
        print (row)

c.close()
```

### Работа с базами данных в Qt

1.Слой драйверов — Включает классы QSqlDriver, QSqlDriverCreator, QSqlDriverCreatorBase, QSqlDriverPlugin и QSqlResult. Этот слой предоставляет низкоуровневый мост между определенными базами данных и слоем SQL API.

2.Слой SQL API — Этот слой предоставляет доступ к базам данных. Соединения устанавливаются с помощью класса QSqlDatabase. Взаимодействие с базой данных осуществляется с помощью класса QSqlQuery. В дополнение к классам QSqlDatabase и QSqlQuery слой SQL API опирается на классы QSqlError, QSqlField, QSqlIndex и QsqlRecord.

3.Слой пользовательского интерфейса — Этот слой связывает данные из базы данных с дата-ориентироваными виджетами. Сюда входят такие классы, как QSqlQueryModel, QSqlTableModel и QSqlRelationalTableModel.

#### Соединение с базой данных
Чтобы получить доступ к базе данных с помощью QSqlQuery и QSqlQueryModel, необходимо создать и открыть одно или более соединений с базой данных.

Qt может работать со следующими базами данных (из-за несовместимости с GPL лицензией, не все плагины поставляются с Qt Open Source Edition):
- QDB2 — IBM DB2 (версия 7.1 и выше
- QIBASE — Borland InterBase
- QMYSQL — MySQL
- QOCI — Драйвер Oracle Call Interface
- QODBC — Open Database Connectivity (ODBC) — Microsoft SQL Server и другие ODBC-совместимые базы данных
- QPSQL — PostgreSQL (версия 7.3 и выше)
- QSQLITE2 — SQLite версии 2
- QSQLITE — SQLite версии 3
- QTDS — Драйвер Sybase Adaptive Server

Соединиться с базой данных можно вот так:
```
    filename = os.path.join(os.path.dirname(__file__), "staff.db")
    create = not QFile.exists(filename)

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(filename)
    if not db.open():
        QMessageBox.warning(None, "Reference Data",
            QString("Database Error: %1").arg(db.lastError().text()))
        sys.exit(1)
```
строка db = QSqlDatabase.addDatabase("QSQLITE") создает объект соединения, а db.open() открывает его. В промежутке инициализируется некоторая информация о соединении, включая имя соединения, имя базы данных, имя узла, имя пользователя, пароль. 

Как только соединение установлено, можно вызвать статическую функцию QSqlDatabase::database() из любого места программы с указанием имени соединения, чтобы получить указатель на это соединение. Если не передать имя соединения, она вернет соединение по умолчанию.

Если open() потерпит неудачу, он вернет false. В этом случае, можно получить информацию об ошибке, вызвав QSqlDatabase::lastError().
```
if not db.open():
        QMessageBox.warning(None, "Reference Data",
            QString("Database Error: %1").arg(db.lastError().text()))
        sys.exit(1)
```

Для удаления соединения с базой данных, надо сначала закрыть базу данных с помощью QSqlDatabase::close(), а затем, удалить соединение с помощью статического метода QSqlDatabase::removeDatabase().

### Выполнение инструкций SQL
Класс QSqlQuery обеспечивает интерфейс для выполнения SQL запросов и навигации по результирующей выборке. Для выполнения SQL запросов, просто создают объект QSqlQuery и вызывают QSqlQuery::exec(). 
```
            query.exec_(QString("SELECT COUNT(*) FROM employee "
                                "WHERE deo_id = %1").arg(id))

```
Конструктор QSqlQuery принимает необязательный аргумент QSqlDatabase, который уточняет, какое соединение с базой данных используется. Если его не указать, то используется соединение по умолчанию. Если возникает ошибка, exec() возвращает false. Доступ к ошибке можно получить с помощью QSqlQuery::lastError().

QSqlQuery предоставляет единовременный доступ к результирующей выборке одного запроса. После вызова exec(), внутренний указатель QSqlQuery указывает на позицию перед первой записью. Если вызвать метод QSqlQuery::next() один раз, то он переместит указатель к первой записи. После этого необходимо повторять вызов next(), чтобы получать доступ к другим записям, до тех пор пока он не вернет false. 

QSqlQuery может выполнять не только SELECT, но также и любые другие запросы. 

При вставке множества записей требуется вызвать QSqlQuery::prepare() только однажды. Далее можно вызвать bindValue() или addBindValue() с последующим вызовом exec() столько раз, сколько потребуется.

### Класс QSqlTableModel
Класс QSqlTableModel предоставляет редактируемую модель данных для одной таблицы базы данных.

QSqlTableModel - это высокоуровневый интерфейс к записям одной таблицы базы данных с возможностью и чтения и записи. Он является надстройкой нижнего уровня QSqlQuery и может быть использован, чтобы предоставлять данные для классов представлений, таких как QTableView. 

Мы устанавливаем имя SQL таблицы и стратегию редактирования, затем мы устанавливаем метки отображаемые в заголовках представления. 
```
    def create_widgets(self):
        self.model = QSqlTableModel(self)
        self.model.setTable("employee")

```

Стратегия редактирования предписывает, когда изменения сделанные пользователем в представлении применяются в базе данных. Возможные значения стратегии - это OnFieldChange, OnRowChange и OnManualSubmit.

### main.py
```
# -*- coding:utf-8 -*-
import os
import sys
from PyQt4.QtCore import (QFile, QString, QVariant, Qt)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtGui import (QApplication, QDialog, QDialogButtonBox, QMenu,
        QMessageBox, QTableView, QVBoxLayout)
from PyQt4.QtSql import (QSqlDatabase, QSqlQuery, QSqlTableModel)

ID, CITY, DEPARTMENT, FIRSTNAME, LASTNAME, SEX, ADDRESS, PID, TITLE, SOLARY, SHIFT, HOURS = range(12)

   

class StaffDataDlg(QDialog):

    def __init__(self, parent=None):
        super(StaffDataDlg, self).__init__(parent)
        self.create_widgets()
        self.layout_widgets()
        self.create_connections()
        self.setMinimumWidth(850)
        self.setWindowTitle(u'Список сотрудников компании')


    def create_widgets(self):
        self.model = QSqlTableModel(self)
        self.model.setTable("employee")
        self.model.setSort(ID, Qt.AscendingOrder)
        self.model.setHeaderData(ID, Qt.Horizontal, QVariant("ID"))
        self.model.setHeaderData(CITY, Qt.Horizontal,
                QVariant("City"))
        self.model.setHeaderData(DEPARTMENT, Qt.Horizontal,
                QVariant("Department"))
        self.model.setHeaderData(FIRSTNAME, Qt.Horizontal,
                QVariant("First Name"))
        self.model.setHeaderData(LASTNAME, Qt.Horizontal,
                QVariant("Last Name"))
        self.model.setHeaderData(SEX, Qt.Horizontal,
                QVariant("sex"))
        self.model.setHeaderData(ADDRESS, Qt.Horizontal,
                QVariant("Address"))
        self.model.setHeaderData(PID, Qt.Horizontal,
                QVariant("PID"))
        
        self.model.setHeaderData(TITLE, Qt.Horizontal,
                QVariant("Title"))
        
        self.model.setHeaderData(SOLARY, Qt.Horizontal,
                QVariant("SOLARY"))
        self.model.setHeaderData(SHIFT, Qt.Horizontal,
                QVariant("SHIFT"))
        self.model.setHeaderData(HOURS, Qt.Horizontal,
                QVariant("HOURS"))
        
        self.model.select()

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setSelectionMode(QTableView.SingleSelection)
        self.view.setSelectionBehavior(QTableView.SelectRows)
        self.view.setColumnHidden(ID, True)
        self.view.resizeColumnsToContents()

        self.buttonBox = QDialogButtonBox()
        self.addButton = self.buttonBox.addButton(u"&Добавить",
                QDialogButtonBox.ActionRole)
        self.deleteButton = self.buttonBox.addButton(u"&Удалить",
                QDialogButtonBox.ActionRole)
        self.sortButton = self.buttonBox.addButton(u"&Сортировать",
                QDialogButtonBox.ActionRole)
        

        menu = QMenu(self)
        self.sortByTitleAction = menu.addAction(u"Сортировка по &Title")
        self.sortBySolaryAction = menu.addAction(
                u"Сортировка по &SOLARY")
        self.sortByIDAction = menu.addAction(u"Сортировка по &ID")
        self.sortButton.setMenu(menu)
        self.closeButton = self.buttonBox.addButton(QDialogButtonBox.Close)


    def layout_widgets(self):
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

    def create_connections(self):
        self.addButton.clicked.connect(self.addRecord)
        self.deleteButton.clicked.connect(self.deleteRecord)
        self.closeButton.clicked.connect(self.accept)

    def addRecord(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        index = self.model.index(row, TITLE)
        self.view.setCurrentIndex(index)
        self.view.edit(index)

    def deleteRecord(self):
        index = self.view.currentIndex()
        if not index.isValid():
            return
        record = self.model.record(index.row())
        title = record.value(TITLE).toString()
        desc = record.value(SOLARY).toString()
        if (QMessageBox.question(self, "Reference Data",
                QString("Delete %1 from title %2?")
                .arg(desc).arg(title),
                QMessageBox.Yes|QMessageBox.No) ==
                QMessageBox.No):
            return
        self.model.removeRow(index.row())
        self.model.submitAll()


def main():
    app = QApplication(sys.argv)

    filename = os.path.join(os.path.dirname(__file__), "staff.db")
    create = not QFile.exists(filename)

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(filename)
    if not db.open():
        QMessageBox.warning(None, "Reference Data",
            QString("Database Error: %1").arg(db.lastError().text()))
        sys.exit(1)

    form = StaffDataDlg()
    form.show()

    sys.exit(app.exec_())

main()

```

### Отображение данных в таблице-представлении
Классы QSqlQueryModel, QSqlTableModel и QSqlRelationalTableModel могут использоваться в качестве источников данных для классов представлений Qt, таких как QListView, QTableView и QTreeView. На практике наиболее часто используется QTableView в связи с тем, что результирующая SQL выборка, по существу, представляет собой двумерную структуру данных.

Если модель является моделью для чтения-записи (например, QSqlTableModel), то представление позволяет редактировать поля. 

Можно использовать одну и ту-же модель в качестве источника данных для нескольких представлений. Если пользователь изменяет данные модели с помощью одного из представлений, другие представления немедленно отобразят изменения.
Классы-представления для обозначения колонок наверху отображают заголовки. Для изменения текста заголовка, используется функция setHeaderData() модели. 

Например:
```
        self.model = QSqlTableModel(self)
        self.model.setTable("employee")
        self.model.setSort(ID, Qt.AscendingOrder)
        self.model.setHeaderData(ID, Qt.Horizontal, QVariant("ID"))
        self.model.setHeaderData(CITY, Qt.Horizontal,
                QVariant("City"))
        self.model.setHeaderData(DEPARTMENT, Qt.Horizontal,
                QVariant("Department"))
        self.model.setHeaderData(FIRSTNAME, Qt.Horizontal,
                QVariant("First Name"))
        self.model.setHeaderData(LASTNAME, Qt.Horizontal,
                QVariant("Last Name"))
        self.model.setHeaderData(SEX, Qt.Horizontal,
                QVariant("sex"))
        self.model.setHeaderData(ADDRESS, Qt.Horizontal,
                QVariant("Address"))
        self.model.setHeaderData(PID, Qt.Horizontal,
                QVariant("PID"))
        
        self.model.setHeaderData(TITLE, Qt.Horizontal,
                QVariant("Title"))
        
        self.model.setHeaderData(SOLARY, Qt.Horizontal,
                QVariant("SOLARY"))
        self.model.setHeaderData(SHIFT, Qt.Horizontal,
                QVariant("SHIFT"))
        self.model.setHeaderData(HOURS, Qt.Horizontal,
                QVariant("HOURS"))
        
        self.model.select()

```

## staff3 sort

main.py
```
# -*- coding:utf-8 -*-
import os
import sys
from PyQt4.QtCore import (QFile, QString, QVariant, Qt)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtGui import (QApplication, QDialog, QDialogButtonBox, QMenu,
        QMessageBox, QTableView, QVBoxLayout)
from PyQt4.QtSql import (QSqlDatabase, QSqlQuery, QSqlTableModel)

ID, CITY, DEPARTMENT, FIRSTNAME, LASTNAME, SEX, ADDRESS, PID, TITLE, SOLARY, SHIFT, HOURS = range(12)

   

class StaffDataDlg(QDialog):

    def __init__(self, parent=None):
        super(StaffDataDlg, self).__init__(parent)
        self.create_widgets()
        self.layout_widgets()
        self.create_connections()
        self.setMinimumWidth(850)
        self.setWindowTitle(u'Список сотрудников компании')

    def create_widgets(self):
        self.model = QSqlTableModel(self)
        self.model.setTable("employee")
        self.model.setSort(ID, Qt.AscendingOrder)
        self.model.setHeaderData(ID, Qt.Horizontal, QVariant("ID"))
        self.model.setHeaderData(CITY, Qt.Horizontal,
                QVariant("City"))
        self.model.setHeaderData(DEPARTMENT, Qt.Horizontal,
                QVariant("Department"))
        self.model.setHeaderData(FIRSTNAME, Qt.Horizontal,
                QVariant("First Name"))
        self.model.setHeaderData(LASTNAME, Qt.Horizontal,
                QVariant("Last Name"))
        self.model.setHeaderData(SEX, Qt.Horizontal,
                QVariant("sex"))
        self.model.setHeaderData(ADDRESS, Qt.Horizontal,
                QVariant("Address"))
        self.model.setHeaderData(PID, Qt.Horizontal,
                QVariant("PID"))
        
        self.model.setHeaderData(TITLE, Qt.Horizontal,
                QVariant("Title"))
        
        self.model.setHeaderData(SOLARY, Qt.Horizontal,
                QVariant("SOLARY"))
        self.model.setHeaderData(SHIFT, Qt.Horizontal,
                QVariant("SHIFT"))
        self.model.setHeaderData(HOURS, Qt.Horizontal,
                QVariant("HOURS"))
        
        self.model.select()
    

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setSelectionMode(QTableView.SingleSelection)
        self.view.setSelectionBehavior(QTableView.SelectRows)
        self.view.setColumnHidden(ID, True)
        self.view.resizeColumnsToContents()

        self.buttonBox = QDialogButtonBox()
        self.addButton = self.buttonBox.addButton(u"&Добавить",
                QDialogButtonBox.ActionRole)
        self.deleteButton = self.buttonBox.addButton(u"&Удалить",
                QDialogButtonBox.ActionRole)
        self.sortButton = self.buttonBox.addButton(u"&Сортировать",
                QDialogButtonBox.ActionRole)
        

        menu = QMenu(self)
        self.sortByTitleAction = menu.addAction(u"Сортировка по &Title")
        self.sortBySolaryAction = menu.addAction(
                u"Сортировка по &SOLARY")
        self.sortByIDAction = menu.addAction(u"Сортировка по &ID")
        self.sortButton.setMenu(menu)
        self.closeButton = self.buttonBox.addButton(QDialogButtonBox.Close)


    def layout_widgets(self):
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

    def create_connections(self):
        self.addButton.clicked.connect(self.addRecord)
        self.deleteButton.clicked.connect(self.deleteRecord)
        self.sortByTitleAction.triggered.connect(
                lambda: self.sort(TITLE))
        self.sortBySolaryAction.triggered.connect(
                lambda: self.sort(SOLARY))
        self.sortByIDAction.triggered.connect(lambda: self.sort(ID))
        self.closeButton.clicked.connect(self.accept)

    def addRecord(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        index = self.model.index(row, TITLE)
        self.view.setCurrentIndex(index)
        self.view.edit(index)


    def deleteRecord(self):
        index = self.view.currentIndex()
        if not index.isValid():
            return
        record = self.model.record(index.row())
        title = record.value(TITLE).toString()
        desc = record.value(SOLARY).toString()
        if (QMessageBox.question(self, "Reference Data",
                QString("Delete %1 from title %2?")
                .arg(desc).arg(title),
                QMessageBox.Yes|QMessageBox.No) ==
                QMessageBox.No):
            return
        self.model.removeRow(index.row())
        self.model.submitAll()


    def sort(self, column):
        self.model.setSort(column, Qt.AscendingOrder)
        self.model.select()

def main():
    app = QApplication(sys.argv)

    filename = os.path.join(os.path.dirname(__file__), "staff.db")
    create = not QFile.exists(filename)

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(filename)
    if not db.open():
        QMessageBox.warning(None, "Reference Data",
            QString("Database Error: %1").arg(db.lastError().text()))
        sys.exit(1)

    form = StaffDataDlg()
    form.show()

    sys.exit(app.exec_())


main()

```
## staff4

```
# -*- coding:utf-8 -*-
import os
import sys
from PyQt4.QtCore import (QFile, QString, QVariant, Qt)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtGui import (QApplication, QDialog, QDialogButtonBox, QMenu,
        QMessageBox, QTableView, QVBoxLayout)
from PyQt4.QtSql import (QSqlDatabase, QSqlQuery, QSqlTableModel)

ID, CITY, DEPARTMENT, FIRSTNAME, LASTNAME, SEX, ADDRESS, PID, TITLE, SOLARY, SHIFT, HOURS = range(12)

   

class StaffDataDlg(QDialog):

    def __init__(self, parent=None):
        super(StaffDataDlg, self).__init__(parent)
        self.create_widgets()
        self.layout_widgets()
        self.create_connections()
        self.setMinimumWidth(850)
        self.setWindowTitle(u'Список сотрудников компании')

    def create_widgets(self):
        self.model = QSqlTableModel(self)
        self.model.setTable("employee")
        self.model.setSort(ID, Qt.AscendingOrder)
        self.model.setHeaderData(ID, Qt.Horizontal, QVariant("ID"))
        self.model.setHeaderData(CITY, Qt.Horizontal,
                QVariant("City"))
        self.model.setHeaderData(DEPARTMENT, Qt.Horizontal,
                QVariant("Department"))
        self.model.setHeaderData(FIRSTNAME, Qt.Horizontal,
                QVariant("First Name"))
        self.model.setHeaderData(LASTNAME, Qt.Horizontal,
                QVariant("Last Name"))
        self.model.setHeaderData(SEX, Qt.Horizontal,
                QVariant("sex"))
        self.model.setHeaderData(ADDRESS, Qt.Horizontal,
                QVariant("Address"))
        self.model.setHeaderData(PID, Qt.Horizontal,
                QVariant("PID"))
        
        self.model.setHeaderData(TITLE, Qt.Horizontal,
                QVariant("Title"))
        
        self.model.setHeaderData(SOLARY, Qt.Horizontal,
                QVariant("SOLARY"))
        self.model.setHeaderData(SHIFT, Qt.Horizontal,
                QVariant("SHIFT"))
        self.model.setHeaderData(HOURS, Qt.Horizontal,
                QVariant("HOURS"))
        
        self.model.select()
    

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setSelectionMode(QTableView.SingleSelection)
        self.view.setSelectionBehavior(QTableView.SelectRows)
        self.view.setColumnHidden(ID, True)
        self.view.resizeColumnsToContents()

        self.buttonBox = QDialogButtonBox()
        self.addButton = self.buttonBox.addButton(u"&Добавить",
                QDialogButtonBox.ActionRole)
        self.deleteButton = self.buttonBox.addButton(u"&Удалить",
                QDialogButtonBox.ActionRole)
        self.sortButton = self.buttonBox.addButton(u"&Сортировать",
                QDialogButtonBox.ActionRole)
        

        menu = QMenu(self)
        self.sortByTitleAction = menu.addAction(u"Сортировка по &Title")
        self.sortBySolaryAction = menu.addAction(
                u"Сортировка по &SOLARY")
        self.sortByIDAction = menu.addAction(u"Сортировка по &ID")
        self.sortButton.setMenu(menu)
        self.closeButton = self.buttonBox.addButton(QDialogButtonBox.Close)


    def layout_widgets(self):
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

    def create_connections(self):
        self.addButton.clicked.connect(self.addRecord)
        self.deleteButton.clicked.connect(self.deleteRecord)
        self.sortByTitleAction.triggered.connect(
                lambda: self.sort(TITLE))
        self.sortBySolaryAction.triggered.connect(
                lambda: self.sort(SOLARY))
        self.sortByIDAction.triggered.connect(lambda: self.sort(ID))
        self.closeButton.clicked.connect(self.accept)

    def addRecord(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        index = self.model.index(row, TITLE)
        self.view.setCurrentIndex(index)
        self.view.edit(index)


    def deleteRecord(self):
        index = self.view.currentIndex()
        if not index.isValid():
            return
        record = self.model.record(index.row())
        title = record.value(TITLE).toString()
        desc = record.value(SOLARY).toString()
        if (QMessageBox.question(self, "Reference Data",
                QString("Delete %1 from title %2?")
                .arg(desc).arg(title),
                QMessageBox.Yes|QMessageBox.No) ==
                QMessageBox.No):
            return
        self.model.removeRow(index.row())
        self.model.submitAll()


    def sort(self, column):
        self.model.setSort(column, Qt.AscendingOrder)
        self.model.select()

def main():
    app = QApplication(sys.argv)

    filename = os.path.join(os.path.dirname(__file__), "staff.db")
    create = not QFile.exists(filename)

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(filename)
    if not db.open():
        QMessageBox.warning(None, "Reference Data",
            QString("Database Error: %1").arg(db.lastError().text()))
        sys.exit(1)

    form = StaffDataDlg()
    form.show()

    sys.exit(app.exec_())


main()


```

## staff5
#### id   INTEGER  primary key AUTOINCREMENT UNIQUE NOT NULL ,
```
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
```

### QSqlRelationalTableModel
QSqlRelationalTableModel используется для работы с таблицами которые имеют поле foreign key. Для работы с foreign key достаточно использовать метод setRelation с параметрами состоящими из номера поля, таблицы от куда подставляют значения, поле идентификатора и поле  значений идентификатора. Также при использовании QSqlRelationalTableModel есть возможность использовать QComboBox в связанных полях в QTableView. Для этого нужно использовать метод setItemDelegate класса QTableView.

### main2.py
```
# -*- coding:utf-8 -*-
import os
import sys
from PyQt4.QtCore import (QFile, QString, QVariant, Qt)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtGui import (QApplication, QDialog, QDialogButtonBox, QMenu,
        QMessageBox, QTableView, QVBoxLayout)
from PyQt4.QtSql import (QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlRelation)
from PyQt4 import QtSql

ID, CITY, DEPARTMENT, FIRSTNAME, LASTNAME, SEX, ADDRESS, PID, TITLE, SOLARY, SHIFT, HOURS = range(12)

   
class StaffDataDlg(QDialog):

    def __init__(self, parent=None):
        super(StaffDataDlg, self).__init__(parent)
        self.create_widgets()
        self.layout_widgets()
        self.create_connections()
        self.setMinimumWidth(850)
        self.setWindowTitle(u'Список сотрудников компании')

    def create_widgets(self):
        # self.model = QSqlTableModel(self)
        self.model = QtSql.QSqlRelationalTableModel(self)
        self.model.setTable("employee")
        #self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.setRelation(CITY, QtSql.QSqlRelation('cities', 'city_id', 'name'))
        self.model.setRelation(DEPARTMENT, QtSql.QSqlRelation('deps', 'dep_id', 'name'))

        self.model.setSort(ID, Qt.AscendingOrder)
        self.model.setHeaderData(ID, Qt.Horizontal, QVariant("ID"))
        self.model.setHeaderData(CITY, Qt.Horizontal,
                QVariant("City"))
        self.model.setHeaderData(DEPARTMENT, Qt.Horizontal,
                QVariant("Department"))
        self.model.setHeaderData(FIRSTNAME, Qt.Horizontal,
                QVariant("First Name"))
        self.model.setHeaderData(LASTNAME, Qt.Horizontal,
                QVariant("Last Name"))
        self.model.setHeaderData(SEX, Qt.Horizontal,
                QVariant("sex"))
        self.model.setHeaderData(ADDRESS, Qt.Horizontal,
                QVariant("Address"))
        self.model.setHeaderData(PID, Qt.Horizontal,
                QVariant("PID"))
        
        self.model.setHeaderData(TITLE, Qt.Horizontal,
                QVariant("Title"))
        
        self.model.setHeaderData(SOLARY, Qt.Horizontal,
                QVariant("SOLARY"))
        self.model.setHeaderData(SHIFT, Qt.Horizontal,
                QVariant("SHIFT"))
        self.model.setHeaderData(HOURS, Qt.Horizontal,
                QVariant("HOURS"))
        
        self.model.select()
    

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setSelectionMode(QTableView.SingleSelection)
        self.view.setSelectionBehavior(QTableView.SelectRows)
        self.view.setColumnHidden(ID, True)
        self.view.resizeColumnsToContents()

        self.buttonBox = QDialogButtonBox()
        self.addButton = self.buttonBox.addButton(u"&Добавить",
                QDialogButtonBox.ActionRole)
        self.deleteButton = self.buttonBox.addButton(u"&Удалить",
                QDialogButtonBox.ActionRole)
        self.sortButton = self.buttonBox.addButton(u"&Сортировать",
                QDialogButtonBox.ActionRole)
        

        menu = QMenu(self)
        self.sortByTitleAction = menu.addAction(u"Сортировка по &Title")
        self.sortBySolaryAction = menu.addAction(
                u"Сортировка по &SOLARY")
        self.sortByIDAction = menu.addAction(u"Сортировка по &ID")
        self.sortButton.setMenu(menu)
        self.closeButton = self.buttonBox.addButton(QDialogButtonBox.Close)


    def layout_widgets(self):
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

    def create_connections(self):
        self.addButton.clicked.connect(self.addRecord)
        self.deleteButton.clicked.connect(self.deleteRecord)
        self.sortByTitleAction.triggered.connect(
                lambda: self.sort(TITLE))
        self.sortBySolaryAction.triggered.connect(
                lambda: self.sort(SOLARY))
        self.sortByIDAction.triggered.connect(lambda: self.sort(ID))
        self.closeButton.clicked.connect(self.accept)

    def addRecord(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        index = self.model.index(row, TITLE)
        self.view.setCurrentIndex(index)
        self.view.edit(index)

    def deleteRecord(self):
        index = self.view.currentIndex()
        if not index.isValid():
            return
        record = self.model.record(index.row())
        title = record.value(TITLE).toString()
        desc = record.value(SOLARY).toString()
        if (QMessageBox.question(self, "Reference Data",
                QString("Delete %1 from title %2?")
                .arg(desc).arg(title),
                QMessageBox.Yes|QMessageBox.No) ==
                QMessageBox.No):
            return
        self.model.removeRow(index.row())
        self.model.submitAll()


    def sort(self, column):
        self.model.setSort(column, Qt.AscendingOrder)
        self.model.select()

def main():
    app = QApplication(sys.argv)

    filename = os.path.join(os.path.dirname(__file__), "staff.db")
    create = not QFile.exists(filename)

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(filename)
    if not db.open():
        QMessageBox.warning(None, "Reference Data",
            QString("Database Error: %1").arg(db.lastError().text()))
        sys.exit(1)

    form = StaffDataDlg()
    form.show()

    sys.exit(app.exec_())


main()

```

#### main3.py
```
# -*- coding:utf-8 -*-
import os
import sys
from PyQt4.QtCore import (QFile, QString, QVariant, Qt)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtGui import (QApplication, QDialog, QDialogButtonBox, QMenu,
        QMessageBox, QTableView, QVBoxLayout)
from PyQt4.QtSql import (QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlRelation)
from PyQt4 import QtSql

ID, CITY, DEPARTMENT, FIRSTNAME, LASTNAME, SEX, ADDRESS, PID, TITLE, SOLARY, SHIFT, HOURS = range(12)
  

class StaffDataDlg(QDialog):

    def __init__(self, parent=None):
        super(StaffDataDlg, self).__init__(parent)
        self.create_widgets()
        self.layout_widgets()
        self.create_connections()
        self.setMinimumWidth(850)
        self.setWindowTitle(u'Список сотрудников компании')

    def create_widgets(self):
        # self.model = QSqlTableModel(self)
        self.model = QtSql.QSqlRelationalTableModel(self)
        self.model.setTable("employee")
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.setRelation(CITY, QtSql.QSqlRelation('cities', 'city_id', 'name'))
        self.model.setRelation(DEPARTMENT, QtSql.QSqlRelation('deps', 'dep_id', 'name'))

        self.model.setSort(ID, Qt.AscendingOrder)
        self.model.setHeaderData(ID, Qt.Horizontal, QVariant("ID"))
        
        self.model.setHeaderData(CITY, Qt.Horizontal,
                QVariant("City"))
        self.model.setHeaderData(DEPARTMENT, Qt.Horizontal,
                QVariant("Department"))
        self.model.setHeaderData(FIRSTNAME, Qt.Horizontal,
                QVariant("First Name"))
        self.model.setHeaderData(LASTNAME, Qt.Horizontal,
                QVariant("Last Name"))
        self.model.setHeaderData(SEX, Qt.Horizontal,
                QVariant("sex"))
        self.model.setHeaderData(ADDRESS, Qt.Horizontal,
                QVariant("Address"))
        self.model.setHeaderData(PID, Qt.Horizontal,
                QVariant("PID"))
        
        self.model.setHeaderData(TITLE, Qt.Horizontal,
                QVariant("Title"))
        
        self.model.setHeaderData(SOLARY, Qt.Horizontal,
                QVariant("SOLARY"))
        self.model.setHeaderData(SHIFT, Qt.Horizontal,
                QVariant("SHIFT"))
        self.model.setHeaderData(HOURS, Qt.Horizontal,
                QVariant("HOURS"))
        
        self.model.select()
    

        self.view = QTableView()
        self.view.setModel(self.model)
        # self.view.setSelectionMode(QTableView.SingleSelection)
        self.view.setItemDelegate(QtSql.QSqlRelationalDelegate(self))
        # self.view.setSelectionBehavior(QTableView.SelectRows)
        self.view.setColumnHidden(ID, True)
        self.view.resizeColumnsToContents()

        self.buttonBox = QDialogButtonBox()
        self.addButton = self.buttonBox.addButton(u"&Добавить",
                QDialogButtonBox.ActionRole)
        self.deleteButton = self.buttonBox.addButton(u"&Удалить",
                QDialogButtonBox.ActionRole)
        self.sortButton = self.buttonBox.addButton(u"&Сортировать",
                QDialogButtonBox.ActionRole)
        

        menu = QMenu(self)
        self.sortByTitleAction = menu.addAction(u"Сортировка по &Title")
        self.sortBySolaryAction = menu.addAction(
                u"Сортировка по &SOLARY")
        self.sortByIDAction = menu.addAction(u"Сортировка по &ID")
        self.sortButton.setMenu(menu)
        self.closeButton = self.buttonBox.addButton(QDialogButtonBox.Close)


    def layout_widgets(self):
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

    def create_connections(self):
        self.addButton.clicked.connect(self.addRecord)
        self.deleteButton.clicked.connect(self.deleteRecord)
        self.sortByTitleAction.triggered.connect(
                lambda: self.sort(TITLE))
        self.sortBySolaryAction.triggered.connect(
                lambda: self.sort(SOLARY))
        self.sortByIDAction.triggered.connect(lambda: self.sort(ID))
        self.closeButton.clicked.connect(self.accept)

    def addRecord(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        index = self.model.index(row, TITLE)
        self.view.setCurrentIndex(index)
        self.view.edit(index)


    def deleteRecord(self):
        index = self.view.currentIndex()
        if not index.isValid():
            return
        record = self.model.record(index.row())
        title = record.value(TITLE).toString()
        desc = record.value(SOLARY).toString()
        if (QMessageBox.question(self, "Reference Data",
                QString("Delete %1 from title %2?")
                .arg(desc).arg(title),
                QMessageBox.Yes|QMessageBox.No) ==
                QMessageBox.No):
            return
        self.model.removeRow(index.row())
        self.model.submitAll()


    def sort(self, column):
        self.model.setSort(column, Qt.AscendingOrder)
        self.model.select()

def main():
    app = QApplication(sys.argv)

    filename = os.path.join(os.path.dirname(__file__), "staff.db")
    create = not QFile.exists(filename)

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(filename)
    if not db.open():
        QMessageBox.warning(None, "Reference Data",
            QString("Database Error: %1").arg(db.lastError().text()))
        sys.exit(1)

    form = StaffDataDlg()
    form.show()

    sys.exit(app.exec_())


main()

```

### main4.py
Класс QTableView предоставляет реализацию модель / представление (по умолчанию представления) таблицы.
```
# -*- coding:utf-8 -*-
import os
import sys
from PyQt4.QtCore import (QFile, QString, QVariant, Qt)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtGui import (QApplication, QDialog, QDialogButtonBox, QMenu,
        QMessageBox, QTableView, QVBoxLayout,QPushButton,QHBoxLayout)
from PyQt4.QtSql import (QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlRelation)
from PyQt4 import QtSql

ID, CITY, DEPARTMENT, FIRSTNAME, LASTNAME, SEX, ADDRESS, PID, TITLE, SOLARY, SHIFT, HOURS = range(12)

ID = 0

NAME = 1

POSTCODE = LOCATION = 2

DESCRIPTION = 3

class ReferenceDataDlg(QDialog):

    def __init__(self, table, title, parent=None):
        super(ReferenceDataDlg, self).__init__(parent)
        self.create_widgets(table)
        self.layout_widgets()
        self.create_connections()
        self.setWindowTitle(
                "Asset Manager - Edit {0} Reference Data".format(title))


    def create_widgets(self, table):
        self.model = QSqlTableModel(self)
        self.model.setTable(table)
        self.model.setSort(NAME, Qt.AscendingOrder)
        self.model.setHeaderData(ID, Qt.Horizontal, QVariant("ID"))
        self.model.setHeaderData(NAME, Qt.Horizontal, QVariant("Name"))
        self.model.setHeaderData(DESCRIPTION, Qt.Horizontal,
                                 QVariant("Description"))
        self.model.select()

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setSelectionMode(QTableView.SingleSelection)
        self.view.setSelectionBehavior(QTableView.SelectRows)
        self.view.setColumnHidden(ID, True)
        self.view.resizeColumnsToContents()

        self.addButton = QPushButton("&Add")
        self.deleteButton = QPushButton("&Delete")
        self.okButton = QPushButton("&OK")


    def layout_widgets(self):
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.addButton)
        buttonLayout.addWidget(self.deleteButton)
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.okButton)
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)


    def create_connections(self):
        self.addButton.clicked.connect(self.addRecord)
        self.deleteButton.clicked.connect(self.deleteRecord)
        self.okButton.clicked.connect(self.accept)


    def addRecord(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        index = self.model.index(row, NAME)
        self.view.setCurrentIndex(index)
        self.view.edit(index)


    def deleteRecord(self):
        index = self.view.currentIndex()
        if not index.isValid():
            return
        
        record = self.model.record(index.row())
        id = record.value(ID).toInt()[0]
        table = self.model.tableName()
        query = QSqlQuery()
        if table == "deps":
            query.exec_(QString("SELECT COUNT(*) FROM employee "
                                "WHERE deo_id = %1").arg(id))
        elif table == "cities":
            query.exec_(QString("SELECT COUNT(*) FROM employee "
                                "WHERE city_id = %1").arg(id))
        count = 0
        if query.next():
            count = query.value(0).toInt()[0]
        if count:
            QMessageBox.information(self,
                    QString("Delete %1").arg(table),
                    (QString("Cannot delete %1<br>"
                             "from the %2 table because it is used by "
                             "%3 records")
                    .arg(record.value(NAME).toString())
                    .arg(table).arg(count)))
            
            return
        self.model.removeRow(index.row())
        self.model.submitAll()
        


class StaffDataDlg(QDialog):

    def __init__(self, parent=None):
        super(StaffDataDlg, self).__init__(parent)
        self.create_widgets()
        self.layout_widgets()
        self.create_connections()
        self.setMinimumWidth(850)
        self.setWindowTitle(u'Список сотрудников компании')

    def create_widgets(self):
        
        self.model = QtSql.QSqlRelationalTableModel(self)
        self.model.setTable("employee")
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.setRelation(CITY, QtSql.QSqlRelation('cities', 'city_id', 'name'))
        self.model.setRelation(DEPARTMENT, QtSql.QSqlRelation('deps', 'dep_id', 'name'))

        self.model.setSort(ID, Qt.AscendingOrder)
        self.model.setHeaderData(ID, Qt.Horizontal, QVariant("ID"))
        
        self.model.setHeaderData(CITY, Qt.Horizontal,
                QVariant("City"))
        self.model.setHeaderData(DEPARTMENT, Qt.Horizontal,
                QVariant("Department"))
        self.model.setHeaderData(FIRSTNAME, Qt.Horizontal,
                QVariant("First Name"))
        self.model.setHeaderData(LASTNAME, Qt.Horizontal,
                QVariant("Last Name"))
        self.model.setHeaderData(SEX, Qt.Horizontal,
                QVariant("sex"))
        self.model.setHeaderData(ADDRESS, Qt.Horizontal,
                QVariant("Address"))
        self.model.setHeaderData(PID, Qt.Horizontal,
                QVariant("PID"))
        
        self.model.setHeaderData(TITLE, Qt.Horizontal,
                QVariant("Title"))
        
        self.model.setHeaderData(SOLARY, Qt.Horizontal,
                QVariant("SOLARY"))
        self.model.setHeaderData(SHIFT, Qt.Horizontal,
                QVariant("SHIFT"))
        self.model.setHeaderData(HOURS, Qt.Horizontal,
                QVariant("HOURS"))
        
        self.model.select()
    

        self.view = QTableView()
        self.view.setModel(self.model)
        
        self.view.setItemDelegate(QtSql.QSqlRelationalDelegate(self))
        
        self.view.setColumnHidden(ID, True)
        self.view.resizeColumnsToContents()

        self.buttonBox = QDialogButtonBox()
        self.addCity = self.buttonBox.addButton(u"&Добавить City",
                QDialogButtonBox.ActionRole)
        self.addDep = self.buttonBox.addButton(u"&Добавить Department",
                QDialogButtonBox.ActionRole)
        self.addButton = self.buttonBox.addButton(u"&Добавить",
                QDialogButtonBox.ActionRole)
        self.deleteButton = self.buttonBox.addButton(u"&Удалить",
                QDialogButtonBox.ActionRole)
        self.sortButton = self.buttonBox.addButton(u"&Сортировать",
                QDialogButtonBox.ActionRole)
        

        menu = QMenu(self)
        self.sortByTitleAction = menu.addAction(u"Сортировка по &Title")
        self.sortBySolaryAction = menu.addAction(
                u"Сортировка по &SOLARY")
        self.sortByIDAction = menu.addAction(u"Сортировка по &ID")
        self.sortButton.setMenu(menu)
        self.closeButton = self.buttonBox.addButton(QDialogButtonBox.Close)


    def layout_widgets(self):
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

    def create_connections(self):
        self.addButton.clicked.connect(self.addRecord)
        self.deleteButton.clicked.connect(self.deleteRecord)
        self.addCity.clicked.connect(self.editCities)
        
        self.sortByTitleAction.triggered.connect(
                lambda: self.sort(TITLE))
        self.sortBySolaryAction.triggered.connect(
                lambda: self.sort(SOLARY))
        self.sortByIDAction.triggered.connect(lambda: self.sort(ID))
        self.closeButton.clicked.connect(self.accept)

    def addRecord(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        index = self.model.index(row, TITLE)
        self.view.setCurrentIndex(index)
        self.view.edit(index)


    def deleteRecord(self):
        index = self.view.currentIndex()
        if not index.isValid():
            return
        record = self.model.record(index.row())
        title = record.value(TITLE).toString()
        desc = record.value(SOLARY).toString()
        if (QMessageBox.question(self, "Reference Data",
                QString("Delete %1 from title %2?")
                .arg(desc).arg(title),
                QMessageBox.Yes|QMessageBox.No) ==
                QMessageBox.No):
            return
        self.model.removeRow(index.row())
        self.model.submitAll()


    def sort(self, column):
        self.model.setSort(column, Qt.AscendingOrder)
        self.model.select()

    def editCities(self):
        form = ReferenceDataDlg("cities", "Cities", self)
        form.exec_()


def main():
    app = QApplication(sys.argv)

    filename = os.path.join(os.path.dirname(__file__), "staff.db")
    create = not QFile.exists(filename)

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(filename)
    if not db.open():
        QMessageBox.warning(None, "Reference Data",
            QString("Database Error: %1").arg(db.lastError().text()))
        sys.exit(1)

    form = StaffDataDlg()
    form.show()

    sys.exit(app.exec_())


main()

```
