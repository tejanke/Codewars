def binary_to_string(binary):
    w = len(binary)
    x = 0
    y = 8
    result = ""
    while x < w:
        b = binary[x:y]
        z = chr(int(b,2))
        x += 8
        y += 8
        result += z
    return result
