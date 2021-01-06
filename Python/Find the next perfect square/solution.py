import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    square = math.sqrt(sq)
    test = square % 1
    perfect = test > 0
    if perfect == False:
        next = square + 1
        result = next * next
        return result
    else:
        return -1
