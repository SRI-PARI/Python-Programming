s=input()
ss=input()
c=0
for i in range(0,len(s)):
    if s[i:i+len(ss)]==ss:
        c+=1
print(c)