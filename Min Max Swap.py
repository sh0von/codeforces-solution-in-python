t=int(input()) #number of test cases 
for i in range(t):
    n=int(input()) #number of elements
    a=list(map(int,input().split())) #list of elements of a
    b=list(map(int,input().split())) #list of elements of b
    mxa=max(a) #maximum element of a
    mxb=max(b) #maximum element of b
    if mxa>mxb: #if maximum element of a is greater than maximum element of b
        for j in range(n):
            if a[j]<b[j]: #if element of a is less than element of b
                a[j],b[j]=b[j],a[j] #swap the elements
        b.sort() #sort the list b
        print(b[n-1]*mxa) #print the product of maximum element of a and second maximum element of b
    else: #if maximum element of b is greater than maximum element of a
        for j in range(n):
            if a[j]>b[j]: #if element of a is greater than element of b
                a[j],b[j]=b[j],a[j] #swap the elements
        a.sort() #sort the list a
        print(a[n-1]*mxb) #print the product of maximum element of b and second maximum element of a
