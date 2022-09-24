n = int(input().strip())
n += 1

while True:
	if len(set(list(str(n)))) == 4:
		print(n)
		break
	n += 1