s=input()
res=""
for i in s:
    if s.count(i)<=1:
        if i not in res:
            res+=str(i)
print(res)