# 21v-python

## События
Все приложения с графическим интерфейсом являются событийно-ориентированными. События вызываются главным образом пользователем приложения. Однако, они могут быть вызваны другими средствами, к примеру подключением к Интернету, диспетчером окон или таймером. Когда мы вызываем метод exec_(), приложение входит в главный цикл. Главный цикл получает события и отправляет их объектам.

В событийной модели имеются три участника:

- Источник события;
- Объект события;
- Цель события.

Источник события – это объект, состояние которого меняется. Он вызывает события. Объект события (событие) внедряет состояние, которое меняется в источнике события. Цель события – это объект, которому требуется уведомление. Объект источника события поручает задачу обработки события цели события.

Чтобы начать работу с событиями, PyQt имеет уникальный механизм сигналов и слотов. Сигналы и слоты используют для связи между объектами. Сигнал срабатывает, когда происходит конкретное событие. Слот может быть чем-то, вызываемым средствами Python. Слот вызывается, когда срабатывает его сигнал.


## Обработка сигналов и событий
При взаимодействии пользователя с окном происходят события. В ответ на события система генерирует определенные сигналы. Сигналы — это своего рода извещения системы о том, что пользователь выполнил какое-либо действие или в самой системе возникло некоторое условие. Сигналы являются важнейшей составляющей приложения с графическим интерфейсом, поэтому необходимо знать, как назначить обработчик сигнала, как удалить обработчик, а также уметь правильно обработать событие. Какие сигналы генерирует тот или иной компонент мы будем рассматривать при изучении конкретного компонента.

## Назначение обработчиков сигналов
Чтобы обработать какой-либо сигнал необходимо сопоставить ему функцию или метод класса, которые будут вызваны при наступлении события. Назначить обработчик позволяет статический метод connect() из класса QObject. Форматы метода:
```
connect(<Объект>, <Сигнал>, <Обработчик>[, <ConnectionType>])
connect(<Объект1>, <Сигнал>, <Объект2>, <Слот>[, <ConnectionType>])
connect(<Объект1>, <Сигнал>, <Объект2>, <Сигнал>[, <ConnectionType>])
```
Кроме того, существует обычный (не статический) метод connect():
```
<Объект2>.connect(<Объект1>, <Сигнал>, <Слот>[, <ConnectionType>])
```
Первый формат позволяет назначить обработчик сигнала <Сигнал>, возникшего при изменении статуса объекта <Объект>. Если обработчик успешно назначен, то метод возвращает значение True. Для одного сигнала можно назначить несколько обработчиков, которые будут вызываться в порядке назначения в программе. 

В параметре Сигнал указывается результат выполнения функции SIGNAL(). 

Формат функции:
```
QtCore.SIGNAL("<Название сигнала>([Тип параметров])")
```
Каждый компонент имеет определенный набор сигналов, например, при щелчке на кнопке генерируется сигнал clicked(bool=0). Внутри круглых скобок могут быть указаны типы параметров, которые передаются в обработчик. Если параметров нет, то указываются только круглые скобки. Пример указания сигнала без параметров:
```
QtCore.SIGNAL("clicked()")
```
В этом случае обработчик не принимает никаких параметров. Указание сигнала с параметром выглядит следующим образом:
```
QtCore.SIGNAL("clicked(bool)")
```
В этом случае обработчик должен принимать один параметр, значение которого всегда будет равно 0 (False), так как это значение по умолчанию для сигнала clicked().

В параметре <Обработчик> можно указать:
➔ ссылку на пользовательскую функцию;
➔ ссылку на метод класса;
➔ ссылку на экземпляр класса. В этом случае внутри класса должен существовать метод __call__().

Пример обработки щелчка на кнопке 0.py
```
# Варианты назначения пользовательского обработчика
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    print("Кнопка нажата. Функция on_clicked()")

class MyClass():
    def __init__(self, x=0):
        self.x = x
    def __call__(self):
        print("Кнопка нажата. Метод MyClass.__call__()")
        print("x =", self.x)
    def on_clicked(self):
        print("Кнопка нажата. Метод MyClass.on_clicked()")

obj = MyClass()
app = QtGui.QApplication(sys.argv)
button = QtGui.QPushButton(u"Нажми меня")

# Назначаем обработчиком функцию
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), on_clicked)

# Назначаем обработчиком метод класса
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), obj.on_clicked)

# Передача параметра в обработчик
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), MyClass(10))
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), MyClass(5))
button.show()
sys.exit(app.exec_())
```
Результат выполнения в окне консоли при одном щелчке на кнопке:
```
Кнопка нажата. Функция on_clicked()
Кнопка нажата. Метод MyClass.on_clicked()
Кнопка нажата. Метод MyClass.__call__()
x = 10
Кнопка нажата. Метод MyClass.__call__()
x = 5
```
Второй формат метода connect() назначает в качестве обработчика метод Qt-объекта <Объект2>. Обычно используется для назначения стандартного метода из класса, входящего в состав библиотеки Qt. В качестве примера при щелчке на кнопке завершим работу приложения.
```
# Завершение работы приложения при щелчке на кнопке 0_1.py
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys
app = QtGui.QApplication(sys.argv)
button = QtGui.QPushButton(u"Завершить работу")
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), app, QtCore.SLOT("quit()"))
button.show()
sys.exit(app.exec_())
```
в третьем параметре метода connect() указывается объект приложения, а в четвертом параметре в функцию SLOT() передается название метода quit() в виде строки. Благодаря гибкости языка Python данное назначение обработчика можно записать иначе:
```
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), app.quit)
```
Третий формат метода connect() позволяет передать сигнал другому объекту.
```
# Передача сигнала другому объекту
##!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
from PyQt4 import QtCore, QtGui
class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.button1 = QtGui.QPushButton(u"Кнопка 1. Нажми меня")
        self.button2 = QtGui.QPushButton(u"Кнопка 2")
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        self.setLayout(vbox)
        self.resize(300, 100)
        # Передача сигнала от кнопки 1 к кнопке 2
        self.connect(self.button1, QtCore.SIGNAL("clicked()"), self.button2, QtCore.SIGNAL('clicked()'))
        # Способ 1 (4 параметра)
        self.connect(self.button2, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("on_clicked_button2()"))
        # Способ 2 (3 параметра)
        self.connect(self.button2, QtCore.SIGNAL("clicked()"), QtCore.SLOT("on_clicked_button2()"))
    @QtCore.pyqtSlot()
    def on_clicked_button2(self):
        print("Сигнал получен кнопкой 2")


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```

В этом примере мы создали класс MyWindow, который наследует класс QtGui.QWidget.
В методе инициализации __init__() вначале вызывается конструктор базового класса и создаются две кнопки. Далее создается вертикальный контейнер и в него добавляются объекты кнопок с помощью метода addWidget(). С помощью метода setLayout() вертикальный контейнер добавляется в основное окно. Затем назначаются обработчики событий для кнопок. Обратите внимание на то, что метод connect() вызывается как метод нашего класса. Это возможно потому, что большинство PyQt-классов наследуют класс QObject, в котором определен метод connect(). Обработка нажатия кнопки производится с помощью метода on_clicked_button2(), который превращен декоратором @QtCore.pyqtSlot() в одноименный слот.
При нажатии первой кнопки производится вызов первого обработчика, который перенаправляет сигнал на вторую кнопку. Назначение перенаправления, соответствующее третьему формату метода connect(), выглядит так:
```
self.connect(self.button1, QtCore.SIGNAL("clicked()"), self.button2, QtCore.SIGNAL('clicked()'))
```
После перенаправления сигнала вызывается обработчик второй кнопки. Для второй кнопки мы назначили обработчик двумя способами. Первый способ соответствует второму формату метода connect():
```
self.connect(self.button2, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("on_clicked_button2()"))
```
Второй способ соответствует четвертому формату метода connect():
```
self.connect(self.button2, QtCore.SIGNAL("clicked()"), QtCore.SLOT("on_clicked_button2()"))
```
Необязательный параметр <ConnectionType> определяет тип соединения между сигналом и обработчиком. На этот параметр следует обратить особое внимание при использовании нескольких потоков в приложении, так как изменять GUI-поток из другого потока нельзя. В параметре можно указать одно из следующих атрибутов из класса QtCore.Qt:

