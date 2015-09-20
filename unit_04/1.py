
infile = open('data1.txt', 'r')
lines = infile.readlines()
print lines

infile = open('data1.txt', 'r')
lines = []
for line in infile:
    lines.append(line)
print lines

infile = open('data1.txt', 'r')
lines = [line for line in infile]
print lines