a=int(input())
b=int(input())
gcd=1
for i in range(a,b+1):
    if a%i==0 & b%i==0:
        gcd=i
print(gcd)
lcm= a*b//(gcd)
print(lcm)