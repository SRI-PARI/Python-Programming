# Get user input
n = int(input("Enter a number: "))

# Initialize variables for Fibonacci sequence
a, b = 0, 1

# Print the first two Fibonacci numbers
print(a, b, end=" ")

# Generate Fibonacci sequence up to n
for i in range(0, n):
    c = a + b
    if c > n:
        break
    print(c, end=" ")
    a, b = b, c
