T=int(input()) #input number of test cases
for i in range(T): #loop for number of test cases
    h,m=map(int, input().split()) #input hours and minutes
    print((23-h)*60+(60-m)) #print the remaining time
