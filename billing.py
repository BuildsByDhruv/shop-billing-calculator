def line_total(price, quantity):
    return price * quantity


def calculate_subtotal(items):
    total = 0.0
    for _, price, quantity in items:
        total += line_total(price, quantity)
    return round(total, 2)


def ask_membership():
    answer = input("Are you a member of our shop? (yes/no): ").strip().lower()
    return answer == "yes"


def get_discount(subtotal, is_member):
    if is_member and subtotal > 3000:
        return round(subtotal * 0.10, 2)
    return 0.0


def calculate_gst(amount, gst_rate=0.18):
    return round(amount * gst_rate, 2)


def get_shipping_fee(amount):
    if amount >= 5000:
        return 0.0
    elif amount >= 2000:
        return 50.0
    return 100.0


items = [("Notebook", 120.0, 3), ("Pen", 15.5, 4), ("Backpack", 850.0, 1)]

member = ask_membership()
subtotal = calculate_subtotal(items)
discount = get_discount(subtotal, member)
discounted_total = subtotal - discount
gst = calculate_gst(discounted_total)
shipping = get_shipping_fee(discounted_total)
grand_total = discounted_total + gst + shipping

print("\n" + "=" * 42)
print(f"{'SHOP RECEIPT':^42}")
print("=" * 42)
print(f"{'Item':<15} {'Qty':>3}   {'Price':>7}   {'Total':>8}")
print("-" * 42)

for name, price, quantity in items:
    item_total = line_total(price, quantity)
    print(f"{name:<15} {quantity:>3} x {price:>7.2f} = {item_total:>8.2f}")

print("-" * 42)
print(f"{'Subtotal:':<32}{subtotal:>10.2f}")

if member:
    print(f"{'Member Discount (10%):':<32}{-discount:>10.2f}")
    print(f"{'After Discount:':<32}{discounted_total:>10.2f}")

print(f"{'GST (18%):':<32}{gst:>10.2f}")
print(f"{'Shipping Charges:':<32}{shipping:>10.2f}")
print("=" * 42)
print(f"{'GRAND TOTAL:':<32}{grand_total:>10.2f}")
print("=" * 42)