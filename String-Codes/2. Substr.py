'''
s=input()
sub_str=input()
flag=0
for i in s.split():
    if i==sub_str:
        flag=1
        break
if flag==1:
    print("yes")
else:
    print("no")
    '''
s=input()
ss=input()
if ss in s:
    print("yes")
else:
    print("no")