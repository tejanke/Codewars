# return masked string
def maskify(cc):
    if len(cc) > 4:
        head = "#" * (len(cc) - 4)
        result = head + cc[-4:]
        return result
    else:
        result = cc[-4:]
        return result
