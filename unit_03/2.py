#!/usr/bin/python

# 20.py append

names = ['Dave', 'Mark', 'Ann', 'Phil']

names.append('Bob')
print names[4]

names.insert(2,'Bob')
print names[2]

li = ['a', 'b', 'mpilgrim', 'z', 'example'] 

li.insert(2, "new")                                

print li 

scores = ["1","2","3"]

# add a score
score = int(raw_input("What score did you get?: "))
scores.append(score)

# list high-score table
for score in scores:
       print score

#     Add an item to the end of the list; equivalent to a[len(a):] = [x]. 

a = [66.25, 333, 333, 1, 1234.5]

a.append(333)
print a

li = ['a', 'b', 'c'] 
li.extend(['d', 'e', 'f'])                         
print li 

print len(li)                                            

print li[-1] 

li = ['a', 'b', 'c'] 
li.append(['d', 'e', 'f'])                        

print li 

print len(li)                                            

print li[-1] 
