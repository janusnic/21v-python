L1 = [1, ('a', 3)]         # same value, unique objects
L2 = [1, ('a', 3)]
print L1 == L2, L1 is L2         # equivalent?, same object?

S1 = 'spam'
S2 = 'spam'
print S1 == S2, S1 is S2


S1 = 'a longer string'
S2 = 'a longer string'
print S1 == S2, S1 is S2

L1 = [1, ('a', 3)]
L2 = [1, ('a', 2)]
print L1 < L2, L1 == L2, L1 > L2     # less,equal,greater: tuple of results
