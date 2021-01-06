def up_array(arr):
    num = ""
    result = []
    if len(arr) == 0:
        return None
    for a in arr:
        if a < 0:
            return None
        if len(str(a)) > 1:
            return None
        num += str(a)
    num = int(num)
    num += 1
    num = str(num)
    num = list(num)
    for n in num:
        result.append(int(n))
    return result