➔ AutoConnection — 0 — значение по умолчанию. Если источник сигнала и
обработчик находятся в одном потоке, то эквивалентно значению DirectConnection, а если в разных потоках — то QueuedConnection;
➔ DirectConnection — 1 — обработчик вызывается сразу после генерации сигнала. Обработчик выполняется в потоке источника сигнала;
➔ QueuedConnection — 2 — сигнал помещается в очередь обработки событий. Обработчик выполняется в потоке приемника сигнала;
➔ BlockingQueuedConnection — 4 — аналогично значению QueuedConnection, но пока сигнал не обработан поток будет заблокирован. Обратите внимание на то, что источник сигнала и обработчик должны быть обязательно расположены в разных потоках;
➔ UniqueConnection — 0x80 — аналогично значению AutoConnection, но обработчик можно назначить только если он не был назначен ранее. Например, если изменить способы назначения обработчика из предыдущего примера для кнопки button2 следующим образом, то второй обработчик назначен не будет:
```
st = self.connect(self.button2, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("on_clicked_button2()"), QtCore.Qt.UniqueConnection)
print(st)
st = self.connect(self.button2, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("on_clicked_button2()"), QtCore.Qt.UniqueConnection)
print(st)
```
Результат:
```
True
False
```
➔ AutoCompatConnection — 3 — значение использовалось по умолчанию в Qt.

```

def createButton(self, text, member):
        button = Button(text)
        # button.clicked.connect(member)
        QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), member)
        return button
```

## Перегрузка QtCore.QObject.connect

button.clicked.connect(member)

void clicked (bool = 0)


## Отправитель события

Отправитель – это объект, который посылает сигнал. Получатель – это объект, который получает сигнал. Слот – это метод, который реагирует на сигнал.

Иногда удобно знать, какой виджет является отправителем сигнала. Для этого, PyQt имеет метод sender().

Мы определяем источник сигнала путём вызова метода sender(). 

```
    def digitClicked(self):
        
        clickedButton = self.sender()
        
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))
```


## Срабатывание сигналов

Объекты, создаваемые из QObject, могут имитировать сигналы. 

Мы создаём новый сигнал, именуемый SIGNAL("clicked()"). Этот сигнал испускается во время события нажатия кнопки мыши. Сигнал присоединяется к слоту quit() класса QApplication.
```
# Завершение работы приложения при щелчке на кнопке
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys
app = QtGui.QApplication(sys.argv)
button = QtGui.QPushButton("Завершить работу")
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), app, QtCore.SLOT("quit()"))
button.show()
sys.exit(app.exec_())
```

1.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys, os
from PyQt4 import QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''

        self.sumInMemory = 0.0
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.waitingForOperand = True

        self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                    self.digitClicked))

        self.pointButton = self.createButton(".", self.pointClicked)
        self.changeSignButton = self.createButton("\261",
                self.changeSignClicked)


        self.divisionButton = self.createButton("\367",
                self.multiplicativeOperatorClicked)
        self.multiplicatButton = self.createButton("\327",
                self.multiplicativeOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)


        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 6)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.pointButton, 5, 2)
        mainLayout.addWidget(self.changeSignButton, 5, 3)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.multiplicatButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.equalButton, 5, 5)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def createButton(self, text, member):
        button = Button(text)
        QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), member)
        # button.clicked.connect(member)
        return button

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))

    def multiplicativeOperatorClicked(self):
        pass

    def additiveOperatorClicked(self):
        pass

    def equalClicked(self):
        pass

    def pointClicked(self):
        pass

    def changeSignClicked(self):
        pass

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calculator()
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()

```
# QLineEdit
QLineEdit – это виджет, который разрешает вводить и редактировать одну строку текста. 

Редактор строки позволяет пользователю вводить и редактировать одну строку простого текста с набором полезных функций редактирования, включая отмену, повтор, вырезание, вставку, а также перетаскивание с помощью механизма drag-and-drop.

Изменяя свойства echoMode() редактора, можно использовать его в качестве поля "только-для-записи" и для ввода паролей.
```
        self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
