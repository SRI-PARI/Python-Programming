s=input()
res=""
for i in s:
    if i not in res:
        if s.count(i)%2==0:
            res+=i
print(res)
