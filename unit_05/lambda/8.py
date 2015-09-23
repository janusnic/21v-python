def f(x, y, z, a=None, b=None):
    print x, y, z, a, b

apply(f, [1, 2, 3], {'a': 4, 'b': 5})
