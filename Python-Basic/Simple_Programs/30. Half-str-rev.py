s=input()
l=len(s)//2
for i in s:
    res=s[0:l][::-1]+s[l:]
print(res)