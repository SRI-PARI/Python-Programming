s=input().split()
res=""
for i in s:
    res+=i[0].upper()+i[1:-1]+i[-1].upper()+" "
print(res)
