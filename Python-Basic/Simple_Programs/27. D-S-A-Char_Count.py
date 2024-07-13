l=input()
d=0
s=0
a=0
for i in l:
    if i.isalpha():
        a+=1
    elif i.isdigit():
        d+=1
    else:
        s+=1
print(a,d,s)