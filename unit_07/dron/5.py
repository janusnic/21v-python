# -*- coding:utf-8 -*-
class Y:
    """The  vertical  motion  of  a  ball."""

    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81

    def value(self, t):
        return self.v0*t - 0.5*self.g*t**2

    def formula(self):
        return 'v0*t - 0.5*g*t**2; v0=%g' % self.v0

y = Y(3)


v = y.value(0.1)
f = y.formula()
print v
print f
