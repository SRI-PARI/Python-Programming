s=input()
n=int(input())
i=1
j=0
res=""
while(i<=len(s)):
    if i%n==0:
        res+=str(s[j]).swapcase()
    else:
        res+=s[j]
    i+=1
    j+=1
print(res)