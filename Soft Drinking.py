import math
n, k, l, c, d, p,nl,np=map(int, input().split())
total_slice=math.floor(c*d)
total_drink=math.floor(k*l/nl)
salt=math.floor(p/np)
print(math.floor(min(total_drink,total_slice,salt)/n))