from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
import sys

class myMainWindow(QtGui.QMainWindow):
  @pyqtSlot(int)
  def onIndexChange(self, i):
    print i  

def main():
    
    app       = QtGui.QApplication(sys.argv)
    window    = myMainWindow()
    palette       = QtGui.QPalette()
    comboBox = QtGui.QComboBox()
    comboBox.addItem("Item 1")
    comboBox.addItem("Item 2")
    comboBox.addItem("Item 3")

    window.setCentralWidget(comboBox)
    
    comboBox.connect(comboBox,SIGNAL("currentIndexChanged(int)"),
                    window,SLOT("onIndexChange(int)"))
   
    window.setWindowTitle('PyQt QComboBox CurrentIndexChange Example')
    window.show()
    
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()