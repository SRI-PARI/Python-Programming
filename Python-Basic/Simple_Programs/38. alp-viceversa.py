s=input()
res=""
for i in s:
    if i.islower():
        res=res+i.upper()
    elif i==" ":
        res+=""   
    elif i.isupper():
        res+=i.lower()
print(res)
