n=int(input())
rev=0
temp=n
while(temp>0):
    r=temp%10
    rev=rev*10+r
    temp=temp//10
if n==rev:
    print("Palindrome")
else:
    print("Not palindrome")
