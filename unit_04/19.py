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

print data