
infile = open('data1.txt', 'r')

lines = [line for line in infile]

mean = 0
for line in lines:
    number = float(line)
    mean = mean + number
mean = mean/len(lines)

print lines
print mean