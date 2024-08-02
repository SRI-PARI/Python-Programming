s=input()
alp='aeiou'
res=""
for i in alp:
    if i in s and i not in res:
        res+=i
print(res)


