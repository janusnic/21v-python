from itertools import chain, islice, izip, starmap, imap

def fib():
    for i in chain([1,1], starmap(lambda x,y: x+y, izip(fib(), islice(fib(), 1, None)))):
        yield i

print list(islice(fib(), 0, 10))