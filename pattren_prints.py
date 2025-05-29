#  Right-Angled Triangle Pattern
print("Right Angled Triangle")
n = 5
for i in range(n):
    print("*" * i)

print("Inverted Right-Angled Triangle")
n = 5
for i in range(n, 0, -1):
    print("*" * i)

print(" Pyramid Pattern")
n = 5
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)

print("Inverted Pyramid Pattern")
n = 5
for i in range(n, 0, -1):
    print(" " * (n-i) + "* " * i)

print("Diamond Pattern")
n = 5
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)
for i in range(n, 0, -1):
    print(" " * (n-i) + "* " * i)

