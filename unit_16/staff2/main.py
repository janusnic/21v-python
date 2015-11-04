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
