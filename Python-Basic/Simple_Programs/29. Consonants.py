s=input()
res=""
C='aeiou'
for i in s.lower():
    if i not in C and i not in res:
        res+=i
print(res)
