#!/usr/bin/python

# the sum of two elements defines the next

x, y = 2, 3

if x == y:
	x, "and", y, "are equal"
else:
	if x < y:
	    print x, "is less then", y
	else:
	    print x, "is greater than", y
