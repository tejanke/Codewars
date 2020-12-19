def alphabet_position(text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = []
    for t in text:
        for l in letters:
            if t.lower() == l:
                result.append(str(letters.index(t.lower()) + 1))
                
    result = " ".join(result)
    return result
