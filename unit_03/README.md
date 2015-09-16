# Списки

Списки в Python похожи на массивы в Perl 5. Там переменные, содержащие массивы, всегда начинаются с символа @; Точнее будет аналогия с Java-классом ArrayList, который может хранить произвольные объекты и динамически расширяться по мере добавления новых элементов. 

## Создание списка
впишите все значения, через запятую, в квадратных скобках. 

# пустой список

my_list = []

# список целых чисел
my_list = [1, 2, 3]

# смешаный список
my_list = [1, "Hello", 3.4]

```
a_list = ['a','b','mpilgrim','z','example']

a_list 

a_list[0]
```

# вложеный список
```
my_list = ["mouse", [8, 4, 6]]

```
## Список — это упорядоченный набор элементов. 

Список можно использовать как массив с нумерацией от нуля. Первый элемент не пустого списка будет всегда a_list[0]. 
Последним элементом пятиэлементного списка будет a_list[4]. 
Используя отрицательный индекс, можно обратиться к элементам по их номеру от конца списка. Последний элемент не пустого списка будет всегда a_list[-1]. 

```
my_list = ['p','r','o','b','e']
my_list[0]

my_list[2]

my_list[4]

my_list[4.0]

n_list = ["Happy", [2,0,1,5]]
n_list[0][1]    

n_list[1][3]    

my_list = ['p','r','o','b','e']
my_list[-1]

my_list[-5]

```

## Разрезание списка Slicing
a_list[0] — первый элемент спискаa_list. 
После того, как список создан, можно получить любую его часть в виде списка. Это называеться «slicing» — срез списка. 
```
a_list 

a_list[1:3]

a_list[1:-1]

a_list[0:3]

a_list[:3]

my_list = ['p','r','o','g','r','a','m','i','z']

my_list[:-5]    # elements beginning to 4th

my_list[5:]     # elements 6th to end

my_list[:]      # elements beginning to end

```
Вы можете получить часть списка, называемую «срезом», указав два индекса. В результате получается новый список, включающий в себя элементы исходного в том же порядке, начиная с первого индекса среза, до последнего, но не включая его. 

Срез работает, даже если один или оба индекса отрицательны. 

Если левый индекс среза — 0, вы можете опустить его, 0 будет подразумеваться. Так, a_list[:3] — это то же самое,что и a_list[0:3], потому что начальный 0 подразумевается. 

Аналогично, если правый индекс среза является длиной списка, вы можете его опустить. Так, a_list[3:] — это то же самое, что и a_list[3:5], потому что этот список содержит пять элементов. На самом деле, a_list[:n] всегда будет возвращать первые n элементов, а a_list[n:] будет возвращать все остальные, независимо от длины списка. 

Если оба индекса списка опущены, включаются все элементы списка. Но это не то же самое, что первоначальная переменная a_list. Это новый список, включающий все элементы исходного. Запись a_list[:] представляет собой простейший способ получения полной копии списка. 

## Добавление элементов в список
Существует четыре способа добавить элементы в список. 
```
odd = [2, 4, 6, 8]    

odd[0] = 1            # меняем 1 элемент

odd[1:4] = [3, 5, 7]  # меняем элементы со 2 по 4


```
Оператор + соединяет списки, создавая новый список. Однако, если вы заботитесь о памяти, знайте, что сложение списков создает ещё один список в памяти. В данном случае, этот новый список немедленно присваивается существующей переменной a_list. 
```
a_list = ['a'] 

a_list =a_list + [2.0, 3]

["re"] * 3

```

- Метод append() добавляет один элемент в конец списка.
Списки реализованы как классы. «Создание» списка — это фактически создание экземпляра класса.

```
odd.append(7)


```

- Метод extend() принимает один аргумент — список, и добавляет каждый его элемент к исходному списку. 

```

odd.extend([9, 11, 13])

```

- Метод insert() вставляет элемент в список. Первым аргументом является индекс первого элемента в списке, который будет сдвинут новым элементом со своей позиции. Элементы списка не обязаны быть уникальными; 

