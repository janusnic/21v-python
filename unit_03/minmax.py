# -*- coding:utf-8 -*-

lines = [1,2,4,66,88,-33,667,3.4,55,99,7.1234,499]

fvalues = [float(line) for line in lines] 

print 'Минимальное значение: ', min(fvalues) 
print 'Максимальное значение: ', max(fvalues)
