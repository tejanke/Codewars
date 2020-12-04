from datetime import datetime
from datetime import date
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code != correct_code or type(entered_code) != type(correct_code):
        return False
    
    cm = datetime.strptime(current_date.split(' ')[0], "%B")
    cm = cm.month
    cd = current_date.split(' ')[1].split(',')[0]
    cy = current_date.split(' ')[2]
    c = datetime(int(cy),int(cm),int(cd))
    
    em = datetime.strptime(expiration_date.split(' ')[0], "%B")
    em = em.month
    ed = expiration_date.split(' ')[1].split(',')[0]
    ey = expiration_date.split(' ')[2]
    e = datetime(int(ey),int(em),int(ed))
    
    days = (e-c).days
    if days > 0 or days == 0:
        return True
    else:
        return False
