def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        interest_income = principal * interest
        interest_income_after_tax = interest_income - (interest_income * tax)
        principal = principal + interest_income_after_tax
        years += 1
        
    return years
