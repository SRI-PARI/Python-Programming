n=int(input())
flag=0
for i in range(0,n+1):
    if i*(i+1)==n:
        flag=1
        break
if flag==1:
    print("Pronic")
else:
    print("Not pronic")
