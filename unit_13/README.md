# 21v-python


# раскрывающийся сnисок

Класс QСоmbоBох реализует раскрывающийся сnисок с возможностью выбора одного nункта.
При щелчке мышью на nоле nоявляется сnисок возможных вариантов, а nри выборе nункта сnисок сворачивается. 

## Добавление, изменение и удаление элементов
Для добавления, изменения, удаления и nолучения значения элементов nредназначены сле­дующие методы из класса QСоmbоBох:

- addItern() - добавляет один элемент в конец сnиска. 
```
addItem (<Строка> [, <Данные>] )
addItem ( <QIcon>, <Строка> [, <Данные>] )
```
В nараметре <Строка> задается текст элемента сnиска, а в nараметре
<QIcon> - иконка, которая будет отображена nеред текстом. Необязательный nараметр <Данные> nозволяет сохранить nользовательские данные, наnример, индекс в таблице базы данных;

- addItems (<Список insertitem()-строк>) -добавляет несколько элементов в конец сnиска;
- insertItem - вставляет один элемент в указанную nозицию сnиска. Все остальные элементы сдвигаются в конец сnиска.
```
insertItem(<Индeкc>, <Строка>[,<Данные>])
insertItem(<Индeкc>, <Qicon>,<Строка>[,<Данные>])
```
- insertItems(<Индекс>,<Сnисок строк>) -вставляет несколько элементов в указанную позицию списка. Все остальные элементы сдвигаются в конец списка;
- insertSeparator (<Индекс>) - вставляет разделительную линию в указанную позицию;
- setItemText (<Индекс>,<Строка>) -изменяет текст элемента с указанным индексом;
- setItemIcon (<Индекс>, <QIcon>) -изменяет иконку элемента с указанным индексом;
- setItemData (<Индекс>, <Данные> [, role=UserRole] ) - изменяет данные для элемента с указанным индексом. Необязательный параметр role позволяет указать роль, для кото­рой задаются данные. Например, если указать атрибут ToolTipRole из класса QtCore.Qt, то данные задают текст всплывающей подсказки, которая будет отображена при наведе­нии указателя мыши на элемент. По умолчанию изменяются пользовательские данные;
- setCurrentIndex (<Индекс>) - делает элемент с указанным индексом текушим. Метод является слотом с сигнатурой setCurrentindex(int);
- currentIndex() -возврашает индекс текушего элемента;
- currentText() - возвращает текст текушего элемента;
- itemText (<Индекс>) -возвращает текст элемента с указанным индексом;
- itеmDаtв(<Индекс>[,role=UserRole])- возвращает данные, сохраненные в роли role элемента с индексом <Индекс>;
- count() - возвращает общее количество элементов списка. Получить количество эле­ментов можно также с помошью функции len();
- removeItem(<Индeкc>) -удаляет элемент с указанным индексом;
- clear() -удаляет все элементы списка.


## Font

Change font family
Adjust font size
Set font color
Choose background color

## qcombobox.py
```
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

```
# combobox.py

```
#!/usr/bin/env python
#
# combobox.py

import sys
from PyQt4 import QtGui, QtCore

class ComboBoxBasic(QtGui.QWidget):
    """
    An basic example combo box application
    """

    def __init__(self):
        # create GUI
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('Combo Box Basic')
        # Set the window dimensions
        self.resize(250,50)
        
        # vertical layout for widgets
        self.vbox = QtGui.QVBoxLayout()
        self.setLayout(self.vbox)

        # Create a combo box and add it to our layout
        self.combo = QtGui.QComboBox()
        self.vbox.addWidget(self.combo)

        # A label to display our selection
        self.lbl = QtGui.QLabel('Ubuntu')
        # Center align text
        self.lbl.setAlignment(QtCore.Qt.AlignHCenter)
        self.vbox.addWidget(self.lbl)

        # You can add items individually:
        self.combo.addItem('Ubuntu')
        self.combo.addItem('Fedora')

        # Or add a sequence in one call
        distrolist = ['Linux Mint', 'Gentoo', 'Mandriva']
        self.combo.addItems(distrolist)
        
        # Connect the activated signal on the combo box to our handler.
        # This is an overloaded signal, meaning there are variants of it, for
        # example the activated(int) variant emits the index of the chosen
        # option, rather than it's text
        self.connect(self.combo, QtCore.SIGNAL('activated(QString)'), self.combo_chosen)

    def combo_chosen(self, text):
        """
        Handler called when a distro is chosen from the combo box
        """
        self.lbl.setText(text)


# If the program is run directly or passed as an argument to the python
# interpreter then create a ComboBoxBasic instance and show it
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gui = ComboBoxBasic()
    gui.show()
    app.exec_()

```

# Список для выбора шрифта
Класс QFontComboBox реализует раскрывающийся сnисок с названиями шрифтов. 
Шрифт можно выбрать из списка или ввести название в поле, nри этом будут отображаться назва­ния, начинающиеся с введенных букв. Иерархия наследования:
Класс QFontComboBox наследует все методы и сигналы из класса QComboBox и содерЖит несколько дополнительных методов:

- setCurrentFont (<QFont>) - делает текущим элемент, соответствующий
шрифту. В качестве параметра указывается экземпляр класса QFont.
Метод является сло­том с сигнатурой setCurrentFont (const QFont&).
- currentFont() - возвращает экземпляр класса QFont с выбранным шрифтом. 
- setFontFilters (<Фильтр>)- ограничивает список указанными типами шрифтов. В ка­честве параметра указывается комбинация следующих атрибутов из класса QFontComboBox:

- AllFonts - все типы шрифтов;
- ScalaЫeFonts - масштабируемые шрифты;
- NonScalaЫeFonts - не масштабируемые шрифты;
- MonospacedFonts - моноширииные шрифты;
- ProportionalFonts - пропорциональные шрифты.

Класс QFontComboBox содержит сигнал currentFontChanged (const QFont&), который генери­руется при изменении текущего шрифта. Внутри обработчика доступен экземпляр класса QFont с текущим шрифтом.


## Окно для выбора цвета QColorDialog.

реализуется с помощью статического метода getColor()
```
getColor([initial=white] [, parent=None])

getCol~r(<QColor>, <Родитель>, <rекст заголовка>[, options=O])
```
В параметрах <Родитель> и parent указывается ссылка на родительское окно или значение None. Параметры initial и <QColor> задают начальный цвет. В параметре options могут быть указаны следующие атрибуты (или их комбинация) из класса QColorDialog:

- ShowAlphaChannel- пользователь может выбрать значение альфа-канала;
- NoButtons- кнопки ОК и Cancel не отображаются;
- DontUseNativeDialog.

Окно дnя выбора цвета с альфа-каналом реализуется также с помощью статического метода getRgba() из класса QColorDialog. 
```
getRgba([initial=4294967295] [, parent=None])
```
В параметре initial указывается целочисленное значение начального цвета. Метод воз­вращает кортеж из двух элементов:(<Цвет>,<Статус>).
Если второй элемент содержит значение True, то первый элемент будет содержать целочисленное значение выбранного цвета:
```
(n, ok} = QtGui.QColorDialog.getRgba(
    initial=QtGui.QColor ("#ffOOOO").rgba(}, parent=window}
if ok:
    color = QtGui.QColor.fromRgba(n)
    print(color.red(), color.green(), color.Ьlue(), color.alpha())

```

