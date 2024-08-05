s=input()
res=""
r=""
for i in s:
    if i.isalnum():
        res+=i
res=res[::-1]
j=0
for i in s:
    if i.isalnum():
        r+=res[j]
        j+=1
    else:
        r+=i
print(r)


