def min_value(digits):
    digits.sort()
    result = []
    r = ""
    for d in digits:
        if d not in result:
            result.append(d)
    for x in result:
        r += str(x)
    return int(r)
