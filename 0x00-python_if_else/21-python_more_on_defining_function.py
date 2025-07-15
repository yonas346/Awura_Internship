def f(a, L=[]):
    L.append(a)
    return L

# you can write the function like this if you don't want to share between subsequent calls

def f(a, L=None):
    if L is None:
        L=[]
    L.append(a)
    return L