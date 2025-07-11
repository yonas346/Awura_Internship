def fib(n): #write fibonacci series less than n
    """print a fibonacci series less than n."""
    a,b =0,1
    while a < n:
        print(a,end=' ')
        a, b = b, a+b
    print()

#naw call the function we just defined:
fib(2000)