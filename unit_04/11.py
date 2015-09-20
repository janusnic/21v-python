# -*- coding:utf-8 -*-
infile = open('budget.csv', 'r')
import csv

table = []
for row in csv.reader(infile):
    table.append(row)
infile.close()

import pprint
pprint.pprint(table)
