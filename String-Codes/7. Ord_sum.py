s=input()
res=0
k=0
for i in range(len(s)):
    res=res+ord(s[i])
for i in str(res):
    k+=int(i)
print(k)
