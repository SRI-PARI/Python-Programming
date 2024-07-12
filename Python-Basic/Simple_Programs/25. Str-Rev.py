'''
s=input()
print(s[::-1])
'''
#---------  ---------------------------------------
'''
s=input().split()
r=reversed(s)
for i in r:
    print(i, end=" ")
'''
#-------------------------------------------------------
s=input()
i=len(s)-1
res=""
while(i>=0):
    res+=s[i]
    i-=1
print(res)