```        

Длина текста может быть ограничена с помощью maxLength(). Для текста можно задать условия, используя validator() или inputMask(), либо оба их.
```
        
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)
```
QTextEdit - это подобный класс, но он позволяет редактировать многострочный форматированный текст.

Вы можете изменять текст с помощью setText() или insert(). Текст может быть получен с помощью text(); отображаемый текст (может отличаться от содержащегося текста) может быть получен с помощью displayText(). Текст может быть выделен с помощью setSelection() или selectAll(), а выделенный текст может быть вырезан с помощью cut(), скопирован с помощью copy() и вставлен с помощью paste(). Текст может быть выровнен с помощью setAlignment().

При изменении текста испускается сигнал textChanged(); при изменении текста с помощью setText(), испускается сигнал textEdited(); при перемещении курсора испускается сигнал cursorPositionChanged(); а при нажатии клавиш Return или Enter испускается сигнал returnPressed().

При окончании редактирования (редактор теряет фокус или нажата клавиша Return/Enter) испускается сигнал editingFinished().

Обратите внимание на то, что если установлено условие для текста (validator()), то сигналы returnPressed()/editingFinished() испускаются только в случае, если условие для текста возвращает QValidator::Acceptable.

По умолчанию, QLineEdits имеет рамку, определенную Windows или или стилем Motif; это может быть изменено с помощью setFrame(false).

Ниже приведены ключевые клавиши и сочетания клавиш и действия, вызываемые ими, определенные по умолчанию. Также редактор строки предоставляет контекстное меню (обычно вызываемое по нажатии правой кнопки мыши), в котором представлены некоторые из этих действий.

- Стрелка Влево   Перемещает курсор на один символ влево.
- Shift+Стрелка Влево Перемещает курсор на один символ влево с выделением текста.
- Стрелка Вправо  Перемещает курсор на один символ вправо.
- Shift+Стрелка Вправо    Перемещает курсор на один символ вправо с выделением текста.
- Home    Перемещает курсор в начало строки.
- End Перемещает курсор в конец строки.
- Backspace   Удаляет один символ, стоящий слева от курсора.
- Ctrl+Backspace  Удаляет одно слово, стоящее слева от курсора.
- Delete  Удаляет один символ, стоящий справа от курсора.
- Ctrl+Delete Удаляет одно слово, стоящее справа от курсора.
- Ctrl+A  Перемещает курсор в начало строки.
- Ctrl+B  Перемещает курсор в конец строки.
- Ctrl+C  Копирует выделенный текст в буфер обмена.
- Ctrl+Insert Копирует выделенный текст в буфер обмена.
- Ctrl+D  Удаляет один символ, стоящие справа от курсора.
- Ctrl+E  Перемещает курсор в конец строки.
- Ctrl+F  Перемещает курсор на один символ вправо.
- Ctrl+H  Удаляет один символ, стоящий слева от курсора.
- Ctrl+K  Удаляет все символы от курсора до конца строки.
- Ctrl+V  Вставляет текст в редактор из буфера обмена.
- Shift+Insert    Вставляет текст в редактор из буфера обмена.
- Ctrl+X  Удаляет выделенный текст и копирует его в буфер обмена.
- Shift+Delete    Удаляет выделенный текст и копирует его в буфер обмена.
- Ctrl+Z  Отменяет последнюю операцию.
- Ctrl+Y  Повторяет последнюю отмененную операцию.
Любые другие сочетания клавиш, имеющие символьное представление, приведут к вставке этого предаставления в строку.


## Описание Типов Членов

### enum QLineEdit::EchoMode

- QLineEdit::Normal   0   Отображаются те-же самые символы, что и введены. Это режим по умолчанию.
- QLineEdit::NoEcho   1   Не отображается вообще ничего. Этот режим может использоваться для ввода паролей там, где даже длинна пароля должна оставаться в секрете.
- QLineEdit::Password 2   Вместо фактически введенных символов отображаются звездочки.


### acceptableInput : const bool

Данное свойство сообщает, соответствует ли введенный текст маске ввода или условию, наложенному на текст.

Функции доступа:

bool hasAcceptableInput () const


### alignment : Qt::Alignment

Данное свойство содержит выравнивание текста в редакторе.

Допускается только выравнивание по горизонтали, Qt::AlignJustify считается Qt::AlignLeft.
```
self.display.setAlignment(QtCore.Qt.AlignRight)
```

Функции доступа:

Qt::Alignment alignment () const
void setAlignment ( Qt::Alignment flag )

### cursorPosition : int

Данное свойство содержит текущее положение курсора в редакторе.

Установка положения курсора приводит к перерисовке виджета, если необходимо.

Функции доступа:

int cursorPosition () const
void setCursorPosition ( int )

### displayText : const QString

Данное свойство содержит отображаемый текст.

Если echoMode равно Normal, то возвращается тоже самое, что возвращается text(); если EchoMode равно Password, то возвращается строка, содержащаю звездочки, с длиной text().length() символов, например, "******"; если EchoMode равно NoEcho, то возвращается пустая строка, "".

Функции доступа:

QString displayText () const


### dragEnabled : bool

Данное свойство указывает, начинает ли редактор процесс перетаскивания, если пользователь начинает перемещать мышь с нажатой кнопкой над выделенным текстом.

По умолчанию перетаскивание запрещено.

Функции доступа:

bool dragEnabled () const
void setDragEnabled ( bool b )

### echoMode : EchoMode

Данное свойство содержит режим отображения содержимого редактора.

Изначальное значение - это Normal, но QLineEdit также поддерживает режимы NoEcho и Password.

Это свойство влияет на отображение содержимого текста, возможность копирования и перетаскивания текста.

Функции доступа:

EchoMode echoMode () const
void setEchoMode ( EchoMode )

### frame : bool

Данное свойство указывает, отображается ли рамка редактора.

Если рамка доступна (по умолчанию), то редактор рисуется внутри рамки, в противном случае редактор отображается без рамки.

Функции доступа:

bool hasFrame () const
void setFrame ( bool )

### hasSelectedText : const bool

Данное свойство сообщает, выделен ли какой либо текст в редакторе.

hasSelectedText() возвращает true, если пользователем выделена часть текста или весь текст; в противном случае возвращает false.

Функции доступа:

bool hasSelectedText () const


### inputMask : QString

Данное свойство содержит маску ввода.

Если маска не установлена, то inputMask() возвращает пустую строку.

Устанавливает маску ввода QLineEdit. Условие для текста может использоваться вместо маски или вместе с ней; 

Сброс маски в возвращение обычной работы QLineEdit производится с помощью передачи пустой строки ("") или с помощью вызова setInputMask() без аргументов.

Формат маски предусматривает следующие символы:


- A   Требуется алфавитный символ ASCII. A-Z, a-z.
- a   Разрешен, но не обязателен алфавитный симовл ASCII.
- N   Требуется алфавитный символ или цифра ASCII. A-Z, a-z, 0-9.
- n   Разрешен, но не обязателен алфавитный символ или цифра ASCII.
- X   Требуется любой символ.
- x   Разрешен, но не обязателен любой символ.
- 9   Требуется цифра ASCII. 0-9.
- 0   Разрешена, но не обязательна цифра ASCII.
- D   Требуется цифра ASCII не равная нулю. 1-9.
- d   Разрешена, но не обязательна цифра ASCII не равная нулю (1-9).
- #   Разрешена, но не обязательна цифра или знак плюс/минус ASCII.
- H   Требуется шестнадцатиричный символ. A-F, a-f, 0-9.
- h   Разрешен, но не обязателен шестнадцатиричный символ.
- B   Требуется двоичный символ. 0-1.
- b   Разрешен, но не обязателен двоичный символ.
- >   Все следующие алфавитный символы переводятся в верхний регистр.
- <   Все следующие алфавитный символы переводятся в нижний регистр.
- !   Изменение регистра отключается.
- \   Используйте \ для того, чтобы отменить действие вышеприведенных знаков, как специальных символов, и использовать их в качестве разделителей.
Маска состоит из строки символов маски и разделителей, иногда сопровождается точкой с запятой и символом, используемым для обозначения пробелов: символы пробелов всегда удаляются из строки после окончания редактирования. По умолчанию, символы пробела, соответствуют обычному пробелу.

Примеры:

- 000.000.000.000;_   IP-адрес; пробелы обозначаются символом _.
- HH:HH:HH:HH:HH:HH;_ MAC-адрес
- 0000-00-00  Дата ISO; пробелы обозначаются символом пробел
- >AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#    Лицензионный номер; пробелы обозначаются символом - и все (алфавитные) символы приводятся к верхнему регистру.
Для контроля диапазона символов (например, при вводе IP-адреса) используйте маску с условием для текста.

Функции доступа:

QString inputMask () const
void setInputMask ( const QString & inputMask )


### maxLength : int

Данное свойство содержит максимальную разрешенную длину текста.

Если текст очень длинный, то он обрезается по установленному пределу.

Если происходит обрезание текста, то текст становится не выделенным (если раньше что либо было выделено), курсор помещается в позицию 0 и отображается первая часть текста.

Если для редактора установлена маска ввода, то эта маска определяет максимальную длину текста.

Функции доступа:

int maxLength () const
void setMaxLength ( int )


## modified : bool

Данное свойство указывает, было ли изменено содержимое редактора пользователем.

QLineEdit никогда не читает флаг изменения; по умолчанию флаг имеет значение false и изменяется на true всякий раз, когда пользователь изменяет содержимое редактора.

Это удобно в случаях, когда приложение предоставляет значение по умолчанию, но не знает, что такое значение есть (возможно, значение по умолчанию зависит от других полей формы). Сначала редактор не отображает значение по умолчанию, но при значет о нем, и только если modified() возвращает false (пользователь не ввел текст), вставляет значение по умолчанию.

Вызов setText() устанавливает флаг модификации в false.

Функции доступа:

bool isModified () const
void setModified ( bool )

### readOnly : bool

Данное свойство указывает, позволяет ли редактор вводить текст или только читать.

В режиме только-для-чтения пользователь все еще может копировать в буфер обмена и перетаскивать текст (если echoMode() равно Normal), но не может редактировать его.

В режиме только-для-чтения, QLineEdit не отображает курсор.

Функции доступа:

bool isReadOnly () const
void setReadOnly ( bool )


### redoAvailable : const bool

Данное свойство сообщает, доступен ли повтор последнего отмененного действия.

Функции доступа:

bool isRedoAvailable () const

#### selectedText : const QString

Данное свойство содержит выделенный текст.

Если ни какой текст не выделен, то значением свойства является пустая строка.

Функции доступа:

QString selectedText () const


#### text : QString

Данное свойство содержит редактируемый текст.

Установка данного свойства отменяет выделение текста, очищает историю отмены/повтора, устанавливает курсор в конец строки и устанавливает свойство modified в false. При вставке текста с помощью setText() не проверяется соответствие устанавливаемого текста заданному условию не текст.

Текст обрезается в соответствии с maxLength().

Функции доступа:

QString text () const
void setText ( const QString & )


### undoAvailable : const bool

Данное свойство сообщает, доступна ли отмена последнего действия.

Функции доступа:

bool isUndoAvailable () const
Описание Функций-Членов

QLineEdit::QLineEdit ( QWidget * parent = 0 )

Создает не заполненный текстом редактор.

Максимальная длина текста установлена равной 32767 символам.

Аргумент parent передается в конструктор QWidget.


QLineEdit::QLineEdit ( const QString & contents, QWidget * parent = 0 )

Создает редактор, содержащий текст contents.

Курсор устанавливается в конец строки, а максимальная длина текста устанавливается равной 32767 символам.

Аргумент parent передается в конструктор QWidget.


QLineEdit::~QLineEdit ()

Разрушает редактор.

void QLineEdit::backspace ()

Если никакой текст не выделен, но символ, стоящий слева от курсора, удаляется, а курсор перемещается на одну позицию левее. Если есть выделенный текст, то курсор перемещается в начало выделенного текста, а выделенный текст удаляется.

void QLineEdit::clear ()   [slot]

Удаляет текст, содрежащийся в редакторе.

void QLineEdit::contextMenuEvent ( QContextMenuEvent * event )   [virtual protected]

Отображает стандартное контекстное меню, созданное с помощью createStandardContextMenu().

Если Вы не хотите, чтобы редактор имел контекстное меню, то можете установить contextMenuPolicy в Qt::NoContextMenu. Если Вы хотите настроить контекстное меню, то должны заново реализовать данную функцию. Если Вы хотите расширить стандартное контекстное меню заново реализовав данную функцию, то вызовите createStandardContextMenu() и дополните возвращенное меню.

    void LineEdit::contextMenuEvent(QContextMenuEvent *event)
    {
        QMenu *menu = createStandardContextMenu();
        menu->addAction(tr("My Menu Item"));
        //...
        menu->exec(event->globalPos());
        delete menu;
    }
Параметр event используется для определения позиции, в которой находится указатель мыши во время создания сообщения контестного меню.

Заново реализовано по отношению к QWidget.

void QLineEdit::copy () const   [slot]

Копирует выделенный текст, если таковой есть и если echoMode() равно Normal, в буфер обмена.

QMenu * QLineEdit::createStandardContextMenu ()

Данная функция создает стандартное контекстное меню отображаемое при щелчке на редакторе правой кнопкой мыши. По умолчанию вызывается обработчиком сообщений contextMenuEvent(). Всплывающее меню передается вызывающему по значению.

void QLineEdit::cursorBackward ( bool mark, int steps = 1 )

Перемещает курсор назад на steps символов. Если mark равно true, то каждый символ, через который перемещается курсор, выделяется; если mark равно false то выделение с текста снимается.

void QLineEdit::cursorForward ( bool mark, int steps = 1 )

Перемещает курсор вперед на steps символов. Если mark равно true, то каждый символ, через который перемещается курсор, выделяется; если mark равно false то выделение с текста снимается.

int QLineEdit::cursorPositionAt ( const QPoint & pos )

Возвращает позицию, которую мог бы занимать курсор, находясь в точке pos.

void QLineEdit::cursorPositionChanged ( int old, int new )   [signal]

Данный сигнал испускается всякий раз при перемещении курсора. Предыдущая позиция курсора помещается в old, а новая позиция - в new.

void QLineEdit::cursorWordBackward ( bool mark )

Перемещает курсор на одно слово назад. Если mark равно true, то слово выделяется.


void QLineEdit::cursorWordForward ( bool mark )

Перемещает курсор на одно слово вперед. Если mark равно true, то слово выделяется.


void QLineEdit::cut ()   [slot]

Копирует выделенный текст, если таковой имеется и если echoMode() равно Normal, в буфер обмена и удаляет его.

Если текущее условие на текст отвергает удаление выделенного текста, то cut() будет скопирован, но не удален.


void QLineEdit::del ()

Если нет выделенного текста, то удаляется символ, стоящий справа от курсора. Если есть выделенный текст, то курсор перемещается в начало выделенного текста, а выделенный текст удаляется.


void QLineEdit::deselect ()

Снимает выделение с выделенным текстом.


void QLineEdit::editingFinished ()   [signal]

Данный сигнал испускается при нажатии клавиши Return или Enter или когда редактор теряет фокус. Обратите внимание, что если для редактора установлены validator() или inputMask() и нажата клавиша enter/return, то сигнал editingFinished() будет испущен только в том случае, если inputMask() и validator() для введенног текста возвратят QValidator::Acceptable.

void QLineEdit::end ( bool mark )

Перемещает курсор в конец редактируемой строки (если он уже не там). Если mark равно true, то текст от текущего положения до конца строки добавляется к выделенному; в противном случае, выделение с выделенного текста снимается (если курсор перемещается).


void QLineEdit::home ( bool mark )

Перемещает курсор в начало редактируемой строки (если он уже не там). Если mark равно true, то текст от начала строки до текущего положения добавляется к выделенному; в противном случае, выделение с выделенного текста снимается (если курсор перемещается).


void QLineEdit::insert ( const QString & newText )

Удаляет выделенный текст, вставляет новый текст newText и проверяет соответствие результата на соответствие установленному условию. Если новый текст соответствует условию, то он становится новым содержимым редактора.


void QLineEdit::keyPressEvent ( QKeyEvent * event )   [virtual protected]

Преобразует полученное сообщение клавиатуры event в действие редактора.

Если нажата клавиша Return или Enter и текущий текст соответствует установленному условию (или может быть сделан соответствующим объектом условия), то испускается сигнал returnPressed().

Список ействий клавиш, заданные по умолчанию, приведен в подробном описании класса.

Повторно реализовано по отношению к QWidget.

QSize QLineEdit::minimumSizeHint () const   [virtual]

Возвращает минимальный размер редактора.

Ширина в возвращаемом значении достаточна для размещения по крайней мере одного символа.

Повторно реализовано по отношению к QWidget.

void QLineEdit::paste ()   [slot]

Вставляет текст из буфера обмена в позицию курсора, удаляет выделенный текст. Поддреживается редактором, если он находится не в режиме только-для-чтения.

Если полученный результат не соответствует установленному условию (validator), ничего не происходит.


void QLineEdit::redo ()   [slot]

Повторяет последнюю отмененную операцию если это возможно (свойство redoАvailable).

void QLineEdit::returnPressed ()   [signal]

Данный сигнал испускается при нажатии клавиши Return или Enter. Обратите внимание, что если для редактора установлены validator() или inputMask(), то сигнал returnPressed() испускается только в том случае, если inputMask() и validator() для введенного текста возвращают QValidator::Acceptable.

void QLineEdit::selectAll ()   [slot]

Выделяет весь текст (т.е. подсвечивает его) и перемещает курсор в конец строки. Это полезно при вставке значения по умолчанию, так как, если пользователь станет вводить текст в виджет, выделенный текст будет удален.


void QLineEdit::selectionChanged ()   [signal]

Данный сигнал испускается всякий раз, когда изменяется выделение текста в редакторе.


int QLineEdit::selectionStart () const

selectionStart() возвращает индекс первого выделенного символа или, если никакой текст не выделен, -1.


void QLineEdit::setSelection ( int start, int length )

Выделяет фрагмент текста начинающийся в позиции start и имеющий длину length символов. Допускается отрицательное значение длины.


void QLineEdit::setValidator ( const QValidator * v )

Устанавливает для редактора условие на вводимый текст v. Это позволяет устанавливать любые ограничения на вводимый текст.

Если v == 0, то setValidator() удаляет установленное условие на текст. Изначально для редактора не установлено никакое условие на текст (т.е. позволяется вводить любой текст длиной не более maxLength() символов).


QSize QLineEdit::sizeHint () const   [virtual]

Возвращает рекомендуемый виджету размер.

Ширина, возвращаемая в пикселях, обычно достаточна для размещения 15-20 символам.

Повторно реализовано по отношению к QWidget.

void QLineEdit::textChanged ( const QString & text )   [signal]

Данный сигнал испускается всякий раз при изменении текста. Аргумент text содержит новый текст.

В отличие от textEdited(), данный сигнал испускается даже тогда, когда текст в редакторе устанавливается программно, с помощью setText().

void QLineEdit::textEdited ( const QString & text )   [signal]

Данный сигнал испускается всякий раз при редактировании текста. Аргумент text содрежит новый текст.

В отличие от textChanged(), данный сигнал не испускается при программной установке текста с помощью setText().

void QLineEdit::undo ()   [slot]

Отменяет последнюю операцию, если отмена возможна (свойство undoAvailable. Снимает выделение текста и переносит начало выделения текста к текущему положению курсора.

const QValidator * QLineEdit::validator () const

Возвращает указатель на текущее условие на вводимый текст или, если таковое условие на установлено, 0.

1_0.py

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Example, self).__init__(parent)

        self.initUI()


    def initUI(self):

        self.lbl = QtGui.QLabel(self)
        qle = QtGui.QLineEdit(self)

        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()


    def onChanged(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```
