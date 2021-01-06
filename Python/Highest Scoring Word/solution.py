def high(x):
    letters = "abcdefghijklmnopqrstuvwxyz"
    words = x.split(" ")
    word_totals = {}
    for word in words:
        if word not in word_totals:
            word_score = 0
            for l in word:
                word_score += letters.index(l) + 1
            word_totals[word] = word_score
    return max(word_totals, key=word_totals.get)
