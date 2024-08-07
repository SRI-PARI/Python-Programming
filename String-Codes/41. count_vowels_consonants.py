s=input()
vc=0
c=0
for i in s:
    if i in 'aeiou':
        vc+=1
    if i not in 'aeiou':
        c+=1
print(vc, c, end="")