```
a_list.append(True)

a_list.extend(['four','Ω'])

a_list.insert(0, 'Ω')
```
В Python конструкция a_list.insert(0, value) действует как функция unshift() в Perl. Она добавляет элемент в начало списка, а все другие элементы увеличивают свой индекс на единицу, чтобы освободить пространство. 

## рассмотрим разницу между append() и extend(). 
```
a_list = ['a', 'b', 'c'] 
a_list.extend(['d', 'e', 'f'])
a_list 

len(a_list)

a_list[-1] 

a_list.append(['g', 'h', 'i'])
a_list 

len(a_list)

a_list[-1] 

```
Метод extend() принимает один аргумент, который всегда является списком, и добавляет каждый элемент этого списка к a_list. 

метод append() получает единственный аргумент, который может быть любого типа. 

## Поиск значений в списке
```
a_list = ['a', 'b', 'new', 'mpilgrim', 'new'] 
```
- метод count возвращает количество вхождений указанного значения в список. 
```
a_list.count('new') 
```
Если всё, что вам нужно — это узнать, присутствует ли значение в списке или нет, тогда оператор in намного быстрее, чем метод count(). Оператор in всегда возвращает True или False; он не сообщает, сколько именно в списке данных значений. 

```
'new' in a_list 

'c' in a_list 
```
Если вам необходимо точно знать, на каком месте в списке находится какое-либо значение, то используйте метод index(). 

```
a_list.index('mpilgrim') 

```
По умолчанию, он просматривает весь список, но вы можете указать вторым аргументом индекс (отсчитываемый от нуля), с которого необходимо начать поиск, и третий аргумент — индекс, на котором необходимо остановить поиск. 

Метод index() находит только первое вхождение значения в списке. если значение не найдено в списке, то метод index() возбудит исключение. 

## Удаление элементов из списка 

- Списки никогда не содержат разрывов. 
- Списки могут увеличиваться и сокращаться автоматически.  

```
a_list =['a', 'b', 'new', 'mpilgrim', 'new'] 
del a_list[1] 
a_list 
```
Можно использовать выражение del для удаления определенного элемента из списка. 
Все элементы после удаления смещают свои индексы, чтобы «заполнить пробел», возникший после удаления элемента. 

Можно удалить элемент из списка при помощи метода remove(). Метод remove() в качестве параметра принимает значение и удаляет первое вхождение этого значения из списка. Кроме того, индексы всех элементов, следующих за удалённым, будут сдвинуты, чтобы «заполнить пробел». Списки никогда не содержат разрывов. 

```
a_list.remove('new')
a_list 

a_list.remove('new') 
```
Можно вызывать метод remove() столько, сколько хотите, однако если попытаться удалить значение, которого нет в списке, будет порождено исключение. 

Метод pop() — это еще один способ удалить элементы из списка. 

```
a_list = ['a', 'b', 'new', 'mpilgrim'] 
a_list.pop() 

a_list 
```

Если вызвать pop() без аргументов, он удалит последний элемент списка и вернет удаленное значение. 
С помощью метода pop() можно удалить любой элемент списка. Просто вызовите метод с индексом элемента. Этот элемент будет удалён, а все элементы после него сместятся, чтобы «заполнить пробел». Метод возвращает удалённое из списка значение. 

- Метод pop() для пустого списка возбуждает исключение. 

Вызов метода pop() без аргументов эквивалентен вызову функции pop() в Perl. Он удаляет последний элемент из списка и возвращает удалённое значение. В языке программирования Perl есть также функция shift(), которая удаляет первый элемент и возвращает его значение. В Python это эквивалентно a_list.pop(0). 

- Пустые списки — ложь, все остальные — истина. 

- В логическом контексте пустой список — ложь. 
- Любой список, состоящий хотя бы из одного элемента, — истина. 
- Любой список, состоящий хотя бы из одного элемента, — истина. Значения элементов не важны. 

Список может содержать объекты любого типа, включая другие списки: 

```
a = ['Dave', 'Mark', ['Dave', 2, 99, [100,200]], 'Ann', [22, 33 ,77],'Phil'] 

print(a[1]) 
print(a[2][2]) 
print(a[2][3][1]) 

# A 3 x 3 matrix, as nested lists

M = [ [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9] ]

print M
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Get row 2

print M[1]
[4, 5, 6]

# Get row 2, then get item 3 of that row

print M[1][2]
6

```
Можно менять как отдельные элементы списка, так и диапазон:
```
lst[3] = 'piano'
lst[0:2] = [1,2]
lst
```

