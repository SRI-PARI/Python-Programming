s=input().split()
res=""
l=[]
for i in s:
    l.append(len(i))
m=min(l)
for i in s:
    if len(i)==m:
        res+=i
print(res)