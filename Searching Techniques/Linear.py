l=list(map(int,input().split()))
target=int(input())
flag=0
for i in l:
    if i==target:
        flag=1
        break
if flag==1:
    print("Element found")
else:
    print("Element not found")