Вставка:
```
lst[1:1] = ['guitar','microphone']
lst
```

Можно сделать выборку из списка с определенной частотой:
```
numbers = [1,2,3,4,5,6,7,8,9,0]
numbers[::4]
```

# Создание копии списка. 

- L1 = L2[:] — создание второй копии списка. Здесь создается вторая копия обьекта. 
- L1 = list(L2) — тоже создание второй копии списка. 
- L1 = L2 — создание второй ссылки, а не копии. 3-й вариант показывает, что создаются две ссылки на один и тот же обьект, а не две копии. 

# Умножение, или повтор списков: 
```
   L1 * 2 
```
# sort() — сортировка списка: 
```
lst.sort() 
```
# reverse() — реверс списка: 
```
lst.reverse() 
a.sort() 
print a 
print a*2 
print '--'*40 
print a 
print '--'*40 
a.reverse() 
print a
```
# len() — длина списка: 
```
len(lst) 
```
# max() — максимальный элемент списка: 
```
max(lst) 
```
# min() — минимальный элемент списка: 

Преобразовать все значения из строк в числа с плавающей точкой 
Вывести минимальное и максимальное значения 

```
# -*- coding:utf-8 -*-

lines = [1,2,4,66,88,-33,667,3.4,55,99,7.1234,499]

fvalues = [float(line) for line in lines] 

print 'Минимальное значение: ', min(fvalues) 
print 'Максимальное значение: ', max(fvalues)

```

# простая итерация списка: 
```
  for x in L: 
```

# сортированная итерация: 
```
  for x in sorted(a): 
    print x 
```

# уникальная итерация: 
```
  for x in set(L): 
```
# итерация в обратном порядке: 
```
for x in reversed(L): 
  l = range(80) 

for x in sorted(l): 
    print x, 

for x in reversed(l): 
    print x, 

for x in set(l): 
    print x, 
```

# исключающая итерация — например, вывести элементы 1-го списка, которых нет во 2-м списке: 

```
for item in set(L).difference(L2)

l2 = l[0:-1:3] 
for x in set(l).difference(l2): 
    print x, 
```


# Операция Sequence unpacking — присваивание списку переменных списка значений: 

```
a, b = [1,2] 

```
# Стек и очереди 
## Список можно использовать как стек — когда последний добавленный элемент извлекается первым (LIFO, last-in, first-out). Для извлечения элемента с вершины стека есть метод pop(): 

```
stack = [1,2,3,4,5]  
stack.append(6) 
stack.append(7) 
stack.pop() 
stack 
```
## Список можно использовать как очередь — элементы извлекаются в том же порядке, в котором они добавлялись (FIFO, first-in, first-out). Для извлечения элемента используется метод pop() с индексом 0: 

```
queue = ['rock','in','roll']  
queue.append('alive') 
queue.pop(0) 
queue 
```
# Удаление элементов списка по условию
Допустим, у нас есть список чисел, из которого надо удалить элементы, удовлетворяющие определенному условию. Будем удалять из списка, состоящего из 20 чисел в диапазоне от 0 до 100, все элементы, которые больше 35 и меньше 65. При этом удаляемые числа сохраним в другом списке.

В Python с помощью инструкции del можно удалить элемент списка, указав сам список и индекс удаляемого элемента.
Алгоритм решения задачи выглядит вроде бы простым: достаточно перебрать элементы списка и удалить те, которые удовлетворяют условию. Но все не так просто. При удалении элемента на его место становится следующий, но поскольку мы переходим к следующему элементу, то пропускаем проверку того, что стал на место удаленного. Цикл for использовать нельзя, т.к. меняется количество элементов списка.

Можно использовать цикл while, измеряя на каждой его итерации длину списка, индекс же увеличивать только в том случае, если удаления элемента не произошло.
```
import random 
 
a = [] 
for i in range(20): 
    n = round(random.random() * 100) # от 0 до 100 включительно 
    a.append(n) 
print("A =",a) 
 
b = [] 
i = 0 
while i < len(a): 
    if 35 < a[i] < 65: 
        b.append(a[i]) 
        del a[i] 
    else: 
        i += 1 
print("A =",a) 
print("B =",b)
```

