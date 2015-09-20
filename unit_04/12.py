# -*- coding:utf-8 -*-
infile = open('budget.csv', 'r')
import csv

table = [row for row in csv.reader(infile)]
infile.close()

for r in range(1,len(table)):
    for c in range(1, len(table[0])):
        table[r][c] =  float(table[r][c])

import pprint
pprint.pprint(table)
