# 21v-python

## Drawing in PyQt4

### Drawing text

### Класс QPixmap
Класс QPixmap nредназначен для работы с изображениями в контекстно-зависимом nредставлении. Данные хранятся в виде, позволяющем отображать изображение на экране наи­более эффективным способом, поэтому класс часто исnользуется в качестве буфера для ри­сования nеред выводом на экран. 

#### метод QPainter
Так как класс QPixmap наследует класс QPaintDevice, мы можем использовать его как nо­верхность для рисования. Вывести изображение позволяет метод QPainter.

## Вывод текста
Вывести текст позволяет метод drawТext  из класса QPainter. 
```
drawТext(X,У, Текст)
drawТext(QPoint, Текст)
drawТext(QRectF, Флаги, Текст)
```
### Форматы метода:

1. drawТext(X,У, Текст) -  выводят текст, начиная с указанных координат.
1. drawТext(QRectF, Флаги, Текст) - выводят текст в указанную прямоугольную область. Если текст не помещается в прямоугольную область, то он будет обрезан, если не указан флаг тextDontClip.  Методы возвращают экземпляр класса QRect (QRectF) с координатами и размерами прямоугольника, в который вписан текст. В параметре Флаги через оператор l указываются атрибуты AlignLeft, AlignRight, AlignHCenter, AlignTop, AlignBottom, AlignVCenter или AlignCenter из класса QtCore.Qt, задающие выравнивание текста внутри прямоугольной области, а также следующие атрибуты:
- TextDontClip- текст может выйти за пределы указанной прямоугольной области;
- TextSingleLine- все специальные символы трактуются как пробелы и текст выводится в одну строку;
- TextWordWrap - если текст не помещается на одной строке, то будет произведен перенос по границам слова;
- TextWrapAnywhere- перенос строки может быть внутри слова;
- TextShowMnemonic- символ, перед которым указан символ &, будет подчеркнут. Чтобы вывести символ &, его необходимо удвоить;
- TextHideMnemonic- то же самое, что и TextShowМnemonic, но символ не подчеркивается;
- TextExpandTabs- символы табуляции будут обрабатываться.

```
qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)
```

### метод boundingRect()
Получить координаты и размеры прямоугольника, в который вписывается текст, позволяет метод boundingRect().
#### Форматы метода:
boundingRect(X, У, Ширина, Высота, Флаги, Текст)


1.py

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Draw text')
        self.show()

    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()
        
    def drawText(self, event, qp):
      
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)        
                
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```


#### def paintEvent(self, event):

```
qp = QtGui.QPainter()
qp.begin(self)
self.drawText(event, qp)
qp.end()
```

#### QtGui.QPainter class
####  setPen (QPen) - устанавливает перо;
```
qp.setPen(QtGui.QColor(168, 34, 3))
qp.setFont(QtGui.QFont('Decorative', 10))
```


### setBrush(QBrush)
Для установки кисти предназначен метод setBrush(QBrush)

Устанавливать перо или кисть нужно будет перед каждой операцией рисования, требующей изменения цвета или стиля. Если перо или кисть не установлены, то будут использоваться объекты с настройками по умолчанию. После установки пера и кисти можно приступать к рисованию точек, линий, фигур, текста и др.
Для рисования точек, линий и фигур класс QPainter предоставляет следующие методы:

- drawPoint() -рисует точку. 
- drawPoints() - рисует несколько точек. Форматы метода:
- drawLine() -рисует линию.
- drawLines() - рисует несколько отдельных линий.
- drawPo1yline() - рисует несколько линий, которые соединяют указанные точки. Пер­вая и последняя точки не соединяются. 
- drawRect() -рисует прямоугольник с границей и заливкой. Чтобы убрать границу, сле­дует использовать перо со стилем NoPen, а чтобы убрать заливку- кисть со стилем Noвrush. 
- fillRect() -рисует прямоугольник с заливкой без границы.
- drawRoundedRect() - рисует прямоугольник с скругленными краями.
- drawPo1ygon() -рисует многоугольник с границей и заливкой. 
- drawEllipse() -рисует эллипс с границей и заливкой. 
- drawArc() -рисует дугу.
- drawChord() - рисует замкнутую дугу.
- drawPie() - рисует замкнутый сектор.

При выводе некоторых фигур (например, эллиnса) контур может отображаться в виде "ле­сенки". Чтобы сгладить контуры фигур, сл.едует вызвать метод setRenderHint() и передать ему атрибут Antialiasing.
Пример:
```
painter.setRenderHint(QtGui.QPainter.Antialiasing)
```

## Drawing points
### small spot on the window.

2.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys, random
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()
        
    def drawPoints(self, qp):
      
        qp.setPen(QtCore.Qt.red)
        size = self.size()
        
        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)     
                
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```


### Colours


3.py
```

#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Colours')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
        
    def drawRectangles(self, qp):
      
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        qp.setBrush(QtGui.QColor(200, 0, 0))
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(QtGui.QColor(255, 80, 0, 160))
        qp.drawRect(130, 15, 90, 60)

        qp.setBrush(QtGui.QColor(25, 0, 90, 200))
        qp.drawRect(250, 15, 90, 60)
              
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```


### QtGui.QPen

