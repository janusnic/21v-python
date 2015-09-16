#!/usr/bin/python

L = [1, 2]
L = L + [3]            # concatenate: slower
print L

L.append(4)            # faster, but in-place
print L

L = L + [5, 6]         # concatenate: slower
print L

L.extend([7, 8])       # faster, but in-place
print L

L += [9, 10]       # mapped to L.extend([9, 10])
print L

li = ['a', 'b', 'mpilgrim'] 
li = li + ['example', 'new']                       
print li 

li += ['two']                                      
print li 

num_list = [43, -1.23, -2, 6.19e5]
str_list = ['jack', 'jumped', 'over', 'candlestick']
mixup_list = [4.0, [1, 'x'], 'beef', -1.9+6j]

print num_list + mixup_list
print str_list + num_list

inventory = ["sword", "armor", "shield", "healing potion"]


chest = ["gold", "gems"]
print "You find a chest which contains:"
print chest
print "You add the contents of the chest to your inventory."
inventory += chest
print "Your inventory is now:"
print inventory

print [1, 2, 3] + [4, 5, 6]             # concatenation

