n = int(input("Enter a number: "))
if n == 0:
    print(0)
elif n % 9 == 0:
    print(9)
else:
    print(n % 9)
