
def function1():
    print '1'
    
def function2():
    print '2'
    
def function3():
    print '3'
switch = {
     'one': function1,
     'two': function2,
     'three': function3,
}

choice = raw_input('Enter one, two or three')
try:
     result = switch[choice]() 
     
except KeyError:
     print "I didn\'t understand your choice"
