# 21-python

- Объектно-ориентированное программирование на Python

# Расширенная работа с файлами в Python.
Для доступа к более широкому функционалу в работе с файлами в Python, как то удаление файлов, создание директорий и т.д. Следует подключить библиотеку os.

# Переименовать или удалить файл
```
os.rename(current_file_name, new_file_name)
import os

# Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt" )
os.remove(file_name)
import os
# Delete file test2.txt
os.remove("text2.txt")

os.mkdir("newdir")
import os
# Create a directory "test"
os.mkdir("test")
os.chdir("newdir")
import os

# Changing a directory to "/home/newdir"
os.chdir("/home/newdir")
os.getcwd()
import os
os.getcwd()
os.rmdir('dirname')
import os

# This would  remove "/tmp/test"  directory.
os.rmdir( "/tmp/test"  )
```

# Пример скрипта который сам создает файлы Python c баш-строкой.
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
myfile = open("newfile.py", "w")
myfile.write("#!/usr/bin/env python\n# -*- coding: utf-8 -*-")
myfile.close()
```

# Скачать и сохранить файл, используя Python

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
url = "http://www.google.ru/index.html"
import urllib
webFile = urllib.urlopen(url)
localFile = open(url.split('/')[-1], 'wb')
localFile.write(webFile.read())
webFile.close()
localFile.close()

```

# IOError except для обработки исключений

```
def FileCheck(fn):
    try:
      open(fn, "r")
      return 1
    except IOError:
      print "Error: File does not appear to exist."
      return 0
    finally:
              fn.close()

```
# FileNotFoundError except для обработки исключений
```
while True:
    prompt = input("\n Hello to my valitator,"
    "\n \n Please type in the path to your file and press 'Enter': ")
    try:
        sudoku = open(prompt, 'r').readlines()
    except FileNotFoundError:
        print("Wrong file or file path")
    else:
        break

```
# errno

```
import os, errno

try:
    f = open('asdfasdf', 'r')
except IOError, ioex:
    print 'errno:', ioex.errno
    print 'err code:', errno.errorcode[ioex.errno]
    print 'err message:', os.strerror(ioex.errno)


```

# Оператор with - автоматическое закрытие файла

```
with open("poem.txt") as f:
    for line in f:
        print(line, end='')

```
Try/Except
```
import os 

def save_to_db(filename,mystaff):
    out_file = open(filename, "wt")
    for emp in mystaff.employee_list:
        out_file.write(str(emp)+ "\n")
    out_file.close()


def save_to_db(filename,mystaff):
    try:
      out_file = open(filename, "wt")
      try:
        for emp in mystaff.employee_list:
          out_file.write(str(emp)+ "\n")
      finally:
        out_file.close()
    except (os.error, IOError) as ex: 
      print "Cannot process file", filename, ": Error is", ex 



def load_from_db(filename,mystaff):
    lines = [line.rstrip('\n') for line in open(filename)]

    for line in lines:
        list = line.split(',')
        mystaff.add_employee(list[1],list[2], float(list[0]), list[3], int(list[4]), int(list[5]),int(list[6]))

def load_from_db(filename,mystaff):
    try:
        lines = [line.rstrip('\n') for line in open(filename)]
    except IOError:
        print "Error: File does not appear to exist."

    for line in lines:
        list = line.split(',')
        mystaff.add_employee(list[1],list[2], float(list[0]), list[3], int(list[4]), int(list[5]),int(list[6]))

```

лучше ловить как можно более конкретные классы исключений 

```

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def print_staff(): 
    try: 
        n = 0 
        for emp in mystaff.employee_list: 
            n += 1 
            print(emp) 

        if n==0 : 
            raise MyError(2) 
    except MyError as e: 
        print '\nНет данных о сотрудниках :', e.value 
    else: 
        print  'Хранилище содержит ', n, ' строк' 
    finally: 
        print  'Дата проверки состояния записей ', datetime.now() 

```

# используем операторы try и except, чтобы корректно и красиво завершить скрипт 

``` 
'''функция диалога. 
Первым аргументом принимаем ответ пользователя, 
вторым - выдаём сообщение при неверном вводе''' 

def answer(prompt, choice='Только Yes или no!'): 
        while True: 
                result = raw_input(prompt) 
                if result in ('y', 'Y', 'yes', 'Yes'): 
                        print '\nВы выбрали "YES" - заканчиваем\n' 
                        '''тут можно использовать оператор break вместо return 
                        так же и в ответе No''' 
                        return False 
                elif result in ('n', 'N', 'no', 'No'): 
                        print "\nВы выбрали NO - Я продолжаю работу...\n" 

                        print_menu() 
                        return True 
                else: 

                        print(choice) 
``` 

