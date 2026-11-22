def line_total(item):
    return item["price"] * item["qty"]


def calculate_subtotal(items):
    total = 0.0
    for item in items:
        total += line_total(item)
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


def get_positive_float():
    while True:
        price = float(input("Enter the price: "))
        if price > 0:
            return price
        else:
            print("The price must be greater than 0. Please enter proper price.")


def get_positive_int():
    while True:
        qty = int(input("Enter the quantity: "))
        if qty > 0:
            return qty
        else:
            print(
                "The quantity must be a whole number greater than 0. please enter proper value."
            )


def read_items():
    items = []
    while True:
        name = input("Enter the name of product, (type 'done' to submit) : ").strip()
        if name == "":
            print("name cannot be empty. please enter the proper name.")
            continue
        if items == [] and name.lower() == "done":
            print("at least one item is needed. please enter the item.")
            continue
        if name.lower() == "done":
            break
        price = get_positive_float()
        qty = get_positive_int()
        item = {"name": name, "price": price, "qty": qty}
        items.append(item)
    return items


items = read_items()

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

for item in items:
    item_total = line_total(item)
    print(
        f"{item['name']:<15} {item['qty']:>3} x {item['price']:>7.2f} = {item_total:>8.2f}"
    )

print("-" * 42)
print(f"{'Subtotal:':<32}{subtotal:>10.2f}")

if member and subtotal > 3000:
    print(f"{'Member Discount (10%):':<32}{-discount:>10.2f}")
    print(f"{'After Discount:':<32}{discounted_total:>10.2f}")

print(f"{'GST (18%):':<32}{gst:>10.2f}")
print(f"{'Shipping Charges:':<32}{shipping:>10.2f}")
print("=" * 42)
print(f"{'GRAND TOTAL:':<32}{grand_total:>10.2f}")
print("=" * 42)