T=int(input()) #input number of test cases
for i in range(T): #loop for number of test cases
    n=input() #input number 
    x = [int(a) for a in str(n)] #convert number to list of integers
    s1=sum(x[0:3]) #sum of first 3 digits
    s2=sum(x[3:6]) #sum of last 3 digits
    
    if s1==s2 : #check if sum of first 3 digits is equal to sum of last 3 digits
        print('Yes')
    else:
        print('No')
