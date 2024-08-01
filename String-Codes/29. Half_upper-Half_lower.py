'''
s=input()
l=len(s)//2
res=""
res=res+s[0:l].upper()+s[l:].lower()
print(res)
'''
s = input()
res = ""
l = len(s) // 2

for i in range(len(s)):
    if i < l:
        res += s[i].upper()
    else:
        res += s[i].lower()

print(res)

