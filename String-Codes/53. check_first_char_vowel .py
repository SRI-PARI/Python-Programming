s=input()
k=s[0]
flag=0
for i in s:
    if k in 'aeiou':
        flag=1
        break
if flag==1:
    print("yes")
else:
    print("No")
