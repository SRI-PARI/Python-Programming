s=input()
flag=0
for i in s:
    if i not in '01':
        flag=1
        break
if flag==0:
    print("Binary")
else:
    print("Not Binary")