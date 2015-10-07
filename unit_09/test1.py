# -*- coding: utf-8 -*-
import person


dad = person.Person()
"first_name", "last_name", 'id', "age", 'city', "addr", "parent"
dad.first_name = "Jason"
dad.last_name = "Koo"
dad.id = 1123
dad.age = 23
dad.city = 'Kiev'

print dad

kid = dad.new_child()
kid.first_name = "Rachel"
kid.age = 2
print "Kid's parent is", kid.parent.first_name, kid.parent.last_name

#print "Kid's parent is", kid

#=>Kid's parent is Jason
