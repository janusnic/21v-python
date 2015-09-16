scores = []

# add score
name = raw_input("What is the player's name?: ")
score = int(raw_input("What score did the player get?: "))
entry = (score, name)
scores.append(entry)
scores.sort()
scores.reverse()        # want the highest number first
scores = scores[:5]     # keep only top 5 scores

# display
print "High Scores\n"
print "NAME\tSCORE" 
for entry in scores:
    score, name = entry    
    print name, "\t", score

q = [2, 3]
p = [1, q, 4]

print len(p)

print p[1]

print p[1][0]

p[1].append('xtra')

print p

print q

#p[1] and q really refer to the same object!

words = 'The quick brown fox jumps over the lazy dog'.split()

print words

stuff = [[w.upper(), w.lower(), len(w)] for w in words]

for i in stuff:
     print i

stuff = map(lambda w: [w.upper(), w.lower(), len(w)], words)

for i in stuff:
     print i