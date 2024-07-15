l=list(map(int,input().split(" ")))
n=int(input())
flag=False
for i in l:
    if i==n:
        flag=True
        break
if flag==True:
    print("Found")
else:
    print("Not Found")
