# -*- coding:utf-8 -*-

# пример: Адрес Улицы

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