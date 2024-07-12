s=input()
res=""
for i in s:
    if s.count(i)<2:
        res+=i
print(res)
