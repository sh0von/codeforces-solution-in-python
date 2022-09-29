t=int(input()) #number of test cases
for i in range(t): #loop for test cases
    a,b,c=map(int,(input().split())) #input of a,b,c
        
    n= abs(b-a) #difference between a and b
    m=2*n #maximum distance
    d=0 #initializing d
    if a>m or b>m or c>m: #if a,b,c are greater than m
        d=-1 #d=-1
    
    elif c>n: #if c is greater than n
        d=c-n #d=c-n
    
    else: #if c is less than n
        d=c+n #d=c+n
    
    print(d) #printing d
    
    t-=1 #decrementing t
