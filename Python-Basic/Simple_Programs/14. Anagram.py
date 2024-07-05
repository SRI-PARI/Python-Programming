'''s1=input()
s2=input()
if sorted(s1)==sorted(s2):
    print("Anagram")
else:
    print("Not anagram")
    '''
s1=input()
s2=input()
if len(s1)==len(s2):
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]!=s2[j]:
                print("Not Anagram")
            else:
                print("anagram")
