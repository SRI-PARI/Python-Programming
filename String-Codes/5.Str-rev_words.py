s=input().split()
i=len(s)-1
res=""
while(i>=0):
    res=res+str(s[i])+" "
    i-=1
print(res)