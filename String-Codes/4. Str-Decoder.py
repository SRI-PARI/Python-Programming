s=input()
res=""
for i in s:
    if i.isalpha():
        temp=i
    if i.isdigit():
        res+=temp*int(i)
print(res)
    