def up_array(arr):
    num = ""
    result = []
    for a in arr:
        if a < 0:
            return None
        num += str(a)
    num = int(num)
    num += 1
    num = str(num)
    num = list(num)
    for n in num:
        result.append(int(n))
    return result
