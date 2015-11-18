# 21v-python

Python и пакеты для машинного обучения
======================================

Python является популярным языком программирования в научных, а также финансовых кругах. Ряд библиотек для научных вычислений, таких как SciPy и NumPy позволяют выполнять операции над векторами и матрицами. Это также делает код еще более читаемым и позволяет писать код, который выглядит как выражения линейной алгебры. Кроме того, научные библиотеки SciPy и NumPy скомпилированы, используя языки низкого уровня (С и Fortran), что делает делает вычисления при использовании этих инструментов значительно быстрее.

Научные инструменты Python отлично работают в связке с графическим инструментом под названием Matplotlib. Matplotlib может строить двухмерные и трехмерные графики и может работать с большинством типов построений, обычно используемых в научном сообществе.

Новый модуль Python, под называнием Pylab, стремится объединить возможности NumPy, SciPy, и Matplotlib в одной среде и установке. На сегодняшний день пакет Pylab пока еще находится в стадии разработки, но за ним большое будущее.


NumPy 
======

NumPy является основным пакетом для научных вычислений в Python. NumPy является расширением языка программирования Python, добавляющим поддержку больших многомерных массивов и матриц, вместе с большой библиотекой высокоуровневых математических функций для работы с этими массивами. Предшественник NumPy, пакет Numeric, был первоначально создан Джимом Хаганином при участии ряда других разработчиков. В 2005 году Трэвис Олифант создал NumPy путем включения функций конкурирующего пакета Numarray в Numeric, произведя при этом обширные изменения.

Сайт пакета: www.numpy.org

Для установки в Терминале Linux выполняем:
```
sudo apt-get update
sudo apt-get install python-numpy
```

Пример использования NumPy, который формирует одномерный вектор из 12 чисел от 1 до 12 и преобразует его в трехмерную матрицу:
1.py:
-----
```
from numpy import *
 
a = arange(12)
a = a.reshape(3,2,2)
print a
```

Интерфейс PyCharm
==================

SciPy
------

SciPySciPy — это open-source библиотека с открытым исходным кодом для научных вычислений. Для работы SciPy требуется, чтобы предварительно был установлен NumPy, обеспечивающий удобные и быстрые операции с многомерными массивами. Библиотека SciPy работает с массивами NumPy, и предоставляет множество удобных и эффективных  вычислительных процедур, например, для численного интегрирования и оптимизации. NumPy и SciPy просты в использовании, но достаточно мощные для проведения различных научных и технических вычислений.

Сайт библиотеки: www.scipy.org

Для установки библиотеки SciPy в Linux, выполняем в терминале:

```
sudo apt-get update
sudo apt-get install python-scipy
```
Пример кода для поиска экстремума функции. Результат отображается используя пакет matplotlib.

scipy/1.py:
-----------
```
import numpy as np
from scipy import special, optimize
import matplotlib.pyplot as plt
 
f = lambda x: -special.jv(3, x)
sol = optimize.minimize(f, 1.0)
x = np.linspace(0, 10, 5000)
plt.plot(x, special.jv(3, x), '-', sol.x, -sol.fun, 'o')
plt.show()
```

SciPy
=====


Pandas
=======

Пакет Pandaspandas — это пакет Python, предназначенный для обеспечения быстрыми, гибкими, и выразительными структурами данных, упрощающими работу с «относительными» или «помечеными» данными простым и интуитивно понятным способом. pandas стремится стать основным высокоуровневым строительным блоком для проведения в Python практического анализа данных, полученных из реального мира. Кроме того, этот пакет претендует стать самым мощным и гибким open-source инструментом для анализа/обработки данных, доступным в любом языке программирования.

Pandas хорошо подходит для работы с различными типами данных:

Табличные данные со столбцами различных типов, как в таблицах SQL или Excel.
Упорядоченными и неупорядоченными данными (не обязательно с постоянной частотой) временных рядов.
Произвольными матричными данными (однородными или разнородными) с помеченными строками и столбцами.
Любыми другими формами наборов данных наблюдений, либо статистических данных. Данные на самом деле не требуют обязательного наличия метки для того, чтобы быть помещенными в структуру данных pandas.

Для установки пакета pandas выполняем в Терминале Linux:

```
sudo apt-get update
sudo apt-get install python-pandas
```
Пример кода, преобразующий одномерный массив в структуру данных pandas:
pandas/1.py:
------------
```

import pandas as pd
import numpy as np
 
values = np.array([2.0, 1.0, 5.0, 0.97, 3.0, 10.0, 0.0599, 8.0])
ser = pd.Series(values)
print ser
```

matplotlib
===========
matplotlib является библиотекой графических построений для языка программирования Python и его расширения вычислительной математики NumPy. Библиотека обеспечивает объектно-ориентированный API для встраивания графиков в приложения, используя инструменты GUI общего назначения, такие как WxPython, Qt, или GTK+. Существует также процедурный pylab-интерфейс напоминающий MATLAB. SciPy использует matplotlib.

Сайт библиотеки: matplotlib.org

Для установки библиотеки matpoltlib в Linux выполните следующие команды:

```
sudo apt-get update
sudo apt-get install python-matplotlib
```
Пример гистограммы matplotlib:
matplotlib/histo.py:
--------------------
```
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
 
# example data
mu = 100 # mean of distribution
sigma = 15 # standard deviation of distribution
x = mu + sigma * np.random.randn(10000)
 
num_bins = 50
# the histogram of the data
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
 
# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
```

Pyplot 
======

matplotlib/1.py:
-----------------
```
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()

```

plot():
-------

matplotlib/2.py:
-----------------
```
import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
```

plotting several lines with different format styles in one command using arrays.
---------------------------------------------------------------------------------

