# 21v-python

# Объектно-ориентированное программирование на Python
## Принципы ООП

- Все данные представляются объектами
- Программа является набором взаимодействующих объектов, посылающих друг другу сообщения
- Каждый объект имеет собственную часть памяти и может иметь в составе другие объекты
- Каждый объект имеет тип
- Объекты одного типа могут принимать одни и те же сообщения (и выполнять одни и те же действия)


# Python. Классы

Классы собирают в себе наборы данных (переменных) вместе с наборами функций на них действующими. Цель состоит в том, чтобы достигнуть более модульного кода с помощью группировки переменных и функций в легко изменяемые (чаще всего небольшие) узлы. Программирование с классами поддерживается большинством современных языков.

## Определение класса
```
class имя_класса(надкласс1, надкласс2, ...):
        # определения атрибутов и методов класса
```

У класса могут быть базовые (родительские) классы (надклассы), которые (если они есть) указываются в скобках после имени определяемого класса.

## Минимально возможное определение класса выглядит так:
```
    class Y:
        pass

```

В терминологии Python члены класса называются экземплярами, функции класса — методами, а поля класса — свойствами (или просто атрибутами).

Определения методов аналогичны определениям функций, но методы всегда имеют первый аргумент, называемый по широко принятому соглашению self:

```
    class Y:
        def m1(self, x):
            # блок кода метода
```

## Простые классы функций

школьная задача о вертикальном движении дрона, подброшенного в воздух. Мы знаем математическую модель, описывающую такое движение и можем найти координату y, в которой оказывается дрон в момент времени t:
```
y(t) = v0*t - g*t**2/2
```
где v0 — начальная скорость дрона, g — ускорение свободного падения и t — время. Заметим, ось y выбрана так, что дрон в начальный момент времени (t = 0) находится в точке с координатой y = 0. Чтобы посмотреть сколько времени займет у дрона вернуться в эту же координату (y = 0), надо с одной стороны в выражении правую часть приравнять нулю, с другой — вынести переменную t:
```
v0*t - (g*t**2)/2 = t(v0- (g*t)/2)= 0

t = 0, t = 2*v0/g
```
Таким образом, мы определили, что возможное время полета дрона задается интервалом времени t  [0, 2*v0/g].

```
y(t) = v0*t - g*t**2/2
```

Здесь y является функций времени t и кроме того, зависит от других параметров v0 и g. Мы могли бы придумать какое-то новое обозначение, вроде y(t; v0, g), чтобы показать, что t является независимой переменной, а v0 и g задаваемыми параметрами. При этом, строго говоря для Земли g, гравитационная постоянная, неизменна, то есть правильнее было бы писать 'y(t; v0). В общем случае, у нас может иметься функция, которая будет записываться f(x; p1, ..., pn).

Первое очевидное решение получать и переменные, и изменяемые параметры как аргументы обычной функции:
```
def y(t, v0):
    g = 9.81
    return  v0*t - 0.5*g*t**2
```
Проблема в этом случае состоит в том, что множество инструментов, что мы используем для математических операций с функциями предполагают, что функция одной переменной должна принимать в своем компьютерном представлении только один аргумент. Например, у нас есть инструмент для дифференцирования f(x) в точке x, которое осуществляется с помощью приближения

1.py
```
f' ~ (f(x+h)-f(x))/h
```
и записывается в виде кода
```
def diff(f, x, h=1E-10):
    return (f(x+h) - f(x))/h
```
И наша функция diff легко работает с функциями, принимающими один аргумент:
```
def h(t):
    return t**4 + 4*t

dh = diff(h, 0.1)

from math import sin, pi
x = 2*pi
dsin = diff(sin, x, h=1E-9)
```
Но diff не будет работать с нашей функцией y(t, v0). Вызов diff(y, t) приведет к ошибке в функции diff, поскольку дифференцируемая функция должна принимать лишь один агумент, а принимает два.

Написание альтернативной diff-функции для f с двумя аргументами это плохое решение, поскольку оно ограничивает всевозможные f до функций с одной переменной и одним аргументом. Фундаментальные принципы программирования гласят, что следует стремиться к такому решению, которое будет настолько общим и настолько широко применимым, насколько это возможно. В настоящем случае это означает, что функция diff должна быть применима к любой функции одной переменной.

## Глобальные переменные

