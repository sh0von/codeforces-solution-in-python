import math as m
t=int(input())
for i in range(t):
    a,b=map(int, input().split())
    c=m.ceil(a/b)
    print(c*b-a)