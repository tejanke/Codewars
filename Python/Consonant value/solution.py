import re
def solve(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    letter_values = []
    letters = re.split('[aeiou]', s)
    letters = list(filter(None, letters))
    for letter in letters:
        current_value = 0
        for l in letter:
            for a in alpha:
                if l == a:
                    current_value = current_value + alpha.index(l) + 1
        letter_values.append(current_value)
    return(max(letter_values))
                    