## Поверхностная копия списка (python 3.3)

```
list.copy()
```
## Очищает список (python 3.3)
```
list.clear()
```

## Lambda, filter, reduce и map

### Lambda Operator
```

f = lambda x, y : x + y
f(1,1)
```
### map() Function

map() имеет 2 аргумента:

```
r = map(func, seq)
```

### пример fahrenheit() и celsius()

```
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5,39)

F = map(fahrenheit, temp)
C = map(celsius, F)
```

Используем lambda:

```
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)

print Fahrenheit
[102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]

C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
print C

[39.200000000000003, 36.5, 37.300000000000004, 37.799999999999997]
 
```

Использование map() к нескольким спискам. 

```
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]

map(lambda x,y:x+y, a,b)
[18, 14, 14, 14]

map(lambda x,y,z:x+y+z, a,b,c)
[17, 10, 19, 23]

map(lambda x,y,z:x+y-z, a,b,c)
[19, 18, 9, 5]

```

## Filtering

function filter(function, list) 

```
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)

print result

[1, 1, 3, 5, 13, 21, 55]

result = filter(lambda x: x % 2 == 0, fib)
print result
[0, 2, 8, 34]
```
 
## Reducing 

function reduce(func, seq) 

```
reduce(lambda x,y: x+y, [47,11,42,13])
113
```

Вычисление maximum:
```
f = lambda a,b: a if (a > b) else b
reduce(f, [47,11,42,102,13])
102

```
Вычисление sum:
```
reduce(lambda x, y: x+y, range(1,101))
5050
```

## Списковое включение list comprehension

Абстракция списков, списковое включение (list comprehension) в синтаксисе языка программирования — компактное описание операций обработки списков.

Списковое включение позволяет вычислять и бесконечные списки (в языках, которые их поддерживают). 

В аксиоматике теории множеств Цермело-Френкеля есть аксиома выделения, которая позволяет строить множество на основе имеющегося, путём выбора элементов, соответствующих некоторому предикату. Абстракция списков является аналогией выделения для списков

- В языке Python есть и выражения-генераторы, которые имеют схожий со списковыми включениями синтаксис, но возвращают итератор. Сумма чётных чисел из предыдущего примера:

```
sum((n for n in range(1, 10000) if n % 2 == 0))
```

# Для генерации списков, кроме статической формы, можно использовать конструктор списков — list comprehension — цикл внутри квадратных скобок — на примере списка квадратов первых 10 натуральных чисел: 

```
a = [ i*i for i in range(1,10)] 
```

- Чётные числа от 2 до 9998 включительно:
```
[n for n in range(1, 10000) if n % 2 == 0]
```

# Конструктор может быть условным — найдем квадраты четных натуральных чисел: 
```
a = [ i*i for i in range(1,10) if i % 2 == 0] 
```
- Списковые включения могут использовать вложенные итерации по переменным:
```
[(x, y) for x in range(1, 10) for y in range(1, 10) if x % y == 0]
```

# С помощью конструктора решим конкретную задачу — отсортируем слова в предложении в порядке их длительности: 

```
words = ' to perform the task of sorting the words in a string by their length'.split() 
wordlens = [(len(word), word) for word in words] 
wordlens.sort() 
print ' '.join(w for (_, w) in wordlens) 

new_range = [i * i for i in range(5) if i % 2 == 0]
print new_range
```

