n=int(input())
k=0
for i in range(1,n+1):
    if n%i==0:
        k+=1
if k==2:
    print("Prime")
else:
    print("Not Prime")