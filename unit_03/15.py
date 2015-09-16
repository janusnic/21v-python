li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements'] 

print li.remove("z")                                     
print li 

li.remove("new")                                   
print li 

li.remove("z")                                    

print li 

# Remove the item at the given position in the list, and return it. If no index is 
# specified, a.pop() removes and returns the last item in the list. The item is 
# also removed from the list. (The square brackets around the i in the method 
# signature denote that the parameter is optional, not that you should type square 
# brackets at that position. You will see this notation frequently in the Python 
# Library Reference.) 


a = [66.25, 333, 333, 1, 1234.5]

print a.pop(1)
print a

#To add an item to the top of the stack, use append(). To retrieve an item from 
#the top of the stack, use pop() without an explicit index.

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print stack

stack.pop()

print stack

print stack.pop()

print stack.pop()

print stack