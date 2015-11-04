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