# -*- coding:utf-8 -*-

def read_file(filename):
    infile = open(filename, 'r')
    infile.readline()       # читаем заголовки столбцов
    dates = [];  prices = []
    for line in infile:
        columns = line.split(',')     # разделяем по запятой
        date = columns[0]
        date = date[:-3]    # пропускаем день месяца (три последних цифры)
        price = columns[-1] # нам нужен только последний столбец
        dates.append(date)
        prices.append(float(price))   # не забываем конвертировать
    infile.close()
    dates.reverse()         # возвращаем порядок: от более старых к новым
    prices.reverse()        # и соответственно цены
    return dates, prices

dates = {};  prices = {}
d, p = read_file('stockprice_sun.csv')
dates['Sun'] = d;  prices['Sun'] = p
d, p = read_file('stockprice_microsoft.csv')
dates['MS'] = d;  prices['MS'] = p
d, p = read_file('stockprice_google.csv')
dates['Google'] = d;  prices['Google'] = p

data = {'prices': prices, 'dates': dates}

# нормировка цен:
norm_price = prices['Sun'][0]
prices['Sun'] = [p/norm_price for p in prices['Sun']]
norm_price = prices['MS'][0]
prices['MS'] = [p/norm_price for p in prices['MS']]

jan15_MS = prices['MS'][dates['MS'].index('2015-01')]
jan15_Sun = prices['Sun'][dates['Sun'].index('2015-01')]
norm_price = prices['Google'][0]/max(jan15_MS, jan15_Sun)
prices['Google'] = [p/norm_price for p in prices['Google']]

# обозначаем "x" точки для построения графиков
x = {}
x['Sun'] = range(len(prices['Sun']))
x['MS']  = range(len(prices['MS']))
# для Google мы должны начать с января 2015:
jan15 = dates['Sun'].index('2015-01')
x['Google'] = range(jan15, jan15 + len(prices['Google']), 1)


import matplotlib.pyplot as plt

plt.plot(x['MS'], prices['MS'], 'g-')
plt.plot(x['Sun'], prices['Sun'], 'b-')
plt.plot(x['Google'], prices['Google'], 'r-')

plt.legend(['Microsoft', 'Sun', 'Google'], loc=0)
plt.grid()
plt.show()

