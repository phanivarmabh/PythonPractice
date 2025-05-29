def is_palindrome(s):
    s = ''.join(s.split()).lower()
    return s == s[::-1]

print(is_palindrome("Racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
    