from cmath import sqrt #importing sqrt function from cmath.
import math #importing math.
a, b= map(int, input().split()) #taking input.
t=60*4 #total time.
l=(t-b) #time left.
s=math.sqrt(1+8*l/5) #solving the quadratic equation.
e=((-1+s)/2) #solving the quadratic equation.
r=math.floor(e) #rounding off the value.
if r>=a : #checking if the value is greater than or equal to the number of pages.
    print(a) #printing the number of pages.
else : #if the value is less than the number of pages.
    print(r) #printing the value. 
