#!/usr/bin/python

# 27.py in range
## print the numbers from 0 through 99
for i in range(100):
    print i,

# lambda

f = lambda x, y : x + y

print f(1,1)

def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return (float(5)/9)*(T-32)

temp = (36.5, 37, 37.5,39)

F = map(fahrenheit, temp)
C = map(celsius, F)

print F, C


Celsius = [39.2, 36.5, 37.3, 37.8]

Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)

print Fahrenheit
# [102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]

C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
print C

# [39.200000000000003, 36.5, 37.300000000000004, 37.799999999999997]
 
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]

print map(lambda x,y:x+y, a,b)
# [18, 14, 14, 14]

print map(lambda x,y,z:x+y+z, a,b,c)
# [17, 10, 19, 23]

print map(lambda x,y,z:x+y-z, a,b,c)
# [19, 18, 9, 5]

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)

print result

#[1, 1, 3, 5, 13, 21, 55]

result = filter(lambda x: x % 2 == 0, fib)
print result
# [0, 2, 8, 34]

print reduce(lambda x,y: x+y, [47,11,42,13])

f = lambda a,b: a if (a > b) else b
print reduce(f, [47,11,42,102,13])
# 102

# Calculating the sum of the numbers from 1 to 100:

print reduce(lambda x, y: x+y, range(1,101))
# 5050

result = []
for x in 'Dostoyevsky':
    result.append(ord(x))
    
print result

result = list(map(ord,'Dostoyevsky'))
print result
# [68, 111, 115, 116, 111, 121, 101, 118, 115, 107, 121]

result = [ord(x) for x in 'Dostoyevsky']
print result
# [68, 111, 115, 116, 111, 121, 101, 118, 115, 107, 121]