Требования к представлению функций таким образом состоит в том, чтобы они принимали только независимую переменную, то есть выглядели так:
```
def y(t):
    g = 9.81
    return  v0*t - 0.5*g*t**2
```
Но поскольку v0 не определено, то вызов функции требует того, чтобы переменная была заранее определена и тогда мы уже можем определить значение для производной:
```
v0 = 3
dy = diff(y, 1)
```
Но использование глобальных переменных в этом случае это плохой стиль программирования. Почему это плохо, можно проиллюстрировать на примере когда нам нужно использовать разные версии одной функции. Например, мы бросаем мячик вверх со скоростями 1 и 5 м/с. Каждый раз, когда мы вызываем y, нам понадобиться задавать перед ним новое значение v0:
```
v0 = 3
dy = diff(y, 1)
print dy

v0 = 1; 
dy = diff(y, 1)
print dy

v0 = 5; 
dy = diff(y, 1)
print dy

```
Другая проблема в том, что переменные с такими простыми именами как v0 могут легко быть использованы в других частях программы. По этим и другим причинам может уже сейчас выступить золотое правило программирования: сокращать число глобальных переменных настолько, насколько это возможно.

## Представление функции в виде класса

Класс заключает в себе набор переменных (данных) и набор функций, связанных в единое целое. Переменные видны изнутри класса всем его функциям. То есть они «глобальные» для функций своего класса. Класс похож на модуль, но находящийся в тексте самой программы. Но при этом по технике его использования он существенно отличается. Например, вы можете создать множество копий одного класса, в то время как модуль выступает в единственном числе.  

Определения атрибутов — обычные операторы присваивания, которые связывают некоторые значения с именами атрибутов.
```
    class Y:
        attr1 = 2 * 2

```
В языке Python класс не является чем-то статическим после определения, поэтому добавить атрибуты можно и после:
```
    class Y:
        pass

    def value(self, t):
        return t

    Y.value = value
    Y.v0 = v0
```

Обращаясь к нашей функции y(t; v0) мы можем сказать, что переменные v0 и g определяют данные, а t служит аргументом некоторой функции Python value(t).
Программист, практикующий классы, соберет данные v0 и g и функцию value(t) вместе в один класс. К тому же класс обычно содержит и другую функцию называемую конструктором (constructor) для инициализации данных. 
```

    def value(self, t):
        return self.v0*t - 0.5*self.g*t**2
```
## Конструктор

Специальные методы вызываются при создании экземпляра класса (конструктор) и при удалении класса (деструктор). В языке Python реализовано автоматическое управление памятью, поэтому деструктор требуется достаточно редко, для ресурсов, требующих явного освобождения.
```

class Y:
    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81
```

Конструктор всегда носит имя __init__. Каждый класс имеет имя, которое традиционно начинают с большой буквы, поэтому для нашего класса мы выберем имя Y, соотнося его таким образом с y для математической функции.

## Реализация
Законченный код для нашего класса Y выглядит следующим образом: 4.py
```
class Y:
    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81

    def value(self, t):
        return self.v0*t - 0.5*self.g*t**2
```
## Использование

Класс создает новый тип данных, так что у нас теперь есть тип данных Y, с помощью которого мы можем создавать объекты. Объекты определенного пользователем класса (как Y) мы будем называть экземплярами. Следующее выражение создает экземпляр класса Y:
```
y = Y(3)
```
Y(3) автоматически представляется Python как вызов конструктора __init__ в классе Y. Аргументы при вызове, здесь это только число 3, всегда принимаются как аргументы функции-конструктора __init__ следующие после всегда стоящего на первом месте аргумента self.
Имея на руках экземпляр y, мы можем узнать значение y(t=0.1; v0=3) с помощью инструкции
```
v = y.value(0.1)
```
Теперь, поскольку происходит вызов value, аргумент self оказывается в стороне. Чтобы обратиться к функциям или переменным класса, нужно указывать префикс этой функции или имени переменной. Например, так мы можем вывести значение v0 экземпляра y:
```
print y.v0
```
В этом случае на выходе мы увидим число 3.
Кроме термина «экземпляр» для объектов, рожденных классом, говорят о функциях класса как методах и переменных класса как атрибутах. В нашем простом классе Y имеются два метода: __init__ и value и два атрибута: v0 и g. Имена методов и атрибутов могут свободно меняться точно так же как имена обычных функций и переменных. Однако, конструктор обязательно должен называться __init__.

