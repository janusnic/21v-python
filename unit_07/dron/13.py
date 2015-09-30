# -*- coding:utf-8 -*-
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

    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81

    def getv0(self):                 # метод для получения значения
        return self._v0
    
    def setv0(self, value):          # присваивания нового значения
        self._v0 = value
    
    def delv0(self):                 # удаления атрибута
        del self._v0                 
    
    v0 = property(getv0, setv0, delv0, "Свойство v0")    # определяем v0 как свойство
    
    def value(self, t):
        return self.v0*t - 0.5*self.g*t**2

    def formula(self):
        return 'v0*t - 0.5*g*t**2; v0=%g' % self.v0

class Y2:
    def value(self, t, v0=None):
        if v0 is not None:
            self.v0 = v0
        g = 9.81
        try:
            value = self.v0*t - 0.5*g*t**2
        except AttributeError:
            msg = ('You cannot call value(t)  without first '
                              'calling value(t, v0) to set v0')
            raise TypeError(msg)
        return value

def diff(f, x, h=1E-10):
    return (f(x+h) - f(x))/h

y1 = Y(1)
y2 = Y(1.5)
y3 = Y(-3)

dy1dt = diff(y1.value, 0.1)
dy2dt = diff(y2.value, 0.1)
dy3dt = diff(y3.value, 0.2)

y = Y2()

print y.__dict__

print y1.__dict__
print y2.__dict__
print y3.__dict__
# print y.v0

# print y3.__doc__

