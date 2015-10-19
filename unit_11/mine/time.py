#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
import sys
class myLCDNumber(QLCDNumber):
  value = 60
    
  @pyqtSlot()
  def count(self):
    self.display(self.value)
    self.value = self.value-1


def main():    
    app      = QApplication(sys.argv)
    lcdNumber    = myLCDNumber()

    #Resize width and height
    lcdNumber.resize(250,250)    
    lcdNumber.setWindowTitle('PyQt QTimer Countdown Example')  
    lcdNumber.display(60)
    timer = QTimer()
    lcdNumber.connect(timer,SIGNAL("timeout()"),lcdNumber,SLOT("count()"))
    timer.start(1000) 

    lcdNumber.show()    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()