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
        self.setWindowTitle(г'Список сотрудников компании')

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