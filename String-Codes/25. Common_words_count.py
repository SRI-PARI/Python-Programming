'''
s=input().split()
s1=input().split()
c=0
for i in s:
    for j in s1:
        if i==j:
            c+=1
print(c)
'''
s1=input().split()
s2=input().split()
c=0
for i in s1:
    if i in s2:
        c+=1
print(c)