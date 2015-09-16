matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print matrix[1]
[4, 5, 6]

print matrix[1][1]

print matrix[2][0]

database = [
    ['A',  '1234'],
    ['B',  '4242'],
    ['C',  '7524'],
    ['D',  '9843']
]

username = raw_input('User name: ')
pin = raw_input('PIN code: ')

if [username, pin] in database: print 'Access granted'