```
print [x+y for x in 'spam' for y in 'SPAM']

print [(x,y) for x in range(5) if x%2 == 0 for y in range(5) if y%2 == 1]

listoftuple = [('bob', 35, 'mgr'), ('mel', 40, 'dev')]

print [age for (name, age, job) in listoftuple]

print map((lambda (name, age, job): age), listoftuple)

# List comprehensions provide a concise way to create lists without resorting to use 
# of map(), filter() and/or lambda. 

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print [weapon.strip() for weapon in freshfruit]

vec = [2, 4, 6]
print [3*x for x in vec]

print [3*x for x in vec if x > 3]

print [3*x for x in vec if x < 2]

print [[x,x**2] for x in vec]

print [(x, x**2) for x in vec]

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]

print [x*y for x in vec1 for y in vec2]

print [x+y for x in vec1 for y in vec2]

print [vec1[i]*vec2[i] for i in range(len(vec1))]


print [str(round(355/113.0, i)) for i in range(1,6)]


S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]
 
print S; print V; print M

#First build a list of non-prime numbers, using a single list comprehension, 
#then use another list comprehension to get the "inverse" of the list, 
#which are prime numbers.

noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print primes

params = {"Key 1":"value 1", "key 2":"value 2", "key 3":"value 3", "key 4":"value 4"} 
print params.items() 

print [k for k, v in params.items()]                    

print [v for k, v in params.items()]                     

print ["%s=%s" % (k, v) for k, v in params.items()] 


```

# Collect the items in column 2
```
M = [ [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9] ]



col2 = [A[1] for A in M]
print col2
[2, 5, 8]

print M
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

```

# Add 10 to each item in column 2
```
[A[1] + 10 for A in M]
[12, 15, 18]
```
# Filter out odd items
```
[A[1] for A in M if A[1] % 2 == 0]
[2, 8]
```

# Collect a diagonal from matrix
```
diag = [M[i][i] for i in [0, 1, 2]]
print diag
[1, 5, 9]
```
# Repeat characters in a string
```
doubles = [ c * 2 for c in 'blah']
print doubles
['bb', 'll', 'aa', 'hh']
```

# Create a generator of row sums

G = (sum(A) for A in M)

# iter(G) not required here
```
print next(G)
6
```
# Run the iteration protocol
```
print next(G)
15
print next(G)
24
```

# Map sum over items in M
```
print list(map(sum,M))
[6, 15, 24]
```

# List of character ordinals
```
print [ord(x) for x in 'google']
[103, 111, 111, 103, 108, 101]
```

## List Comprehension vs. map

Функция ord возвращает ASCII код символа:
```
ord('A')
65
```

Использование for:
```
result = []
for x in 'Dostoyevsky':
    result.append(ord(x))
    
print result
[68, 111, 115, 116, 111, 121, 101, 118, 115, 107, 121]
 
```

Использование map:
```
result = list(map(ord,'Dostoyevsky'))
print result
[68, 111, 115, 116, 111, 121, 101, 118, 115, 107, 121]

```

list comprehension expression:

```
result = [ord(x) for x in 'Dostoyevsky']
result
[68, 111, 115, 116, 111, 121, 101, 118, 115, 107, 121]

``` 

Использование lambda вместо def:

```
list(map((lambda x: x ** 2),range(5)))
[0, 1, 4, 9, 16]
```

### List Comprehension аналог filter

```
[x for x in range(10) if x % 2 == 0]
[0, 2, 4, 6, 8]

list(filter((lambda x: x % 2 == 0), range(10)))
[0, 2, 4, 6, 8]

result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x)
    
print result
[0, 2, 4, 6, 8]
``` 

Условия:
```
[x ** 2 for x in range(10) if x % 2 == 0]
[0, 4, 16, 36, 64]
``` 

Фильтрация:
```
list( map((lambda x: x ** 2), filter((lambda x: x % 2== 0),range(10))) )
[0, 4, 16, 36, 64]
```

Циклы:

```
result = []
result = [ x ** y for x in [10, 20, 30] for y in [2, 3, 4]]
print result
[100, 1000, 10000, 400, 8000, 160000, 900, 27000, 810000]


result = []
for x in [10, 20, 30]:
    for y in [2, 3, 4]:
        result.append(x ** y)
        
print result
[100, 1000, 10000, 400, 8000, 160000, 900, 27000, 810000]
``` 

генерация последовательностей:

```
[x + y for x in 'ball' for y in 'boy']
['bb', 'bo', 'by', 'ab', 'ao', 'ay', 'lb', 'lo', 'ly', 'lb', 'lo', 'ly']
``` 
генерация последовательностей:
```
[(x,y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
[(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]
```

Аналог

