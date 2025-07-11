# return fibonacci series up to n
def fib2(n):
    result = []
    a, b = 0 ,1
    while a < n:
        result.append(a) # see below
        a, b = b,a+b
    return result
