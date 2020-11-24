def reverse_words(text):
    result = []
    words_split = text.split()
    words_len = len(words_split)
    total_spaces = words_len - 1
    found_spaces = 0
    for l in text:
        if l.isspace():
            found_spaces +=1
    if total_spaces > 0:
        final_spaces = found_spaces / total_spaces
        for word in words_split:
            result.append(word[::-1])
        printspace = ' ' * int(final_spaces)
        return printspace.join(result)        
    else:
        for word in words_split:
            result.append(word[::-1])
        return ' '.join(result)
