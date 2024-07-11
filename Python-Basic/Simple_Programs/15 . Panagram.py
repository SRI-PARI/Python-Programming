s=input()
alp_str="abcdefghijklmnopqrstuvwxyz"

flag=0
for i in  alp_str:
    if i not in s:
        flag=1
        break
if flag==0:
    print("Panagram")
else:
    print("Not panagram")