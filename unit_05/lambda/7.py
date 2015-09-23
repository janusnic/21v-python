numbers = [2, 3, 4, 5, 6]
print reduce(lambda res, x: res*x, numbers, 1)

print reduce(lambda res, x: [x]+res, [1, 2, 3, 4], [])

print sum(numbers)
print list(reversed(numbers))