## Переменная self
Внутри конструктора __init__ аргумент self это переменная, содержащая создаваемый экземпляр. Когда мы пишем
```
self.v0 = v0
self.g = 9.81
```
мы определяем два новых атрибута в этом экземпляре. Записывая y = Y(3) мы не только передаем число, но и имя экземпляра, то есть этот вызов можно представить как

Y.__init__(y, 3)

Когда мы пишем в теле конструктора self.v0 = v0, мы в действительности инициализируем y.v0. Когда же пишем
```
value = y.value(0.1)
```
Python переводит это как вызов
```
value = y.value(y, 0.1)
```
Выражение внутри метода value
```
self.v0*t - 0.5*self.g*t**2
```
ввиду того, что self это y имеет смысл тот же, что
```
y.v0*t - 0.5*y.g*t**2
```
Правила касательно self следующие:
- Любой метод класса содержит self в качестве первого аргумента.
- self представляет в своем лице (произвольный) экземпляр класса.
- Другой метод или атрибут класса используют self в виде self.name, где name имя этого атрибута или метода.
- self в качестве аргумента пропускается при вызове методов класса

## Расширение класса
В классе мы можем иметь так много атрибутов и методов, как захотим, так что давайте добавим новый метод к классу Y. Этот метод назовем formula он будет выводить строку, содержащую формулу математической функции y. После этой формулы мы выводим значение v0:
```
'v0*t - 0.5*g*t**2; v0=%g' % self.v0
```
где self это экземпляр класса Y. Вызов formula не требует никаких аргументов:
```
print y.formula()
```
Однако, из правил о self мы помним, что хотя метод formula при вызове и не требует никаких аргументов, но при определении мы должны передать ему аргумент self:
```
def formula(self):
    'v0*t - 0.5*g*t**2; v0=%g' % self.v0
```
Теперь наш класс целиком выглядит так 5.py:
```
class Y:
    """The  vertical  motion  of  a  ball."""

    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81

    def value(self, t):
        return self.v0*t - 0.5*self.g*t**2

    def formula(self):
        return 'v0*t - 0.5*g*t**2; v0=%g' % self.v0
```

## Создание экземпляра

Для создания объекта — экземпляра класса (то есть, инстанцирования класса), достаточно вызвать класс по имени и задать параметры конструктора:

```
y = Y(5)
t = 0.2
v = y.value(t)
print 'y(t=%g; v0=%g) = %g' % (t, y.v0, v)
print y.formula()
```
Результат:

```
y(t=0.2; v0=5) = 0.8038
v0*t - 0.5*g*t**2; v0=5
```

## Методы как обычные функции
Использование класса позволяет создать несколько функций y с разными значениями v0:
```
y1 = Y(1)
y2 = Y(1.5)
y3 = Y(-3)
```
При этом мы можем использовать y1.value, y2.value и y3.value как обычные функции от t, а значит и применять все то же, что имеется их для любых других функций одной переменной. 6.py:
```
def diff(f, x, h=1E-10):
    return (f(x+h) - f(x))/h

dy1dt = diff(y1.value, 0.1)
dy2dt = diff(y2.value, 0.1)
dy3dt = diff(y3.value, 0.2)

print dy1dt
print dy2dt
print dy3dt

```

## Инкапсуляция и доступ к свойствам
Все значения в Python являются объектами, инкапсулирующими код (методы) и данные и предоставляющими пользователям общедоступный интерфейс. Методы и данные объекта доступны через его атрибуты.

## Сокрытие информации о внутреннем устройстве объекта
Сокрытие информации о внутреннем устройстве объекта выполняется в Python на уровне соглашения между программистами о том, какие атрибуты относятся к общедоступному интерфейсу класса, а какие — к его внутренней реализации. Одиночное подчеркивание в начале имени атрибута говорит о том, что метод не предназначен для использования вне методов класса (или вне функций и классов модуля), однако, атрибут все-таки доступен по этому имени. Два подчеркивания в начале имени дают несколько большую защиту: атрибут перестает быть доступен по этому имени.

Особым случаем является наличие двух подчеркиваний в начале и в конце имени атрибута. Они используются для специальных свойств и функций класса (например, для перегрузки операции). Такие атрибуты доступны по своему имени, но их использование зарезервировано для специальных атрибутов, изменяющих поведение объекта.

