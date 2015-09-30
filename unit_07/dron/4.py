# -*- coding:utf-8 -*-
class Y:
    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81

    def value(self, t):
        return self.v0*t - 0.5*self.g*t**2

y = Y(3)

print y
v = y.value(0.1)

print v
print y.v0
