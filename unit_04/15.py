# -*- coding:utf-8 -*-

temps = {'Oslo': 13, 'London': 15.4, 'Paris': 17.5}
# или
temps = dict(Oslo=13, London=15.4, Paris=17.5)

temps['Madrid'] = 26.0

print temps

for city in temps:
    print 'The temperature in %s is %g' % (city, temps[city])

if 'Berlin' in temps:
    print 'Berlin:', temps['Berlin']
else:
    print 'No temperature data for Berlin'

for city in sorted(temps):
    print city