## Доступ к атрибуту 

может быть как прямой 7.py:
```
class Y:
    """The  vertical  motion  of  a  ball."""

    def __init__(self, v0):
        self.v0 = v0 # атрибут получает значение в конструкторе
        self.g = 9.81

a = Y(5)
print a.v0
a.v0 = 5
```

Доступ к атрибуту с использованием свойств с заданными методами для получения, установки и удаления атрибута 8.py:

```
class Y:
    """The  vertical  motion  of  a  ball."""

    def __init__(self, v0):
        self.v0 = v0 # атрибут получает значение в конструкторе
        self.g = 9.81
    def getv0(self):                 # метод для получения значения
        return self._v0
    def setv0(self, value):          # присваивания нового значения
        self._v0 = value
    def delv0(self):                 # удаления атрибута
        del self._v0                 
    v0 = property(getv0, setv0, delv0, "Свойство v0")    # определяем v0 как свойство

a = Y(5)      
print a.v0      # Синтаксис доступа к атрибуту при этом прежний
a.v0 = 5

```

## Строки документации

Классы, как и функции, могут быть описаны простым человеческим языком сразу в следующей строке после заголовка с помощью doc strings — строк документации. Вводятся они абсолютно таким же образом, с помощью тройки двойных кавычек с каждой стороны:
```
class Y:
    """The vertical motion of a ball."""

    def __init__(self, v0):
        ...
```
В случае объемного конечного продукта обычно пишут более исчерпывающее объяснение о том как этот класс может быть использован, какие методы и атрибуты включает, примеры использования класса 9.py:
```
class Y:
    """Mathematical function for the vertical motion of a ball.

    Methods:
        constructor(v0): set initial velocity v0.
        value(t): compute the height as function of t.
        formula(): print out the formula for the height.

    Attributes:
        v0: the initial velocity of the ball (time 0).
        g: acceleration of gravity (fixed).

    Usage:
    >>> y  =  Y(3)
    >>> position1 = y.value(0.1)
    >>> position2 = y.value(0.3)
    >>> print  y.formula()
    v0*t - 0.5*g*t**2; v0=3
    """
```
## Альтернативная реализация классов функций

Это хорошая привычка всегда в классе иметь конструктор и инициализировать в нем атрибуты класса. Но это не обязательное требование. Давайте выбросим конструктор и представим v0 как аргумент метода value. Если пользователь при вызове не задает v0, то мы используем значение из более ранних вызовов, находящееся в атрибуте self.v0. О том, задал ли пользователь v0 или нет, мы узнаем, задав в определении v0 значение по умолчанию None, а дальше проверяя его с помощью if. Наша альтернативная реализация представлена теперь классом Y2:
```
class Y2:
    def value(self, t, v0=None):
        if v0 is not None:
            self.v0 = v0
        g = 9.81
        return self.v0*t - 0.5*g*t**2
```
В этот раз у класса только один метод и один атрибут, поскольку мы обошлись без конструктора, а g сделали локальной переменной метода value.
Но если здесь нет конструктора, то как же создается экземпляр? Python создает пустой конструктор. Это позволяет нам написать как и раньше:
```
y = Y2()
```
чтобы создать экземпляр y. Поскольку в автоматически сгенерированном пустом конструкторе ничего не происходит, то на этом этапе y не получает никаких атрибутов. Написав
```
print y.v0
```
мы получим ошибку:
```
AttributeError: Y2  instance has no attribute 'v0'
```
Но при вызове
```
v = y.value(0.1, 5)
```
мы создаем атрибут self.v0 в методе value. Теперь
```
print y.v0
```
дает 5. Это значение v0 используется пока новый вызов не изменит его.
Возникающее исключение AttributeError следовало бы учесть в теле класса (а еще точнее методе value) с помощью блока try-except 11.py:
```
class Y2:
    def value(self, t, v0=None):
        if v0 is not None:
            self.v0 = v0
        g = 9.81
        try:
            value = self.v0*t - 0.5*g*t**2
        except AttributeError:
            msg = 'You cannot call value(t)  without first '
                  'calling value(t, v0) to set v0'
            raise TypeError(msg)
        return value
```
Конечно, класс Y это лучшая реализация, чем Y2, поскольку имеет более простую форму. 

