s=input()
res=""
for i in s:
    if i not in res:
            res+=i+"-"+str(s.count(i))+" "

print(res)