Этот пример показывает виджет строки редактирования и метку. Текст, который мы вбиваем в строку редактирования, немедленно отображается в виджете метки.
```
qle = QLineEdit(self)
```
Создается виджет QLineEdit.
```
qle.textChanged[str].connect(self.onChanged)
```
Если текст в виджете редактирования строки меняется, мы вызываем метод onChanged().
```
def onChanged(self, text):

    self.lbl.setText(text)
    self.lbl.adjustSize()
```
Внутри метода onChanged, мы устанавливаем напечатанный текст в виджет метки. Мы вызываем метод adjustSize(), чтобы менять размер метки соответственно длине текста.


### setText
```
    def pointClicked(self):
        if self.waitingForOperand:
            self.display.setText('0')

        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.waitingForOperand = False
```
### text

```

    def changeSignClicked(self):
        text = self.display.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(text)
```
2.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

"""
import sys, os
from PyQt4 import QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''

        self.sumInMemory = 0.0
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.waitingForOperand = True

        self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                    self.digitClicked))

        self.pointButton = self.createButton(".", self.pointClicked)
        self.changeSignButton = self.createButton("\261",
                self.changeSignClicked)


        self.divisionButton = self.createButton("\367",
                self.multiplicativeOperatorClicked)
        self.multiplicatButton = self.createButton("\327",
                self.multiplicativeOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)


        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 6)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.pointButton, 5, 2)
        mainLayout.addWidget(self.changeSignButton, 5, 3)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.multiplicatButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.equalButton, 5, 5)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))

    def multiplicativeOperatorClicked(self):
        pass

    def additiveOperatorClicked(self):
        pass

    def equalClicked(self):
        pass

    def pointClicked(self):
        if self.waitingForOperand:
            self.display.setText('0')

        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.waitingForOperand = False

    def changeSignClicked(self):
        text = self.display.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(text)

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calculator()
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()

```

## def calculate(self, rightOperand, pendingOperator)
```
    def abortOperation(self):
        self.clearAll()
        self.display.setText("####")

    def equalClicked(self):
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True
```


```
    self.pendingAdditiveOperator = ''
    self.pendingMultiplicativeOperator = ''
```

```
    def additiveOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True
```

```

    def calculate(self, rightOperand, pendingOperator):
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
        elif pendingOperator == "\327":
            self.factorSoFar *= rightOperand
        elif pendingOperator == "\367":
            if rightOperand == 0.0:
                return False

            self.factorSoFar /= rightOperand

        return True
```
3.py

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

"""
import sys, os
from PyQt4 import QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size



