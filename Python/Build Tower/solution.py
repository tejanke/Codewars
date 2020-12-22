def tower_builder(n_floors):
    x = 1
    last = 0
    result = []
    final_result = []
    while x < n_floors + 1:
        o = "*" * (x + last)
        result.append(o)
        last = x
        x += 1

    base = len(max(result))
    for r in result:
        f = "{:^{width}}".format(r,width=base)
        final_result.append(f)
    return(final_result)
