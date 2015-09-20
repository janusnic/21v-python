
infile = open('data1.txt', 'r')

lines = [line for line in infile]


mean = sum([float(line) for line in lines])/len(lines)

print lines
print mean