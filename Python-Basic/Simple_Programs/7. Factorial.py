#without recursion
'''n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
'''
# with recursion method 1
def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input())
print(factorial(n))

# with recursion method 1
n=int(input())
if n==0:
    print("1")
elif n==1:
    print("1")
else:
    print(n*factorial(n-1))
    
