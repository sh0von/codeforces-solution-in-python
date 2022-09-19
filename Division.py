x = int(input())
for g in range(x):
    rating = int(input())
    if(1900<=rating):
        print("Division 1")
    elif(1600<=rating and rating<=1899):
        print("Division 2")
    elif(1400<=rating and rating<=1599):
        print("Division 3")
    else:

        print("Division 4")
