import numpy as np
T=int(input())
for i in range(T):
    n=int(input())
    x = [int(a) for a in str(n)]
    s1=np.sum(x[0:3])
    s2=np.sum(x[3:6])
    if s1==s2 :
        print('Yes')
    else:
        print('No')