```
result = []
for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                result.append((x,y))
                
print result
[(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]
``` 

## Работа с матрицами
3 x 3 matrixes:
```
M1 = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

M2 = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]


M1[2]
[7, 8, 9]

M1[2][2]
9
```
Извлечение колонки из матрицы:
```
[r[2] for r in M1]
[3, 6, 9]

[M1[r][2] for r in (0, 1, 2)]
[3, 6, 9]

```
Использование List Comprehension

Реализация математических формул  { x2 | x ∈ ℕ } или { (x,y) | x ∈ ℤ ∧ y ∈ ℤ }. 

### Создание треугольников Пифагора:
```
[(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]

[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (10, 24, 26), (12, 16, 20), (15, 20, 25), (20, 21, 29)]
```

### Пересечение двух свойств продукта
```
colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print coloured_things
[('red', 'house'), ('red', 'car'), ('red', 'tree'), ('green', 'house'), ('green', 'car'), ('green', 'tree'), ('yellow', 'house'), ('yellow', 'car'), ('yellow', 'tree'), ('blue', 'house'), ('blue', 'car'), ('blue', 'tree')]
``` 

## Generator Comprehension

Calculation of the prime numbers between 1 and 100 using the sieve of Eratosthenes:

```
noprimes = [j for i in range(2, 8) for j in range(i*2, 100, i)]
primes = [x for x in range(2, 100) if x not in noprimes]
print primes

``` 

We want to bring the previous example into more general form, so that we can calculate the list of prime numbers up to an arbitrary number n:

```
from math import sqrt

n = 100
sqrt_n = int(sqrt(n))
no_primes = [j for i in range(2,sqrt_n) for j in range(i*2, n, i)]

print no_primes

```
### Recursive Function to Calculate the Primes

```
from math import sqrt
def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = {j for i in p for j in xrange(i*2, n+1, i)}
        p = {x for x in xrange(2, n + 1) if x not in no_p}
    return p

for i in range(1,50):
    print i, primes(i) 

```

# Кортежи (Tuple)
Кортеж — это неизменяемый список. Кортеж не может быть изменён никаким способом после его создания. 

Для создания простейших структур данных можно использовать кортежи, которые позволяют упаковывать коллекции значений в единый объект. Кортеж создается заключением группы значений в круглые скобки, 
```
stock = (‘GOOG’, 100, 490.10)
address = (‘www.python.org’, 80) 
person = (first_name, last_name, phone) 
```
Интерпретатор Python часто распознает кортежи, даже если они не заключены в круглые скобки: 
```
stock = ‘GOOG’, 100, 490.10 
address = ‘www.python.org’,80 
person = first_name, last_name, phone 
```
Для полноты можно отметить, что имеется возможность определять кортежи, содержащие 0 или 1 элемент, для чего используется специальный синтаксис: 
```
a = () 
print(type(a)) 
```
# Кортеж с нулевым количеством элементов (пустой кортеж) 
```
b = ('item',) # Кортеж с одним элементом (обратите внимание на запятую в конце) 
print(type(b)) 
c = 'item', # Кортеж с одним элементом (обратите внимание на запятую в конце) 
print(type(c))
print tuple('abc') 

t = 1,[2,3] 
t[1].append(4) 
print t
```
Элементы кортежа могут извлекаться с помощью целочисленных индексов, как и в случае со списками. Однако более часто используется прием распаковывания кортежей во множество переменных, как показано ниже: 
```
name, shares, price = stock 
print(price) 
host, port = address 
print(host) 
first_name, last_name, phone = person 
print(phone)
```
Кортежи поддерживают практически те же операции, что и списки (такие как доступ к элементам по индексу, извлечение среза и конкатенация), тем не менее содержимое кортежа после его создания невозможно изменить (то есть нельзя изменить, удалить или добавить новый элемент в существующий кортеж). По этой причине кортеж лучше рассматривать как единый объект, состоящий из нескольких частей, а не как коллекцию отдельных объектов, в которую можно вставлять новые или удалять существующие элементы. 

