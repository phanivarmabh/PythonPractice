def reversed_string(s):
    return s[::-1]

print(reversed_string("race"))

def reversed_string(s):
    reverse = ''
    for char in s:
        reverse = char + reverse
    return reverse

print(reversed_string('Phani'))