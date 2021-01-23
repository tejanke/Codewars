def printer_error(s):
    good = "abcdefghijklm"
    errors = 0
    total = 0
    for l in s:
        if l not in good:
            errors += 1
        total += 1
    return "{}/{}".format(errors, total)