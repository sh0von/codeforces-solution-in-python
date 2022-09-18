x=input()
unique = []
for char in x[::]:
    if char not in unique:
        unique.append(char)
if len(unique)%2 ==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')