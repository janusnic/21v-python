# -*- coding:utf-8 -*-
from math import sin, pi

def diff(f, x, h=1E-10):
    return (f(x+h) - f(x))/h

def y(t):
    g = 9.81
    return  v0*t - 0.5*g*t**2

v0 = 3
dy = diff(y, 1)

print dy
