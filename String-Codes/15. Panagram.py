s=input()
a="abcdefghijklmnopqrstuvwxyz"
flag=0
for i in a:
    if i not in s:
        flag=1
        break
if flag==0:
    print("Panagram")
else:
    print("not a panagram")