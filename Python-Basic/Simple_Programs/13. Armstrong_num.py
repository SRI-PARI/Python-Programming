n=int(input())
sum=0
temp=n
while(temp>0):
    r=temp%10
    fact=1
    for i in range(0,r+1):
        fact=fact*i
    sum=sum+fact
    temp=temp//10
if n==sum:
    print("Strong Num")
else:
    print("Not Strong num")
    
