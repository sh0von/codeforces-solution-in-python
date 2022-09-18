k ,n ,w =map(int, input().split())
total_cost=(k*(w*(w+1)/2))
left=(total_cost-n)
if left >0:
    print("{:.0f}".format(left))
else:
    print('0')