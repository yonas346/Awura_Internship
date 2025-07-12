# the point of function definition in the defining scope
i = 5

def f(arg=i):
    print(arg)

i = 6
f()