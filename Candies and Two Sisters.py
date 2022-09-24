import math as m
t=int(input())
for i in range(t):
    a=int(input())
    if a%2==0:
        print("{:.0f}".format((a/2)-1))
    else:
        b=m.ceil(a/2)
        print("{:.0f}".format(a-b))