# pad1.py
## initFormatbar():
```
fontBox = QtGui.QFontComboBox(self)
fontBox.currentFontChanged.connect(self.fontFamily)

fontSize = QtGui.QComboBox(self)
fontSize.setEditable(True)

# Minimum number of chars displayed
fontSize.setMinimumContentsLength(3)

fontSize.activated.connect(self.fontSize)

# Typical font sizes
fontSizes = ['6','7','8','9','10','11','12','13','14',
             '15','16','18','20','22','24','26','28',
             '32','36','40','44','48','54','60','66',
             '72','80','88','96']

for i in fontSizes:
    fontSize.addItem(i)

fontColor = QtGui.QAction(QtGui.QIcon("icons/font-color.png"),"Change font color",self)
fontColor.triggered.connect(self.fontColor)

backColor = QtGui.QAction(QtGui.QIcon("icons/highlight.png"),"Change background color",self)
backColor.triggered.connect(self.highlight)

self.formatbar = self.addToolBar("Format")

self.formatbar.addWidget(fontBox)
self.formatbar.addWidget(fontSize)

self.formatbar.addSeparator()

self.formatbar.addAction(fontColor)
self.formatbar.addAction(backColor)

self.formatbar.addSeparator()
```

Реализация методов:

```
def fontFamily(self,font):
  self.text.setCurrentFont(font)

def fontSize(self, fontsize):
    self.text.setFontPointSize(int(fontsize))

def fontColor(self):

    # Get a color from the text dialog
    color = QtGui.QColorDialog.getColor()

    # Set it as the new text color
    self.text.setTextColor(color)

def highlight(self):

    color = QtGui.QColorDialog.getColor()

    self.text.setTextBackgroundColor(color)
```


Добавим действия над текстом:

- bold
- italic
- underlined
- strikeout
- superscript
- subscript


initFormatbar():
```
boldAction = QtGui.QAction(QtGui.QIcon("icons/bold.png"),"Bold",self)
boldAction.triggered.connect(self.bold)

italicAction = QtGui.QAction(QtGui.QIcon("icons/italic.png"),"Italic",self)
italicAction.triggered.connect(self.italic)

underlAction = QtGui.QAction(QtGui.QIcon("icons/underline.png"),"Underline",self)
underlAction.triggered.connect(self.underline)

strikeAction = QtGui.QAction(QtGui.QIcon("icons/strike.png"),"Strike-out",self)
strikeAction.triggered.connect(self.strike)

superAction = QtGui.QAction(QtGui.QIcon("icons/superscript.png"),"Superscript",self)
superAction.triggered.connect(self.superScript)

subAction = QtGui.QAction(QtGui.QIcon("icons/subscript.png"),"Subscript",self)
subAction.triggered.connect(self.subScript)
```
Добавим действия:
```
self.formatbar.addAction(boldAction)
self.formatbar.addAction(italicAction)
self.formatbar.addAction(underlAction)
self.formatbar.addAction(strikeAction)
self.formatbar.addAction(superAction)
self.formatbar.addAction(subAction)

self.formatbar.addSeparator()
```
Реализация методов:
```
def bold(self):

    if self.text.fontWeight() == QtGui.QFont.Bold:

        self.text.setFontWeight(QtGui.QFont.Normal)

    else:

        self.text.setFontWeight(QtGui.QFont.Bold)

def italic(self):

    state = self.text.fontItalic()

    self.text.setFontItalic(not state)

def underline(self):

    state = self.text.fontUnderline()

    self.text.setFontUnderline(not state)

def strike(self):

    # Grab the text's format
    fmt = self.text.currentCharFormat()

    # Set the fontStrikeOut property to its opposite
    fmt.setFontStrikeOut(not fmt.fontStrikeOut())

    # And set the next char format
    self.text.setCurrentCharFormat(fmt)

def superScript(self):

    # Grab the current format
    fmt = self.text.currentCharFormat()

    # And get the vertical alignment property
    align = fmt.verticalAlignment()

    # Toggle the state
    if align == QtGui.QTextCharFormat.AlignNormal:

        fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)

    else:

        fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

    # Set the new format
    self.text.setCurrentCharFormat(fmt)

def subScript(self):

    # Grab the current format
    fmt = self.text.currentCharFormat()

    # And get the vertical alignment property
    align = fmt.verticalAlignment()

    # Toggle the state
    if align == QtGui.QTextCharFormat.AlignNormal:

        fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)

    else:

        fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

    # Set the new format
    self.text.setCurrentCharFormat(fmt)

```

# Выравнивание Alignment
```
# -*- coding:utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
 
app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle(u"Изображение в качестве фона")
window.resize(300,200)
 
# создание объекта-палитры с помощью получения текущей палитры компонента
pal = window.palette()
# установка цвета (3) для фона (2) состояния Normal (1)
pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Background,
             QtGui.QBrush(QtGui.QPixmap("green.png")))
window.setPalette(pal) # использование объекта-палитры
 
label = QtGui.QLabel("Hello World!")
pal1 = label.palette()
pal1.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Background,
             QtGui.QBrush(QtGui.QPixmap("blue.png")))
label.setPalette(pal1)
label.setAlignment(QtCore.Qt.AlignCenter)
label.setStyleSheet("color: #ffffff; font-family: Times; font-size: 18px;")
label.setAutoFillBackground(True)
 
label2 = QtGui.QLabel("Goodbye World!")
label2.setAlignment(QtCore.Qt.AlignCenter)
label2.setStyleSheet('background-image: url("yellow.png"); font-family: Times; font-size: 18px;')
 
 
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(label2)
window.setLayout(vbox)
 
window.show()
sys.exit(app.exec_())
```

initFormatbar():
```
alignLeft = QtGui.QAction(QtGui.QIcon("icons/align-left.png"),"Align left",self)
alignLeft.triggered.connect(self.alignLeft)

alignCenter = QtGui.QAction(QtGui.QIcon("icons/align-center.png"),"Align center",self)
alignCenter.triggered.connect(self.alignCenter)

alignRight = QtGui.QAction(QtGui.QIcon("icons/align-right.png"),"Align right",self)
alignRight.triggered.connect(self.alignRight)

alignJustify = QtGui.QAction(QtGui.QIcon("icons/align-justify.png"),"Align justify",self)
alignJustify.triggered.connect(self.alignJustify)
```
Добавим действия:
```
self.formatbar.addAction(alignLeft)
self.formatbar.addAction(alignCenter)
self.formatbar.addAction(alignRight)
self.formatbar.addAction(alignJustify)

self.formatbar.addSeparator()
```
Реализация методов:
```
def alignLeft(self):
    self.text.setAlignment(Qt.AlignLeft)

def alignRight(self):
    self.text.setAlignment(Qt.AlignRight)

def alignCenter(self):
    self.text.setAlignment(Qt.AlignCenter)

def alignJustify(self):
    self.text.setAlignment(Qt.AlignJustify)
```

# Indent - dedent

