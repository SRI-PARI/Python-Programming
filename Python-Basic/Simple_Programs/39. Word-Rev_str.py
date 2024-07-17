s=input().split()
rev=""
i=len(s)-1
while(i>=0):
    rev=rev+s[i]+" "
    i-=1
print(rev)
