s=input()
res=""
l=len(s)//2
res=res+s[0:l][::-1]+s[l:]
print(res)