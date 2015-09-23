def add(n):
    return lambda x: x + n

adds = [add(x) for x in xrange(100)]

print adds[34](5)

print adds[10](5)

