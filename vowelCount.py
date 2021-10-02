def get_count(input_str):
    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in input_str:
        if letter in vowels:
            num_vowels+=1

    return num_vowels

print(get_count('fundamental'))