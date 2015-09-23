def tuple_test(x,y):
     x += 1
     y += 1
     print x, y

d = {'x':1, 'y': 2}
# tuple_test(d) #error

tuple_test(**d)
