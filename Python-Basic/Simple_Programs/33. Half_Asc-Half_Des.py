l=list(map(int,input().split(" ")))
res=""
k=""
for i in range(0,len(l)//2):
    for j in range(i,len(l)//2):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
for i in range(len(l)//2,len(l)):
    for j in range(i,len(l)):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
for i in l:
    print(i, end=" ")
  