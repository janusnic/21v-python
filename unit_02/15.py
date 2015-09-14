#!/usr/bin/python

# 15.py s.lstrip, s.rstrip, s.strip 

s = "\t no parking " 

print(s.lstrip())
print(s.rstrip())
print(s.strip())

s = "<[unbracketed]>"

print(s.strip("[](){><>"))



