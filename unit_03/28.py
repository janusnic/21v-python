print [x+y for x in 'spam' for y in 'SPAM']

print [(x,y) for x in range(5) if x%2 == 0 for y in range(5) if y%2 == 1]

listoftuple = [('bob', 35, 'mgr'), ('mel', 40, 'dev')]

print [age for (name, age, job) in listoftuple]

print map((lambda (name, age, job): age), listoftuple)

# List comprehensions provide a concise way to create lists without resorting to use 
# of map(), filter() and/or lambda. 

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print [weapon.strip() for weapon in freshfruit]

vec = [2, 4, 6]
print [3*x for x in vec]

print [3*x for x in vec if x > 3]

print [3*x for x in vec if x < 2]

print [[x,x**2] for x in vec]

print [(x, x**2) for x in vec]

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]

print [x*y for x in vec1 for y in vec2]

print [x+y for x in vec1 for y in vec2]

print [vec1[i]*vec2[i] for i in range(len(vec1))]


print [str(round(355/113.0, i)) for i in range(1,6)]


S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]
 
print S; print V; print M

#First build a list of non-prime numbers, using a single list comprehension, 
#then use another list comprehension to get the "inverse" of the list, 
#which are prime numbers.

noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print primes

params = {"Key 1":"value 1", "key 2":"value 2", "key 3":"value 3", "key 4":"value 4"} 
print params.items() 

print [k for k, v in params.items()]                    

print [v for k, v in params.items()]                     

print ["%s=%s" % (k, v) for k, v in params.items()] 

