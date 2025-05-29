def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

print(sum_of_digits(12345))  # Output: 15
print(sum_of_digits(-6789))  # Output: 30