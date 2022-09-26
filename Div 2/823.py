T=int(input())
for i in range(T):
    n,c =map(int, input().split())    
    orbit=list(map(int, input().strip().split()))[:n]
    orbit2=list(dict.fromkeys(orbit))
    x=len(orbit2)
    mina=1
    dup=[]
    for a in orbit:
        d=orbit.count(a)
        if d > 1:
                if dup.count(a) == 0:   
                    dup.append(a)
    yy=len(dup)
    if mina==c:
            print(x)
    else:
            print(min(mina*n,c*x,yy*c+(x-yy)))##incomplete