initFormatbar():
```
indentAction = QtGui.QAction(QtGui.QIcon("icons/indent.png"),"Indent Area",self)
indentAction.setShortcut("Ctrl+Tab")
indentAction.triggered.connect(self.indent)

dedentAction = QtGui.QAction(QtGui.QIcon("icons/dedent.png"),"Dedent Area",self)
dedentAction.setShortcut("Shift+Tab")
dedentAction.triggered.connect(self.dedent)
```
Действия:
```
self.formatbar.addAction(indentAction)
self.formatbar.addAction(dedentAction)  
```
Реализация методов:
```
def indent(self):

    # Grab the cursor
    cursor = self.text.textCursor()

    if cursor.hasSelection():

        # Store the current line/block number
        temp = cursor.blockNumber()

        # Move to the selection's last line
        cursor.setPosition(cursor.selectionEnd())

        # Calculate range of selection
        diff = cursor.blockNumber() - temp

        # Iterate over lines
        for n in range(diff + 1):

            # Move to start of each line
            cursor.movePosition(QtGui.QTextCursor.StartOfLine)

            # Insert tabbing
            cursor.insertText("\t")

            # And move back up
            cursor.movePosition(QtGui.QTextCursor.Up)

    # If there is no selection, just insert a tab
    else:

        cursor.insertText("\t")

def dedent(self):

    cursor = self.text.textCursor()

    if cursor.hasSelection():

        # Store the current line/block number
        temp = cursor.blockNumber()

        # Move to the selection's last line
        cursor.setPosition(cursor.selectionEnd())

        # Calculate range of selection
        diff = cursor.blockNumber() - temp

        # Iterate over lines
        for n in range(diff + 1):

            self.handleDedent(cursor)

            # Move up
            cursor.movePosition(QtGui.QTextCursor.Up)

    else:
        self.handleDedent(cursor)


def handleDedent(self,cursor):

    cursor.movePosition(QtGui.QTextCursor.StartOfLine)

    # Grab the current line
    line = cursor.block().text()

    # If the line starts with a tab character, delete it
    if line.startswith("\t"):

        # Delete next character
        cursor.deleteChar()

    # Otherwise, delete all spaces until a non-space character is met
    else:
        for char in line[:8]:

            if char != " ":
                break

            cursor.deleteChar()
```

# Показать/Скрыть блок:

initMenubar():
```
# Toggling actions for the various bars
toolbarAction = QtGui.QAction("Toggle Toolbar",self)
toolbarAction.triggered.connect(self.toggleToolbar)

formatbarAction = QtGui.QAction("Toggle Formatbar",self)
formatbarAction.triggered.connect(self.toggleFormatbar)

statusbarAction = QtGui.QAction("Toggle Statusbar",self)
statusbarAction.triggered.connect(self.toggleStatusbar)

view.addAction(toolbarAction)
view.addAction(formatbarAction)
view.addAction(statusbarAction)
```

Реализация методов:
```
def toggleToolbar(self):

  state = self.toolbar.isVisible()

  # Set the visibility to its inverse
  self.toolbar.setVisible(not state)

def toggleFormatbar(self):

    state = self.formatbar.isVisible()

    # Set the visibility to its inverse
    self.formatbar.setVisible(not state)

def toggleStatusbar(self):

    state = self.statusbar.isVisible()

    # Set the visibility to its inverse
    self.statusbar.setVisible(not state)
```

# pad2.py
# Структура каталогов

```
pad.py
icons/
  lots of icons
ext/
  __init__.py
```
# Регулярные выражения

В Python, строки имеют методы для поиска и замены: index(), find(), split(), count(), replace() и т.д. Но эти методы ограничены для простейших случаев. Например метод index() ищет простую жёстко заданную часть строки и поиск всегда регистрозависимый. Чтобы выполнить регистронезависимый поиск по строке s, вы должны вызвать s.lower() или s.upper() для того чтобы быть уверенным что строка имеет соответствующий регистр для поиска. Методы replace() и split() имеют те же ограничения.

Если ваша задача может быть решена при помощи этих методов, лучше использовать их. Они простые и быстрые, легко читаемые, много может быть сказано о быстром, простом и удобочитаемом коде. Но если вы обнаружите что вы используете большое количество строковых функций с условиями if для обработки специальных случаев, или используете множество последовательных вызовов split() и join() чтобы нарезать на кусочки ваши строки, значит вы нуждаетесь в регулярных выражениях.

Регулярные выражения это мощный и (по большей части) стандартизированный способ для поиска, замены и парсинга текста при помощи комплексных шаблонов. Хотя синтаксис регулярных выражений довольно сложный и выглядит непохожим на нормальный код (прим. пер. «смахивает на perl»), конечный результат часто более удобочитаемый чем набор из последовательных функций для строк. Существует даже способ поместить комментарии внутрь регулярных выражений, таким образом вы можете включить небольшую документацию в регулярное выражение.

- ^ совпадение с началом строки.
- $ совпадение с концом строки.
- \b совпадает с границей слова.
- \d совпадает с цифрой.
- \D совпадает с не цифрой.
- x? совпадает с опциональным символом x (другими словами ноль или один символов x).
- x* совпадает с ноль или более x.
- x+ совпадает с один или более x.
- x{n, m} совпадает с x не менее n раз, но не более m раз.
- (a|b|c) совпадает с a или b или c.
- (x) группа для запоминания. Вы можете получить значение используя метод groups() на объекте который возвращает re.search.


# пример: Адрес Улицы

```
# -*- coding:utf-8 -*-

# re1.py пример: Адрес Улицы

s = '100 NORTH MAIN ROAD'
# задача стандартизировать адрес улицы, 
# например 'ROAD' всегда выражается сокращением 'RD.'
print s
print s.replace('ROAD', 'RD.') 
# '100 NORTH MAIN RD.'
# Проблема заключалась в том что 'ROAD' появилась в адресе дважды, 
# один раз как 'ROAD', а во второй как часть названия улицы 'BROAD'. 
# Метод replace() обнаруживал 2 вхождения и слепо заменял оба, 
# разрушая таким образом правильный адрес.

s = '100 NORTH BROAD ROAD'
print s.replace('ROAD', 'RD.') 
# '100 NORTH BRD. RD.'
# Чтобы решить эту проблему вхождения более одной подстроки 'ROAD', вам необходимо прибегнуть к следующему: искать и заменять 'ROAD' в последних четырёх символах адреса (s[-4:]), оставляя строку отдельно (s[:-4]). Как вы могли заметить, это уже становится громоздким. К примеру, шаблон зависит от длины заменяемой строки. (Если вы заменяли 'STREET' на 'ST.', вам придется использовать s[:-6] и s[-6:].replace(...).)

import re 
print re.sub('ROAD$', 'RD.', s) 
# '100 NORTH BROAD RD.'
# 'ROAD$'. Это простое регулярное выражение которое находит 'ROAD' только в конце строки. Знак $ означает «конец строки». (Также существует символ ^, означающий «начало строки».) Используя функцию re.sub() вы ищете в строке s регулярное выражение 'ROAD$' и заменяете на 'RD.'. Оно совпадает с 'ROAD' в конце строки s, но не совпадает с 'ROAD', являющимся частью названия 'BROAD', так как оно находится в середине строки s.

```

# re2.py
```
# -*- coding:utf-8 -*-
import re
# пример: Адрес Улицы

s = '100 BROAD'
re.sub('ROAD$', 'RD.', s)
# '100 BRD.'
re.sub('\\bROAD$', 'RD.', s)   # Требуется совпадения с 'ROAD' когда оно на конце строки и является самостоятельным словом (а не частью большего). Чтобы описать это в регулярном выражении необходимо использовать '\b', что означает «слово должно оказаться прямо тут.» В Python '\' знак в строке должен быть экранирован. Иногда это называют как «бедствие бэкслэша» и это одна из причин почему регулярные выражения проще в Perl чем в Python. Однако недостаток Perl в том что регулярные выражения смешиваются с другим синтаксисом, если у вас ошибка, достаточно сложно определить где она, в синтаксисе или в регулярном выражении.
# '100 BROAD'
re.sub(r'\bROAD$', 'RD.', s)   # тобы обойти проблему «бедствие бэкслэша» вы можете использовать то, что называется неформатированная строка (raw string), путём применения префикса строки при помощи символа 'r'. Это скажет Python-у что ничего в этой строке не должно быть экранировано; '\t' это табулятор, но r'\t' это символ бэкслэша '\' , а следом за ним буква 't'. 

# '100 BROAD'
s = '100 BROAD ROAD APT. 3'
re.sub(r'\bROAD$', 'RD.', s)   # В этом случае адрес улицы содержал в себе цельное отдельное слово 'ROAD' и оно не было на конце строки, так как адрес содержал номер квартиры после определения улицы. Так как слово 'ROAD' не находится в конце строки, регулярное выражение re.sub() его пропускало и мы получали на выходе ту же строку что и на входе.

# '100 BROAD ROAD APT. 3'
re.sub(r'\bROAD\b', 'RD.', s)  # Чтобы решить эту проблему нужно удалить символ '$' и добавить ещё один '\b'. Теперь регулярное выражение совпадает с 'ROAD' если оно являлось цельным словом в любой части строки, на конце, в середине и в начале.
# '100 BROAD RD. APT 3'

```

