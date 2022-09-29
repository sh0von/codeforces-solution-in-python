t = int(input()) # number of test cases
for i in range(t): # loop for each test case
    l, r = map(int,input().split()) # taking input of l and r
    if r >= l*2: # if r is greater than or equal to 2l
        print(l, l*2) # print l and 2l
    else: # else
        print(-1, -1) # else print -1 -1
