infile = open('data1.txt', 'r')

filestr = infile.read()
print filestr

words = filestr.split()

numbers = [float(w) for w in words]
mean = sum(numbers)/len(numbers)
print mean

infile = open('data1.txt', 'r')
numbers = [float(w) for w in infile.read().split()]
mean = sum(numbers)/len(numbers)
print mean