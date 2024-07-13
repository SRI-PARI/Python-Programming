s=input()
res=""
v='aeiou'
for i in s:
    if i in v and i not in res:
        res+=i
print(res)
    
