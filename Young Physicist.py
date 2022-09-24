n=int(input())
x=0
y=0
z=0
for i in range(0,n,1):
    list2=[int(i) for i in input().split()]
    x=x+list2[0]
    y=y+list2[1]
    z=z+list2[2]
if x!=0 or y!=0 or z!=0:
    print("NO")
else:
    print("YES")