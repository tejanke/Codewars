def get_count(input_str):
    num_vowels = 0
    for s in input_str:
        if s in ['a', 'e', 'i', 'o', 'u']:
            num_vowels += 1
    
    return num_vowels