matplotlib/3.py:
-----------------
```
import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```

Working with multiple figures and axes
--------------------------------------

matplotlib/pyplot_two_subplots.py:
----------------------------------
```
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
```


Working with text
-----------------
matplotlib/pyplot_text.py:
----------------------------------
```
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
```

Annotating text
----------------
matplotlib/pyplot_annotate.py:
----------------------------------
```
import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.ylim(-2,2)
plt.show()
```

plt.xscale(‘log’)
-----------------

matplotlib/pyplot_text.py:
----------------------------------
```

import numpy as np
import matplotlib.pyplot as plt

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure(1)

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.05)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(223)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)

plt.show()
```

matplotlib/pyplot_text.py:
----------------------------------
```

import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(10))
ax.set_yticks((2,5,7))
labels = ax.set_yticklabels(('really, really, really', 'long', 'labels'))

def on_draw(event):
   bboxes = []
   for label in labels:
       bbox = label.get_window_extent()
       # the figure transform goes from relative coords->pixels and we
       # want the inverse of that
       bboxi = bbox.inverse_transformed(fig.transFigure)
       bboxes.append(bboxi)

   # this is the bbox that bounds all the bboxes, again in relative
   # figure coords
   bbox = mtransforms.Bbox.union(bboxes)
   if fig.subplotpars.left < bbox.width:
       # we need to move it over
       fig.subplots_adjust(left=1.1*bbox.width) # pad a little
       fig.canvas.draw()
   return False

fig.canvas.mpl_connect('draw_event', on_draw)

plt.show()
```

Configure the tick linewidths
-----------------------------

matplotlib/pyplot_text.py:
----------------------------------
```

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(10))

for line in ax.get_xticklines() + ax.get_yticklines():
    line.set_markersize(10)

plt.show()
```

Align my ylabels across multiple subplots
-----------------------------------------

matplotlib/hires.py:
----------------------------------
```

import numpy as np
import matplotlib.pyplot as plt

box = dict(facecolor='yellow', pad=5, alpha=0.2)

fig = plt.figure()
fig.subplots_adjust(left=0.2, wspace=0.6)


ax1 = fig.add_subplot(221)
ax1.plot(2000*np.random.rand(10))
ax1.set_title('ylabels not aligned')
ax1.set_ylabel('misaligned 1', bbox=box)
ax1.set_ylim(0, 2000)
ax3 = fig.add_subplot(223)
ax3.set_ylabel('misaligned 2',bbox=box)
ax3.plot(np.random.rand(10))


labelx = -0.3  # axes coords

ax2 = fig.add_subplot(222)
ax2.set_title('ylabels aligned')
ax2.plot(2000*np.random.rand(10))
ax2.set_ylabel('aligned 1', bbox=box)
ax2.yaxis.set_label_coords(labelx, 0.5)
ax2.set_ylim(0, 2000)

ax4 = fig.add_subplot(224)
ax4.plot(np.random.rand(10))
ax4.set_ylabel('aligned 2', bbox=box)
ax4.yaxis.set_label_coords(labelx, 0.5)

plt.show()
```

Skip dates where there is no data
---------------------------------
matplotlib/pyplot_index_formatter.py:
----------------------------------
```

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.ticker as ticker

r = mlab.csv2rec('../data/aapl.csv')
r.sort()
r = r[-30:]  # get the last 30 days

N = len(r)
ind = np.arange(N)  # the evenly spaced plot indices

def format_date(x, pos=None):
    thisind = np.clip(int(x+0.5), 0, N-1)
    return r.date[thisind].strftime('%Y-%m-%d')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(ind, r.adj_close, 'o-')
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
fig.autofmt_xdate()

plt.show()
```

IPython
========
IPythonIPython является командной оболочкой для интерактивных вычислений на нескольких языках программирования, первоначально разработанной для языка программирования Python. IPython позволяет расширить возможности представления, добавляет синтаксис оболочке, автодополнение и обширную историю команд. IPython в настоящее время предоставляет следующие возможности:


- Мощные интерактивные оболочки (терминального типа и основанную на Qt).
- Браузерный редактор с поддержкой кода, текста, математических выражений, встроенных графиков и других возможностей представления.
- Поддерживает интерактивную визуализацию данных и использование инструментов GUI.
- Гибкие, встраиваемые интерпретаторы для работы в собственных проектах.
- Простые в использовании, высокопроизводительные инструменты для параллельных вычислений.

Сайт IPython: www.ipython.org
------------------------------
Для установки IPython в Linux, выполняем следующие команды в терминале:

