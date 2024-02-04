def myfunc(a):
    return lambda b:a*b
x=myfunc(5)
print(x(3))