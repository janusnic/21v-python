# -*- coding:utf-8 -*-

formula = raw_input('Give a formula involving x: ')
x = eval(raw_input('Give x: '))
from math import *     #  теперь доступны все функции из math
result = eval(formula)
print '%s for x=%g yields %g' % (formula, x, result)