```
sudo apt-get update
sudo pip install ipython
```
Замечательное видео, демонстрирующее возможности IPython:
----------------------------------------------------------
[youtube width="600"](http://www.youtube.com/watch?v=H6dLGQw9yFQ#t=149[/youtube)

IPython
-------
[![Parallel Machine Learning](https://img.shields.io/badge/Machine%20Learning-IPython-orange.svg)](https://github.com/ogrisel/parallel_ml_tutorial)
[![notebooks](https://img.shields.io/badge/notebooks-IPython-red.svg)](https://github.com/ogrisel/parallel_ml_tutorial)
[![jupyter](https://img.shields.io/badge/jupyter-IPython-yellowgreen.svg)](http://nbviewer.ipython.org/github/ogrisel/parallel_ml_tutorial/tree/master/rendered_notebooks/)
[![MIT License](https://img.shields.io/cocoapods/l/AFNetworking.svg)](http://opensource.org/licenses/MIT)

Install NumPy, SciPy, matplotlib, IPython, psutil, and scikit-learn in their latest stable version 
python fetch_data.py
```
sudo pip install jupyter

cd notebooks
ipython notebook

```

scikit-learn
=============
Пакет, в котором находятся реализации множества различных алгоритмов машинного обучения и data mining.

Сайт пакета: scikit-learn.org
-----------------------------
Для установки выполняем в Терминале Linux:
```
sudo apt-get update
sudo apt-get install python-sklearn
```
Линейная регрессия в scikit-learn
----------------------------------
Пример кода, строящего линейную регрессию для некоторого набора данных, имеющихся в пакете scikit-learn:

```

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
 
# Load the diabetes dataset
diabetes = datasets.load_diabetes()
 
# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis]
diabetes_X_temp = diabetes_X[:, :, 2]
 
# Split the data into training/testing sets
diabetes_X_train = diabetes_X_temp[:-20]
diabetes_X_test = diabetes_X_temp[-20:]
 
# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]
 
# Create linear regression object
regr = linear_model.LinearRegression()
 
# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)
 
# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean square error
print("Residual sum of squares: %.2f"
% np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
 
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))
 
# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
linewidth=3)
 
plt.xticks(())
plt.yticks(())
 
plt.show()
```

Стек, очередь, дерево, куча, граф
---------------------------------

Стек (иногда говорят “магазин/обойма” - по аналогии с магазином огнестрельного оружия) - это упорядоченная коллекция элементов, где добавление нового или удаление существующего всегда происходит только на одном из концов. Этот конец обычно называют “вершиной”, а противоположный ему - “основанием”.
Организован по принципу LIFO, last-in, first-out (англ. «последним пришёл — первым вышел»). Он предоставляет упорядочение по времени нахождения в коллекции. Более новые элементы расположены ближе к вершине, более старые - ближе к основанию.

Операции со стеком
------------------
- Stack() - создаёт новый пустой стек. Параметры не нужны, возвращает пустой стек.
- push(item) - добавляет новый элемент на вершину стека. В качестве параметра выступает элемент; функция ничего не возвращает.
- pop() - удаляет верхний элемент из стека. Параметры не требуются, функция возвращает элемент. Стек изменяется.
- peek() - возвращает верхний элемент стека, но не удаляет его. Параметры не требуются, стек не модифицируется.
- isEmpty() - проверяет стек на пустоту. Параметры не требуются, возвращает булево значение.
- size() - возвращает количество элементов в стеке. Параметры не требуются, тип результата - целое число.

Реализация с помощью списка
----------------------------
```
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[-1]

     def size(self):
         return len(self.items)

s = Stack()
s.push('hello')
s.push('true')
print(s.pop())
print(s.pop())
print(s.pop())
```

Реализация стека, найденная на Code Review.
-------------------------------------------

Очередь - это упорядоченная коллекция элементов, в которой добавление новых происходит с одного конца, называемого “хвост очереди”, а удаление существующих - с другого, “головы очереди”. Как только элемент добавляется в конец очереди, он начинает свой путь к её началу, ожидая удаления предыдущих.
Самые последние из добавленных в очередь единиц должны ждать в конце коллекции. Элемент, который пробыл в очереди дольше всего, находится в её начале. Такой принцип упорядочения иногда называют FIFO, first-in first-out (англ. “первым пришёл - первым вышел”). Ещё он известен, как “первым пришёл - первым обслужен”
https://docs.python.org/2/library/queue.html

Операции с очередью
--------------------
- Queue() создаёт новую пустую очередь. Не нуждается в параметрах, возвращает пустую очередь.
enqueue(item) добавляет новый элемент в конец очереди. Требует элемент в качестве параметра, ничего не возвращает.
- dequeue() удаляет из очереди передний элемент. Не нуждается в параметрах, возвращает элемент. Очередь изменяется.
- isEmpty() проверяет очередь на пустоту. Не нуждается в параметрах, возвращает булево значение.
size() возвращает количество элементов в очереди (целое число). Не нуждается в параметрах.
```
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
```
Симуляция: Hot Potato
----------------------
Одно из типичных приложений для демонстрации очереди в действии - это симуляция реальной ситуации, которая требует управления данными в манере FIFO. Для начала давайте рассмотрим детскую игру Hot Potato. В этой игре дети выстраиваются в круг и перебрасывают предмет от соседа к соседу так быстро, как только могут. В некоторый момент игры действие останавливается, и ребёнок, у которого в руках остался предмет (картошка), выбывает из круга. Игра продолжается до тех пор, пока не останется единственный победитель.

Для симуляции круга мы будем использовать очередь

```
def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    
    print(simqueue.items)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
    
        simqueue.dequeue()
    print(simqueue.items)
    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],1))
```

Пример использования queue - симуляция подтверждения регистрации пользователей на каком-либо ресурсе

```
from queue import Queue

unconfirmed_users_queue = Queue()

def user_registration(user):
    global unconfirmed_users_queue
    unconfirmed_users_queue.put(user)
    print("User {0} registered".format(user))
    
def confirm_users():
    print("Confirming users (FIFO)")
    global unconfirmed_users_queue
    while not unconfirmed_users_queue.empty():
        user = unconfirmed_users_queue.get()
        print("User {0} confirmed".format(user))

def register_several_users(): 
    user=''

    while True:
        user = input()
        if user == "quit":
            break
        else:
            user_registration(user)

register_several_users()
confirm_users()
```

Деревья
----------
Основные понятия
- Узел - это основная часть дерева. Он может иметь название, которое мы будем называть “ключом”. Также узел может содержать дополнительную информацию, которую мы будем называть “полезной нагрузкой”. Хотя во многих алгоритмах для деревьев ей не уделяется достаточно внимания, для приложений, использующих эту структуру данных, она часто оказывается критичным фактором
- Ветвь - другая фундаментальная часть дерева. Она соединяет два узла вместе, показывая наличие между ними определённых отношений. Каждый узел (кроме корня) имеет ровно одну входящую ветвь. При этом он может иметь несколько исходящих ветвей.
- Корень дерева - единственный узел, не имеющий входящих ветвей
- Путь - это упорядоченный список узлов, соединённых ветвями.
- Высота - дерева равна максимальному уровню любого его узла.
Определение 1: 
--------------
- Дерево состоит из набора узлов и набора ветвей, соединяющих пары узлов. Оно имеет следующие свойства:
- Один из узлов дерева определён, как его корень.
- Каждый узел n (кроме корневого) соединяется ветвью с единственным другим узлом p, где p - родитель n.
- Каждый узел соединён с корнем единственно возможным путём.
- Если каждый из узлов дерева имеет максимум двух потомков, то такая структура называется двоичным деревом.

Определение 2: 
--------------
Дерево либо пусто, либо содержит корень и нуль или более поддеревьев, каждое из которых тоже является деревом. Корень каждого поддерева соединён ветвью с родительским деревом.

структура имеет как минимум четыре узла, поскольку каждый из треугольников, представляющих поддеревья, должен иметь корень. В этом дереве может быть намного больше узлов, но сказать точнее нельзя до тех пор, пока мы не продвинемся по нему глубже.

Реализация с использованием списков
-----------------------------------
В дереве, представленном как список списков, на первой позиции мы будем хранить значение корневого узла. Второй элемент сам по себе будет списком и представит левое поддерево. Третий элемент станет правым поддеревом. Чтобы проиллюстрировать такую технику хранения, рассмотрим пример

```
myTree = ['a',   #root
      ['b',  #left subtree
       ['d' [], []],
       ['e' [], []] ],
      ['c',  #right subtree
       ['f' [], []],
       [] ]
     ]
```
Обратите внимание, что у нас есть доступ к каждому из поддеревьев с использованием стандартной списковой индексации. Корень дерева - myTree[0], левое поддерево - myTree[1], правое - myTree[2].
```
myTree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
print(myTree)
print('left subtree = ', myTree[1])
print('root = ', myTree[0])
print('right subtree = ', myTree[2])
print(myTree[1][2][0])
['a', ['b', ['d', [], []], ['e', [], []]], ['c', ['f', [], []], []]]
left subtree =  ['b', ['d', [], []], ['e', [], []]]
root =  a
right subtree =  ['c', ['f', [], []], []]
```
Давайте формализуем это определение с помощью некоторых функций, которые сделают проще использование списков в качестве деревьев. Обратите внимание, мы не собираемся определять новый класс для двоичного дерева. Функции, которые будут написаны, всего лишь помогут манипулировать стандарным списком, с которым мы работаем, как с деревом.
```
def BinaryTree(r):
    return [r, [], []]

def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print(l)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))
```

Реализация с помощью ссылок и узлов
------------------------------------
Наш второй способ представления деревьев будет использовать узлы и ссылки. Для этого случая мы определим класс, чьими атрибутами станут корневое значение и левое и правое поддеревья.
Начнём с простого определения класса для варианта с узлами и ссылками. Важно помнить, что в этом представлении атрибуты left и right являются ссылками на другие сущности класса BinaryTree. Например, когда мы вставляем нового левого потомка в дерево, мы создаём другой объект BinaryTree и изменяем self.leftChild корня, чтобы этот атрибут ссылался на новое дерево.
```
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
```
Далее давайте рассмотрим функцию, которую требуется написать для строительства дерева за пределы корневого значения. Чтобы добавить левого потомка в дерево, мы создадим новый объект двоичного дерева и поместим в его атрибут корня left ссылку на новый объект.
```
def insertLeft(self, newNode):
    if self.leftChild == None:
        self.leftChild = BinaryTree(newNode)
    else:
        t = BinaryTree(newNode)
        t.leftChild = self.leftChild
        self.leftChild = t
```
Нам необходимо рассмотреть два случая вставки. Первый - для узла, у которого нет левого потомка. В этом варианте узел просто вставляется в дерево. Второй вариант характеризуется узлом, имеющим левого потомка. Тогда нам надо вставить новый узел и спустить имеющегося потомка на один уровень ниже.
Код для insertRight должен содержать симметричный набор случаев. Здесь также может либо отсутствовать правый потомок, либо существовать необходимость вставить узел между корнем и имеющимся правым потомком
```
def insertRight(self,newNode):
    if self.rightChild == None:
        self.rightChild = BinaryTree(newNode)
    else:
        t = BinaryTree(newNode)
        t.rightChild = self.rightChild
        self.rightChild = t
```
Завершая наше определение простого двоичного дерева, напишем методы доступа к корню, правому и левому потомкам
```
def getRightChild(self):
    return self.rightChild

def getLeftChild(self):
    return self.leftChild

def setRootVal(self,obj):
    self.key = obj

def getRootVal(self):
    return self.key
```
Подводя итог проделанной работы:
```
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    
#     def __str__(self):
#         if self.getRootVal():
#             print(self.getRootVal())


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())
```
Куча
-----
Куча — двоичное дерево. А это значит, что каждый родительский элемент имеет два дочерних. И хотя мы называем эту структуру данных кучей, но выражается она через обычный массив. Высота кучи - примерно целая часть log(n), где n — количество элементов.
https://docs.python.org/2/library/heapq.html

Существуют также кучи min-heap, где дочерние элементы всегда больше родительского.

Несколько простых функций для работы с кучами:
```
global heap
global currSize

def parent(i): #Получить индекс родителя для i-того элемента
    return i/2

def left(i): #Получить левый дочерний элемент от i-того
    return 2*i

def right(i): #Получить правый дочерний элемент от i-того
    return (2*i + 1)
```
Добавление элемента в существующую кучу
---------------------------------------
Для начала мы добавляем элемент в самый низ кучи, т.е. в конец массива. Затем мы меняем его местами с родительским элементом до тех пор, пока он не встанет на свое место.
Алгоритм:
----------
- Добавляем элемент в самый низ кучи.
- Сравниваем добавленный элемент с родительским; если порядок верный — останавливаемся.
- Если нет — меняем элементы местами, и возвращаемся к предыдущему пункту.

```
def swap(a, b): # меняем элемент с индексом a на элемент с индексом b
    temp = heap[a]
    heap[a] = heap[b]
    heap[b] = temp

def insert(elem):
    global currSize
    
    index = len(heap)
    heap.append(elem)
    currSize += 1
    par = parent(index)
    flag = 0
    while flag != 1:
        if index == 1: #Дошли до корневого элемента
            flag = 1
        elif heap[par] > elem: #Если индекс корневого элемента больше индекса нашего элемента - наш элемент на своем месте
            flag = 1
        else: #Меняем местами родительский элемент с нашим
            swap(par, index)
            index = par
            par = parent(index)
            
    print(heap)
```
Максимальное количество проходов цикла while равно высоте дерева, или log(n), следовательно, трудоемкость алгоритма — O(log(n)).
Извлечение максимального элемента кучи
---------------------------------------
Первый элемент в куче — всегда максимальный, так что мы просто удалим его (предварительно запомнив), и заменим самым нижним. Затем мы приведем кучу в правильный порядок, используя функцию: maxHeapify()
Алгоритм:
---------
- Заменить корневой элемент самым нижним.
- Сравнить новый корневой элемент с дочерними. Если они в правильном порядке — остановиться.
- Если нет — заменить корневой элемент на одного из дочерних (меньший для min-heap, больший для max-heap), и повторить шаг 2.
```
def extractMax():
    global currSize
    if currSize != 0:
        maxElem = heap[1]
        heap[1] = heap[currSize] # Заменяем корневой элемент - последним
        heap.pop(currSize) # Удаляем последний элемент
        currSize -= 1 # Уменьшаем размер кучи
        maxHeapify(1)
        return maxElem

def maxHeapify(index):
    global currSize
    
    lar = index
    l = left(index)
    r = right(index)

    # Вычисляем, какой из дочерних элементов больше; если он больше родительского - меняем местами
    if l <= currSize and heap[l] > heap[lar]:
        lar = l
    if r <= currSize and heap[r] > heap[lar]:
        lar = r
    if lar != index:
        swap(index, lar)
        maxHeapify(lar)
```
И вновь максимальное количество вызовов функции maxHeapify равно высоте дерева, или log(n), а значит, трудоемкость алгоритма — O(logn).
Делаем кучу из любого рандомного массива
-----------------------------------------
Есть два пути сделать это. Первый — поочередно вставлять каждый элемент в кучу. Это просто, но совершенно неэффективно. Трудоемкость алгоритма в этом случае будет O(nlogn), т.к. функция O(logn) будет выполняться n раз.
Более эффективный способ — применить функцию maxHeapify для под-кучи, от (currSize/2) до первого элемента.
Сложность получится O(n), и доказательство этого утверждения, к сожалению, выходит за рамки данного курса. Интуиция: элементы, находящиеся в части кучи от currSize/2 до currSize, не имеют потомков, и большинство образованных таким образом под-куч будут высотой меньше, чем log(n).

```
def buildHeap():
    global currSize
    for i in range(currSize/2, 0, -1): #третий агрумент в range() - шаг перебора, в данном случае определяет направление.
        print heap
        maxHeapify(i)
    currSize = len(heap)-1
```
Графы
------
Вершина
--------
Вершина (иногда её называют “узел”) - основная часть графа. Может иметь имя, которое называется “ключ”. Также вершина может обладать дополнительной информацией, которую мы будем называть “полезной нагрузкой”.
Ребро
------
Ребро (или “дуга”) - другая фундаментальная часть графа. Ребро, соединяющее две вершины, показывает наличие между ними определённых отношений. Рёбра могут быть одно- и двунаправленными.
Если все рёбра графа однонаправленные, то мы называем его направленным графом или диграфом (от англ. directed graph - прим. переводчика). Показанный выше граф необходимых для профилирования предметов - явный диграф, поскольку вы обязаны проходить одни курсы прежде, чем другие.
Вес
----
Рёбра могут иметь вес, показывающий стоимость перемещения от одной вершины к другой. Например, в графе дорог, связывающих города, вес ребра может отображать расстояние между двумя населёнными пунктами. Имея на руках все эти формулировки, мы способны дать формальное определение графа. Он может быть представлен как G, где G=(V,E). Здесь V - множество вершин графа, а E - множество соединяющих их рёбер. Каждое ребро представляет собой кортеж (v,w), где w,v∈V. Сюда можно добавлять третий компонент, отображающий вес ребра. Подграф s - это набор рёбер e и вершин v таких, что e⊂E и v⊂V.

Путь
-----
Путь в графе - это последовательность вершин, соединённых рёбрами. Формально путь можно определить, как w1,w2,...,wn такой, что (wi,wi+1)∈E для всех 1 ≤ i ≤n−1.
Длиной пути без весов станет количество в нём рёбер: n−1. Взвешенный путь в графе будет суммой весов всех входящих в него рёбер. Например, на рисунке 2 путём из V3 в V1 является последовательность вершин (V3,V4,V0,V1). Рёбрами - (v3,v4,7),(v4,v0,1),(v0,v1,5).
Цикл
----
Цикл в направленном графе начинается и заканчивается в одной и той же вершине. Например, на рисунке 2 циклом будет путь (V5,V2,V3,V5). Граф без циклов называется ацикличным. Направленный граф без циклов - это ациклический направленный граф или DAG (от англ. directed acyclic graph - прим. автора). Мы увидим, что с его помощью можно решить некоторые важные задачи.
http://www.python-course.eu/graphs_python.php
https://networkx.github.io/
Операции с графами
-------------------
- Graph() создаёт новый пустой граф.
- addVertex(vert) добавляет в граф объект типа Vertex.
- addEdge(fromVert, toVert) Добавляет в граф новое направленное ребро, соединяющее две вершины.
- addEdge(fromVert, toVert, weight) Добавляет в граф новое взвешенное направленное ребро, соединяющее две вершины.
- getVertex(vertKey) находит в графе вершину vertKey.
- getVertices() возвращает список всех вершин графа.
in возвращает True для оператора формы vertex in graph, если данная вершина в графе имеется, и False в противном случае.
Представление графа
-------------------
Матрица смежности
------------------
Одним из простейших способов реализовать граф является использование двумерной матрицы. В ней каждая строка и столбец представляют собой вершину графа, а хранимое в ячейке на пересечении строки v и столбца w значение показывает, что существует ребро из вершины v к вершине w. Когда две вершины соединены, мы говорим, что они смежные

Список смежности
-----------------
Более пространственно-экономичным способом реализации разреженного графа является использование списка смежности. В таком представлении мы храним основной список из всех вершин объекта Graph, каждый из элементов которого поддерживает перечень из связанных с ним вершин. В нашей реализации класса Vertex в качестве последнего будет использоваться словарь, где ключами станут вершины, а значениями - веса.

Преимуществом такой реализации является то, что она позволяет нам компактно представлять разреженные графы. Также в списке смежности легко найти все ссылки, непосредственно связанные с конкретной вершиной.
Реализация
------------
- Graph - содержит основной список вершин.
- Vertex - представление в графе.
Объекты Vertex будут использовать словарь для отслеживания смежных вершин и весов рёбер. Называться он будет connectedTo. Листинг ниже показывает код для класса Vertex. Конструктор просто инициализирует id (обычную строку) и словарь connectedTo. Метод addNeighbor используется для добавления связи данной вершины с другой. Метод getConnections возвращает все вершины из списка смежности, которые представлены в connectedTo. Метод getWeight возвращает вес ребра из этой вершины к передаваемой ему в качестве параметра.
```
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
```
Класс Graph, показанный в следующем листинге, содержит словарь, отображающий имена вершин на их объекты. Также Graph предоставляет методы для добавления вершин в граф и связывания их друг с другом. Дополнительно мы имеем реализацию метода iter, облегчающего итерации по объектам Vertex в конкретном графе. Вместе два метода позволяют делать итерации по именам вершин или непосредственно по объектам.
```
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
```

Классические алгоритмы на графах
================================
Кратчайший путь в графе
-----------------------
Заданы n вершин графа (узлов сети) v1,v2,…,vn и положительные целые длины дуг dij=d(vi,vj) между ними. Нужно для всех k∈{2,…,n} найти минимальную длину пути из v1 в vk.
Для начала посмотрим, как мы сами могли бы реализовать класс "Неориентированный граф"
```
class UndirectedGraph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []
        
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance
```
Алгоритм Дейкстры основывается на том простом факте, что что если у нас есть кратчайший путь от v до w, проходящий через вершину y, назовем его (v→w)∗, то его первая часть от v до y, (v→y)∗ тоже будет кратчайшим путем.

Задачи с подобными свойствами, когда оптимальное решение можно легко получить из оптимальных решений подзадач, обычно хорошо решаются так называемыми "жадными алгоритмами". Алгоритм Дейкстры - как раз один их примеров. Его сложность при использовании min-кучи - O(|E|+|V|log|V|), где |E|, |V| - число дуг и вершин соответственно
Описание алгоритма Дейкстры на Хабрахабре
-----------------------------------------
```
def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = graph.nodes

    while nodes: 
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in G.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

G = UndirectedGraph()

for node in range(1,8):
    G.add_node(node)

for edge in [(1,7,15),(1,3,6),(1,5,7),
            (1,6,6),(1,2,4),(2,4,10),
            (3,5,10),(3,7,5),(3,6,5),
            (4,7,3),(4,5,15),(5,6,5)]:
    G.add_edge(*edge)
    
# print(G.edges)
# print(G.distances)
    
dijsktra(G, 1)


import networkx as nx

G=nx.Graph()
G.add_nodes_from(range(1,8))
G.add_weighted_edges_from([(1,7,15),(1,3,6),(1,5,7),
                           (1,6,6),(1,2,4),(2,4,10),
                           (3,5,10),(3,7,5),(3,6,5),
                           (4,7,3),(4,5,15),(5,6,5)])

pos = nx.spring_layout(G) # positions for all nodes

# nodes and node labels
nx.draw_networkx_nodes(G,pos,node_size=700)
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

# edges
edges = [(u,v) for (u,v,d) in G.edges(data=True)]
nx.draw_networkx_edges(G, pos, edgelist=edges, font_size=16)

# edge labels
edge_labels=dict([((u,v,),d['weight'])
             for u,v,d in G.edges(data=True)])
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)

show() # matplotlib.pyplot.show()
Populating the interactive namespace from numpy and matplotlib
WARNING: pylab import has clobbered these variables: ['source']
`%matplotlib` prevents importing * from pylab and numpy
```
Реализация с помощью кучи
-------------------------
```
import heapq

def dijkstra(adj, costs, s, t):
    ''' Return predecessors and min distance if there exists a shortest path 
        from s to t; Otherwise, return None '''
    Q = []     # priority queue of items; note item is mutable.
    d = {s: 0} # vertex -> minimal distance
    Qd = {}    # vertex -> [d[v], parent_v, v]
    p = {}     # predecessor
    visited_set = set([s])

    for v in adj.get(s, []):
        d[v] = costs[s, v]
        item = [d[v], s, v]
        heapq.heappush(Q, item)
        Qd[v] = item

    while Q:
#         print(Q)
        cost, parent, u = heapq.heappop(Q)
        if u not in visited_set:
#             print('visit:', u)
            p[u]= parent
            visited_set.add(u)
            if u == t:
                return p, d[u]
            for v in adj.get(u, []):
                if d.get(v):
                    if d[v] > costs[u, v] + d[u]:
                        d[v] =  costs[u, v] + d[u]
                        Qd[v][0] = d[v]    # decrease key
                        Qd[v][1] = u       # update predecessor
                        heapq._siftdown(Q, 0, Q.index(Qd[v]))
                else:
                    d[v] = costs[u, v] + d[u]
                    item = [d[v], u, v]
                    heapq.heappush(Q, item)
                    Qd[v] = item

    return None

def make_undirected(cost):
    ucost = {}
    for k, w in cost.items():
        ucost[k] = w
        ucost[(k[1],k[0])] = w
    return ucost

# adjacent list
adj = { 1: [2, 3, 5, 7],
        2: [1, 4],
        3: [1, 5, 6,7],
        4: [2, 5, 7],
        5: [1, 3, 4, 6],
        6: [3, 5],
        7: [1, 3, 4]}
    
# edge costs
edges = {(1, 2): 4, (4, 7): 3, (1, 3): 6, (4, 5): 15,
        (1, 5): 7, (1, 6): 6, (3, 6): 5, (1, 7): 15, 
        (5, 6): 5, (3, 7): 5, (2, 4): 10, (3, 5): 10}

edge_cost = make_undirected(edges)

source, target = 1, 7
predecessors, min_cost = dijkstra(adj, edge_cost, source, target)
c = target
path = [c]
print('Minimal cost from {0} to {1}: {2}'.format(source, target, min_cost))
while predecessors.get(c):
    path.insert(0, predecessors[c])
    c = predecessors[c]

print('shortest path from {0} to {1}: {2}'.format(source, target, path))

```
Нахождение кратчайших путей с помощью методов библиотеки Networkx
------------------------------------------------------------------
```
help(nx.single_source_dijkstra)
Help on function single_source_dijkstra in module networkx.algorithms.shortest_paths.weighted:

single_source_dijkstra(G, source, target=None, cutoff=None, weight='weight')
    Compute shortest paths and lengths in a weighted graph G.
    
    Uses Dijkstra's algorithm for shortest paths.
    
    Parameters
    ----------
    G : NetworkX graph
    
    source : node label
       Starting node for path
    
    target : node label, optional
       Ending node for path
    
    cutoff : integer or float, optional
       Depth to stop the search. Only paths of length <= cutoff are returned.
    
    Returns
    -------
    distance,path : dictionaries
       Returns a tuple of two dictionaries keyed by node.
       The first dictionary stores distance from the source.
       The second stores the path from the source to that node.
    
    
    Examples
    --------
    >>> G=nx.path_graph(5)
    >>> length,path=nx.single_source_dijkstra(G,0)
    >>> print(length[4])
    4
    >>> print(length)
    {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
    >>> path[4]
    [0, 1, 2, 3, 4]
    
    Notes
    ---------
    Edge weight attributes must be numerical.
    Distances are calculated as sums of weighted edges traversed.
    
    Based on the Python cookbook recipe (119466) at
    http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/119466
    
    This algorithm is not guaranteed to work if edge weights
    are negative or are floating point numbers
    (overflows and roundoff errors can cause problems).
    
    See Also
    --------
    single_source_dijkstra_path()
    single_source_dijkstra_path_length()


nx.single_source_dijkstra(G, source=1)
nx.dijkstra_path(G,1,4)
```
Реализация алгоритма Беллмана-Форда. 
------------------------------------
Его сложность O(|V||E|) (хуже, чем у алгоритма Дейкстры), зато можно работать с отрицательными весами.
```
help(nx.bellman_ford)
Help on function bellman_ford in module networkx.algorithms.shortest_paths.weighted:

bellman_ford(G, source, weight='weight')
    Compute shortest path lengths and predecessors on shortest paths
    in weighted graphs.
    
    The algorithm has a running time of O(mn) where n is the number of
    nodes and m is the number of edges.  It is slower than Dijkstra but
    can handle negative edge weights.
    
    Parameters
    ----------
    G : NetworkX graph
       The algorithm works for all types of graphs, including directed
       graphs and multigraphs.
    
    source: node label
       Starting node for path
    
    weight: string, optional (default='weight')
       Edge data key corresponding to the edge weight
    
    Returns
    -------
    pred, dist : dictionaries
       Returns two dictionaries keyed by node to predecessor in the
       path and to the distance from the source respectively.
    
    Raises
    ------
    NetworkXUnbounded
       If the (di)graph contains a negative cost (di)cycle, the
       algorithm raises an exception to indicate the presence of the
       negative cost (di)cycle.  Note: any negative weight edge in an
       undirected graph is a negative cost cycle.
    
    Examples
    --------
    >>> import networkx as nx
    >>> G = nx.path_graph(5, create_using = nx.DiGraph())
    >>> pred, dist = nx.bellman_ford(G, 0)
    >>> sorted(pred.items())
    [(0, None), (1, 0), (2, 1), (3, 2), (4, 3)]
    >>> sorted(dist.items())
    [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
    
    >>> from nose.tools import assert_raises
    >>> G = nx.cycle_graph(5, create_using = nx.DiGraph())
    >>> G[1][2]['weight'] = -7
    >>> assert_raises(nx.NetworkXUnbounded, nx.bellman_ford, G, 0)
    
    Notes
    -----
    Edge weight attributes must be numerical.
    Distances are calculated as sums of weighted edges traversed.
    
    The dictionaries returned only have keys for nodes reachable from
    the source.
    
    In the case where the (di)graph is not connected, if a component
    not containing the source contains a negative cost (di)cycle, it
    will not be detected.


pred, dist = nx.bellman_ford(G, 1)
print(pred)
print(dist)
```
Задача коммивояжера
--------------------
Заданы неориентированный граф из n вершин-городов, и dij=d(vi,vj) — положительные целые расстояния между городами. Чему равна наименьшая возможная длина гамильтонова цикла (кольцевого маршрута, проходя- щего по одному разу через все города)? То есть нужно найти
min∑i=1n−1dpi,pi+1+dpn,p1,
где минимум берется по всем перестановкам p чисел 1,…,n
```
from itertools import permutations

INFINITY = pow(10, 20)

def TSP_BruteForce(G, init_node_index):
    def get_path_length(path):
        path_length = 0
        for i, v1 in enumerate(path):
            v2 = path[ (i+1) % len(path)]
            if not G.has_edge(v1, v2):
                return INFINITY
            path_length += G[v1][v2]["weight"]
        return path_length
    
    def node_permutations(G, init_node_index):
        nodes = G.nodes()
        init_node = nodes[init_node_index]
        nodes.remove(init_node)
        return [[init_node] + list(a_tuple) 
                 for a_tuple in permutations(nodes)]
    
    min_path = min_path_length = None
    # перебор всех перестановок с фиксированным первым узлом
    for path in node_permutations(G, init_node_index):
        path_length = get_path_length(path)
        if not min_path or min_path_length > path_length:
            min_path, min_path_length = path, path_length
    return min_path, min_path_length


import networkx as nx

G=nx.Graph()
G.add_nodes_from(range(1,8))
G.add_weighted_edges_from([(1,7,15),(1,3,6),(1,5,7),
                           (1,6,6),(1,2,4),(2,4,10),
                           (3,5,10),(3,7,5),(3,6,5),
                           (4,7,3),(4,5,15),(5,6,5)])

pos = nx.spring_layout(G) # positions for all nodes

# nodes and node labels
nx.draw_networkx_nodes(G,pos,node_size=700)
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

# edges
edges = [(u,v) for (u,v,d) in G.edges(data=True)]
nx.draw_networkx_edges(G, pos, edgelist=edges, font_size=16)

# edge labels
edge_labels=dict([((u,v,),d['weight'])
             for u,v,d in G.edges(data=True)])
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)

show() # matplotlib.pyplot.show()
Populating the interactive namespace from numpy and matplotlib
WARNING: pylab import has clobbered these variables: ['source', 'dist']
`%matplotlib` prevents importing * from pylab and numpy
```
Гамильтонов цикл с минимальной суммой весов ребер
-------------------------------------------------
```
"Оптимальный маршрут: {0}. Его стоимость = {1}".format(*TSP_BruteForce(G, 0))

'Оптимальный маршрут: [1, 2, 4, 7, 3, 6, 5]. Его стоимость = 39'
```
Поиск в глубину
---------------
Поиск в глубину (англ. Depth-first search, DFS) — один из методов обхода графа. Стратегия поиска в глубину, как и следует из названия, состоит в том, чтобы идти "вглубь" графа, насколько это возможно. Алгоритм поиска описывается рекурсивно: перебираем все исходящие из рассматриваемой вершины рёбра. Если ребро ведёт в вершину, которая не была рассмотрена ранее, то запускаем алгоритм от этой нерассмотренной вершины, а после возвращаемся и продолжаем перебирать рёбра. Возврат происходит в том случае, если в рассматриваемой вершине не осталось рёбер, которые ведут в нерассмотренную вершину. Если после завершения алгоритма не все вершины были рассмотрены, то необходимо запустить алгоритм от одной из нерассмотренных вершин.
Рассмотрим на примере следующего неориентированного невзвешенного графа

```
import networkx as nx

G=nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])
G.add_edges_from([('A','B'),('A','C'),('B','D'),
                    ('B','E'),('C','F'), ('E','F')])

pos = nx.spring_layout(G) # positions for all nodes

# nodes and node labels
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

nx.draw_networkx_edges(G, pos, edgelist=G.edges(), font_size=16)

show() # matplotlib.pyplot.show()
Populating the interactive namespace from numpy and matplotlib


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    # adjacent to start - graph.adj[start].keys()
    for next in set(graph.adj[start].keys()) - visited:
        dfs(graph, next, visited)
    return visited

dfs(G, 'C')


def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in set(graph.adj[start].keys()) - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])

list(dfs_paths(G, 'C', 'F'))
```
Поиск в ширину
--------------
Поиск в ширину (англ. breadth-first search, BFS) — метод обхода графа и поиска пути в графе. Поиск в ширину работает путём последовательного просмотра отдельных уровней графа, начиная с узла-источника u.
Рассмотрим все рёбра (u,v), выходящие из узла u. Если очередной узел v является целевым узлом, то поиск завершается; в противном случае узел v добавляется в очередь. После того, как будут проверены все рёбра, выходящие из узла u, из очереди извлекается следующий узел u, и процесс повторяется.
```
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.adj[vertex].keys()) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

list(bfs_paths(G, 'A', 'F'))
```


