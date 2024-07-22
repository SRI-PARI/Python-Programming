s=input()
n=int(input())
res=""
for i in range(0,len(s),n):
    res+=s[i:i+n]+" "
for i in res.split():
    r=""
    for j in i:
        if j not in r:
            r+=j
    print(r)