- при Ctrl+C (KeyboardInterrupt - SIGINT) 
- или Ctrl+D (EOFError - SIGQUIT) команда 
```

elif menu_choice == '7': 
    try: 
        if  (answer("\nВы уверены, что хотите закончить работу? ('y' или 'n', Ctrl+C для выхода) ")==False): 
            break 
    except (KeyboardInterrupt, EOFError): 
        exit('\nВыход\n') 

``` 

## __setattr__  __getattr__
```
# -*- coding: utf-8 -*-

class Private:
    def __init__(self, names):
        self.__names = names
        self.__data = {}
    def __getattr__(self, name):
        if name in self.__names:
            return self.__data[name]
        raise AttributeError(name)
    def __setattr__(self, name, value):
        if name.startswith("_Private"):
            self.__dict__[name] = value
            return
        if name in self.__names:
            self.__data[name] = value
            return
        raise TypeError("cannot set the attribute %r" % (name,))

class Person(Private):
    """ Класс person.

    """
    def __init__(self, parent = None):
        Private.__init__(self, ["first_name", "last_name", 'id', "age", 'city', "addr", "parent"])
        self.parent = parent
    def new_child(self):
        return Person(self)


# -*- coding: utf-8 -*-
import person


dad = person.Person()
"first_name", "last_name", 'id', "age", 'city', "addr", "parent"
dad.first_name = "Jason"
dad.last_name = "Koo"
dad.id = 1123
dad.age = 23
dad.city = 'Kiev'
kid = dad.new_child()
kid.first_name = "Rachel"
kid.age = 2
print "Kid's parent is", kid.parent.first_name, kid.parent.last_name
#=>Kid's parent is Jason

```
__str__()

```
# -*- coding: utf-8 -*-

class Private:
    def __init__(self, names):
        self.__names = names
        self.__data = {}
    def __getattr__(self, name):
        if name in self.__names:
            return self.__data[name]
        raise AttributeError(name)
    def __setattr__(self, name, value):
        if name.startswith("_Private"):
            self.__dict__[name] = value
            return
        if name in self.__names:
            self.__data[name] = value
            return
        raise TypeError("cannot set the attribute %r" % (name,))

class Person(Private):
    """ Класс person.

    """
    def __init__(self, parent = None):
        Private.__init__(self, ["first_name", "last_name", 'id', "age", 'city', "addr", "parent"])
        self.parent = parent

    def __str__(self):
        return ''.join((self.first_name.lower().title(),' ', self.last_name.lower().title()))
    
    def new_child(self):
        return Person(self)

```

calc.py
```
# -*- coding: utf-8 -*-

import re
_places_re = re.compile(r"\.(\d+)")

default_places = 0

class FixNum:
    def __init__(self, value, places = None):
        self.value = value
        if places is None:
            # get from the value
            m = _places_re.search(str(value))
            if m:
                places = int(m.group(1))
            else:
                places = default_places
        self.places = places

    def __add__(self, other):
        return FixNum(self.value + other.value,
                      max(self.places, other.places))

    def __mul__(self, other):
        return FixNum(self.value * other.value,
                      max(self.places, other.places))

    def __div__(self, other):
        # Force to use floating point, since 2/3 in Python is 0
        # Don't use float() since that will convert strings
        return FixNum((self.value+0.0) / other.value,
                      max(self.places, other.places))

    def __str__(self):
        return "STR%s: %.*f" % (self.__class__.__name__,
                                self.places, self.value)
    def __int__(self):
        return int(self.value)

    def __float__(self):
        return self.value

def demo():
    x = FixNum(40)
    y = FixNum(12, 0)

    print "sum of", x, "and", y, "is", x+y
    print "product of", x, "and", y, "is", x*y

    z = x/y
    print "%s has %d places" % (z, z.places)
    if not z.places:
        z.places = 2

    print "div of", x, "by", y, "is", z
    print "square of that is ", z*z

if __name__ == "__main__":
    demo()



# -*- coding: utf-8 -*-

class TimeNumber:
    def __init__(self, hours, minutes, seconds):
        assert minutes < 60 and seconds < 60
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def __str__(self):
        return "%d:%02d:%02d" % (self.hours, self.minutes, self.seconds)
    def __add__(self, other):
        seconds = self.seconds + other.seconds
        minutes = self.minutes + other.minutes
        hours = self.hours + other.hours
        if seconds >= 60:
            seconds %= 60
            minutes += 1
        if minutes >= 60:
            minutes %= 60
            hours += 1
        return TimeNumber(hours, minutes, seconds)

    def __sub__(self, other):
        raise NotImplementedError

    def __mul__(self, other):
        raise NotImplementedError

    def __div__(self, other):
        raise NotImplementedError

t1 = TimeNumber(0, 58, 59)
sec = TimeNumber(0, 0, 1)
min = TimeNumber(0, 1, 0)
print t1 + sec + min + min
# 1:01:00


```