# пример: Обработка телефонных номеров
- \d совпадает с любыми цифрами (0–9). 
- \D совпадает со всем кроме цифр

Клиент хочет ввести телефонный номер в простое поле (без разделителей), но потом также хочет сохранить индекс, магистраль, номер и опционально добавочную информацию в базе данных компании. 

Вот телефонные номера которые я должен был обработать:
```
800-555-1212
800 555 1212
800.555.1212
(800) 555-1212
1-800-555-1212
800-555-1212-1234
800-555-1212x1234
800-555-1212 ext. 1234
work 1-(800) 555.1212 #1234
```

##  первый шаг:
```
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')  
# Всегда читайте регулярное выражение слева направо. Выражение совпадает с началом строки и потом с (\d{3}). Что такое \d{3}? 
- \d значит «любая цифра» (от 0 до 9). 
- {3} значит «совпадение с конкретно тремя цифрами»; 
Если заключить это выражение в круглые скобки, то это значит «совпасть должно точно три цифры и потом запомнить их как группу которую я запрошу позже». 
Потом выражение должно совпасть с дефисом. 
Потом совпасть с другой группой из трёх цифр, потм опять дефис. 
Потом ещё одна группа из четырёх цифр. 
И в конце совпадение с концом строки.

phonePattern.search('800-555-1212').groups()             

# Чтобы получить доступ к группам которые запомнил обработчик регулярного выражения, используйте метод groups() на объекте который возвращает метод search(). Он должен вернуть кортеж такого количества групп, которое было определено в регулярном выражении. В нашем случае определены три группы, одна с тремя цифрами, другая с тремя цифрами и третья с четырьмя цифрами.

# ('800', '555', '1212')

phonePattern.search('800-555-1212-1234')                 
# Это регулярное выражение не окончательный ответ, так как оно не обрабатывает расширение после телефонного номера. Для этого вы должны расширить регулярное выражение.

phonePattern.search('800-555-1212-1234').groups()        

# Если метод search() не вернёт совпадения, то он вернёт None, это не стандартный объект регулярного выражения. Вызов None.groups() генерирует очевидное исключение: None не имеет метода groups(). 

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'groups'

```
re4.py
```
# -*- coding:utf-8 -*-
import re
# Обработка телефонных номеров

phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')  
print phonePattern.search('800-555-1212-1234').groups()              
# ('800', '555', '1212', '1234')
# Метод groups() теперь возвращает кортеж из четырёх элементов, а регулярное выражение теперь запоминает четыре группы.
print phonePattern.search('800 555 1212 1234')                       

print phonePattern.search('800-555-1212')                            

```
re5.py 
```

phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$') 
# совпадает начало строки, потом группа из трёх цифр, потом \D+. 
\D совпадает с любым символом кроме цифр и также «+» означает «1 или более». Итак \D+ означает один или более символом не являющихся цифрами. 

print phonePattern.search('800 555 1212 1234').groups()
# Использование \D+ вместо «-» значит, что теперь регулярное выражение совпадает с телефонным номером разделённым пробелами вместо дефисов.
# ('800', '555', '1212', '1234')
print phonePattern.search('800-555-1212-1234').groups()
# телефонные номера разделенные дефисами тоже срабатывают.
# ('800', '555', '1212', '1234')
print phonePattern.search('80055512121234') 
# Что если номер введён без всяких разделителей?

print phonePattern.search('800-555-1212')  
```
re6.py
```
# -*- coding:utf-8 -*-
import re
# Обработка телефонных номеров

phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$') 
# замена «+» на «*». Вместо \D+ между частями номера, теперь используется \D*. «*» означает «ноль или более»
print phonePattern.search('80055512121234').groups() 
# ('800', '555', '1212', '1234')
# совпадает начало строки, потом запоминается группа из трёх цифр (800), потом ноль или более нецифровых символов, потом запоминается группа из трёх цифр (555), потом ноль или более нецифровых символов, потом запоминается группа из четырёх цифр (1212), потом ноль или более нецифровых символов, потом запоминается группа из произвольного количества цифр (1234), потом конец строки.
print phonePattern.search('800.555.1212 x1234').groups() 
# ('800', '555', '1212', '1234')
# точки вместо дефисов, и также пробелы или «x» перед расширением.
print phonePattern.search('800-555-1212').groups() 
# ('800', '555', '1212', '')
print phonePattern.search('(800)5551212 x1234')   
# Существуют дополнительные символы до «area» кода, но регулярное выражение думает что код города это первое что находится в начале строки.
```

re7.py
```
# -*- coding:utf-8 -*-
import re
# Обработка телефонных номеров

phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
# \D*, ноль или более нецифровых символов, до первой запомненной группы (код города). 
print phonePattern.search('(800)5551212 ext. 1234').groups() 
# ('800', '555', '1212', '1234')
# Правая скобка также обрабатывается; как нецифровой символ и совпадает с \D* после первой запоминаемой группы.
print phonePattern.search('800-555-1212').groups() 
# ('800', '555', '1212', '')
# Так как лидирующие символы полностью опциональны, совпадает начало строки, ноль нецифровых символов, потом запоминается группа из трёх цифр (800), потом один нецифровой символ (дефис), потом группа из трёх цифр (555), потом один нецифровой (дефис), потом запоминается группа из четырёх цифр (1212), потом ноль нецифровых символов, потом группа цифр из нуля символов, потом конец строки.
print phonePattern.search('work 1-(800) 555.1212 #1234') 
# До сих пор регулярное выражение совпадало с началом строки. Но сейчас вы видите что в начале могут быть непредсказуемые символы которые мы хотели бы проигнорировать. Лучше не пытаться подобрать совпадение для них, а просто пропустить их все, давайте сделаем другое допущение: не пытаться совпадать с началом строки вообще. 
```
re8.py
```
# -*- coding:utf-8 -*-
import re
# Обработка телефонных номеров

phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$') 
# отсутствие ^ в регулярном выражении.
print phonePattern.search('work 1-(800) 555.1212 #1234').groups() 
# ('800', '555', '1212', '1234')
print phonePattern.search('800-555-1212') 
# ('800', '555', '1212', '')
print phonePattern.search('80055512121234') 
# ('800', '555', '1212', '1234')
```

# Поиск и замена  Find-and-replace

