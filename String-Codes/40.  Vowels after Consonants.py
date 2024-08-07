s=input()
alp=""
con=""
for i in s:
    if i in 'aeiou':
        alp+=i
    elif i not in 'aeiou':
        con+=i
print(alp+con)





   