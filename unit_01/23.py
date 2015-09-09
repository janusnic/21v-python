#!/usr/bin/python
import math
# return statement

def printLog(x):
	if x <= 0:
		print "Positive number only, please."
		return
	result = math.log(x)
	print "The log of x is", result

x, y = -2, 3

printLog(y)
