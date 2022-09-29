n=input()#input
count1=0#initializing count1
count2=0#initializing count2
for i in n:#for loop
      if(i.islower()):#condition
            count1=count1+1#incrementing count1
      elif(i.isupper()):#condition
            count2=count2+1#incrementing count2
if count1 >= count2 :#condition
    print(n.lower())#printing lower case
else:
    print(n.upper())#printing upper case
