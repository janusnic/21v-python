#!/usr/bin/python

# culc ex

def funcPaw():
	print "paw"

def funcSum():
	print "sum"

def funcDiv():
	print "Div"

def funcMod():
	print "mod"

choice = '*'

print "Take your choice, please:"
choice = raw_input()

if choice == '*':
	funcPaw()
elif choice == '/':
	funcDiv()
elif choice == '+':
	funcSum()
elif choice == '%':
	funcMod()
else:
	print "Invalid choice"