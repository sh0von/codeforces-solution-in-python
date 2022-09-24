Str=input()
s=""
vowels=['A','E','I','O','U','Y','a','e','i','o','u','y']
for i in Str:
    if i not in vowels:
        s+='.'+i
print(s.lower())