ext/find.py:
```
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

import re

class Find(QtGui.QDialog):
    def __init__(self, parent = None):

        QtGui.QDialog.__init__(self, parent)

        self.parent = parent

        self.lastMatch = None

        self.initUI()

    def initUI(self):

        # Button to search the document for something
        findButton = QtGui.QPushButton("Find",self)
        findButton.clicked.connect(self.find)

        # Button to replace the last finding
        replaceButton = QtGui.QPushButton("Replace",self)
        replaceButton.clicked.connect(self.replace)

        # Button to remove all findings
        allButton = QtGui.QPushButton("Replace all",self)
        allButton.clicked.connect(self.replaceAll)

        # Normal mode - radio button
        self.normalRadio = QtGui.QRadioButton("Normal",self)
        self.normalRadio.toggled.connect(self.normalMode)

        # Regular Expression Mode - radio button
        self.regexRadio = QtGui.QRadioButton("RegEx",self)
        self.regexRadio.toggled.connect(self.regexMode)

        # The field into which to type the query
        self.findField = QtGui.QTextEdit(self)
        self.findField.resize(250,50)

        # The field into which to type the text to replace the
        # queried text
        self.replaceField = QtGui.QTextEdit(self)
        self.replaceField.resize(250,50)

        optionsLabel = QtGui.QLabel("Options: ",self)

        # Case Sensitivity option
        self.caseSens = QtGui.QCheckBox("Case sensitive",self)

        # Whole Words option
        self.wholeWords = QtGui.QCheckBox("Whole words",self)

        # Layout the objects on the screen
        layout = QtGui.QGridLayout()

        layout.addWidget(self.findField,1,0,1,4)
        layout.addWidget(self.normalRadio,2,2)
        layout.addWidget(self.regexRadio,2,3)
        layout.addWidget(findButton,2,0,1,2)

        layout.addWidget(self.replaceField,3,0,1,4)
        layout.addWidget(replaceButton,4,0,1,2)
        layout.addWidget(allButton,4,2,1,2)

        # Add some spacing
        spacer = QtGui.QWidget(self)

        spacer.setFixedSize(0,10)

        layout.addWidget(spacer,5,0)

        layout.addWidget(optionsLabel,6,0)
        layout.addWidget(self.caseSens,6,1)
        layout.addWidget(self.wholeWords,6,2)

        self.setGeometry(300,300,360,250)
        self.setWindowTitle("Find and Replace")
        self.setLayout(layout)

        # By default the normal mode is activated
        self.normalRadio.setChecked(True)

    def find(self):

        # Grab the parent's text
        text = str(self.parent.text.toPlainText())

        # And the text to find
        query = self.findField.toPlainText()

        # If the 'Whole Words' checkbox is checked, we need to append
        # and prepend a non-alphanumeric character
        if self.wholeWords.isChecked():
            query = r'\W' + query + r'\W'

        # By default regexes are case sensitive but usually a search isn't
        # case sensitive by default, so we need to switch this around here
        flags = 0 if self.caseSens.isChecked() else re.I

        # Compile the pattern
        pattern = re.compile(query,flags)

        # If the last match was successful, start at position after the last
        # match's start, else at 0
        start = self.lastMatch.start() + 1 if self.lastMatch else 0

        # The actual search
        self.lastMatch = pattern.search(text,start)

        if self.lastMatch:

            start = self.lastMatch.start()
            end = self.lastMatch.end()

            # If 'Whole words' is checked, the selection would include the two
            # non-alphanumeric characters we included in the search, which need
            # to be removed before marking them.
            if self.wholeWords.isChecked():
                start += 1
                end -= 1

            self.moveCursor(start,end)

        else:

            # We set the cursor to the end if the search was unsuccessful
            self.parent.text.moveCursor(QtGui.QTextCursor.End)

    def replace(self):

        # Grab the text cursor
        cursor = self.parent.text.textCursor()

        # Security
        if self.lastMatch and cursor.hasSelection():

            # We insert the new text, which will override the selected
            # text
            cursor.insertText(self.replaceField.toPlainText())

            # And set the new cursor
            self.parent.text.setTextCursor(cursor)

    def replaceAll(self):

        # Set lastMatch to None so that the search
        # starts from the beginning of the document
        self.lastMatch = None

        # Initial find() call so that lastMatch is
        # potentially not None anymore
        self.find()

        # Replace and find until find is None again
        while self.lastMatch:
            self.replace()
            self.find()

    def regexMode(self):

        # First uncheck the checkboxes
        self.caseSens.setChecked(False)
        self.wholeWords.setChecked(False)

        # Then disable them (gray them out)
        self.caseSens.setEnabled(False)
        self.wholeWords.setEnabled(False)

    def normalMode(self):

        # Enable checkboxes (un-gray them)
        self.caseSens.setEnabled(True)
        self.wholeWords.setEnabled(True)

    def moveCursor(self,start,end):

        # We retrieve the QTextCursor object from the parent's QTextEdit
        cursor = self.parent.text.textCursor()

        # Then we set the position to the beginning of the last match
        cursor.setPosition(start)

        # Next we move the Cursor by over the match and pass the KeepAnchor parameter
        # which will make the cursor select the the match's text
        cursor.movePosition(QtGui.QTextCursor.Right,QtGui.QTextCursor.KeepAnchor,end - start)

        # And finally we set this new cursor as the parent's
        self.parent.text.setTextCursor(cursor)
```

ext/__init__.py:
```
__all__ = ["find"]

```
pad.py:
```
  from ext import *
```
initToolbar():
```
self.findAction = QtGui.QAction(QtGui.QIcon("icons/find.png"),"Find and replace",self)
self.findAction.setStatusTip("Find and replace words in your document")
self.findAction.setShortcut("Ctrl+F")
self.findAction.triggered.connect(find.Find(self).show)
```
Добавим действие:
```
self.toolbar.addSeparator()

self.toolbar.addAction(self.findAction)
```
Метод:
```
edit.addAction(self.findAction)
```

# initUI()

Диалог поиска и замены

```
# Кнопка поиска
findButton = QtGui.QPushButton("Find",self)
findButton.clicked.connect(self.find)

# Кнопка замены
replaceButton = QtGui.QPushButton("Replace",self)
replaceButton.clicked.connect(self.replace)

# Кнопка замены всего найденного
allButton = QtGui.QPushButton("Replace all",self)
allButton.clicked.connect(self.replaceAll)
```
Режимы поиска:
```
# Normal режим - radio button
self.normalRadio = QtGui.QRadioButton("Normal",self)
self.normalRadio.toggled.connect(self.normalMode)

# Regular Expression режим - radio button
self.regexRadio = QtGui.QRadioButton("RegEx",self)
self.regexRadio.toggled.connect(self.regexMode)
```
Создаем 2 текстовых поля 250x50 pixels:
```
# Поле запроса
self.findField = QtGui.QTextEdit(self)
self.findField.resize(250,50)

# Поле для замены

self.replaceField = QtGui.QTextEdit(self)
self.replaceField.resize(250,50)
```
Создаем метку QLabel "Options:":
```
optionsLabel = QtGui.QLabel("Options: ",self)

# Опция Case Sensitivity 
self.caseSens = QtGui.QCheckBox("Case sensitive",self)

# Опция Whole Words
self.wholeWords = QtGui.QCheckBox("Whole words",self)
```
Помещаем виджеты в диалоговое окно:
```
# Макет
layout = QtGui.QGridLayout()

layout.addWidget(self.findField,1,0,1,4)
layout.addWidget(self.normalRadio,2,2)
layout.addWidget(self.regexRadio,2,3)
layout.addWidget(findButton,2,0,1,2)

layout.addWidget(self.replaceField,3,0,1,4)
layout.addWidget(replaceButton,4,0,1,2)
layout.addWidget(allButton,4,2,1,2)

# Поля между виджетами
spacer = QtGui.QWidget(self)

spacer.setFixedSize(0,10)

layout.addWidget(spacer,5,0)

layout.addWidget(optionsLabel,6,0)
layout.addWidget(self.caseSens,6,1)
layout.addWidget(self.wholeWords,6,2)
```
Установки окна. 
```
self.setGeometry(300,300,360,250)
self.setWindowTitle("Find and Replace")
self.setLayout(layout)

# По умолчанию активен режим normal
self.normalRadio.setChecked(True)
```
Ищем введенный запрос

