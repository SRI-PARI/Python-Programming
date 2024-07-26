'''
s=input()
a=False
for i in s:
    if i.isalnum():
        a=True
        break
print(a)
b=False
for i in s:
    if i.isalpha():
        b=True
        break
print(b)
c=False
for i in s:
    if i.isdigit():
        c=True
        break
print(c)
d=False
for i in s:
    if i.islower():
        d=True
        break
print(d)
e=False
for i in s:
    if i.isupper():
        e=True
        break
print(e)
'''
s = input()

# Check if there is at least one alphanumeric character
for i in s:
    if i.isalnum():
        print("True")
        break
else:
    print("False")

# Check if there is at least one alphabetic character
for i in s:
    if i.isalpha():
        print("True")
        break
else:
    print("False")

# Check if there is at least one digit
for i in s:
    if i.isdigit():
        print("True")
        break
else:
    print("False")

# Check if there is at least one lowercase character
for i in s:
    if i.islower():
        print("True")
        break
else:
    print("False")

# Check if there is at least one uppercase character
for i in s:
    if i.isupper():
        print("True")
        break
else:
    print("False")
