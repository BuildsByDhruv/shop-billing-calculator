# Shop Billing Calculator

A command-line program for a small shop. The shopkeeper types in the items a customer buys, and the program prints a clean, itemised bill with a member discount, GST and a shipping fee.

## Pricing rules

| Rule | Details |
|---|---|
| Member discount | 10% off the subtotal, only if the customer is a member **and** the subtotal is **above** 3000 |
| GST | 18% on the amount **after** the discount |
| Shipping | Based on the amount after the discount, **before** GST: 5000 or more is free, 2000 up to (not including) 5000 costs 50, below 2000 costs 100 |

Calculation order: items → subtotal → discount → GST → shipping → grand total.

## How to run

Requires Python 3.

```bash
python3 billing.py
```

The program then:
1. Asks for each item's name, price and quantity. Type `done` as the item name to finish.
2. Asks whether the customer is a member (`yes` or `no`).
3. Prints the receipt.

### Input rules
- The item name cannot be empty. Extra spaces are removed.
- The price must be a number greater than 0.
- The quantity must be a whole number greater than 0.
- At least one item is required before `done` is accepted.

## Example output

Items: `Notebook` (120.00 x 3) and `Backpack` (1500.00 x 2), member: yes.

```text
==========================================
               SHOP RECEIPT
==========================================
Item            Qty     Price      Total
------------------------------------------
Notebook          3 x  120.00 =   360.00
Backpack          2 x 1500.00 =  3000.00
------------------------------------------
Subtotal:                          3360.00
Member Discount (10%):             -336.00
After Discount:                    3024.00
GST (18%):                          544.32
Shipping Charges:                    50.00
==========================================
GRAND TOTAL:                       3618.32
==========================================
```

## Project structure

Each item is a dictionary with the keys `name`, `price` and `qty`, for example `{"name": "Pen", "price": 10.5, "qty": 4}`.

| Function | Purpose |
|---|---|
| `line_total(item)` | Price multiplied by quantity for one item |
| `calculate_subtotal(items)` | Sum of all line totals |
| `ask_membership()` | Asks whether the customer is a member |
| `get_discount(subtotal, is_member)` | Returns the discount amount (0 if not eligible) |
| `calculate_gst(amount, gst_rate=0.18)` | Returns the GST amount |
| `get_shipping_fee(amount)` | Returns the shipping fee |
| `get_positive_float()` | Asks until the user enters a number above 0 |
| `get_positive_int()` | Asks until the user enters a whole number above 0 |
| `read_items()` | Collects items as dictionaries with the keys `name`, `price` and `qty` |

Calculation functions only return values. Asking and printing happen outside them.

## Testing

Tested by hand, using real program output:

| Case | Result |
|---|---|
| Member, subtotal exactly 3000 | No discount, because the rule says "above 3000" |
| Member, subtotal 3500 | Discount of 350.00 |
| Non-member, subtotal 3500 | No discount |
| Subtotal 1900 | Shipping fee of 100 |
| `done` typed before any item | Asks for an item again |
| Empty item name | Rejected with a message |
| Price or quantity of 0 or below | Rejected with a message |
| Name with extra spaces | Spaces removed |

### Refactor check

When items moved from tuples to dictionaries, three cases were run before and after the change. The grand totals matched exactly.

| Case | Grand total before | Grand total after |
|---|---|---|
| Normal: Notebook 120 x 3 and Pen 10.5 x 4, non-member | 574.36 | 574.36 |
| Boundary: Bag 3000 x 1, member | 3590.00 | 3590.00 |
| Invalid inputs, then Pen 10 x 2, non-member | 123.60 | 123.60 |

## Known limitations

- Typing letters in a number field, or a decimal such as `2.5` for the quantity, crashes the program with a `ValueError`.
- Bills are not saved anywhere.
- Item names longer than 15 characters are not wrapped, so they push the rest of that row out of line.
- Calculations are not covered by automated tests yet.

## Open questions for the shopkeeper

- Shipping is applied to every bill by the current rule, even a small in-store purchase. Should shipping apply only to deliveries?

## Roadmap

- [x] Calculation functions and receipt
- [x] Enter items at run time, with input validation
- [x] Store items as dictionaries instead of tuples
- [ ] Wrap long item names across receipt lines
- [ ] Handle invalid input without crashing
- [ ] Save bills to a file
- [ ] Automated tests with pytest