class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''

        self.sumInMemory = 0.0
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.waitingForOperand = True

        self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                    self.digitClicked))

        self.pointButton = self.createButton(".", self.pointClicked)
        self.changeSignButton = self.createButton("\261",
                self.changeSignClicked)


        self.divisionButton = self.createButton("\367",
                self.multiplicativeOperatorClicked)
        self.multiplicatButton = self.createButton("\327",
                self.multiplicativeOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)


        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 6)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.pointButton, 5, 2)
        mainLayout.addWidget(self.changeSignButton, 5, 3)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.multiplicatButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.equalButton, 5, 5)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))

    def multiplicativeOperatorClicked(self):
        pass

    def additiveOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True


    def equalClicked(self):
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True

    def pointClicked(self):
        if self.waitingForOperand:
            self.display.setText('0')

        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.waitingForOperand = False

    def changeSignClicked(self):
        text = self.display.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(text)

    def calculate(self, rightOperand, pendingOperator):
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
        elif pendingOperator == "\327":
            self.factorSoFar *= rightOperand
        elif pendingOperator == "\367":
            if rightOperand == 0.0:
                return False

            self.factorSoFar /= rightOperand

        return True

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calculator()
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()

```

4.py

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

"""
import sys, os
from PyQt4 import QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size



class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''

        self.sumInMemory = 0.0
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.waitingForOperand = True

        self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                    self.digitClicked))

        self.pointButton = self.createButton(".", self.pointClicked)
        self.changeSignButton = self.createButton("\261",
                self.changeSignClicked)


        self.divisionButton = self.createButton("\367",
                self.multiplicativeOperatorClicked)
        self.multiplicatButton = self.createButton("\327",
                self.multiplicativeOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)


        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 6)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.pointButton, 5, 2)
        mainLayout.addWidget(self.changeSignButton, 5, 3)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.multiplicatButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.equalButton, 5, 5)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))

    def multiplicativeOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
        else:
            self.factorSoFar = operand

        self.pendingMultiplicativeOperator = clickedOperator
        self.waitingForOperand = True

    def additiveOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True


    def equalClicked(self):
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True

    def pointClicked(self):
        if self.waitingForOperand:
            self.display.setText('0')

        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.waitingForOperand = False

    def changeSignClicked(self):
        text = self.display.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(text)

    def calculate(self, rightOperand, pendingOperator):
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
        elif pendingOperator == "\327":
            self.factorSoFar *= rightOperand
        elif pendingOperator == "\367":
            if rightOperand == 0.0:
                return False

            self.factorSoFar /= rightOperand

        return True

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calculator()
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()

```

Backspace Clear "Clear All
```


        self.backspaceButton = self.createButton("Backspace",
                self.backspaceClicked)
        self.clearButton = self.createButton("Clear", self.clear)
        self.clearAllButton = self.createButton("Clear All", self.clearAll)


        mainLayout.addWidget(self.backspaceButton, 1, 0, 1, 2)
        mainLayout.addWidget(self.clearButton, 1, 2, 1, 2)
        mainLayout.addWidget(self.clearAllButton, 1, 4, 1, 2)

        def backspaceClicked(self):
        if self.waitingForOperand:
            return

        text = self.display.text()[:-1]
        if not text:
            text = '0'
            self.waitingForOperand = True

        self.display.setText(text)

    def clear(self):
        if self.waitingForOperand:
            return

        self.display.setText('0')
        self.waitingForOperand = True

    def clearAll(self):
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''
        self.display.setText('0')
        self.waitingForOperand = True

```
5.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

