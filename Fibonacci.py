def fibonacci(n):
    a, b = 0, 1
    fib_sequence = [a, b]
    for i in range(2,n):
        a, b = b, a+b
        fib_sequence.append(b)
    return fib_sequence

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]