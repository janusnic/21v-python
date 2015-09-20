# -*- coding:utf-8 -*-
infile = open('budget.csv', 'r')
import csv
table = []
for row in csv.reader(infile):
    table.append(row)
infile.close()

import pprint
pprint.pprint(table)

# трансформируем числа из string в float
# (оставляя в покое первую строку и первый столбец)
for r in range(1,len(table)):
    for c in range(1, len(table[0])):
        table[r][c] = float(table[r][c])
pprint.pprint(table)

# добавляем строку с суммой
row = [0.0]*len(table[0])
row[0] = 'sum'
for c in range(1, len(row)):
    s = 0
    for r in range(1, len(table)):
        s += table[r][c]
    row[c] = s
table.append(row)
pprint.pprint(table)

outfile = open('budget2.csv', 'w')
writer = csv.writer(outfile)
for row in table:
    writer.writerow(row)
outfile.close()