```
# Захватываем текст
text = self.parent.text.toPlainText()

# Формируем запрос
query = self.findField.toPlainText()
```
Установка опций поиска
```
# Опция 'Whole Words'
# и non-alphanumeric character
if self.wholeWords.isChecked():
    query = r'\W' + query + r'\W'

# По умолчанию regexes - case sensitive

flags = 0 if self.caseSens.isChecked() else re.I

# Компиляция шаблона
pattern = re.compile(query,flags)

# Если нашли совпадение, увеличиваем позицию на 1
# иначе 0
start = self.lastMatch.start() + 1 if self.lastMatch else 0

# Актуальный поиск
self.lastMatch = pattern.search(text,start)
```
Последнее совпадение:
```
if self.lastMatch:

    start = self.lastMatch.start()
    end = self.lastMatch.end()

    # If 'Whole words' is checked, the selection would include the two
    # non-alphanumeric characters we included in the search, which need
    # to be removed before marking them.
    if self.wholeWords.isChecked():
        start += 1
        end -= 1

    self.moveCursor(start,end)

else:

    # We set the cursor to the end if the search was unsuccessful
    self.parent.text.moveCursor(QtGui.QTextCursor.End)
```
# Подсветка Highlights

```
def moveCursor(self,start,end):

  # We retrieve the QTextCursor object from the parent's QTextEdit
  cursor = self.parent.text.textCursor()

  # Then we set the position to the beginning of the last match
  cursor.setPosition(start)

  # Next we move the Cursor over the match and pass the KeepAnchor parameter
  # which will make the cursor select the match's text
  cursor.movePosition(QtGui.QTextCursor.Right,QtGui.QTextCursor.KeepAnchor,end - start)

  # And finally we set this new cursor as the parent's
  self.parent.text.setTextCursor(cursor)
```
# Замена Replacing


```
    def replace(self):

        # Grab the text cursor
        cursor = self.parent.text.textCursor()

        # Security
        if self.lastMatch and cursor.hasSelection():

            # We insert the new text, which will override the selected
            # text
            cursor.insertText(self.replaceField.toPlainText())

            # And set the new cursor
            self.parent.text.setTextCursor(cursor)
```
# Заменить все Replace ALL


```
    def replaceAll(self):

        # Set lastMatch to None so that the search
        # starts from the beginning of the document
        self.lastMatch = None

        # Initial find() call so that lastMatch is
        # potentially not None anymore
        self.find()

        # Replace and find until find is None again
        while self.lastMatch:
            self.replace()
            self.find()
```
Режимы поиска:
```
    def regexMode(self):

        # First uncheck the checkboxes
        self.caseSens.setChecked(False)
        self.wholeWords.setChecked(False)

        # Then disable them (gray them out)
        self.caseSens.setEnabled(False)
        self.wholeWords.setEnabled(False)

    def normalMode(self):

        # Enable checkboxes (un-gray them)
        self.caseSens.setEnabled(True)
        self.wholeWords.setEnabled(True)
```


Вставка изображения Image insertion

initToolbar():
```
imageAction = QtGui.QAction(QtGui.QIcon("icons/image.png"),"Insert image",self)
imageAction.setStatusTip("Insert image")
imageAction.setShortcut("Ctrl+Shift+I")
imageAction.triggered.connect(self.insertImage)

self.toolbar.addAction(imageAction)
```
Метод self.insertImage():
```
def insertImage(self):

    # Get image file name
    filename = QtGui.QFileDialog.getOpenFileName(self, 'Insert image',".","Images (*.png *.xpm *.jpg *.bmp *.gif)")

    # Create image object
    image = QtGui.QImage(filename)

    # Error if unloadable
    if image.isNull():

        popup = QtGui.QMessageBox(QtGui.QMessageBox.Critical,
                                  "Image load error",
                                  "Could not load image file!",
                                  QtGui.QMessageBox.Ok,
                                  self)
        popup.show()

    else:

        cursor = self.text.textCursor()

        cursor.insertImage(image,filename)
```
Считаем слова

```
ext/wordcount.py:

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class WordCount(QtGui.QDialog):
    def __init__(self,parent = None):
        QtGui.QDialog.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):

        # Word count in selection
        currentLabel = QtGui.QLabel("Current selection",self)
        currentLabel.setStyleSheet("font-weight:bold; font-size: 15px;")

        currentWordsLabel = QtGui.QLabel("Words: ", self)
        currentSymbolsLabel = QtGui.QLabel("Symbols: ",self)

        self.currentWords = QtGui.QLabel(self)
        self.currentSymbols = QtGui.QLabel(self)

        # Total word/symbol count
        totalLabel = QtGui.QLabel("Total",self)
        totalLabel.setStyleSheet("font-weight:bold; font-size: 15px;")

        totalWordsLabel = QtGui.QLabel("Words: ", self)
        totalSymbolsLabel = QtGui.QLabel("Symbols: ",self)

        self.totalWords = QtGui.QLabel(self)
        self.totalSymbols = QtGui.QLabel(self)

        # Layout

        layout = QtGui.QGridLayout(self)

        layout.addWidget(currentLabel,0,0)

        layout.addWidget(currentWordsLabel,1,0)
        layout.addWidget(self.currentWords,1,1)

        layout.addWidget(currentSymbolsLabel,2,0)
        layout.addWidget(self.currentSymbols,2,1)

        spacer = QtGui.QWidget()
        spacer.setFixedSize(0,5)

        layout.addWidget(spacer,3,0)

        layout.addWidget(totalLabel,4,0)

        layout.addWidget(totalWordsLabel,5,0)
        layout.addWidget(self.totalWords,5,1)

        layout.addWidget(totalSymbolsLabel,6,0)
        layout.addWidget(self.totalSymbols,6,1)

        self.setWindowTitle("Word count")
        self.setGeometry(300,300,200,200)
        self.setLayout(layout)

    def getText(self):

        # Get the text currently in selection
        text = self.parent.text.textCursor().selectedText()

        # Split the text to get the word count
        words = str(len(text.split()))

        # And just get the length of the text for the symbols
        # count
        symbols = str(len(text))

        self.currentWords.setText(words)
        self.currentSymbols.setText(symbols)

        # For the total count, same thing as above but for the
        # total text

        text = self.parent.text.toPlainText()

        words = str(len(text.split()))
        symbols = str(len(text))

        self.totalWords.setText(words)
        self.totalSymbols.setText(symbols)
And in __init__.py:

__all__ = ["find","wordcount"]

```

