def calculate_discount_price(price,discount_percent):
    discount= price - (price*discount_percent/100)
    return price - discount

def calculate_tax(price,tax_percent):
    return price*tax_percent/100

def calculate_total(price,discount_percent,tax_percent):
    return price - calculate_discount_price(price,discount_percent)- calculate_tax(price,tax_percent)