"""
import sys, os
from PyQt4 import QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size



class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''

        self.sumInMemory = 0.0
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.waitingForOperand = True

        self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                    self.digitClicked))

        self.pointButton = self.createButton(".", self.pointClicked)
        self.changeSignButton = self.createButton("\261",
                self.changeSignClicked)

        self.backspaceButton = self.createButton("Backspace",
                self.backspaceClicked)
        self.clearButton = self.createButton("Clear", self.clear)
        self.clearAllButton = self.createButton("Clear All", self.clearAll)


        self.divisionButton = self.createButton("\367",
                self.multiplicativeOperatorClicked)
        self.multiplicatButton = self.createButton("\327",
                self.multiplicativeOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)


        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 6)
        mainLayout.addWidget(self.backspaceButton, 1, 0, 1, 2)
        mainLayout.addWidget(self.clearButton, 1, 2, 1, 2)
        mainLayout.addWidget(self.clearAllButton, 1, 4, 1, 2)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.pointButton, 5, 2)
        mainLayout.addWidget(self.changeSignButton, 5, 3)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.multiplicatButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.equalButton, 5, 5)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))

    def multiplicativeOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
        else:
            self.factorSoFar = operand

        self.pendingMultiplicativeOperator = clickedOperator
        self.waitingForOperand = True

    def additiveOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True


    def equalClicked(self):
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True

    def pointClicked(self):
        if self.waitingForOperand:
            self.display.setText('0')

        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.waitingForOperand = False

    def changeSignClicked(self):
        text = self.display.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(text)

    def backspaceClicked(self):
        if self.waitingForOperand:
            return

        text = self.display.text()[:-1]
        if not text:
            text = '0'
            self.waitingForOperand = True

        self.display.setText(text)

    def clear(self):
        if self.waitingForOperand:
            return

        self.display.setText('0')
        self.waitingForOperand = True

    def clearAll(self):
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''
        self.display.setText('0')
        self.waitingForOperand = True

    def calculate(self, rightOperand, pendingOperator):
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
        elif pendingOperator == "\327":
            self.factorSoFar *= rightOperand
        elif pendingOperator == "\367":
            if rightOperand == 0.0:
                return False

            self.factorSoFar /= rightOperand

        return True

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calculator()
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()

```
unaryOperatorClicked
```
        self.squareRootButton = self.createButton("Sqrt",
                self.unaryOperatorClicked)
        self.powerButton = self.createButton("x\262",
                self.unaryOperatorClicked)
        self.reciprocalButton = self.createButton("1/x",
                self.unaryOperatorClicked)
        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout.addWidget(self.squareRootButton, 2, 5)
        mainLayout.addWidget(self.powerButton, 3, 5)
        mainLayout.addWidget(self.reciprocalButton, 4, 5)
        mainLayout.addWidget(self.equalButton, 5, 5)

    def unaryOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if clickedOperator == "Sqrt":
            if operand < 0.0:
                self.abortOperation()
                return

            result = math.sqrt(operand)
        elif clickedOperator == "x\262":
            result = math.pow(operand, 2.0)
        elif clickedOperator == "1/x":
            if operand == 0.0:
                self.abortOperation()
                return

            result = 1.0 / operand

        self.display.setText(str(result))
        self.waitingForOperand = True

mport math
```
6.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

""" # Хорошо написанная документация на модуль, может быть отображена при help(имя_модуля).

import sys, os
import math
from PyQt4 import QtGui, QtCore # Из модуля PyQt4 импортируем подмодуль QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size



class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''

        self.sumInMemory = 0.0
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.waitingForOperand = True

        self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                    self.digitClicked))

        self.pointButton = self.createButton(".", self.pointClicked)
        self.changeSignButton = self.createButton("\261",
                self.changeSignClicked)

        self.backspaceButton = self.createButton("Backspace",
                self.backspaceClicked)
        self.clearButton = self.createButton("Clear", self.clear)
        self.clearAllButton = self.createButton("Clear All", self.clearAll)


        self.divisionButton = self.createButton("\367",
                self.multiplicativeOperatorClicked)
        self.multiplicatButton = self.createButton("\327",
                self.multiplicativeOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)


        self.squareRootButton = self.createButton("Sqrt",
                self.unaryOperatorClicked)
        self.powerButton = self.createButton("x\262",
                self.unaryOperatorClicked)
        self.reciprocalButton = self.createButton("1/x",
                self.unaryOperatorClicked)
        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        # Создаём виждет.
        mainLayout.addWidget(self.display, 0, 0, 1, 6)
        mainLayout.addWidget(self.backspaceButton, 1, 0, 1, 2)
        mainLayout.addWidget(self.clearButton, 1, 2, 1, 2)
        mainLayout.addWidget(self.clearAllButton, 1, 4, 1, 2)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.pointButton, 5, 2)
        mainLayout.addWidget(self.changeSignButton, 5, 3)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.multiplicatButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)

        
        mainLayout.addWidget(self.squareRootButton, 2, 5)
        mainLayout.addWidget(self.powerButton, 3, 5)
        mainLayout.addWidget(self.reciprocalButton, 4, 5)
        mainLayout.addWidget(self.equalButton, 5, 5)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")
        # Заголовок окна, отображается в рамке и панели задач.
    
    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))

    def unaryOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if clickedOperator == "Sqrt":
            if operand < 0.0:
                self.abortOperation()
                return

            result = math.sqrt(operand)
        elif clickedOperator == "x\262":
            result = math.pow(operand, 2.0)
        elif clickedOperator == "1/x":
            if operand == 0.0:
                self.abortOperation()
                return

            result = 1.0 / operand

        self.display.setText(str(result))
        self.waitingForOperand = True

    def multiplicativeOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
        else:
            self.factorSoFar = operand

        self.pendingMultiplicativeOperator = clickedOperator
        self.waitingForOperand = True

    def additiveOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True


    def equalClicked(self):
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True

    def pointClicked(self):
        if self.waitingForOperand:
            self.display.setText('0')

        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.waitingForOperand = False

    def changeSignClicked(self):
        text = self.display.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(text)

    def backspaceClicked(self):
        if self.waitingForOperand:
            return

        text = self.display.text()[:-1]
        if not text:
            text = '0'
            self.waitingForOperand = True

        self.display.setText(text)

    def clear(self):
        if self.waitingForOperand:
            return

        self.display.setText('0')
        self.waitingForOperand = True

    def clearAll(self):
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''
        self.display.setText('0')
        self.waitingForOperand = True

    def calculate(self, rightOperand, pendingOperator):
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
        elif pendingOperator == "\327":
            self.factorSoFar *= rightOperand
        elif pendingOperator == "\367":
            if rightOperand == 0.0:
                return False

            self.factorSoFar /= rightOperand

        return True

def main():
    # Для удобства работы, определим главную функцию нашего примера:
    app = QtGui.QApplication(sys.argv)
    # Создаём класс QApplication, который управляет
    # всем приложением на PyQt4.
    calc = Calculator()
    sys.exit(calc.exec_())
    # app.exec_() содержит в себе главный цикл обработки событий бибиотеки
    # PyQt4, который завершится, когда пользователь закроет окно или мы
    # своей программе вызовем функцию завершения этого цикла. Только после
    # этого прозойдёт выход из питона с помощью функции sys.exit.


if __name__ == '__main__':
    # Если файл запущен как программа (а не импортирован как модуль),
    main()                 # вызовем фукнцийю main.
    

