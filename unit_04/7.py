# -*- coding:utf-8 -*-
def extract_data(filename):
    infile = open(filename, 'r')
    infile.readline()
    numbers = [float(line.split()[1]) for line in infile]
    infile.close()
    return numbers

values = extract_data('rainfall.dat')

import matplotlib.pyplot as plt
month_indices = range(1, 13)
plt.plot(month_indices, values[:-1], 'o--')
plt.show()
