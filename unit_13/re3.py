# -*- coding:utf-8 -*-
import re
# Обработка телефонных номеров

phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')  

print phonePattern.search('800-555-1212').groups()  

print phonePattern.search('800-555-1212-1234')

print phonePattern.search('800-555-1212-1234').groups() 

