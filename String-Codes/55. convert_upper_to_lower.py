s=input()
res=""
for i in s:
    if i.isupper():
        res=res+i.lower()
    else:
        res+=i
print(res)