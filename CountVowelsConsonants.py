def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowels_count = consonants_count = 0
    for char in s:
        if char in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
    return vowels_count, consonants_count

vowels, consonants = count_vowels_consonants(input("Enter the string: "))

print(f"Vowels: {vowels}, Consonants: {consonants}")