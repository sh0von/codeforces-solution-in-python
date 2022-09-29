from math import sqrt , ceil, pow
n=int(input())
for i in range(n):
    hi=int(input())
    gen_sqr = list(i for i in range( 1, hi +1) if sqrt(i) == ceil( sqrt(i)) )
    gen_cub = list(i for i in range( 1, hi +1) if (i**(1/3)) == ceil( (i**(1/3))) )    
    print(len(gen_sqr)+len(gen_cub))
    
    ##Brute force timed out