def delete_nth(order,max_e):
    result = []
    for o in order:
        if o not in result:
            result.append(o)
        else:
            if result.count(o) < max_e:
                result.append(o)
    return result
