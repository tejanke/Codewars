def is_int_array(arr):
    
    accepted_types = [int, float]
    
    if arr is None:
        return False
    if arr == "":
        return False
    if not arr:
        return True

    for a in arr:
        if type(a) not in accepted_types:
            return False
        if type(a) == float:
            if a.is_integer() == False:
                return False
    return True
