T=int(input())
for i in range(T):
    n=input()
    x = [int(a) for a in str(n)]
    s1=sum(x[0:3])
    s2=sum(x[3:6])
    
    if s1==s2 :
        print('Yes')
    else:
        print('No')