использование конструктора это хорошая привычка программирования, конструктор осуществляет удобную связь между «внешним миром» и классом. 

## Классы без классов

Класс содержит набор переменных (данных) и набор методов (функций). Набор переменных уникален для каждого экземпляра класса. То есть, если вы создадите десять экземпляров, каждый из них имеет свои переменные. Эти переменные можно представить как словарь, в котором ключами служат названия переменных. Каждый экземпляр тогда имеет свой словарь и, грубо говоря, мы можем рассматривать экземпляр как такой словарь.

С другой стороны, методы у всех экземпляров общие. Метод класса можно представить как обычную глобальную функцию, принимающую экземпляр в форме словаря как первый аргумент. Метод далее обращается к переменным в экземпляре (словаре), указанным при вызове. Для класса Y и экземпляра y, методы это обычные функции со следующими именами и аргументами:
```
Y.value(y, t)
Y.formula(y)
```
Класс представляется как пространство имен, то есть все его функции должны иметь префикс Y. Два разных класса, скажем С1 и С2 могут иметь функции с одним и тем же именем, например value, но при этом поскольку они относятся к разным классам, их имена становятся различны: С1.value и С2.value. Модули также представляют собой пространства имен для своих функций и переменных (math.sin, cmath.sin, numpy.sin)
Единственным отличием конструктора класса в Python является то, что он позволяет нам использовать другой синтаксис для вызова методов:
```
y.value(t)
y.formula()
```
Наш класс Y может быть реализован и так:
```
def value(self, t):
    return self['v0']*t - 0.5*self['g']*t**2

def formula(self):
    print 'v0*t - 0.5*g*t**2; v0=%g' % self['v0']
```
Представим эти две функции расположены в модуле Y 12.py:
```
import Y
y = {'v0': 4, 'g': 9.81}  # создаем "экземпляр"
y1 = Y.value(y, t)
```
Теперь у нас нет вообще никакого конструктора, поскольку нет и класса. Инициализация происходит при создании словаря y, но мы можем включить инициализацию и в модуль Y:
```
def init(v0):
    return {'v0': v0,  'g': 9.81}
```
Использование такого модуля-класса теперь выглядит более похожим на обычное:
```
import Y
y = Y.init(4)
y1 = Y.value(y, t)
```
И такая реализация вполне возможна и существует. На самом деле любой класс в Python имеет словарь-атрибут __dict__, который хранит все имеющиеся в экземпляре переменные 13.py:
```
y = Y(1.2)
print y.__dict__
{'v0': 1.2, 'g': 9.8100000000000005}
```
Классы (типы) — это объектные фабрики. Их главная задача — создавать объекты, обладающие определенным поведением.

Классы определяют поведение объектов с помощью своих атрибутов (которые хранятся в __dict__ класса): методов, свойств, классовых переменные, дескрипторов, а также с помощью атрибутов, унаследованных от родительских классов.

Инстанцирование обычного объекта происходит в 2 этапа: сначала его создание, потом инициализация. Соответственно, сначала запускается метод класса __new__, который возвращает объект данного класса, потом выполняется метод класса __init__, который инициализирует уже созданный объект.

def __new__(cls, ...) — статический метод (но его можно таковым не объявлять), который создает объект класса cls.

def __init__(self, ...) — метод класса, который инициализирует созданный объект.

```
class Car(object):

    wheels = 4
    def __init__(self, make, model):
        self.make = make
        self.model = model


mustang = Car('Ford', 'Mustang')
print mustang.wheels
# 4
print Car.wheels 
```

# Статические методы

Статические методы в Python являются синтаксическими аналогами статических функций в основных языках программирования. Они не получают ни экземпляр (self), ни класс (cls) первым параметром. Для создания статического метода (только «новые» классы могут иметь статические методы) используется декоратор staticmethod
```
class Car(object):

    wheels = 4
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @staticmethod
    def test(x):
        return x == 0
...

Car.test(1)    # доступ к статическому методу можно получать и через класс
False
f = Car()
f.test(0)    # и через экземпляр класса
True
```
Статические методы реализованы с помощью свойств (property).

```
# Static Methods
class Car(object):

    wheels = 4

    #Static Methods
    @staticmethod
    def make_car_sound(): 
        print 'VRooooommmm!'


    def __init__(self, make, model):
        self.make = make
        self.model = model


mustang = Car('Ford', 'Mustang')
print mustang.wheels
# 4
print Car.wheels 
# 4
mustang.make_car_sound()
Car.make_car_sound()

```
## Метод класса

