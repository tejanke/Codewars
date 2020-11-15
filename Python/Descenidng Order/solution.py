def descending_order(num):
    # Bust a move right here
    s = str(num)
    if len(s) == 1:
        result = num
        return result
    else:
        s = list(s)
        s.sort(reverse=True)
        result = ''.join(s)
        result = int(result)
        return result
        
