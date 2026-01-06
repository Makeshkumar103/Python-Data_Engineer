delivery_partner = "siggy"

def hotel():
    item="pizza"

    def order_now():
        quantity=2
        print(f"ordering {quantity} {item} using {delivery_partner}")
    order_now()

hotel()

print(__file__)
