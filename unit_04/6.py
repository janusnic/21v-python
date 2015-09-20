# -*- coding:utf-8 -*-
def extract_data(filename):
    infile = open(filename, 'r')    
    infile.readline()      # пропускаем первую строчку
    numbers = []
    for line in infile:
        words = line.split()
        number = float(words[1])
        numbers.append(number)
    infile.close()
    return numbers

values = extract_data('rainfall.dat')

import matplotlib.pyplot as plt
month_indices = range(1, 13)
plt.plot(month_indices, values[:-1], 'o--')
plt.show()
