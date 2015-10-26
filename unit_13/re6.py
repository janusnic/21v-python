# -*- coding:utf-8 -*-
import re
# Обработка телефонных номеров

phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$') 
print phonePattern.search('80055512121234').groups() 
# ('800', '555', '1212', '1234')
print phonePattern.search('800.555.1212 x1234').groups() 
# ('800', '555', '1212', '1234')
print phonePattern.search('800-555-1212').groups() 
# ('800', '555', '1212', '')
print phonePattern.search('(800)5551212 x1234')   