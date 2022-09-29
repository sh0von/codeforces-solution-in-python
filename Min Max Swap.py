t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    mxa=max(a)
    mxb=max(b)
    if mxa>mxb:
        for j in range(n):
            if a[j]<b[j]:
                a[j],b[j]=b[j],a[j]
        b.sort()
        print(b[n-1]*mxa)
    else:
        for j in range(n):
            if a[j]>b[j]:
                a[j],b[j]=b[j],a[j]
        a.sort()
        print(a[n-1]*mxb)