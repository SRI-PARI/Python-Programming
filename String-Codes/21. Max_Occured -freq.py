s=input()
res=""
l=[]
for i in s:
    l.append(s.count(i))
m=max(l)
for i in s:
    if i not in res:
        if s.count(i)==m :
            res=res+i+"-"+str(m)
            #print(i+"-"+str(m))
            print(res)
