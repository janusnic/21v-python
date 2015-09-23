def tuple_test(x,y):
     x += 1
     y += 1
     print x, y

t = (1,2)
# tuple_test(t) # error
tuple_test(*t) # success