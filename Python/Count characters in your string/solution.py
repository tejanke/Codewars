def count(string):
    letters = {}
    for x in string:
        if x not in letters:
            letters[x] = 1
        else:
            letters[x] += 1
    return letters
