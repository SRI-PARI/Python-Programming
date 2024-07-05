'''n=int(input())
s=0
for i in range(1, n):
    if n%i==0:
        s=s+i
if s==n:
    print("Perfect")
else:
    print("Not perfect")'''

n = int(input("Enter a number: "))

# Iterate through each number from 1 to n
for i in range(1, n):
    res = ""
    k = 0
    # Find the sum of divisors of i
    for j in range(1, i):
        if i % j == 0:
            k += j
    # Check if the sum of divisors is equal to the n3umber itself (perfect number)
    if k == i:
        res = str(i)
        print(res, end=" ")