4.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Pen styles')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()
        
    def drawLines(self, qp):
      
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        pen.setStyle(QtCore.Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(QtCore.Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(QtCore.Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(QtCore.Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        pen.setStyle(QtCore.Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)
              
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```


### QtGui.QBrush

5.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.setGeometry(300, 300, 355, 280)
        self.setWindowTitle('Brushes')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()
        
    def drawBrushes(self, qp):
      
        brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 15, 90, 60)

        brush.setStyle(QtCore.Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)

        brush.setStyle(QtCore.Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 15, 90, 60)

        brush.setStyle(QtCore.Qt.Dense3Pattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush.setStyle(QtCore.Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush.setStyle(QtCore.Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)

        brush.setStyle(QtCore.Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)

        brush.setStyle(QtCore.Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)

        brush.setStyle(QtCore.Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 195, 90, 60)

        brush.setStyle(QtCore.Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(250, 195, 90, 60)
              
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```


### drawEllipse

6.py
```
from PyQt4.QtCore import *
from PyQt4.QtGui import *
class DrawCircles(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('Draw circles')
    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        # optional
        paint.setRenderHint(QPainter.Antialiasing)
        # make a white drawing background
        paint.setBrush(Qt.white)
        paint.drawRect(event.rect())
        # for circle make the ellipse radii match
        radx = 100
        rady = 100
        # draw red circles
        paint.setPen(Qt.red)
        for k in range(125, 220, 10):
            center = QPoint(k, k)
            # optionally fill each circle yellow
            paint.setBrush(Qt.yellow)
            paint.drawEllipse(center, radx, rady)
        paint.end()
app = QApplication([])
circles = DrawCircles()
circles.show()
app.exec_()
```

## My paint Brush

1.py
```
#!/usr/bin/env python

import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

from PyQt4 import QtCore, QtGui

class ScribbleArea(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(ScribbleArea, self).__init__(parent)

        self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 1
        self.myPenColor = QtCore.Qt.blue
        imageSize = QtCore.QSize(500, 500)
        self.image = QtGui.QImage(imageSize, QtGui.QImage.Format_RGB32)
        self.lastPoint = QtCore.QPoint()

    def openImage(self, fileName):
        loadedImage = QtGui.QImage()
        if not loadedImage.load(fileName):
            return False

        w = loadedImage.width()
        h = loadedImage.height()    
        self.mainWindow.resize(w, h)

        self.image = loadedImage
        self.modified = False
        self.update()
        return True

    def saveImage(self, fileName, fileFormat):
        pass

    def clearImage(self):
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.modified = True
        self.update()

    def print_(self):
        pass

    def isModified(self):
        return self.modified

    def penColor(self):
        return self.myPenColor

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.saveAsActs = []

        self.scribbleArea = ScribbleArea(self)
        self.scribbleArea.clearImage()
        self.scribbleArea.mainWindow = self  # maybe not using this?
        self.setCentralWidget(self.scribbleArea)

        self.createActions()
        self.createMenus()

        self.setWindowTitle("My Paint Brush")
        self.resize(500, 500)

    def open(self):
        pass

    def save(self):
        action = self.sender()
        fileFormat = action.data()
        self.saveFile(fileFormat)

    def penColor(self):
        newColor = QtGui.QColorDialog.getColor(self.scribbleArea.penColor())
        if newColor.isValid():
            self.scribbleArea.setPenColor(newColor)


    def createActions(self):
        self.openAct = QtGui.QAction("&Open...", self, shortcut="Ctrl+O",
            triggered=self.open)

        for format in QtGui.QImageWriter.supportedImageFormats():
            format = str(format)
            text = format.upper() + "..."
            action = QtGui.QAction(text, self, triggered=self.save)
            action.setData(format)
            self.saveAsActs.append(action)

        self.printAct = QtGui.QAction("&Print...", self,
            triggered=self.scribbleArea.print_)

        self.exitAct = QtGui.QAction("E&xit", self, shortcut="Ctrl+Q",
            triggered=self.close)

        self.penColorAct = QtGui.QAction("&Pen Color...", self,
            triggered=self.penColor)

        self.aboutQtAct = QtGui.QAction("About &Qt", self,
            triggered=QtGui.qApp.aboutQt)

    def createMenus(self):
        self.saveAsMenu = QtGui.QMenu("&Save As", self)
        for action in self.saveAsActs:
            self.saveAsMenu.addAction(action)

        fileMenu = QtGui.QMenu("&File", self)
        fileMenu.addAction(self.openAct)
        fileMenu.addMenu(self.saveAsMenu)
        fileMenu.addAction(self.printAct)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAct)

        optionMenu = QtGui.QMenu("&Options", self)
        optionMenu.addAction(self.penColorAct)
        optionMenu.addSeparator()
        helpMenu = QtGui.QMenu("&Help", self)
        helpMenu.addAction(self.aboutQtAct)

        self.menuBar().addMenu(fileMenu)
        self.menuBar().addMenu(optionMenu)
        self.menuBar().addMenu(helpMenu)


    def saveFile(self, fileFormat):
        pass

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

2.py

```
#!/usr/bin/env python

import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

from PyQt4 import QtCore, QtGui


class ScribbleArea(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(ScribbleArea, self).__init__(parent)

        self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 1
        self.myPenColor = QtCore.Qt.blue
        imageSize = QtCore.QSize(500, 500)
        self.image = QtGui.QImage(imageSize, QtGui.QImage.Format_RGB32)
        self.lastPoint = QtCore.QPoint()

    def openImage(self, fileName):
        loadedImage = QtGui.QImage()
        if not loadedImage.load(fileName):
            return False

        w = loadedImage.width()
        h = loadedImage.height()    
        self.mainWindow.resize(w, h)

        self.image = loadedImage
        self.modified = False
        self.update()
        return True

    def saveImage(self, fileName, fileFormat):
        pass

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def clearImage(self):
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.modified = True
        self.update()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.lastPoint = event.pos()
            self.scribbling = True

    def mouseMoveEvent(self, event):
        if (event.buttons() & QtCore.Qt.LeftButton) and self.scribbling:
            self.drawLineTo(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.scribbling:
            self.drawLineTo(event.pos())
            self.scribbling = False

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(event.rect(), self.image)

    def resizeEvent(self, event):

        self.resizeImage(self.image, event.size())

        super(ScribbleArea, self).resizeEvent(event)

    def drawLineTo(self, endPoint):
        painter = QtGui.QPainter(self.image)
        painter.setPen(QtGui.QPen(self.myPenColor, self.myPenWidth,
            QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        painter.drawLine(self.lastPoint, endPoint)
        self.modified = True

        self.update()
        self.lastPoint = QtCore.QPoint(endPoint)

    def resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

        newImage = QtGui.QImage(newSize, QtGui.QImage.Format_RGB32)
        newImage.fill(QtGui.qRgb(255, 255, 255))
        painter = QtGui.QPainter(newImage)
        painter.drawImage(QtCore.QPoint(0, 0), image)

        self.image = newImage

    def print_(self):
        pass

    def isModified(self):
        return self.modified

    def penColor(self):
        return self.myPenColor

    def penWidth(self):
        return self.myPenWidth


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.saveAsActs = []

        self.scribbleArea = ScribbleArea(self)
        self.scribbleArea.clearImage()
        self.scribbleArea.mainWindow = self  # maybe not using this?
        self.setCentralWidget(self.scribbleArea)

        self.createActions()
        self.createMenus()

        self.setWindowTitle("My Paint Brush")
        self.resize(500, 500)

 
    def open(self):
        pass

    def save(self):
        action = self.sender()
        fileFormat = action.data()
        self.saveFile(fileFormat)

    def penColor(self):
        newColor = QtGui.QColorDialog.getColor(self.scribbleArea.penColor())
        if newColor.isValid():
            self.scribbleArea.setPenColor(newColor)
  
    
    def createActions(self):
        self.openAct = QtGui.QAction("&Open...", self, shortcut="Ctrl+O",
            triggered=self.open)

        for format in QtGui.QImageWriter.supportedImageFormats():
            format = str(format)

            text = format.upper() + "..."

            action = QtGui.QAction(text, self, triggered=self.save)
            action.setData(format)
            self.saveAsActs.append(action)

        self.printAct = QtGui.QAction("&Print...", self,
            triggered=self.scribbleArea.print_)

        self.exitAct = QtGui.QAction("E&xit", self, shortcut="Ctrl+Q",
            triggered=self.close)

        self.penColorAct = QtGui.QAction("&Pen Color...", self,
            triggered=self.penColor)

        self.aboutQtAct = QtGui.QAction("About &Qt", self,
            triggered=QtGui.qApp.aboutQt)

    def createMenus(self):
        self.saveAsMenu = QtGui.QMenu("&Save As", self)
        for action in self.saveAsActs:
            self.saveAsMenu.addAction(action)

        fileMenu = QtGui.QMenu("&File", self)
        fileMenu.addAction(self.openAct)
        fileMenu.addMenu(self.saveAsMenu)
        fileMenu.addAction(self.printAct)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAct)

        optionMenu = QtGui.QMenu("&Options", self)
        optionMenu.addAction(self.penColorAct)
    
        optionMenu.addSeparator()
    

        helpMenu = QtGui.QMenu("&Help", self)
    
        helpMenu.addAction(self.aboutQtAct)

        self.menuBar().addMenu(fileMenu)
        self.menuBar().addMenu(optionMenu)
        self.menuBar().addMenu(helpMenu)

 
    def saveFile(self, fileFormat):
        pass


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

### События мыши
Для обработки нажатия кнопки мыши и перемещения мыши следует наследовать класс, реализующий графический объект, и переопределить следующие методы:

- mousePressEvent (self,event) - вызывается при нажатии кнопки мыши над объек­том. Через параметр event доступен экземпляр класса QGraphicsSceneMouseEvent. Если событие принято, то необходимо вызвать метод accept() через объект события, в про­тивном случае следует вызвать метод ignore(). Если вызван метод ignore(), то методы mouseReleaseEvent() и mouseMoveEvent() вызваны не будут.
- С помощью метода setAcceptedМouseButtons(КНопки) из класса QGraphicsitem можно указать кнопки, события от которых объект принимает. По умолчанию объект принима­ет события от всех кнопок мыши. Если в параметре КНопки указать атрибут NoButton из класса QtCore.Qt, то обработка событий мыши будет отключена;
- mouseReleaseEvent (self,event) - вызывается при отпускании ранее нажатой кнопки мыши. Через параметр event доступен экземпляр класса QGraphicsSceneMouseEvent;
- mouseDouЬleClickEvent (self,event) - Через параметр вызывается event при двойном щелчке мышью в области объекта.
- mouseMoveEvent (self, event) - вызывается при перемещении мыши с нажатой кноп­кой. Через параметр event доступен экземпляр класса QGraphicsSceneMouseEvent. 

Класс QGraphicsSceneMouseEvent наследует QEvent и добавляет следующие методы:

- pos() - все методы из классов QGraphicsSceneEvent и возвращает экземпляр класса QPointF с координатами в пределах области объ­екта;
- scenePos() -возвращает экземпляр класса screenPos() с координатами в пределах сцены;
- QPointF возвращает экземпляр класса QPoint с координатами в пределах экрана;
- lastScenePos() - возвращает экземпляр класса QPointF с координатами последней за­помненной представленнем позиции в пределах сцены;
- lastScreenPos() - возвращает экземпляр класса QPoint с координатами последней за­помненной представленнем позиции в пределах экрана;
- buttonDownPos(КНопка) - возвращает экземпляр класса QPointF с координатами щелчка указанной кнопки мыши в пределах области объекта;
- buttonDownScenePos(КНопка) -возвращает экземпляр класса QPointF с координатами щелчка указанной кнопки мыши в пределах сцены;
- buttonDownScreenPos(КНопка)- возвращает экземпляр класса QPoint с координатами щелчка указанной кнопки мыши в пределах экрана;
- button() - позволяет определить, какая кнопка мыши вызвала событие;
- buttons() - позволяет определить все кнопки, которые нажаты одновременно;
- modifiers() - позволяет определить, какие клавиши-модификаторы (Shift, Ctrl,и др.) были нажаты вместе с кнопкой мыши.
По умолчанию событие мыши перехватывает объект, над которым произведен щелчок мышью. Чтобы перехватывать нажатие и отпускание мыши вне объекта, следует захватить мышь с помощью метода grabMouse() из класса QGraphicsitein. Освободить захваченную ранее мышь позволяет метод ungrabMouse(). Получить ссылку на объект, захвативший мышь, можно с помощью метода mouseGrabberitem() из класса QGraphicsScene.
Для обработки прочих событий мыши следует наследовать класс, реализующий графиче­ский объект, и переопределить следующие методы:

- hoverEnterEvent (self, event) - вызывается при наведении указателя мыши на область объекта. Через параметр event доступен экземпляр класса QGraphicsSceneHoverEvent;

- hoverLeaveEvent (self, event) - вызывается, когда указатель мыши покидает область объекта. Через параметр event доступен экземпляр класса QGraphicsSceneHoverEvent;
- hoverмoveEvent (self,event) - вызывается при перемещении указателя мыши внутри области объекта.

- wheelEvent (self,event) - вызывается при повороте колесика мыши при нахож­дении указателя мыши над объектом. Чтобы обрабатывать событие, в любом случае следует захватить мышь.

Следует учитывать, что методы hoverEnterEvent(), hoverLeaveEvent() и hoverMoveEvent() будут вызваны только в том случае, если обработка этих событий разрешена. Чтобы разре­шить обработку событий nеремещения мыши, следует вызвать метод setAcceptHoverEvents(Флаг) из класса QGraphicsitem и nередать ему значение True. Зна­чение False заnрещает обработку событий nеремещения указателя. Получить текущее со­стояние nозволяет метод acceptHoverEvents().

Класс QGraphicsSceneHoverEvent наследует все методы из классов QGraphicsSceneEvent и QEvent и добавляет следующие методы:
- pos () - возвращает экземnляр класса QPointF с координатами в nределах области объекта;
- scenePos () -возвращает экземnляр класса QPointF с координатами в nределах сцены;
- screenPos () -возвращает экземnляр класса QPoint с координатами в nределах экрана;
- lastpos () - возвращает экземnляр класса QPointF с координатами nоследней заnом­ненной nредставленнем nозиции в nределах области объекта;
- lastScenePos () - возвращает экземnляр класса QPointF с координатами nоследней за­ nомненной nредставленнем nозиции в nределах сцены;
- lastScreenPos () - возвращает экземnляр класса QPoint с координатами nоследней за­nомненной nредставленнем nозиции в nределах экрана;
- modifiers() - nозволяет оnределить, какие клавиши-модификаторы (Shift, Ctrl, и др.) были нажаты.
- delta() -возвращает расстояние nоворота колесика;
- orientation () -возвращает ориентацию в виде значения одного из следующих атрибутов из класса­ QtCore.Qt:
1. Horizontal- 1 - no горизонтали;
2. Vertical -2 ~ no вертикали;
- pos () -возвращает экземnляр класса QPointF с координатами указателя мыши в nреде­лах области объекта;
- scenePos () - возвращает экземnляр класса QPointF с координатами указателя мыши·в nределах сцены;
- screenPos () - возвращает экземnляр класса QPoint с координатами указателя мыши в nределах экрана;
- buttons () - nозволяет оnределить кноnки, которые нажаты однqвременно с nоворотом колесика;
- modifiers()- nозволяет оnределить, какие клавиши-модификаторы (Shift, Ctrl, Ait и др.) были нажаты.

## Single click
chandler.py

```
from PyQt4 import QtCore, QtGui

class ClickHandler():
    def __init__(self, time):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(time)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.timeout)
        self.click_count = 0

    def timeout(self):
        if self.click_count == 1:
            print('Single click')
        elif self.click_count > 1:
            print('Double click')    
        self.click_count = 0

    def __call__(self):
        self.click_count += 1
        if not self.timer.isActive():
            self.timer.start()


class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)

        self.button1 = QtGui.QPushButton("Button 1")
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.button1)
        self.setLayout(hbox)

        self.click_handler = ClickHandler(300)
        self.button1.clicked.connect(self.click_handler)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    w = MyDialog()
    w.show()
    sys.exit(app.exec_())
```

# Mouse Right Button Release Event

brut.py

```
from PyQt4 import QtGui
from PyQt4 import QtCore
import sys

class myPushButton(QtGui.QPushButton):

  def mouseReleaseEvent(self,event):    
  
      # Mouse Right Button Release Event
      if event.button() == QtCore.Qt.RightButton:
        QtGui.QMessageBox.information(self, "Mouse Right Button Release Detected!","Detected Mouse Right Button Release")   
    
    
def main():    

    app      = QtGui.QApplication(sys.argv)
    pushButton   = myPushButton("My QPushButton")
    
    #Resize width and height
    pushButton.resize(300,120)    
    pushButton.setWindowTitle('PyQT QPushButton: Mouse Right Button Released!')  
    pushButton.show()     

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```
### CustomButton

```
from PyQt4 import QtCore, QtGui

class CustomButton(QtGui.QPushButton):

    left_clicked= QtCore.pyqtSignal(int)
    right_clicked = QtCore.pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        QtGui.QPushButton.__init__(self, *args, **kwargs)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(250)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.timeout)
        self.left_click_count = self.right_click_count = 0

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.left_click_count += 1
            if not self.timer.isActive():
                self.timer.start()
        if event.button() == QtCore.Qt.RightButton:
            self.right_click_count += 1
            if not self.timer.isActive():
                self.timer.start()

    def timeout(self):
        if self.left_click_count >= self.right_click_count:
            self.left_clicked.emit(self.left_click_count)
        else:
            self.right_clicked.emit(self.right_click_count)
        self.left_click_count = self.right_click_count = 0


class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.button1 = CustomButton("Button 1")
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.button1)
        self.setLayout(hbox)
        self.button1.left_clicked[int].connect(self.left_click)
        self.button1.right_clicked[int].connect(self.right_click)

    def left_click(self, nb):
        if nb == 1: print('Single left click')
        else: print('Double left click')

    def right_click(self, nb):
        if nb == 1: print('Single right click')
        else: print('Double right click')


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    w = MyDialog()
    w.show()
    sys.exit(app.exec_())

```

3.py
```
#!/usr/bin/env python

import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

from PyQt4 import QtCore, QtGui


class ScribbleArea(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(ScribbleArea, self).__init__(parent)

        self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 1
        self.myPenColor = QtCore.Qt.blue
        imageSize = QtCore.QSize(500, 500)
        self.image = QtGui.QImage(imageSize, QtGui.QImage.Format_RGB32)
        self.lastPoint = QtCore.QPoint()

    def openImage(self, fileName):
        loadedImage = QtGui.QImage()
        if not loadedImage.load(fileName):
            return False

        w = loadedImage.width()
        h = loadedImage.height()    
        self.mainWindow.resize(w, h)

        self.image = loadedImage
        self.modified = False
        self.update()
        return True

    def saveImage(self, fileName, fileFormat):
        pass

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def clearImage(self):
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.modified = True
        self.update()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.lastPoint = event.pos()
            self.scribbling = True

    def mouseMoveEvent(self, event):
        if (event.buttons() & QtCore.Qt.LeftButton) and self.scribbling:
            self.drawLineTo(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.scribbling:
            self.drawLineTo(event.pos())
            self.scribbling = False

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(event.rect(), self.image)

    def resizeEvent(self, event):

        self.resizeImage(self.image, event.size())

        super(ScribbleArea, self).resizeEvent(event)

    def drawLineTo(self, endPoint):
        painter = QtGui.QPainter(self.image)
        painter.setPen(QtGui.QPen(self.myPenColor, self.myPenWidth,
            QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        painter.drawLine(self.lastPoint, endPoint)
        self.modified = True

        self.update()
        self.lastPoint = QtCore.QPoint(endPoint)

    def resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

        newImage = QtGui.QImage(newSize, QtGui.QImage.Format_RGB32)
        newImage.fill(QtGui.qRgb(255, 255, 255))
        painter = QtGui.QPainter(newImage)
        painter.drawImage(QtCore.QPoint(0, 0), image)

        self.image = newImage

    def print_(self):
        pass

    def isModified(self):
        return self.modified

    def penColor(self):
        return self.myPenColor

    def penWidth(self):
        return self.myPenWidth


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.saveAsActs = []

        self.scribbleArea = ScribbleArea(self)
        self.scribbleArea.clearImage()
        self.scribbleArea.mainWindow = self  # maybe not using this?
        self.setCentralWidget(self.scribbleArea)

        self.createActions()
        self.createMenus()

        self.setWindowTitle("My Paint Brush")
        self.resize(500, 500)

    def closeEvent(self, event):
        pass

    def open(self):
        pass

    def save(self):
        action = self.sender()
        fileFormat = action.data()
        self.saveFile(fileFormat)

    def penColor(self):
        newColor = QtGui.QColorDialog.getColor(self.scribbleArea.penColor())
        if newColor.isValid():
            self.scribbleArea.setPenColor(newColor)

    def penWidth(self):
        newWidth, ok = QtGui.QInputDialog.getInteger(self, "Paint Brush",
            "Select pen width:", self.scribbleArea.penWidth(), 1, 50, 1)
        if ok:
            self.scribbleArea.setPenWidth(newWidth)


    def createActions(self):
        self.openAct = QtGui.QAction("&Open...", self, shortcut="Ctrl+O",
            triggered=self.open)

        for format in QtGui.QImageWriter.supportedImageFormats():
            format = str(format)

            text = format.upper() + "..."

            action = QtGui.QAction(text, self, triggered=self.save)
            action.setData(format)
            self.saveAsActs.append(action)

        self.printAct = QtGui.QAction("&Print...", self,
            triggered=self.scribbleArea.print_)

        self.exitAct = QtGui.QAction("E&xit", self, shortcut="Ctrl+Q",
            triggered=self.close)

        self.penColorAct = QtGui.QAction("&Pen Color...", self,
            triggered=self.penColor)

        self.penWidthAct = QtGui.QAction("Pen &Width...", self,
            triggered=self.penWidth)

        self.clearScreenAct = QtGui.QAction("&Clear Screen", self,
            shortcut="Ctrl+L", triggered=self.scribbleArea.clearImage)

        self.aboutQtAct = QtGui.QAction("About &Qt", self,
            triggered=QtGui.qApp.aboutQt)

    def createMenus(self):
        self.saveAsMenu = QtGui.QMenu("&Save As", self)
        for action in self.saveAsActs:
            self.saveAsMenu.addAction(action)

        fileMenu = QtGui.QMenu("&File", self)
        fileMenu.addAction(self.openAct)
        fileMenu.addMenu(self.saveAsMenu)
        fileMenu.addAction(self.printAct)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAct)

        optionMenu = QtGui.QMenu("&Options", self)
        optionMenu.addAction(self.penColorAct)
        optionMenu.addAction(self.penWidthAct)
        optionMenu.addSeparator()
        optionMenu.addAction(self.clearScreenAct)

        helpMenu = QtGui.QMenu("&Help", self)

        helpMenu.addAction(self.aboutQtAct)

        self.menuBar().addMenu(fileMenu)
        self.menuBar().addMenu(optionMenu)
        self.menuBar().addMenu(helpMenu)


    def saveFile(self, fileFormat):
        pass


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```



4.py
```
#!/usr/bin/env python

import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

from PyQt4 import QtCore, QtGui


class ScribbleArea(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(ScribbleArea, self).__init__(parent)

        self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 1
        self.myPenColor = QtCore.Qt.blue
        imageSize = QtCore.QSize(500, 500)
        self.image = QtGui.QImage(imageSize, QtGui.QImage.Format_RGB32)
        self.lastPoint = QtCore.QPoint()

    def openImage(self, fileName):
        loadedImage = QtGui.QImage()
        if not loadedImage.load(fileName):
            return False

        w = loadedImage.width()
        h = loadedImage.height()    
        self.mainWindow.resize(w, h)

        self.image = loadedImage
        self.modified = False
        self.update()
        return True

    def saveImage(self, fileName, fileFormat):
        visibleImage = self.image
        self.resizeImage(visibleImage, self.size())

        if visibleImage.save(fileName, fileFormat):
            self.modified = False
            return True
        else:
            return False

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def clearImage(self):
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.modified = True
        self.update()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.lastPoint = event.pos()
            self.scribbling = True

    def mouseMoveEvent(self, event):
        if (event.buttons() & QtCore.Qt.LeftButton) and self.scribbling:
            self.drawLineTo(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.scribbling:
            self.drawLineTo(event.pos())
            self.scribbling = False

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(event.rect(), self.image)

    def resizeEvent(self, event):

        self.resizeImage(self.image, event.size())

        super(ScribbleArea, self).resizeEvent(event)

    def drawLineTo(self, endPoint):
        painter = QtGui.QPainter(self.image)
        painter.setPen(QtGui.QPen(self.myPenColor, self.myPenWidth,
            QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        painter.drawLine(self.lastPoint, endPoint)
        self.modified = True

        self.update()
        self.lastPoint = QtCore.QPoint(endPoint)

    def resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

        newImage = QtGui.QImage(newSize, QtGui.QImage.Format_RGB32)
        newImage.fill(QtGui.qRgb(255, 255, 255))
        painter = QtGui.QPainter(newImage)
        painter.drawImage(QtCore.QPoint(0, 0), image)

        self.image = newImage

    def print_(self):
        printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)

        printDialog = QtGui.QPrintDialog(printer, self)
        if printDialog.exec_() == QtGui.QDialog.Accepted:
            painter = QtGui.QPainter(printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), QtCore.Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0, 0, self.image)
            painter.end()

    def isModified(self):
        return self.modified

    def penColor(self):
        return self.myPenColor

    def penWidth(self):
        return self.myPenWidth


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.saveAsActs = []

        self.scribbleArea = ScribbleArea(self)
        self.scribbleArea.clearImage()
        self.scribbleArea.mainWindow = self  # maybe not using this?
        self.setCentralWidget(self.scribbleArea)

        self.createActions()
        self.createMenus()

        self.setWindowTitle("My Paint Brush")
        self.resize(500, 500)

    def closeEvent(self, event):
        if self.maybeSave():
            event.accept()
        else:
            event.ignore()

    def open(self):
        if self.maybeSave():
            fileName = QtGui.QFileDialog.getOpenFileName(self, "Open File",
                QtCore.QDir.currentPath())
            if fileName:
                self.scribbleArea.openImage(fileName)

    def save(self):
        action = self.sender()
        fileFormat = action.data()
        self.saveFile(fileFormat)

    def penColor(self):
        newColor = QtGui.QColorDialog.getColor(self.scribbleArea.penColor())
        if newColor.isValid():
            self.scribbleArea.setPenColor(newColor)

    def penWidth(self):
        newWidth, ok = QtGui.QInputDialog.getInteger(self, "Paint Brush",
            "Select pen width:", self.scribbleArea.penWidth(), 1, 50, 1)
        if ok:
            self.scribbleArea.setPenWidth(newWidth)

    def about(self):
        QtGui.QMessageBox.about(self, "About My Paint Brush",
            "<p>The <b>My Paint Brush</b> example shows how to use "
            "QMainWindow as the base widget for an application, and how "
            "to reimplement some of QWidget's event handlers to receive "
            "the events generated for the application's widgets:</p>"
            "<p> We reimplement the mouse event handlers to facilitate "
            "drawing, the paint event handler to update the application "
            "and the resize event handler to optimize the application's "
            "appearance. In addition we reimplement the close event "
            "handler to intercept the close events before terminating "
            "the application.</p>"
            "<p> The example also demonstrates how to use QPainter to "
            "draw an image in real time, as well as to repaint "
            "widgets.</p>")
```

### Работа с изображениями

Библиотека PyQt содержит несколько классов, позволяющих работать с растровыми изо­бражениями в контекстно-зависимом (классы QPixmap и QBitmap) и контекстно-независимом Qimage) представлениях. Получить список форматов, которые можно загрузить, по­зволяет статический метод supportedimageFormats() из класса QimageReader. Метод воз­вращает список с экземплярами класса QByteArray. Получим список поддерживаемых фор­матов для чтения:
```
for i in QtGui.QimageReader.supportedimageFormats():
    print (str (i, "ascii") .upper(), end="· ")
```
#### Результат выполнения:
```
ВМР
GIF ICO JPEG JPG
МNG
РВМ
PGM PNG
РРМ
SVG SVGZ TIF TIFF
ХВМ ХРМ
```
Получить список форматов, в которых можно сохранить изображение, позволяет стати­ческий метод supportedimageFormats ( 1 из класса QimageWri ter. Метод возвращает список QByteArray. Получим список поддерживаемых: форматов для записи:
с экземплярами класса
```
for i in QtGui.QimageWriter.supportedimageFormats():
    print(str(i, "ascii") .upper(), end=" ")
```
Результат выполнения:
```
ВМР
ICO JPEG JPG PNG
РРМ
TIF TIFF
ХВМ ХРМ
```
Обратите внимание на то, что мы можем загрузить изображение в формате GIF, но не имеем возможности сохранить изображение в этом формате, т. к. алгоритм сжатия, исnользуемый в этом формате, защищен патентом.

```
        self.openAct = QtGui.QAction("&Open...", self, shortcut="Ctrl+O",
            triggered=self.open)

        for format in QtGui.QImageWriter.supportedImageFormats():
            format = str(format)

            text = format.upper() + "..."

            action = QtGui.QAction(text, self, triggered=self.save)
            action.setData(format)
            self.saveAsActs.append(action)

```

#### def createActions(self):
```
    def createActions(self):
        self.openAct = QtGui.QAction("&Open...", self, shortcut="Ctrl+O",
            triggered=self.open)

        for format in QtGui.QImageWriter.supportedImageFormats():
            format = str(format)

            text = format.upper() + "..."

            action = QtGui.QAction(text, self, triggered=self.save)
            action.setData(format)
            self.saveAsActs.append(action)

        self.printAct = QtGui.QAction("&Print...", self,
            triggered=self.scribbleArea.print_)

        self.exitAct = QtGui.QAction("E&xit", self, shortcut="Ctrl+Q",
            triggered=self.close)

        self.penColorAct = QtGui.QAction("&Pen Color...", self,
            triggered=self.penColor)

        self.penWidthAct = QtGui.QAction("Pen &Width...", self,
            triggered=self.penWidth)

        self.clearScreenAct = QtGui.QAction("&Clear Screen", self,
            shortcut="Ctrl+L", triggered=self.scribbleArea.clearImage)

        self.aboutAct = QtGui.QAction("&About", self, triggered=self.about)

        self.aboutQtAct = QtGui.QAction("About &Qt", self,
            triggered=QtGui.qApp.aboutQt)

    def createMenus(self):
        self.saveAsMenu = QtGui.QMenu("&Save As", self)
        for action in self.saveAsActs:
            self.saveAsMenu.addAction(action)

        fileMenu = QtGui.QMenu("&File", self)
        fileMenu.addAction(self.openAct)
        fileMenu.addMenu(self.saveAsMenu)
        fileMenu.addAction(self.printAct)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAct)

        optionMenu = QtGui.QMenu("&Options", self)
        optionMenu.addAction(self.penColorAct)
        optionMenu.addAction(self.penWidthAct)
        optionMenu.addSeparator()
        optionMenu.addAction(self.clearScreenAct)

        helpMenu = QtGui.QMenu("&Help", self)
        helpMenu.addAction(self.aboutAct)
        helpMenu.addAction(self.aboutQtAct)

        self.menuBar().addMenu(fileMenu)
        self.menuBar().addMenu(optionMenu)
        self.menuBar().addMenu(helpMenu)

    def maybeSave(self):
        if self.scribbleArea.isModified():
            ret = QtGui.QMessageBox.warning(self, "Paint Brush",
                "The image has been modified.\n"
                "Do you want to save your changes?",
                QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard |
                QtGui.QMessageBox.Cancel)
            if ret == QtGui.QMessageBox.Save:
                return self.saveFile('png')
            elif ret == QtGui.QMessageBox.Cancel:
                return False

        return True

    def saveFile(self, fileFormat):
        initialPath = QtCore.QDir.currentPath() + '/untitled.' + fileFormat

        fileName = QtGui.QFileDialog.getSaveFileName(self, "Save As",
            initialPath,
            "%s Files (*.%s);;All Files (*)" % (fileFormat.upper(), fileFormat))
        if fileName:
            return self.scribbleArea.saveImage(fileName, fileFormat)

        return False


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```
## Изменение обработчика события
События в PyQt4 обрабатываются с помощью изменения обработчиков событий.

```
import sys
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 

class myWin(QMainWindow):
     def __init__(self, parent=None):
         QWidget.__init__(self, parent)
         
     def keyPressEvent(self, event):
         if type(event) == QKeyEvent:
             #here accept the event and do something
             print event.key()
             event.accept()
         else:
             event.ignore()


if __name__ == "__main__":
     app = QApplication(sys.argv)
     mainW = myWin()
     mainW.show()
     sys.exit(app.exec_())
```
ketp.py

```
from PyQt4.QtGui import * 
import sys

class MyWidget(QWidget):
 
    def keyPressEvent(self, event):
        QMessageBox.information(None,"Received Key Press Event!!",
                     "You Pressed: "+ event.text())
      
     
def main():    
    app      = QApplication(sys.argv)
    window   = MyWidget()      
    
    window.resize(250,250)    
    window.setWindowTitle('Detect Key Press Event')    
    window.show()    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```
реинициализируем обработчик события

```
def event(self, event):
        if (event.type()==QEvent.KeyPress) and (event.key()==Qt.Key_Tab):
            self.emit(SIGNAL("tabPressed"))
            return True
```

### capture the Tab key
tabpress.py
```
import sys
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 

#################################################################### 
def main(): 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
    sys.exit(app.exec_()) 

####################################################################
class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args)

        # create objects
        self.la = QLabel("Press tab in this box:")
        self.le = MyLineEdit()
        self.la2 = QLabel("\nLook here:")
        self.le2 = QLineEdit()

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.la)
        layout.addWidget(self.le)
        layout.addWidget(self.la2)
        layout.addWidget(self.le2)
        self.setLayout(layout)

        # connections
        self.connect(self.le, SIGNAL("tabPressed"),
                     self.update)

    def update(self):
        newtext = str(self.le2.text()) + "tab pressed "
        self.le2.setText(newtext)

####################################################################
class MyLineEdit(QLineEdit):
    def __init__(self, *args):
        QLineEdit.__init__(self, *args)
        
    def event(self, event):
        if (event.type()==QEvent.KeyPress) and (event.key()==Qt.Key_Tab):
            self.emit(SIGNAL("tabPressed"))
            return True

        return QLineEdit.event(self, event)

####################################################################
if __name__ == "__main__": 
    main()
```

## реинициализируем обработчик события keyPressEvent()


```
def keyPressEvent(self, event):
        
        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            super(Board, self).keyPressEvent(event)
            return

        key = event.key()
        
        if key == QtCore.Qt.Key_P:
            self.pause()
            return
            
        if self.isPaused:
            return
                
        elif key == QtCore.Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)
            
        elif key == QtCore.Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)
            
        elif key == QtCore.Qt.Key_Down:
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)
            
        elif key == QtCore.Qt.Key_Up:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
            
        elif key == QtCore.Qt.Key_Space:
            self.dropDown()
            
        elif key == QtCore.Qt.Key_D:
            self.oneLineDown()
            
        else:
            super(Board, self).keyPressEvent(event)
```

# Tetris

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, random
from PyQt4 import QtCore, QtGui


class Tetris(QtGui.QMainWindow):
    
    def __init__(self):
        super(Tetris, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):    

        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()        
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        
        self.tboard.start()
        
        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')        
        self.show()
        

    def center(self):
        
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)
        

class Board(QtGui.QFrame):
    
    msg2Statusbar = QtCore.pyqtSignal(str)
    
    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent):
        super(Board, self).__init__(parent)
        
        self.initBoard()
        
        
    def initBoard(self):     

        self.timer = QtCore.QBasicTimer()
        self.isWaitingAfterLine = False
        
        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []

        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()
        
        
    def shapeAt(self, x, y):
        return self.board[(y * Board.BoardWidth) + x]

        
    def setShapeAt(self, x, y, shape):
        self.board[(y * Board.BoardWidth) + x] = shape
        

    def squareWidth(self):
        return self.contentsRect().width() / Board.BoardWidth
        

    def squareHeight(self):
        return self.contentsRect().height() / Board.BoardHeight
        

    def start(self):
        
        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()

        self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.newPiece()
        self.timer.start(Board.Speed, self)

        
    def pause(self):
        
        if not self.isStarted:
            return

        self.isPaused = not self.isPaused
        
        if self.isPaused:
            self.timer.stop()
            self.msg2Statusbar.emit("paused")
            
        else:
            self.timer.start(Board.Speed, self)
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.update()

        
    def paintEvent(self, event):
        
        painter = QtGui.QPainter(self)
        rect = self.contentsRect()

        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)
                
                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter,
                        rect.left() + j * self.squareWidth(),
                        boardTop + i * self.squareHeight(), shape)

        if self.curPiece.shape() != Tetrominoe.NoShape:
            
            for i in range(4):
                
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                    boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                    self.curPiece.shape())

                    
    def keyPressEvent(self, event):
        
        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            super(Board, self).keyPressEvent(event)
            return

        key = event.key()
        
        if key == QtCore.Qt.Key_P:
            self.pause()
            return
            
        if self.isPaused:
            return
                
        elif key == QtCore.Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)
            
        elif key == QtCore.Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)
            
        elif key == QtCore.Qt.Key_Down:
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)
            
        elif key == QtCore.Qt.Key_Up:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
            
        elif key == QtCore.Qt.Key_Space:
            self.dropDown()
            
        elif key == QtCore.Qt.Key_D:
            self.oneLineDown()
            
        else:
            super(Board, self).keyPressEvent(event)
                

    def timerEvent(self, event):
        
        if event.timerId() == self.timer.timerId():
            
            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()
                
        else:
            super(Board, self).timerEvent(event)

            
    def clearBoard(self):
        
        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)

        
    def dropDown(self):
        
        newY = self.curY
        
        while newY > 0:
            
            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break
                
            newY -= 1

        self.pieceDropped()
        

    def oneLineDown(self):
        
        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()
            

    def pieceDropped(self):
        
        for i in range(4):
            
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()
            

    def removeFullLines(self):
        
        numFullLines = 0
        rowsToRemove = []

        for i in range(Board.BoardHeight):
            
            n = 0
            for j in range(Board.BoardWidth):
                if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                    n = n + 1

            if n == 10:
                rowsToRemove.append(i)

        rowsToRemove.reverse()
        

        for m in rowsToRemove:
            
            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                        self.setShapeAt(l, k, self.shapeAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)

        if numFullLines > 0:
            
            self.numLinesRemoved = self.numLinesRemoved + numFullLines
            self.msg2Statusbar.emit(str(self.numLinesRemoved))
                
            self.isWaitingAfterLine = True
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.update()
            

    def newPiece(self):
        
        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth / 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()
        
        #print self.curY

        if not self.tryMove(self.curPiece, self.curX, self.curY):
            
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.msg2Statusbar.emit("Game over")



    def tryMove(self, newPiece, newX, newY):
        
        for i in range(4):
            
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)
            
            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False
                
            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()
        
        return True
        

    def drawSquare(self, painter, x, y, shape):
        
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QtGui.QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2, 
            self.squareHeight() - 2, color)

        painter.setPen(color.light())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.dark())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
            x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1, 
            y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)


