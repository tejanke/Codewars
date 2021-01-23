def rot13(message):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for l in message:
        if l.isalpha():
            if letters.index(l.lower()) + 13 >= len(letters):
                i = letters.index(l.lower()) - 13
                if l.isupper():
                    result = result + letters[i].upper()
                else:
                    result = result + letters[i]
            if letters.index(l.lower()) + 13 < len(letters):
                i = letters.index(l.lower()) + 13
                if l.isupper():
                    result = result + letters[i].upper()
                else:
                    result = result + letters[i]
        else:
            result = result + l
    return result