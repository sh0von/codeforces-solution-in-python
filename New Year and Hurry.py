from cmath import sqrt
import math
a, b= map(int, input().split())
t=60*4
l=(t-b)
s=math.sqrt(1+8*l/5)
e=((-1+s)/2)
r=math.floor(e)
if r>=a :
    print(a)
else :
    print(r)