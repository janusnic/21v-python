for x in [1, 2, 3]: print x,      # iteration

a = ['cat', 'window', 'defenestrate']
for x in a:
     print x, len(x)

a = ['cat', 'window', 'defenestrate']

for x in a[:]: # make a slice copy of the entire list
    if len(x) > 6: a.insert(0, x)
 
print a

a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
     print i, a[i]

words = ['A', 'B', 'C', 'D', 'E']
for word in words:
    print word

range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in range:
    print number