t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    c=0
    ans=[0]*n
    ans[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        if arr[i]+ans[i+1]>0 and ans[i+1]-arr[i]>0:
            c=1
            break
        else:
            ans[i]=ans[i+1]-arr[i]
    if c==1:
        print(-1)
    else:
        for i in range(n):
            print(ans[i],end=" ")
        print()
