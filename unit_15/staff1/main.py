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

#sys.exit(app.exec_())

app.exec_()