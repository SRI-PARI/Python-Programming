s=input().split()
k=int(input())
res=""
for i in s:
    if len(i)>k:
        res+=i
print(res)