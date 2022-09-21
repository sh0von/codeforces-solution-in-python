n = int(input())                     
list =[]                              
if (n % 2 == 1):                      
    list.append(3)
    n -= 3
while (n > 0):
    list.append(2)
    n -= 2
print(len(list))
for i in range(len(list)):
    print(list[i],end=" ")