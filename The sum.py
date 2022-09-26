def fibo(n):
    counter = 1
    old_num = 0
    new_num = 1
    sum_fib = 1
    while counter < n:
        fib = old_num + new_num

        if counter < n:
            old_num = new_num
            new_num = fib
            sum_fib = sum_fib + fib
            counter = counter + 1

    print(str(sum_fib))

n=int(input())
fibo(n)
