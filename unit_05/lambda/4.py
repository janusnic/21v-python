def f(x):
    return x + 3

def g(function, x):
    return function(x) * function(x)

print g(f, 7)