class Tetrominoe(object):
    
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7


class Shape(object):
    
    coordsTable = (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))
    )

    def __init__(self):
        
        self.coords = [[0,0] for i in range(4)]
        self.pieceShape = Tetrominoe.NoShape

        self.setShape(Tetrominoe.NoShape)
        

    def shape(self):
        return self.pieceShape
        

    def setShape(self, shape):
        
        table = Shape.coordsTable[shape]
        
        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]

        self.pieceShape = shape
        

    def setRandomShape(self):
        self.setShape(random.randint(1, 7))

        
    def x(self, index):
        return self.coords[index][0]

        
    def y(self, index):
        return self.coords[index][1]

        
    def setX(self, index, x):
        self.coords[index][0] = x

        
    def setY(self, index, y):
        self.coords[index][1] = y

        
    def minX(self):
        
        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])

        return m

        
    def maxX(self):
        
        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])

        return m

        
    def minY(self):
        
        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])

        return m

        
    def maxY(self):
        
        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])

        return m

        
    def rotateLeft(self):
        
        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape
        
        for i in range(4):
            
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))

        return result

        
    def rotateRight(self):
        
        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape
        
        for i in range(4):
            
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        return result


def main():
    
    app = QtGui.QApplication([])
    tetris = Tetris()    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```