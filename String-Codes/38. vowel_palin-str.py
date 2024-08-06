s=input()
v='aeiou'
res=""
for i in s:            
    if i in v:
        res+=i
if res==res[::-1]:
    print("palindrome")
elif res=="":
    print("-1")
else:
    print("not palindrome")


