# -*- coding:utf-8 -*-
import sys

C = float(sys.argv[1])

if C < -273.15:
    print '%g degrees Celsius is non-physical!' % C
    print 'The Fahrenheit temperature will not be computed.'
else:
    F = 9.0/5*C + 32
    print '%gC is %.1fF' % (C, F)
print 'end of program'