L = ['spam', 'Spam', 'SPAM!']

print L.append('please')                # append method call
print L

L.sort()                          # sort list items ('S' < 'e')
print L

aList = [ 2, 6, 4, 8, 10, 12, 89, 68, 45, 37 ]

print "Data items in original order"

for item in aList:
   print item,

aList.sort()

print "\n\nData items after sorting"

for item in aList:
   print item,

print

# Sort the items of the list, in place. 

a = [66.25, 333, 333, 1, 1234.5]

a.sort()

print a