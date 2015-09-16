#!/usr/bin/python

# 1.py lists

names = ['Dave', 'Mark', 'Ann', 'Phil']


# print(names[2])
print names[2]
 
aList = [123, 'abc', 4.56, ['inner', 'list'], 7-9j]
anotherList = [None, 'something to see here']
print aList
print anotherList
aListThatStartedEmpty = []
print aListThatStartedEmpty
print list('foo')

aList = [123, 'abc', 4.56, ['inner', 'list'], (7-9j)]
print aList[2]
aList[2] = 'float replacer'
print aList
aList.append("hi, i'm new here")
print aList

L = ['Already', 'got', 'one']
L[1:] = []
print L

L[0] = []
print L

inventory = ["sword", "armor", "shield", "healing potion"]

inventory[0] = "crossbow"

print inventory

inventory = ["sword", "armor", "shield", "healing potion"]

inventory[4:6] = ["orb of future telling"]

print inventory


