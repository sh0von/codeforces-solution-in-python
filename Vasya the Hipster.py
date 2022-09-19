import math
a,b = map(int, input().split())
if a<b:
    x=(b-a)
    z=math.floor(x/2)
    
    if z < 0:
        print(a, "0")
    else:
        print(a, "" , z)
else:
    y=(a-b)
    c=math.floor(y/2)
    if c < 0:
        print(b, "0")
    else:
        print(b, "" , c)