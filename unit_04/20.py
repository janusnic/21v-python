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

print prices['MS']
jan15_MS = prices['MS'][dates['MS'].index('2015-01')]
jan15_Sun = prices['Sun'][dates['Sun'].index('2015-01')]
norm_price = prices['Google'][0]/max(jan15_MS, jan15_Sun)
prices['Google'] = [p/norm_price for p in prices['Google']]

print prices['Google']