initToolbar():
```
wordCountAction = QtGui.QAction(QtGui.QIcon("icons/count.png"),"See word/symbol count",self)
wordCountAction.setStatusTip("See word/symbol count")
wordCountAction.setShortcut("Ctrl+W")
wordCountAction.triggered.connect(self.wordCount)

self.toolbar.addAction(wordCountAction)
```
Метод:
```
def wordCount(self):

    wc = wordcount.WordCount(self)

    wc.getText()

    wc.show()

```
Количество слов и символов :
```
    # Word count in selection
    currentLabel = QtGui.QLabel("Current selection",self)
    currentLabel.setStyleSheet("font-weight:bold; font-size: 15px;")

    currentWordsLabel = QtGui.QLabel("Words: ", self)
    currentSymbolsLabel = QtGui.QLabel("Symbols: ",self)

    self.currentWords = QtGui.QLabel(self)
    self.currentSymbols = QtGui.QLabel(self)

    # Total word/symbol count
    totalLabel = QtGui.QLabel("Total",self)
    totalLabel.setStyleSheet("font-weight:bold; font-size: 15px;")

    totalWordsLabel = QtGui.QLabel("Words: ", self)
    totalSymbolsLabel = QtGui.QLabel("Symbols: ",self)

    self.totalWords = QtGui.QLabel(self)
    self.totalSymbols = QtGui.QLabel(self)
```
Макет:
```
    # Layout

    layout = QtGui.QGridLayout(self)

    layout.addWidget(currentLabel,0,0)

    layout.addWidget(currentWordsLabel,1,0)
    layout.addWidget(self.currentWords,1,1)

    layout.addWidget(currentSymbolsLabel,2,0)
    layout.addWidget(self.currentSymbols,2,1)

    spacer = QtGui.QWidget()
    spacer.setFixedSize(0,5)

    layout.addWidget(spacer,3,0)

    layout.addWidget(totalLabel,4,0)

    layout.addWidget(totalWordsLabel,5,0)
    layout.addWidget(self.totalWords,5,1)

    layout.addWidget(totalSymbolsLabel,6,0)
    layout.addWidget(self.totalSymbols,6,1)

    self.setWindowTitle("Word count")
    self.setGeometry(300,300,200,200)
    self.setLayout(layout)
```
Метод getText().
```
    def getText(self):

        # Get the text currently in selection
        text = self.parent.text.textCursor().selectedText()

        # Split the text to get the word count
        words = str(len(text.split()))

        # And just get the length of the text for the symbols
        # count
        symbols = str(len(text))

        self.currentWords.setText(words)
        self.currentSymbols.setText(symbols)

        # For the total count, same thing as above but for the
        # total text

        text = self.parent.text.toPlainText()

        words = str(len(text.split()))
        symbols = str(len(text))

        self.totalWords.setText(words)
        self.totalSymbols.setText(symbols)
```

Дата и время

ext/datetime.py:
```
# Inserting time and date

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

from time import strftime

class DateTime(QtGui.QDialog):
    def __init__(self,parent = None):
        QtGui.QDialog.__init__(self, parent)

        self.parent = parent

        self.formats = ["%A, %d. %B %Y %H:%M",
                        "%A, %d. %B %Y",
                        "%d. %B %Y %H:%M",
                        "%d.%m.%Y %H:%M",
                        "%d. %B %Y",
                        "%d %m %Y",
                        "%d.%m.%Y",
                        "%x",
                        "%X",
                        "%H:%M"]

        self.initUI()

    def initUI(self):

        self.box = QtGui.QComboBox(self)

        for i in self.formats:
            self.box.addItem(strftime(i))

        insert = QtGui.QPushButton("Insert",self)
        insert.clicked.connect(self.insert)

        cancel = QtGui.QPushButton("Cancel",self)
        cancel.clicked.connect(self.close)

        layout = QtGui.QGridLayout()

        layout.addWidget(self.box,0,0,1,2)
        layout.addWidget(insert,1,0)
        layout.addWidget(cancel,1,1)

        self.setGeometry(300,300,400,80)
        self.setWindowTitle("Date and Time")
        self.setLayout(layout)

    def insert(self):

        # Grab cursor
        cursor = self.parent.text.textCursor()

        datetime = strftime(self.formats[self.box.currentIndex()])

        # Insert the comboBox's current text
        cursor.insertText(datetime)

        # Close the window
        self.close()
```
ext/__init__.py:

__all__ = ["find","wordcount","datetime"]
```
initToolbar():
```
    dateTimeAction = QtGui.QAction(QtGui.QIcon("icons/calender.png"),"Insert current date/time",self)
    dateTimeAction.setStatusTip("Insert current date/time")
    dateTimeAction.setShortcut("Ctrl+D")
    dateTimeAction.triggered.connect(datetime.DateTime(self).show)

    self.toolbar.addAction(dateTimeAction)
```


# Таблицы

ext/table.py:
```
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class Table(QtGui.QDialog):
    def __init__(self,parent = None):
        QtGui.QDialog.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):

        # Rows
        rowsLabel = QtGui.QLabel("Rows: ",self)

        self.rows = QtGui.QSpinBox(self)

        # Columns
        colsLabel = QtGui.QLabel("Columns",self)

        self.cols = QtGui.QSpinBox(self)

        # Cell spacing (distance between cells)
        spaceLabel = QtGui.QLabel("Cell spacing",self)

        self.space = QtGui.QSpinBox(self)

        # Cell padding (distance between cell and inner text)
        padLabel = QtGui.QLabel("Cell padding",self)

        self.pad = QtGui.QSpinBox(self)

        self.pad.setValue(10)

        # Button
        insertButton = QtGui.QPushButton("Insert",self)
        insertButton.clicked.connect(self.insert)

        # Layout
        layout = QtGui.QGridLayout()

        layout.addWidget(rowsLabel,0,0)
        layout.addWidget(self.rows,0,1)

        layout.addWidget(colsLabel,1,0)
        layout.addWidget(self.cols,1,1)

        layout.addWidget(padLabel,2,0)
        layout.addWidget(self.pad,2,1)

        layout.addWidget(spaceLabel,3,0)
        layout.addWidget(self.space,3,1)

        layout.addWidget(insertButton,4,0,1,2)

        self.setWindowTitle("Insert Table")
        self.setGeometry(300,300,200,100)
        self.setLayout(layout)

    def insert(self):

        cursor = self.parent.text.textCursor()

        # Get the configurations
        rows = self.rows.value()

        cols = self.cols.value()

        if not rows or not cols:

            popup = QtGui.QMessageBox(QtGui.QMessageBox.Warning,
                                      "Parameter error",
                                      "Row and column numbers may not be zero!",
                                      QtGui.QMessageBox.Ok,
                                      self)
            popup.show()

        else:

            padding = self.pad.value()

            space = self.space.value()

            # Set the padding and spacing
            fmt = QtGui.QTextTableFormat()

            fmt.setCellPadding(padding)

            fmt.setCellSpacing(space)

            # Inser the new table
            cursor.insertTable(rows,cols,fmt)

            self.close()

