#!/usr/bin/env python
"""This script prompts a user to enter a message to encode or decode
using a classic Caeser shift substitution (3 letter shift)"""

# import string

print("""\
Usage: variable1 operation variable2
     operation                 + - * ** / %
     example               	   2 * 2
""")

# src = '2 ** 6'
src = input('Enter your expression : ')
# op = src.find('+')
# print(op)

print(src.split(' '))

tmp = src.split(' ')

#x = int(tmp[0])
# op = tmp[1]
# y = int(tmp[2])

if tmp[1] == '+':
    print(src, '= ', int(tmp[0]) + int(tmp[2]))
elif tmp[1] == '-':
    print(int(tmp[0]) - int(tmp[2]))
elif tmp[1] == '*':
    print(int(tmp[0]) * int(tmp[2]))
elif tmp[1] == '/':
    print(int(tmp[0]) / int(tmp[2]))
elif tmp[1] == '**':
    print(int(tmp[0]) ** int(tmp[2]))
elif tmp[1] == '%':
    print(int(tmp[0]) % int(tmp[2]))
else:
    print('wrong expression')
