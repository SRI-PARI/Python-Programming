s = input().split()
res = []
for i in s:
    l = sorted(i)
    res.append("".join(l))
print("-".join(res))
