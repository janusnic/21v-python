# -*- coding:utf-8 -*-
from math import sin, pi

def y(t, v0):
    g = 9.81
    return  v0*t - 0.5*g*t**2

def diff(f, x, h=1E-10):
    return (f(x+h) - f(x))/h

def h(t):
    return t**4 + 4*t

dh = diff(h, 0.1)
print dh

x = 2*pi
dsin = diff(sin, x, h=1E-9)
print dsin