```
clearMemoryButton

```
        self.clearMemoryButton = self.createButton("MC", self.clearMemory)
        self.readMemoryButton = self.createButton("MR", self.readMemory)
        self.setMemoryButton = self.createButton("MS", self.setMemory)
        self.addToMemoryButton = self.createButton("M+", self.addToMemory)


        mainLayout.addWidget(self.clearMemoryButton, 2, 0)
        mainLayout.addWidget(self.readMemoryButton, 3, 0)
        mainLayout.addWidget(self.setMemoryButton, 4, 0)
        mainLayout.addWidget(self.addToMemoryButton, 5, 0)


   def clearMemory(self):
        self.sumInMemory = 0.0

    def readMemory(self):
        self.display.setText(str(self.sumInMemory))
        self.waitingForOperand = True

    def setMemory(self):
        self.equalClicked()
        self.sumInMemory = float(self.display.text())

    def addToMemory(self):
        self.equalClicked()
        self.sumInMemory += float(self.display.text())

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def abortOperation(self):
        self.clearAll()
        self.display.setText("####")
```
7.py

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

"""
import sys, os
import math
from PyQt4 import QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size



class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''

        self.sumInMemory = 0.0
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.waitingForOperand = True

        self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                    self.digitClicked))

        self.pointButton = self.createButton(".", self.pointClicked)
        self.changeSignButton = self.createButton("\261",
                self.changeSignClicked)

        self.backspaceButton = self.createButton("Backspace",
                self.backspaceClicked)
        self.clearButton = self.createButton("Clear", self.clear)
        self.clearAllButton = self.createButton("Clear All", self.clearAll)


        self.clearMemoryButton = self.createButton("MC", self.clearMemory)
        self.readMemoryButton = self.createButton("MR", self.readMemory)
        self.setMemoryButton = self.createButton("MS", self.setMemory)
        self.addToMemoryButton = self.createButton("M+", self.addToMemory)

        self.divisionButton = self.createButton("\367",
                self.multiplicativeOperatorClicked)
        self.multiplicatButton = self.createButton("\327",
                self.multiplicativeOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)


        self.squareRootButton = self.createButton("Sqrt",
                self.unaryOperatorClicked)
        self.powerButton = self.createButton("x\262",
                self.unaryOperatorClicked)
        self.reciprocalButton = self.createButton("1/x",
                self.unaryOperatorClicked)
        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 6)
        mainLayout.addWidget(self.backspaceButton, 1, 0, 1, 2)
        mainLayout.addWidget(self.clearButton, 1, 2, 1, 2)
        mainLayout.addWidget(self.clearAllButton, 1, 4, 1, 2)

        mainLayout.addWidget(self.clearMemoryButton, 2, 0)
        mainLayout.addWidget(self.readMemoryButton, 3, 0)
        mainLayout.addWidget(self.setMemoryButton, 4, 0)
        mainLayout.addWidget(self.addToMemoryButton, 5, 0)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.pointButton, 5, 2)
        mainLayout.addWidget(self.changeSignButton, 5, 3)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.multiplicatButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)

        
        mainLayout.addWidget(self.squareRootButton, 2, 5)
        mainLayout.addWidget(self.powerButton, 3, 5)
        mainLayout.addWidget(self.reciprocalButton, 4, 5)
        mainLayout.addWidget(self.equalButton, 5, 5)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))

    def unaryOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if clickedOperator == "Sqrt":
            if operand < 0.0:
                self.abortOperation()
                return

            result = math.sqrt(operand)
        elif clickedOperator == "x\262":
            result = math.pow(operand, 2.0)
        elif clickedOperator == "1/x":
            if operand == 0.0:
                self.abortOperation()
                return

            result = 1.0 / operand

        self.display.setText(str(result))
        self.waitingForOperand = True

    def multiplicativeOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
        else:
            self.factorSoFar = operand

        self.pendingMultiplicativeOperator = clickedOperator
        self.waitingForOperand = True

    def additiveOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True


    def equalClicked(self):
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True

    def pointClicked(self):
        if self.waitingForOperand:
            self.display.setText('0')

        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.waitingForOperand = False

    def changeSignClicked(self):
        text = self.display.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(text)

    def backspaceClicked(self):
        if self.waitingForOperand:
            return

        text = self.display.text()[:-1]
        if not text:
            text = '0'
            self.waitingForOperand = True

        self.display.setText(text)

    def clear(self):
        if self.waitingForOperand:
            return

        self.display.setText('0')
        self.waitingForOperand = True

    def clearAll(self):
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''
        self.display.setText('0')
        self.waitingForOperand = True

    def clearMemory(self):
        self.sumInMemory = 0.0

    def readMemory(self):
        self.display.setText(str(self.sumInMemory))
        self.waitingForOperand = True

    def setMemory(self):
        self.equalClicked()
        self.sumInMemory = float(self.display.text())

    def addToMemory(self):
        self.equalClicked()
        self.sumInMemory += float(self.display.text())

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def abortOperation(self):
        self.clearAll()
        self.display.setText("####")


    def calculate(self, rightOperand, pendingOperator):
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
        elif pendingOperator == "\327":
            self.factorSoFar *= rightOperand
        elif pendingOperator == "\367":
            if rightOperand == 0.0:
                return False

            self.factorSoFar /= rightOperand

        return True

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calculator()
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()

```

# Сапёр (игра)

### Принцип игры
Плоское или объёмное игровое поле разделено на смежные ячейки (квадраты, шестиугольники, кубы и т. п.), некоторые из которых «заминированы»; количество «заминированных» ячеек известно. Целью игры является открытие всех ячеек, не содержащих мины.

Игрок открывает ячейки, стараясь не открыть ячейку с миной. Открыв ячейку с миной, он проигрывает. Мины расставляются после первого хода, поэтому проиграть на первом же ходу невозможно. Если под открытой ячейкой мины нет, то в ней появляется число, показывающее, сколько ячеек, соседствующих с только что открытой, «заминировано» (в каждом варианте игры соседство определяется по-своему); используя эти числа, игрок пытается рассчитать расположение мин, однако иногда даже в середине и в конце игры некоторые ячейки всё же приходится открывать наугад. Если под соседними ячейками тоже нет мин, то открывается некоторая «не заминированная» область до ячеек, в которых есть цифры. «Заминированные» ячейки игрок может пометить, чтобы случайно не открыть их. Открыв все «не заминированные» ячейки, игрок выигрывает.

## Оценка сложности поля
Часто сложность поля оценивают с помощью величины 3BV (Bechtel’s Board Benchmark Value). Эта величина численно равна минимальному количеству непосредственных открытий ячеек (в стандартном варианте «Сапёра» открытия ячеек только левой кнопкой мыши, без использования флагов и двойных кликов), необходимому для открытия всего поля. Следует отметить, что эта величина отображает лишь количество определённых действий в идеальном случае при определенной манере игры, а вовсе не трудность расстановки для конкретного игрока.

## Рекорды
В большинстве вариантов игры подсчитывается время решения головоломки, поэтому регистрируются рекорды для стандартных уровней сложности игры. Для серьёзных соревнований используются версии игры, фиксирующие время прохождения с точностью до миллисекунд.

Результат сильно зависит от расположения мин. Теоретически при любых игровых параметрах есть вероятность прохождения одним щелчком. Но практическая реализация генератора случайных комбинаций не позволяет получить слишком простую расстановку на больших досках. Поэтому результаты на уровнях сложности Intermediate и Expert хорошо отражают уровень игрока. В официальных программах установлены ограничители для простых досок по 3bv. В настоящее время они составляют 2 для уровня сложности Beginner, 30 — Intermediate и 100 — Expert. См. также исследование достаточности ныне установленного ограничения для «Профессионала», вызванное результатом Яна Фрейзера.


