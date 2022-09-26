t=int(input())
for i in range(t):
    a,b,c=map(int,(input().split()))
        
    n= abs(b-a)
    m=2*n
    d=0
    if a>m or b>m or c>m:
        d=-1
    
    elif c>n:
        d=c-n
    
    else:
        d=c+n
    
    print(d)
    
    t-=1
    