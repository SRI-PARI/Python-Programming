'''s = input().lower()
s = s.split()
al = 'abcdefghijklmnopqrstuvwxyz'
res = ""
for i in s:
    sum = 0
    start = 0
    end = len(i) - 1
    for j in range((len(i) + 1) // 2):
        if i[start] in al and i[end] in al:
            if start < end:
                sum += abs((al.index(i[start]) + 1) - (al.index(i[end]) + 1)) 
                start += 1
                end -= 1
            else:
                sum += (al.index(i[end]) + 1) 
                break
        else:
            sum += (al.index(i[end]) + 1)
            break
    res += str(sum)
print(res)'''
s = input().lower()
s = s.split()
al = "abcdefghijklmnopqrstuvwxyz"
res = ""

for i in s:
    sum = 0
    m = 0
    n = len(i) - 1
    for j in range(len(i)):
        if i[m] in al and i[n] in al:
            if m < n:
                sum += abs((al.index(i[m]) + 1) - (al.index(i[n]) + 1))
            elif m == n:  # Handle middle character case for odd-length words
                sum += al.index(i[m]) + 1
            m += 1
            n -= 1
            if m > n:
                break
        else:
            sum += al.index(i[n]) + 1
            break
    res += str(sum)

print(res)
