l=list(map(int,input().strip().split(",")))
for i in range(0,len(l)):
    for j in range(i,len(l)):
        if l[i]<l[j]:
            l[i]=l[i]+l[j]
            l[j]=l[i]-l[j]
            l[i]=l[i]-l[j]

for i in l:
    print(i,end=",")

