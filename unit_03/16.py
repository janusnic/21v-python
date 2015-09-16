L = ['SPAM!', 'eat', 'more', 'please']
del L[0]                       # delete one item
print L

del L[1:]                      # delete an entire section
print L                              # same as L[1:] = []
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements'] 

print li.remove("z")                                     
print li 

li.remove("new")                                   
print li 

li.remove("z")                                    

print li

inventory = ["sword", "armor", "shield", "healing potion"]


print "In a great battle, your shield is destroyed."
del inventory[2]
print "Your inventory is now:"
print inventory

inventory = ["sword", "armor", "shield", "healing potion"]

del inventory[:2]

print inventory

scores = ["1","2","3"]

# delete a score
score = int(raw_input("Delete which score?: "))
if score in scores:
   scores.remove(score)
else:
   print score, "isn't in the high scores list."

# list high-score table
for score in scores:
   print score