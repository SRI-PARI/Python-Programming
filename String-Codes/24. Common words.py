'''
a=input().split()
b=input().split()
res=""
for i in a:
    for j in b:
        if i==j:
            print(i,end=" ")
'''
s1=input().split()
s2=input().split()
res=""
for i in s1:
    if i in s2:
        res+=i+" "
print(res)
        