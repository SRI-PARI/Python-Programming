s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())
res=str(s1)+str(s2)+str(s3)+str(s4)
l=[]
for i in res:
    l.append(res.count(i))
    
M=max(l)
r=""
for i in res:
    if (res.count(i)==M) and i not in r:
        r+=str(i)
print(r)
