21v-python
============

[![GeoLiteCity](https://img.shields.io/badge/Django-Requirements-orange.svg)](http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz)
[![Pygeoip](https://img.shields.io/badge/Django-Dependencies-red.svg)](http://pygeoip.googlecode.com/files/pygeoip-0.1.3.zip)
[![setuptools](https://img.shields.io/badge/Django-devDependencies-yellowgreen.svg)](http://svn.python.org/projects/sandbox/trunk/setuptools/ez_setup.py)
[![MIT License](https://img.shields.io/cocoapods/l/AFNetworking.svg)](http://opensource.org/licenses/MIT)


GeoLiteCity Database
=====================

Step 1: Открыть Terminal

Step 2: Download Database
```
> wget -N -q http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
```
Распаковать.
```
> gzip -d GeoLiteCity.dat.gz
```
Проверить
```
> ls -alh GeoLiteCity.dat
```
Step 3: Download & Install Pygeoip
```

> wget http://pygeoip.googlecode.com/files/pygeoip-0.1.3.zip
```

Распаковать
```
> unzip pygeoip-0.1.3.zip

```
download setup tools в pygeoip каталог.
```
> cd /pygeoip-0.1.3

> wget http://svn.python.org/projects/sandbox/trunk/setuptools/ez_setup.py

> wget http://pypi.python.org/packages/2.5/s/setuptools-0.6c11-py2.5.egg
```

build и install setup tools.
```
> mv setuptools-0.6c11-py2.5.egg setuptools-0.7a1-py2.5.egg

> python setup.py build

> python setup.py install
```

Step 4: Запрос к Database

Start Python shell.

```
python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.

>>> import pygeoip

>>> gip = pygeoip.GeoIP('GeoLiteCity.dat')

>>> rec = gip.record_by_addr('64.233.161.99')

>>> for key,val in rec.items():
...     print "%s: %s" %(key,val)
... 
city: Mountain View
region_name: CA
area_code: 650
longitude: -122.0574
country_code3: USA
latitude: 37.4192
postal_code: 94043
dma_code: 807
country_code: US
country_name: United States
>>> 

```

PYTHON GUI - PYQT
=================

*REQUIREMENTS*
-------------------------
- PyQT ( Installed By Default )
- [Qt Designer](http://www.riverbankcomputing.com/software/pyqt/download) If you don't have anything installed you can get PyQt for Windows here. 
- [Pyuic4](http://download.qt.io/archive/qt/4.8/4.8.6/) QtCreator (which contains Qt Designer). 


For linux:
```
apt-get install pyqt4-dev-tools qt4-designer
```

- [PyQt4 Reference Guide](http://pyqt.sourceforge.net/Docs/PyQt4/). 
- [Using Qt Designer](http://pyqt.sourceforge.net/Docs/PyQt4/designer.html). 

#### design.ui
```
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>240</width>
    <height>345</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QListWidget" name="listWidget"/>
    </item>
    <item>
     <widget class="QPushButton" name="btnBrowse">
      <property name="text">
       <string>Pick a folder</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
```

#### design.py
```
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Sat Nov 14 12:20:14 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(240, 345)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.btnBrowse = QtGui.QPushButton(self.centralwidget)
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.verticalLayout.addWidget(self.btnBrowse)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnBrowse.setText(_translate("MainWindow", "Pick a folder", None))


```

#### main.py
```
from PyQt4 import QtGui  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication

import design  # This file holds our MainWindow and all design related things

# it also keeps events etc that we defined in Qt Designer
import os  # For listing directory methods


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        self.btnBrowse.clicked.connect(self.browse_folder)  # When the button is pressed
                                                            # Execute browse_folder function

    def browse_folder(self):
        self.listWidget.clear() # In case there are any existing elements in the list
        directory = QtGui.QFileDialog.getExistingDirectory(self,
                                                           "Pick a folder")
        # execute getExistingDirectory dialog and set the directory variable to be equal
        # to the user selected directory

        if directory: # if user didn't pick a directory don't continue
            for file_name in os.listdir(directory): # for all files, if any, in the directory
                self.listWidget.addItem(file_name)  # add file to the listWidget


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
```
## PyGeoIP User Interface
### Поиск любого Internet Address ( GUI - Linux )

### Step 01: User Interface ( UI ) Of Qt Designer

Запускаем QtDesigner.

Имеем пустую форму.


## Step 02: Designing User Interface

### Frame 1
Добавим

- 1 label с описанием: IP Address:
- 1 PushButton 
- 1 lineEdit 

### Frame 2

Добавим

- 1 label с описанием: Tip: Enter An IP Address In The TextBox And Click Search

### Frame 3

- 1 listWidget

#### A CLOSE VIEW AT THE FINISHED WINDOW
Сохраним Ctrl + S ( Control Save ) как pygeo_ip.ui. 

Тзменим свойства:

Click ip address label, изменим имя label на ip_label
- Click textbox, изменим имя objectName на ip_textbox
- Click button search изменим имя objectName на search_btn
- Click Tip: Enter An IP ... label изменим имя objectName на info_bar
- Click listWidget ( listbox ) изменим имя objectName на search_list
- Click main form - изменим имя objectName на PyGeoIP_Window
### Step 03: Compiling

```
 pyuic4 --help
 pyuic4 -x filename.ui -o filename.py
```
#### PyGeoIP_Window - pygeo_ip.ui
```
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>PyGeoIP_Window</class>
 <widget class="QMainWindow" name="PyGeoIP_Window">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>640</width>
    <height>480</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QFrame" name="frame">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>10</y>
      <width>591</width>
      <height>71</height>
     </rect>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <widget class="QLabel" name="ip_label">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>20</y>
       <width>131</width>
       <height>20</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Noto Sans [unknown]</family>
       <pointsize>16</pointsize>
      </font>
     </property>
     <property name="text">
      <string>IP Address:</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="ip_textbox">
     <property name="geometry">
      <rect>
       <x>170</x>
       <y>10</y>
       <width>231</width>
       <height>27</height>
      </rect>
     </property>
    </widget>
    <widget class="QPushButton" name="search_btn">
     <property name="geometry">
      <rect>
       <x>450</x>
       <y>10</y>
       <width>85</width>
       <height>27</height>
      </rect>
     </property>
     <property name="text">
      <string>PushButton</string>
     </property>
    </widget>
   </widget>
   <widget class="QFrame" name="frame_2">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>100</y>
      <width>561</width>
      <height>61</height>
     </rect>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <widget class="QLabel" name="info_bar">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>9</y>
       <width>541</width>
       <height>51</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Noto Sans [unknown]</family>
       <pointsize>14</pointsize>
      </font>
     </property>
     <property name="text">
      <string>Tip: Enter An IP Address In The TextBox And Click Search</string>
     </property>
    </widget>
   </widget>
   <widget class="QFrame" name="frame_3">
    <property name="geometry">
     <rect>
      <x>49</x>
      <y>190</y>
      <width>551</width>
      <height>241</height>
     </rect>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <widget class="QListWidget" name="search_list">
     <property name="geometry">
      <rect>
       <x>15</x>
       <y>10</y>
       <width>511</width>
       <height>211</height>
      </rect>
     </property>
    </widget>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>640</width>
     <height>27</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>

```
#### pygeo_ip.py
```
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pygeo_ip.ui'
#
# Created: Sat Nov 14 12:20:14 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PyGeoIP_Window = QtGui.QMainWindow()
    ui = Ui_PyGeoIP_Window()
    ui.setupUi(PyGeoIP_Window)
    PyGeoIP_Window.show()
    sys.exit(app.exec_())


```

### Step 04: The Code

Свяжем search button ( search_btn ) с действием - function search.

```
        self.search_btn.setObjectName(_fromUtf8("search_btn"))

        self.search_btn.clicked.connect(self.search)

        self.frame_2 = QtGui.QFrame(self.centralwidget)
        
```

function search().

```
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

```

### Step 05: 2 Functions
msg_box function и update_search_list(self, data)

```
import pygeoip, sys, socket

def msg_box(title, message):
    w = QtGui.QWidget()
    QtGui.QMessageBox.information(w, title, message)

def update_search_list(self, data):
    self.search_list.addItem(data)

```

### Step 06: 

В текущем каталоге должна находиться база PyGeoIP.

#### Step 07: Проверка

Введем: 63.12.14.90

# Chat

## STEP 1: Designing User Interface

- Запусеаем Qt Designer

- Создаем MainWindow

#### Main Form

- Добавим Widgets

1. 3 Frames ( frame )
2. 2 Labels ( label)
3. 2 Textboxes ( lineEdit )
4. 2 Buttons ( Send Message and Clear Logs )
5. A Menu Bar with the text: Menu Actions
- Has A Sub item labelled: Version
- Has A Sub item labelled: Exit

### MENU BAR: 
Menu Actions
Version
Exit.


## FRAME 1: 2 labels, 2 lineEdits ( TextBox ).
Имя label1 - IP Address:
Имя label2 - Nick:


### FRAME 2: 
textEdit ( Rich Text Box ) 
2 PushButtons ( Button )
Подписать кнлпки
Send Message 
Clear Logs.

### FRAME 3:
listWidget

## STEP 2: Compiling

Save project Ctrl + S.

```
#> pyuic4 -x chat.ui -o chat.py
```
## STEP 3: Вставим Code

chat.py

```
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, socket
from thread import *

```

Создаем BackGround Server Process

```
    def start_server(self):
        start_new_thread(server_socket, (self,))
        msg_box("Success", "Server Started Sucessfully")
```


Сразу за инструкцией import

```
def app_version():
    msg_box("Application Version", "P2P Chat v1.0")

def msg_box(title, data):
    w = QWidget()
    QMessageBox.information(w, title, data)

def update_list(self, data):
    self.listWidget.addItem(data)
    print "\a"

def server_socket(self):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 6190))
        s.listen(1)
    except socket.error, e:
        msg_box("Socket Error !!", 
            "Unable To Setup Local Socket. Port In Use")
        return

    while 1:
        conn, addr = s.accept()

        incoming_ip = str(addr[0])
        current_chat_ip = self.lineEdit.text()

        if incoming_ip != current_chat_ip:
            conn.close()
        else:
            data = conn.recv(4096)
            update_list(self, data)
            conn.close()

    s.close()

```

Создаем Client Socket

```
def start_server(self):
        start_new_thread(server_socket, (self,))
        msg_box("Success", "Server Started Sucessfully")
    
    def client_send_message(self):
        ip_address = self.lineEdit.text()

        nick = self.lineEdit_2.text()
        nick = nick.replace("#>","")
        rmessage = self.textEdit.toPlainText()
        rmessage = rmessage.replace("#>","")

        rmsg =  nick + " #> " + rmessage

        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            c.connect((ip_address, 9000))
        except Exception, e:
            msg_box("Connection Refused", "The Address You Are Trying To Reach Is Currently Unavailable")
            return

        try:
            c.send(rmsg)
            self.listWidget.addItem(rmsg)
            self.textEdit.setText("")
        except Exception, e:
            msg_box("Connection Refused", "The Message Cannot Be Sent. End-Point Not Connected !!")

        c.close()
```

Очистка Logs

```
    def clear_logs(self):
        self.listWidget.clear()

```

## STEP 3: Вызов Functions

self.start_server()

```
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.start_server()

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(662, 448)

```
для pushButton_3

```

        #############################################################
        # Executes When The Send Message Button Is Clicked
        self.pushButton_3.clicked.connect(self.client_send_message)
        ############################################################


        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QRect(190, 280, 93, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))


        #############################################################
        # Executes When The Clear Logs Button Is Clicked
        self.pushButton_4.clicked.connect(self.clear_logs)
        ##############################################################
```
для actionExit

```
        #######################################################
        # Executes When The SubMenu Item Version Is Clicked
        self.actionExit.triggered.connect(app_version)
        #######################################################

        self.actionExit_2 = QAction(MainWindow)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))

        #######################################################
        # Executes When The SubMenu Item Exit Is Clicked
        self.actionExit_2.triggered.connect(qApp.quit)
        #######################################################
```
## STEP 4: Проверка

Полты с 9000 по 6190 






