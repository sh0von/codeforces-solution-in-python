n=int(input())
ar=[0]*(n+1)
ans=0
for k in range(2,n+1):
    if ar[k]==2:
        ans+=1
    if ar[k]==0:
        for p in range(k,n+1,k):
            ar[p]+=1
print(ans)