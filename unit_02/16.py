#!/usr/bin/python

# 16.py split
record = "Leo Tolstoy*1828-8-28*1910-11-20" 
fields = record.split("*") 
print(fields)
# ['Leo Tolstoy', '1828-8-28', '1910-11-20'] 
born = fields[1].split('-')  
# born 
# ['1828', '8', '28'] 
died = fields[2].split('-') 
print('lived about', int(died[0]) - int(born[0]), "years") 
# lived about 82 years 



