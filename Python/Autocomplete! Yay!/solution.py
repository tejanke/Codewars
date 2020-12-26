def autocomplete(input_, dictionary):
    letters = "abcdefghijklmnopqrstuvwxyz"
    valid_input = ""
    result = []
    prefix_limit = 3
    
    for l in input_:
        if l in letters:
            valid_input += l
            
    for d in dictionary:
        current_string = ""
        prefix = d[:prefix_limit]
        for l in prefix:
            if l in letters:
                current_string += l
        suffix = d[prefix_limit:(len(d))]
        word = prefix + suffix
        if word.lower().startswith(valid_input):
            if len(result) < 5:
                result.append(word)
    return result
