def intersect(seq1, seq2):
    res = []                     # start empty
    for x in seq1:               # scan seq1
        if x in seq2:            # common item?
            res.append(x)        # add to end
    return res

s1 = "SPAM"
s2 = "SCAM"

print intersect(s1, s2)                   # strings

s1 = [1,2,3,4,5]
s2 = [3,4,5,6,7]


print intersect(s1, s2)                   # list

def intersect(seq1, seq2):
    res = []                     # start empty
    for x in seq1:               # scan seq1
        if x in seq2:            # common item?
            res.append(x)        # add to end
    return res

x = intersect([1, 2, 3], (1, 4))    # mixed types
print x                                   # saved result object