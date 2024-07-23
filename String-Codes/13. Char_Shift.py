s=input()
res=""
for i in s:
    if i.isalpha():
        res+=i
        ch=i
    else:
        res+=chr(ord(ch)+int(i))
print(res) 
