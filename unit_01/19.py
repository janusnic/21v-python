#!/usr/bin/python

# the sum of two elements defines the next

def isPos(x):
	if x%2 == 0:
		print x, "x even"
	else:
		print x, "x odd"

a, b = 0, 1
isPos(a)