Вследствие большого сходства кортежей и списков некоторые программисты склонны полностью игнорировать кортежи и использовать списки, потому что они выглядят более гибкими. Хотя в значительной степени это так и есть, тем не менее, если в программе создается множество небольших списков (когда каждый содержит не более десятка элементов), то они занимают больший объем памяти, по сравнению с кортежами. Это обусловлено тем, что для хранения списков выделяется немного больше памяти, чем требуется, – с целью оптимизировать скорость выполнения операций, реализующих добавление новых элементов. Так как кортежи доступны только для чтения, для их хранения используется меньше памяти, т. к. дополнительное пространство не выделяется. 


# Словари
Словарь — это неупорядоченное множество пар ключ—значение. Когда вы добавляете ключ в словарь, вы также должны добавить и значение для этого ключа. (Значение всегда можно изменить позже.) Словари в Python оптимизированы для получения значения по известному ключу. 

Словарь в Python аналогичен хэшу в Perl 5. В Perl 5 переменные, хранящие хэши, всегда начинаются с символа %. В Python переменные могут быть названы как угодно, язык сам отслеживает типы данных. 

## Создание словаря
Создать его можно несколькими способами. Во-первых, с помощью литерала: 
```
d = {} 
d = {'dict': 1, 'dictionary': 2} 
```
Синтаксис похож на синтаксис создания множеств, но вместо элементов, используются пары ключ-значение. 

Если у вас есть словарь, вы можете просматривать значения по их ключу. 
```
a_dict = {'server': 'localhost','database':'mysql'} 

print(a_dict) 
print(a_dict['server']) 
print(a_dict['database'])

```

Во-вторых, с помощью функции dict: 
```
d = dict(short='dict', long='dictionary') 
d = dict([(1, 1), (2, 4)]) 
```
В-третьих, с помощью метода fromkeys: 
```
d = dict.fromkeys(['a', 'b']) 
d = dict.fromkeys(['a', 'b'], 100) 
```
В-четвертых, с помощью генераторов словарей, которые очень похожи на генераторы списков. 
```
d = {a: a ** 2 for a in range(7)} 
```
Теперь попробуем добавить записей в словарь и извлечь значения ключей: 
```
d = {1: 2, 2: 4, 3: 9} 
d[1] 

d[4] = 4 ** 2 
d 
{1: 2, 2: 4, 3: 9, 4: 16} 

```
Как видно из примера, присвоение по новому ключу расширяет словарь, присвоение по существующему ключу перезаписывает его, а попытка извлечения несуществующего ключа порождает исключение. 

## Изменение словаря
Словари не имеют какого-либо предопределенного ограничения размера. Когда угодно можно добавлять новые пары ключ—значение в словарь или изменять значение, соответствующее существующему ключу. Продолжим предыдущий пример: 
```
a_dict = {'server': 'localhost','database':'mysql'} 

print(a_dict) 
print(a_dict['server']) 
print(a_dict['database']) 

a_dict['database'] = 'blog' 
print(a_dict['database']) 

a_dict['user'] = 'root' 
print(a_dict['user']) 

print(a_dict)
```
### Словари со смешанными значениями

Словари могут состоять не только из строк. Значения словарей могут быть любого типа, включая целые, логические, произвольные объекты, или даже другие словари. И значения в одном словаре не обязаны быть одного и того же типа; можно смешивать и сочетать их, как вам необходимо. Ключи словаря более ограниченны, но они могут быть строками, целыми числами и некоторыми другими типами. Ключи разных типов тоже можно смешивать и сочетать в одном словаре. 
```
a_dict = {'server': 'localhost','database':'mysql',1000:['KB','MB','GB'],1024:['KiB','MiB','GiB']} 

print(a_dict) 
print(len(a_dict)) 

if 1000 in a_dict: 
    print('1000 in dict') 
else: 
    print('not in dict') 

print(a_dict[1000]) 

print(a_dict[1024]) 

print(a_dict[1024][2]) 
```
## Методы словарей
- dict() — создание словаря;
- dict.clear() - очищает словарь.
- dict.copy() - возвращает копию словаря.
- deepcopy() — создает полную копию словаря;
- dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).
- dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).
- has_key() — проверка значения по ключу;

