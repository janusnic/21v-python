list1 = [7, 2, 3, 10, 12]
list2 = [-1, 1, -5, 4, 6]

print map(lambda x, y: x*y, list1, list2)


print [x*y for x, y in zip(list1, list2)]
