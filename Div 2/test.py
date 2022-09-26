# program to print duplicate numbers in a given orbit
# provided input
orbit = [3,2,1,2,2]

dup=[]
for a in orbit:
        d=orbit.count(a)
        if d > 1:
                if dup.count(a) == 0:   
                    dup.append(a)
yy=len(dup)
print(len(orbit))
print(yy)
# This code is contributed by Himanshu Khune
