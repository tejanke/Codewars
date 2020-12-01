def series_sum(n):
    if n > 1:
        fractions = 0
        for x in range(4,(3 * n),3):
            fractions += 1 / x
        fractions += 1
        return f'{fractions:.2f}'
    else:
        return f'{n:.2f}'
        