```
ext/__init__.py:

__all__ = ["find","datetime","wordcount","table"]
```
initToolbar():
```
tableAction = QtGui.QAction(QtGui.QIcon("icons/table.png"),"Insert table",self)
tableAction.setStatusTip("Insert table")
tableAction.setShortcut("Ctrl+T")
tableAction.triggered.connect(table.Table(self).show)

self.toolbar.addAction(tableAction)
In initUI():

# We need our own context menu for tables
self.text.setContextMenuPolicy(Qt.CustomContextMenu)
self.text.customContextMenuRequested.connect(self.context)
```
Методы:
```
def context(self,pos):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table, if there is one
        table = cursor.currentTable()

        # Above will return 0 if there is no current table, in which case
        # we call the normal context menu. If there is a table, we create
        # our own context menu specific to table interaction
        if table:

            menu = QtGui.QMenu(self)

            appendRowAction = QtGui.QAction("Append row",self)
            appendRowAction.triggered.connect(lambda: table.appendRows(1))

            appendColAction = QtGui.QAction("Append column",self)
            appendColAction.triggered.connect(lambda: table.appendColumns(1))


            removeRowAction = QtGui.QAction("Remove row",self)
            removeRowAction.triggered.connect(self.removeRow)

            removeColAction = QtGui.QAction("Remove column",self)
            removeColAction.triggered.connect(self.removeCol)


            insertRowAction = QtGui.QAction("Insert row",self)
            insertRowAction.triggered.connect(self.insertRow)

            insertColAction = QtGui.QAction("Insert column",self)
            insertColAction.triggered.connect(self.insertCol)


            mergeAction = QtGui.QAction("Merge cells",self)
            mergeAction.triggered.connect(lambda: table.mergeCells(cursor))

            # Only allow merging if there is a selection
            if not cursor.hasSelection():
                mergeAction.setEnabled(False)


            splitAction = QtGui.QAction("Split cells",self)

            cell = table.cellAt(cursor)

            # Only allow splitting if the current cell is larger
            # than a normal cell
            if cell.rowSpan() > 1 or cell.columnSpan() > 1:

                splitAction.triggered.connect(lambda: table.splitCell(cell.row(),cell.column(),1,1))

            else:
                splitAction.setEnabled(False)


            menu.addAction(appendRowAction)
            menu.addAction(appendColAction)

            menu.addSeparator()

            menu.addAction(removeRowAction)
            menu.addAction(removeColAction)

            menu.addSeparator()

            menu.addAction(insertRowAction)
            menu.addAction(insertColAction)

            menu.addSeparator()

            menu.addAction(mergeAction)
            menu.addAction(splitAction)

            # Convert the widget coordinates into global coordinates
            pos = self.mapToGlobal(pos)

            # Add pixels for the tool and formatbars, which are not included
            # in mapToGlobal(), but only if the two are currently visible and
            # not toggled by the user

            if self.toolbar.isVisible():
              pos.setY(pos.y() + 45)

            if self.formatbar.isVisible():
                pos.setY(pos.y() + 45)

            # Move the menu to the new position
            menu.move(pos)

            menu.show()

        else:

            event = QtGui.QContextMenuEvent(QtGui.QContextMenuEvent.Mouse,QtCore.QPoint())

            self.text.contextMenuEvent(event)

    def removeRow(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Delete the cell's row
        table.removeRows(cell.row(),1)

    def removeCol(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Delete the cell's column
        table.removeColumns(cell.column(),1)

    def insertRow(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Insert a new row at the cell's position
        table.insertRows(cell.row(),1)

    def insertCol(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Insert a new row at the cell's position
        table.insertColumns(cell.column(),1)
```
Строки и столбцы
```
# Rows
rowsLabel = QtGui.QLabel("Rows: ",self)

self.rows = QtGui.QSpinBox(self)

# Columns
colsLabel = QtGui.QLabel("Columns",self)

self.cols = QtGui.QSpinBox(self)

# Cell spacing (distance between cells)
spaceLabel = QtGui.QLabel("Cell spacing",self)

self.space = QtGui.QSpinBox(self)

# Cell padding (distance between cell and inner text)
padLabel = QtGui.QLabel("Cell padding",self)

self.pad = QtGui.QSpinBox(self)

self.pad.setValue(10)

# Button

insertButton = QtGui.QPushButton("Insert",self)
insertButton.clicked.connect(self.insert)
```

Метод insertTable():
```
    def insert(self):

        cursor = self.parent.text.textCursor()

        # Get the configurations
        rows = self.rows.value()

        cols = self.cols.value()

        if not rows or not cols:

            popup = QtGui.QMessageBox(QtGui.QMessageBox.Warning,
                                      "Parameter error",
                                      "Row and column numbers may not be zero!",
                                      QtGui.QMessageBox.Ok,
                                      self)
            popup.show()

        else:

            padding = self.pad.value()

            space = self.space.value()

            # Set the padding and spacing
            fmt = QtGui.QTextTableFormat()

            fmt.setCellPadding(padding)

            fmt.setCellSpacing(space)

            # Insert the new table
            cursor.insertTable(rows,cols,fmt)

            self.close()

```

customContextMenuRequested() signal:
```
# We need our own context menu for tables
self.text.setContextMenuPolicy(Qt.CustomContextMenu)
self.text.customContextMenuRequested.connect(self.context)
```

self.context():
```
event = QtGui.QContextMenuEvent(QtGui.QContextMenuEvent.Mouse,QtCore.QPoint())

self.text.contextMenuEvent(event)
```
Создаем пунут меню QMenu :

Методы appendRows() и appendColumns():

```
appendRowAction = QtGui.QAction("Append row",self)
appendRowAction.triggered.connect(lambda: table.appendRows(1))

appendColAction = QtGui.QAction("Append column",self)
appendColAction.triggered.connect(lambda: table.appendColumns(1))
```
Действия:
```
removeRowAction = QtGui.QAction("Remove row",self)
removeRowAction.triggered.connect(self.removeRow)

removeColAction = QtGui.QAction("Remove column",self)
removeColAction.triggered.connect(self.removeCol)


insertRowAction = QtGui.QAction("Insert row",self)
insertRowAction.triggered.connect(self.insertRow)

insertColAction = QtGui.QAction("Insert column",self)
insertColAction.triggered.connect(self.insertCol)
```

mergeCells() method:

```
mergeAction = QtGui.QAction("Merge cells",self)
mergeAction.triggered.connect(lambda: table.mergeCells(cursor))

# Only allow merging if there is a selection
if not cursor.hasSelection():
    mergeAction.setEnabled(False)
```
splitCell() method:
```
splitAction = QtGui.QAction("Split cells",self)

cell = table.cellAt(cursor)

# Only allow splitting if the current cell is larger
# than a normal cell
if cell.rowSpan() > 1 or cell.columnSpan() > 1:

    splitAction.triggered.connect(lambda: table.splitCell(cell.row(),cell.column(),1,1))

else:
    splitAction.setEnabled(False)
```
Меню:
```
menu.addAction(appendRowAction)
menu.addAction(appendColAction)

menu.addSeparator()

menu.addAction(removeRowAction)
menu.addAction(removeColAction)

menu.addSeparator()

menu.addAction(insertRowAction)
menu.addAction(insertColAction)

menu.addSeparator()

menu.addAction(mergeAction)
menu.addAction(splitAction)
```
mapToGlobal() method:
```
# Convert the widget coordinates into global coordinates
pos = self.mapToGlobal(pos)

# Add pixels for the tool and format bars, which are not included
# in mapToGlobal(), but only if the two are currently visible and
# not toggled by the user

if self.toolbar.isVisible():
    pos.setY(pos.y() + 45)

if self.formatbar.isVisible():
    pos.setY(pos.y() + 45)


# Move the menu to the new position
menu.move(pos)

menu.show()
```
removeRow():
```
def removeRow(self):

    # Grab the cursor
    cursor = self.text.textCursor()

    # Grab the current table (we assume there is one, since
    # this is checked before calling)
    table = cursor.currentTable()

    # Get the current cell
    cell = table.cellAt(cursor)

    # Delete the cell's row
    table.removeRows(cell.row(),1)
```

writer.py:
```
В __init__() добавим:

self.changesSaved = True

В initUI() добавим:

self.text.textChanged.connect(self.changed)
```
Метод changed:
```
def changed(self):
    self.changesSaved = False

def closeEvent(self,event):

    if self.changesSaved:

        event.accept()

    else:

        popup = QtGui.QMessageBox(self)

        popup.setIcon(QtGui.QMessageBox.Warning)

        popup.setText("The document has been modified")

        popup.setInformativeText("Do you want to save your changes?")

        popup.setStandardButtons(QtGui.QMessageBox.Save    |
                                  QtGui.QMessageBox.Cancel |
                                  QtGui.QMessageBox.Discard)

        popup.setDefaultButton(QtGui.QMessageBox.Save)

        answer = popup.exec_()

        if answer == QtGui.QMessageBox.Save:
            self.save()

        elif answer == QtGui.QMessageBox.Discard:
            event.accept()

        else:
            event.ignore()
```
В конце self.save() добавим:
```
self.changesSaved = True
```
