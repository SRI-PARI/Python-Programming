n=int(input())
dec=""
while(n!=0):
    r=str(n%2)
    dec=dec+r
    n=n//2
print(dec[::-1])

    
