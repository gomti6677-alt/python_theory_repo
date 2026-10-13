def get_price(item):
    if item == "idli":
        return 30
    elif item == "dosa":
        # TODO
    # TODO: complete the remaining items
    else:
        # TODO


def item_cost(item, qty):
    # TODO: call get_price() and return the cost


def calculate_gst(amount, rate=0.05):
    # TODO: return the GST rounded to 2 decimals


def generate_bill(subtotal, discount_percent=0):
    discount = # TODO
    amount_after_discount = # TODO
    gst = # TODO: call calculate_gst()
    total = # TODO
    return # TODO: return discount, gst and total


def split_bill(total, people):
    each_pays = # TODO
    left_over = # TODO
    return # TODO


# ---------------- Main program ----------------
# A group of 3 friends orders 2 dosa and 3 coffee, with a 10% coupon.

subtotal = item_cost('dosa',2)
discount1,gst,total1+ generate_bill(subtotal1,0.02)
subtotal2 = item_cost('coffe',3)
discount2, gst2, total2 = generate_bill(subtotal2,0.02)

each,extra =split_bill(total+total2,3)

print("Subtotal :", subtotal)
print("Discount :", discount)
print("GST      :", gst)
print("Total    :", total1)
print("subtotal :",subtotal2)
print("gst      :",gst2)
print("gst      :",gst2)
print("total    :",total2)

print("Each pays:", each, "| Left over:", extra)