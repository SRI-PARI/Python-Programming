S=input()
res=""
s=0
for i in S:
    if i.isdigit():
        res+=str(i)
print(res)
while(res!=0):
    r=int(res)%100
    s+=r
    res=int(res)//100
print(s)