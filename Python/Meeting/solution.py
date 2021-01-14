from operator import itemgetter
def meeting(s):
    names = []
    result = ""
    split = s.split(";")
    for name in split:
        name = name.split(":")
        firstname = name[0].upper()
        lastname = name[1].upper()
        out = [firstname, lastname]
        names.append(out)
    
    # sort by last name, then first name
    names_sort = sorted(names, key=itemgetter(1, 0))
    
    for names in names_sort:
        firstname = names[0]
        lastname = names[1]
        result = result + "(" + lastname + ", " + firstname + ")"
    return result