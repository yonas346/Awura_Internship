#if statement 
x=int(input("please enter an number"))
if x<0:
    x=0
    print('negative changed to zero')
elif x==0:
    print('zero')
elif x==1:
    print('single')
else:
    print('more')