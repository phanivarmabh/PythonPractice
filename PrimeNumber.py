def is_prime(n):
    if n <= 1:
        return f"Not a prime"
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return f"Not a prime"
    return f"Prime"

try:
    num = int(input("Enter a number: "))
    result = is_prime(num)
    print(result)
except ValueError:
    print("Please enter a valid integer")