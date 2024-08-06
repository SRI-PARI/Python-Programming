s=input()
l=len(s)//2
if s[0:l]==s[l:]:
    print("symmetric")
else:
    print("Not symmetric")
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")
