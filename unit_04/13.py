# -*- coding:utf-8 -*-
infile = open('budget.csv', 'r')
import csv

table = [row for row in csv.reader(infile)]
infile.close()

for r in range(1,len(table)):
    for c in range(1, len(table[0])):
        table[r][c] =  float(table[r][c])

row = [0.0]*len(table[0])
row[0] = 'sum'
for c in range(1, len(row)):
    s = 0
    for r in range(1, len(table)):
        s += table[r][c]
    row[c] = s

table.append(row)

import pprint
pprint.pprint(table)
