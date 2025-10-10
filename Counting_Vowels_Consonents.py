def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_list = []
    consonant_list = []

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_list.append(char)
            else:
                consonant_list.append(char)

    print("Vowels found:", vowel_list)
    print("Number of vowels:", len(vowel_list))

    print("Consonants found:", consonant_list)
    print("Number of consonants:", len(consonant_list))


# Read input from user
input_string = input("Enter a string: ")
count_vowels_consonants(input_string)
