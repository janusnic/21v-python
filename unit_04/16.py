# -*- coding:utf-8 -*-

p = {0: -1, 2: 1, 7: 3}

def poly1(data, x):
    sum = 0.0
    for power in data:
        sum += data[power]*x**power
    return sum

print poly1(p,3.14)