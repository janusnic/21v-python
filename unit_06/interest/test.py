# -*- coding:utf-8 -*-
from interest import days
# сколько лет потребуется для удвоения суммы вклада
# если процент p=1,2,3,...14?
for p in range(1,  15):
    years = days(1, 2, p)/365.0
    print 'With p=%d%% it takes %.1f years to double the amount' \
    % (p, years)