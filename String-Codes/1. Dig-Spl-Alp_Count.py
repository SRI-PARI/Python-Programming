s=input()
dc,sc,ac=0,0,0
for i in s:
    if i.isalpha():
        ac+=1
    elif i.isdigit():
        dc+=1
    else:
        sc+=1
print(dc,sc,ac)
