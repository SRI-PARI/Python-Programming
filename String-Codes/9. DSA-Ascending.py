s=input()
A=""
D=""
S=""
for i in s:
    if i.isalpha():
        A+=i
    elif i.isdigit():
        D+=i
    else:
        S+=i
print(D+S+A)