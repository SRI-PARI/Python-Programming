s=input().split()
res=""
flag=0
for i in s:
    k=len(i)
    if k%2==0:
        res=res+i
        flag=1
if flag==1:
    print(res)
else:
    print("-1")
