# -*- coding:utf-8 -*-

import random,time


p=lambda:random.choice('abcdfelmn')
for i in range(1,40):
    print '|'.join([p(),p(),p()]),
    #print '{}{}{}'.format(p(),p(),p())
