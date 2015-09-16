#!/usr/bin/python

# 3.py seq

names = ['Dave', 'Mark', 'Ann', 'Phil']

a = names[0:2]
b = names[2:]

print a
print b

names[1] = 'Jeff'
print names[1]
names[0:2] = ['Dave', 'Mark', 'Phil']
print names[0:2]

L = ['spam', 'Spam', 'SPAM!']

print L

L[0:2] = ['eat', 'more']       # slice assignment: delete+insert
print L                        # replaces items 0,1


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print numbers[3:6]

print numbers[0:1]

print numbers[7:10]

print numbers[-3:-1]

print numbers[-3:]


print numbers[:3]

print numbers[:]

inventory = ["sword", "armor", "shield", "healing potion"]


begin = int(raw_input("\nEnter the index number to begin a slice: "))
end = int(raw_input("Enter the index number to end the slice: "))
print "inventory[", begin, ":", end, "]\t\t",
print inventory[begin:end]

a = ['spam', 'eggs', 100, 1234]
print a[0]

print a[3]

print a[-2]

print a[1:-1]

print a[:2] + ['bacon', 2*2]

print 3*a[:3] + ['Boo!']

li = ['a', 'b', 'mpilgrim', 'z', 'example'] 
print li[1:3]                                            

print li[1:-1]                                           

print li[0:3]                                            

aList = [123, 'abc', 4.56, ['inner', 'list'], 7-9j]
aList[0]
print aList[1:4]
print aList[:3]
print aList[3][1]

li = ['a', 'b', 'mpilgrim', 'z', 'example'] 
print li[:3]                                             

print li[3:]                                             

print li[:]             

