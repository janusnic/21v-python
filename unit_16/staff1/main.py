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
