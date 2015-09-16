L = ['spam', 'Spam', 'SPAM!']

print L[2]                               # offsets start at zero

print L[-2]                              # negative: count from the right

print L[1:]                              # slicing fetches sections

L1 = [2,3,4]
L2 = L1
L1[0] = 24


print L2

li = ['a', 'b', 'mpilgrim', 'z', 'example'] 

print li[-1]                                             

print li[-3]            


a = ['spam', 'eggs', 100, 1234]
print a

a[2] = a[2] + 23

print a

foo = [42, 'www.java2s.com', lambda x: x**2, [47, '11']]

print foo


print foo[3]


print foo[2](3)

foo[3][0] = 99
print foo


for i in foo:
     print i, "--", type(i)

# Create a list of even integers 0 to 198
aList = range( 0, 199, 2 )

secarhKey = int( raw_input( "Enter integer search key: " ) )

if secarhKey in aList:
   print "Found at index:", aList.index( secarhKey )
else:
   print "Value not found"

inventory = ["sword", "armor", "shield", "healing potion"]

index = int(raw_input("\nEnter the index number for an item in inventory: "))

print "At index", index, "is", inventory[index]

