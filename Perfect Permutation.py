n = int(input())

if n % 2 == 1:
	print(-1)
else:
	arr = []
	for i in range(1,n+1,2):
		arr.append(i+1)
		arr.append(i)
	print(" ".join(map(str,arr)))