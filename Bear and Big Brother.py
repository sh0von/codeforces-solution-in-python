import math 
a,b =map(int, input().split())
la=math.log(a)
lb=math.log(b)
c=math.log(2/3)
n=(la-lb)/c
print(math.floor(n+1))