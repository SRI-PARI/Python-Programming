s=input()
res=""
for i in s:
    if i==",":
        res=res+"."
    elif i==".":
        res=res+","
    else:
        res=res+i
print(res)