# Генерация случайных чисел (модуль random)
«Генерация случайных чисел слишком важна, чтобы оставлять её на волю случая»

—  Роберт Кавью

Python порождает случайные числа на основе формулы, так что они не на самом деле случайные, а, как говорят, псевдослучайные. Этот способ удобен для большинства приложений (кроме онлайновых казино).

Модуль random позволяет генерировать случайные числа. Прежде чем использовать модуль, необходимо подключить его с помощью инструкции:
```
import random
random.random
random.random() — возвращает псевдослучайное число от 0.0 до 1.0
```

### random.seed
random.seed(<Параметр>) — настраивает генератор случайных чисел на новую последовательность. По умолчанию используется системное время. Если значение параметра будет одиноким, то генерируется одинокое число:

```
   random.seed(20)
   random.random()
```

### random.uniform
random.uniform(<Начало>, <Конец>) — возвращает псевдослучайное вещественное число в диапазоне от <Начало> до <Конец>:

```
   random.uniform(0, 20)
   15.330185127252884
   random.uniform(0, 20)
   18.092324756265473
```
## random.randint
random.randint(<Начало>, <Конец>) — возвращает псевдослучайное целое число в диапазоне от <Начало> до <Конец>:

```
    random.randint(1,27)
    9
    random.randint(1,27)
    22
```
## random.choince
random.choince(<Последовательность>) — возвращает случайный элемент из любой последовательности (строки, списка, кортежа):

```

    random.choice('Chewbacca')
    'h'
    random.choice([1,2,'a','b'])
    2
    random.choice([1,2,'a','b'])
    'a'
```
## random.randrange
random.randrange(<Начало>, <Конец>, <Шаг>) — возвращает случайно выбранное число из последовательности.

### random.shuffle
random.shuffle(<Список>) — перемешивает последовательность (изменяется сама последовательность). Поэтому функция не работает для неизменяемых объектов.

```
    List = [1,2,3,4,5,6,7,8,9]
    List
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(List)
    List
    [6, 7, 1, 9, 5, 8, 3, 2, 4]

```

# Вероятностные распределения
random.triangular(low, high, mode) — случайное число с плавающей точкой, low ≤ N ≤ high. Mode - распределение.

random.betavariate(alpha, beta) — бета-распределение. alpha>0, beta>0. Возвращает от 0 до 1.

random.expovariate(lambd) — экспоненциальное распределение. lambd равен 1/среднее желаемое. Lambd должен быть отличным от нуля. Возвращаемые значения от 0 до плюс бесконечности, если lambd положительно, и от минус бесконечности до 0, если lambd отрицательный.

random.gammavariate(alpha, beta) — гамма-распределение. Условия на параметры alpha>0 и beta>0.

random.gauss(значение, стандартное отклонение) — распределение Гаусса.

random.lognormvariate(mu, sigma) — логарифм нормального распределения. Если взять натуральный логарифм этого распределения, то вы получите нормальное распределение со средним mu и стандартным отклонением sigma. mu может иметь любое значение, и sigma должна быть больше нуля.

random.normalvariate(mu, sigma) — нормальное распределение. mu - среднее значение, sigma - стандартное отклонение.

random.vonmisesvariate(mu, kappa) — mu - средний угол, выраженный в радианах от 0 до 2π, и kappa - параметр концентрации, который должен быть больше или равен нулю. Если каппа равна нулю, это распределение сводится к случайному углу в диапазоне от 0 до 2π.

random.paretovariate(alpha) — распределение Парето.

random.weibullvariate(alpha, beta) — распределение Вейбулла.

## Генерация произвольного пароля

Хороший пароль должен быть произвольным и состоять минимум из 6 символов, в нём должны быть цифры, строчные и прописные буквы. Приготовить такой пароль можно по следующему рецепту:
passwd.py
```
    import random
    # Щепотка цифр
    str1 = '123456789'
    # Щепотка строчных букв
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    # Щепотка прописных букв. Готовится преобразованием str2  в верхний регистр.
    str3 = str2.upper()
    print(str3)
    # Выведет: 'QWERTYUIOPASDFGHJKLZXCVBNM'

    # Соединяем все строки в одну
    str4 = str1+str2+str3
    print(str4)
    # Выведет: '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

    # Преобразуем получившуюся строку в список
    ls = list(str4)
    # Тщательно перемешиваем список
    random.shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    psw = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов
    print(psw)
    # Выведет: '1t9G4YPsQ5L7'
```
Этот же скрипт можно записать всего в две строки:
```

    import random
    print(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxc
vbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(12)]))
```
Данная команда является краткой записью цикла for, вместо неё можно было написать так:
```
    import random
    psw = '' # предварительно создаем переменную psw
    for x in range(12):
        psw = psw + random.choice(list('123456789qwertyuiopasdfgh
jklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    print(psw)
    # Выведет: Ci7nU6343YGZ
```
Данный цикл повторяется 12 раз и на каждом круге добавляет к строке psw произвольно выбранный элемент из списка.


# QTimer
```
# call f() in 3 seconds
QTimer.singleShot(3000, f)
The sec­ond is this:

# Create a QTimer
timer = QTimer()
# Connect it to f
timer.timeout.connect(f)
# Call f() every 5 seconds
timer.start(5000)
```



pro­ces­­sEv­ents

```

def f():
    try:
        # Do things
    finally:
        QTimer.singleShot(5000, f)

f()
```

time.py
```
```
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
```


```


t1.py
```
import sys
from PyQt4 import QtGui, QtCore
 
from time import strftime
 
 
class Main(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
 
    def initUI(self):
 
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)
        self.timer.start(1000)
 
        self.lcd = QtGui.QLCDNumber(self)
        self.lcd.display(strftime("%H"+":"+"%M"))
 
        self.setCentralWidget(self.lcd)
 
#---------Window settings --------------------------------
         
        self.setGeometry(300,300,250,100)
        self.setWindowTitle("Clock")
 
#-------- Slots ------------------------------------------
 
    def Time(self):
        self.lcd.display(strftime("%H"+":"+"%M"))
         
def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
```

t2.py
```
import sys
from PyQt4 import QtGui, QtCore
 
from time import strftime
 
var = True
 
class Main(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
 
    def initUI(self):
 
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.Time)
#Reduced update time to fasten the change from w/ secs to w/o secs
        timer.start(10)
 
        self.lcd = QtGui.QLCDNumber(self)
        self.lcd.resize(250,100)
         
#Added self.lcd.move and moved the clock 30px down to make space for buttons
         
        self.lcd.move(0,30)
        self.lcd.display(strftime("%H"+":"+"%M"))
 
        self.r1 = QtGui.QRadioButton("Hide seconds",self)
        self.r1.move(10,0)
        self.r2 = QtGui.QRadioButton("Show seconds",self)
        self.r2.move(110,0)
 
        self.r1.toggled.connect(self.woSecs)
        self.r2.toggled.connect(self.wSecs)
 
#---------Window settings --------------------------------
 
# Expanded window height by 30px
 
        self.setGeometry(300,300,250,130)
        self.setWindowTitle("Clock")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()
 
#-------- Slots ------------------------------------------
 
    def Time(self):
        global var
        if var == True:
            self.lcd.display(strftime("%H"+":"+"%M"))
        elif var == False:
            self.lcd.display(strftime("%H"+":"+"%M"+":"+"%S"))
 
    def wSecs(self):
        global var
        var = False
         
        self.resize(375,130)
        self.lcd.resize(375,100)
        self.lcd.setDigitCount(8)
 
    def woSecs(self):
        global var
        var = True
         
        self.resize(250,130)
        self.lcd.resize(250,100)
        self.lcd.setDigitCount(5)
 
     
def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
```


