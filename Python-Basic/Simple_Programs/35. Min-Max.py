l=list(map(int,input().split(" ")))
min=l[0]
max=l[0]
for i in l:
    if i<min:
        min=i
    if i>max:
        max=i
print(min,max)