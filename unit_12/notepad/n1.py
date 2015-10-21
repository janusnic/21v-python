#! /usr/bin/python

import sys
import os
from PyQt4 import QtGui

class Notepad(QtGui.QMainWindow):
    def __init__(self):
        super(Notepad, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Notepad')
        self.show() 

def main():
    app = QtGui.QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
