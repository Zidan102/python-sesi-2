from ecommerce.pricing import calculate_tax,calculate_discount_price,calculate_total
from ecommerce.order import generate_order_id

def creat_order():
    price= 100000
    discount_percent= 0.25
    tax_percent=0.11
    name = "John"

    #menghitung discount
    after_discount = calculate_discount_price(price,discount_percent)

    #menghitung tax
    after_tax = calculate_tax(price,tax_percent)

    #menghitung total
    after_all = price - after_discount - after_tax
    print("<-------------------->")
    print(f"Order ID: {generate_order_id()}")
    print(f"Price: {price}")
    print(f"Discount: {after_discount}")
    print(f"Tax: {after_tax}")
    print(f"Total: {after_all}")
    print("<-------------------->")
    print("Thank you!".center(10))

if __name__ == "__main__":
    creat_order()