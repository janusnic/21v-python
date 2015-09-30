# -*- coding:utf-8 -*-
class Y:
    """The  vertical  motion  of  a  ball."""

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

def diff(f, x, h=1E-10):
    return (f(x+h) - f(x))/h

y1 = Y(1)
y2 = Y(1.5)
y3 = Y(-3)


dy1dt = diff(y1.value, 0.1)
dy2dt = diff(y2.value, 0.1)
dy3dt = diff(y3.value, 0.2)

print y1.v0
print y2.v0
print y3.v0

y3.v0 = 5

print y3.v0