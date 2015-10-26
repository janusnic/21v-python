# -*- coding:utf-8 -*-
import re
# Обработка телефонных номеров

phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$') 
print phonePattern.search('(800)5551212 ext. 1234').groups() 
# ('800', '555', '1212', '1234')
print phonePattern.search('800-555-1212').groups() 
# ('800', '555', '1212', '')
print phonePattern.search('work 1-(800) 555.1212 #1234') 