Классовые методы в Python занимают промежуточное положение между статическими и обычными. В то время как обычные методы получают первым параметром экземпляр класса, а статические не получают ничего, в классовые методы передается класс. Возможность создания классовых методов является одним из следствий того, что в Python классы также являются объектами. Для создания классового (только «новые» классы могут иметь классовые методы) метода можно использовать декоратор classmethod
```
# Static Methods
class Car(object):

    wheels = 4

    #Static Methods
    @staticmethod
    def make_car_sound(): 
        print 'VRooooommmm!'

    # Class Methods
    @classmethod
    def is_motorcycle(cls):
        return cls.wheels == 2

    def __init__(self, make, model):
        self.make = make
        self.model = model


mustang = Car('Ford', 'Mustang')
print mustang.wheels
# 4
print Car.wheels 
# 4
mustang.make_car_sound()
Car.make_car_sound()

if mustang.is_motorcycle():
    print 'it is not a car'
else:
    print 'mustang is a car'

```
Классовые методы достаточно часто используются для перегрузки конструктора. Классовые методы, как и статические, реализуются через свойства (property).


car2.py
```

class Car(object):
    """A car for sale by Jeffco Car Dealership.

    Attributes:
        wheels: An integer representing the number of wheels the car has.
        miles: The integral number of miles driven on the car.
        make: The make of the car as a string.
        model: The model of the car as a string.
        year: The integral year the car was built.
        sold_on: The date the vehicle was sold.
    """

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Car object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this car as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the car."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return 8000 - (.10 * self.miles)

class Truck(object):
    """A truck for sale by Jeffco Car Dealership.

    Attributes:
        wheels: An integer representing the number of wheels the truck has.
        miles: The integral number of miles driven on the truck.
        make: The make of the truck as a string.
        model: The model of the truck as a string.
        year: The integral year the truck was built.
        sold_on: The date the vehicle was sold.
    """

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Truck object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this truck as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the truck."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return 10000 - (.10 * self.miles)


v = Car(4,10000,'Ford','Rodeo',2014,1)
print v.purchase_price()

t = Truck(4,10000,'Honda','Accord',2014,1)
print t.purchase_price()

```
## Наследование

Python поддерживает как одиночное наследование, так и множественное, позволяющее классу быть производным от любого количества базовых классов.
```
class Car(object):                # наследуем один базовый класс - object
        def name1(self): return 'Car'
class Truck(object):
        def name2(self): return 'Truck'
class Child(Car, Truck):           # создадим класс, наследующий Car, Truck (и, опосредованно, object)
        pass
x = Child()
x.name1(), x.name2()               # экземпляру Child доступны методы из Car и Truck
'Par1','Par2'
```
## одиночное наследование

car3.py
```
class Vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.

    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    base_sale_price = 0

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Vehicle object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on


    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

class Car(Vehicle):

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Car object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.base_sale_price = 8000


class Truck(Vehicle):

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Truck object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.base_sale_price = 10000

v = Car(4,10000,'Ford','Rodeo',2014,1)
print v.purchase_price()

t = Truck(4,10000,'Honda','Accord',2014,1)
print t.purchase_price()

```
Начиная с версии языка 2.6 в стандартную библиотеку включается модуль abc, добавляющий в язык абстрактные базовые классы 

позволяют определить класс, указав при этом, какие методы или свойства обязательно переопределить в классах-наследниках:
```
    @abstractmethod
    def vehicle_type():
        """"Return a string representing the type of vehicle this is."""
        pass

    @abstractproperty
        def speed():
        """Скорость объекта"""
```
car4.py
```
from abc import ABCMeta, abstractmethod
class Vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.


    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type():
        """"Return a string representing the type of vehicle this is."""
        pass
        
    @abstractproperty
        def speed():
        """Скорость объекта"""

class Car(Vehicle):

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Car object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.base_sale_price = 8000

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'car'


class Truck(Vehicle):

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Truck object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.base_sale_price = 10000

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'truck'

v = Car(4,10000,'Ford','Rodeo',2014,1)
print v.purchase_price()

t = Truck(4,10000,'Honda','Accord',2014,1)
print t.purchase_price()


```




