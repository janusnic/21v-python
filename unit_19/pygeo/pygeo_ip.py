# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pygeo_ip.ui'
#
# Created: Sat Nov 14 12:20:14 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pygeoip, sys, socket

def msg_box(title, message):
    w = QtGui.QWidget()
    QtGui.QMessageBox.information(w, title, message)

def update_search_list(self, data):
    self.search_list.addItem(data)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PyGeoIP_Window(object):
    def setupUi(self, PyGeoIP_Window):
        PyGeoIP_Window.setObjectName(_fromUtf8("PyGeoIP_Window"))
        PyGeoIP_Window.resize(640, 480)
        self.centralwidget = QtGui.QWidget(PyGeoIP_Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 10, 591, 71))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.ip_label = QtGui.QLabel(self.frame)
        self.ip_label.setGeometry(QtCore.QRect(10, 20, 131, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(16)
        self.ip_label.setFont(font)
        self.ip_label.setObjectName(_fromUtf8("ip_label"))
        self.ip_textbox = QtGui.QLineEdit(self.frame)
        self.ip_textbox.setGeometry(QtCore.QRect(170, 10, 231, 27))
        self.ip_textbox.setObjectName(_fromUtf8("p_textbox"))
        self.search_btn = QtGui.QPushButton(self.frame)
        self.search_btn.setGeometry(QtCore.QRect(450, 10, 85, 27))
        self.search_btn.setObjectName(_fromUtf8("search_btn"))

        self.search_btn.clicked.connect(self.search)

        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(40, 100, 561, 61))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.info_bar = QtGui.QLabel(self.frame_2)
        self.info_bar.setGeometry(QtCore.QRect(10, 9, 541, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.info_bar.setFont(font)
        self.info_bar.setObjectName(_fromUtf8("info_bar"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(49, 190, 551, 241))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.search_list = QtGui.QListWidget(self.frame_3)
        self.search_list.setGeometry(QtCore.QRect(15, 10, 511, 211))
        self.search_list.setObjectName(_fromUtf8("search_list"))
        PyGeoIP_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PyGeoIP_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        PyGeoIP_Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PyGeoIP_Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PyGeoIP_Window.setStatusBar(self.statusbar)

        self.retranslateUi(PyGeoIP_Window)
        QtCore.QMetaObject.connectSlotsByName(PyGeoIP_Window)

    def retranslateUi(self, PyGeoIP_Window):
        PyGeoIP_Window.setWindowTitle(_translate("PyGeoIP_Window", "MainWindow", None))
        self.ip_label.setText(_translate("PyGeoIP_Window", "IP Address:", None))
        self.search_btn.setText(_translate("PyGeoIP_Window", "PushButton", None))
        self.info_bar.setText(_translate("PyGeoIP_Window", "Tip: Enter An IP Address In The TextBox And Click Search", None))

    def search(self):
        message = ''
        result_count = 0
        gip = pygeoip.GeoIP('GeoLiteCity.dat')
        ip = self.ip_textbox.text()
        try:
            ip = socket.gethostbyname(str(ip))
            message = 'Host: %s Is Currently Available' % (str(ip))
        except socket.error, e:
            message = 'Host: %s Is Currently Unavailable' % (str(ip))
        self.info_bar.setText(message)
        self.search_list.clear()
        try:
            rec = gip.record_by_addr(str(ip))
            for key, val in rec.items():
                update_search_list(self, '[*] %s => %s' % (key,val))
                result_count += 1
            msg_box('Search Complete', '%d Results were Found for %s' % (result_count, str(ip)))
        except Exception, e:
            msg_box('', str(e))
            msg_box('Search Complete', 'No Results were Found For %s' % (str(ip)))
            return





if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PyGeoIP_Window = QtGui.QMainWindow()
    ui = Ui_PyGeoIP_Window()
    ui.setupUi(PyGeoIP_Window)
    PyGeoIP_Window.show()
    sys.exit(app.exec_())

