s1=input()
s2=input()
flag=0
if len(s1)!=len(s2):
    print("Not Anagram")
else:
    flag=0
    for i in range(len(s1)):
        if s1[i] not in s2:
            flag=1
            break
    if flag==1:
        print("not anagram")
    else:
        print("Anagram")
            
       