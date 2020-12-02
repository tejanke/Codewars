def get_sum(a,b):
    c = []
    if a == b:
        return a
    if a > b:
        if (a - b) == 1:
            return a + b
        for x in range(b,a):
            c.append(x)
        return sum(c) + a
    if b > a:
        if (b - a) == 1:
            return b + a
        for x in range(a,b):
            c.append(x)
        return sum(c) + b