- dict.items() - возвращает пары (ключ, значение).
- iteriyems() — возвращает итератор;
- dict.keys() - возвращает ключи в словаре.
- iterkeys() — возвращает итератор ключей;
- len() — возвращает число пар;
- dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).
- dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.
- dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ с значением default (по умолчанию None).
- dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
- dict.values() - возвращает значения в словаре.

- itervalues() — возвращает итератор на список значений.
- in — оператор, проверяет наличие значения по ключу;
- del — оператор, удаляет пару по ключу;
- dict() — конструирует словарь с помощью последовательности.




# 1.py Telephone Numbers
```
# -*- coding:utf-8 -*-

def print_numbers(numbers):
    print("Telephone Numbers:")
    for k, v in numbers.items():
        print "Name:", k, "\tNumber:", v
    print()
 
def add_number(numbers, name, number):
    numbers[name] = number
 
def lookup_number(numbers, name):
    if name in numbers:
        return "The number is " + numbers[name]
    else:
        return name + " was not found"
 
def remove_number(numbers, name):
    if name in numbers:
        del numbers[name]
    else:
        print(name," was not found")
 
def load_numbers(numbers, filename):
    pass
 
def save_numbers(numbers, filename):
    pass
 
def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Load numbers')
    print('6. Save numbers')
    print('7. Quit')
    print()
 
phone_list = {}

menu_choice = 0

print_menu()

while True:
    menu_choice = int(input("Type in a number (1-7): "))
    if menu_choice == 1:
        print_numbers(phone_list)
    elif menu_choice == 2:
        print("Add Name and Number")
        name = raw_input("Name: ")
        phone = raw_input("Number: ")
        add_number(phone_list, name, phone)
    elif menu_choice == 3:
        print("Remove Name and Number")
        name = raw_input("Name: ")
        remove_number(phone_list, name)
    elif menu_choice == 4:
        print("Lookup Number")
        name = raw_input("Name: ")
        print(lookup_number(phone_list, name))
    elif menu_choice == 5:
        filename = raw_input("Filename to load: ")
        load_numbers(phone_list, filename)
    elif menu_choice == 6:
        filename = raw_input("Filename to save: ")
        save_numbers(phone_list, filename)
    elif menu_choice == 7:
        break
    else:
        print_menu()
 
print("Goodbye")

```
# 2.py Telephone Numbers
```
# -*- coding:utf-8 -*-


def print_numbers(numbers):
    print("Telephone Numbers:")
    for k, v in numbers.items():
        print("Name:", k, "\tNumber:", v)
    print()
 
def add_number(numbers, name, number):
    numbers[name] = number
 
def lookup_number(numbers, name):
    if name in numbers:
        return "The number is " + numbers[name]
    else:
        return name + " was not found"
 
def remove_number(numbers, name):
    if name in numbers:
        del numbers[name]
    else:
        print(name," was not found")
 
def load_numbers(numbers, filename):
    in_file = open(filename, "rt")
    while True:
        in_line = in_file.readline()
        if not in_line:
            break
        in_line = in_line[:-1]
        name, number = in_line.split(",")
        numbers[name] = number
    in_file.close()
 
def save_numbers(numbers, filename):
    out_file = open(filename, "wt")
    for k, v in numbers.items():
        out_file.write(k + "," + v + "\n")
    out_file.close()
 
def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Load numbers')
    print('6. Save numbers')
    print('7. Quit')
    print()
 
phone_list = {}
menu_choice = 0
print_menu()
while True:
    menu_choice = int(input("Type in a number (1-7): "))
    if menu_choice == 1:
        print_numbers(phone_list)
    elif menu_choice == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        add_number(phone_list, name, phone)
    elif menu_choice == 3:
        print("Remove Name and Number")
        name = input("Name: ")
        remove_number(phone_list, name)
    elif menu_choice == 4:
        print("Lookup Number")
        name = input("Name: ")
        print(lookup_number(phone_list, name))
    elif menu_choice == 5:
        filename = input("Filename to load: ")
        load_numbers(phone_list, filename)
    elif menu_choice == 6:
        filename = input("Filename to save: ")
        save_numbers(phone_list, filename)
    elif menu_choice == 7:
        break
    else:
        print_menu()
 
print("Goodbye")

```
