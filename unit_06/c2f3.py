# -*- coding:utf-8 -*-
import sys

try:
    C = float(sys.argv[1])
except IndexError:
    print 'Celsius degrees must be supplied on the command line'
    sys.exit(1)
except ValueError:
    print 'Celsius degrees must be a pure number, '\
          'not  "%s"' % sys.argv[1]
    sys.exit(1)

if C < -273.15:
    print '%g degrees Celsius is non-physical!' % C
    print 'The Fahrenheit temperature will not be computed.'
else:
    F = 9.0/5*C + 32
    print '%gC is %.1fF' % (C, F)
print 'end of program'
