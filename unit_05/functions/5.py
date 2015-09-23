def foo(*args, **kwargs):
     return args if args else kwargs

print foo(1,2)


print foo(1,2,3)


print foo(x=1, y=2)
