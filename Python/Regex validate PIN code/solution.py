import re
def validate_pin(pin):
    #return true or false
    pattern = "(^\d{4}$)|(^\d{6}$)"
    if re.match(pattern,pin) != None:
        if pin == pin.strip():
            return True
        else:
            return False
    else:
        return False
