s=input()
res=""
for i in s:
    if i not in res:
        c=s.count(i)
        res+=i
        print(i+str(c),end="")

      