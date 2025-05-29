def remove_first_string(s):
    words = s.lower().split()
    modified_words = [word[1:] if word.startswith('s') else word for word in words]
    result = ' '.join(modified_words)
    return result

s = "Sword fiSh is a fish with sword like Nose"
print(remove_first_string(s))