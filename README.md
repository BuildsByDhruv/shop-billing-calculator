# Shop Billing Calculator

A command-line program that prints a clean, itemised bill for a small shop. It applies a member discount, GST and a shipping fee, following the shop's pricing rules.

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

The program asks whether the customer is a member (`yes` or `no`) and prints the receipt.

## Example output

```text
==========================================
               SHOP RECEIPT
==========================================
Item            Qty     Price      Total
------------------------------------------
Notebook          3 x  120.00 =   360.00
Pen               4 x   15.50 =    62.00
Backpack          1 x  850.00 =   850.00
------------------------------------------
Subtotal:                          1272.00
GST (18%):                          228.96
Shipping Charges:                   100.00
==========================================
GRAND TOTAL:                       1600.96
==========================================
```

## Project structure

| Function | Purpose |
|---|---|
| `line_total(price, quantity)` | Price multiplied by quantity for one item |
| `calculate_subtotal(items)` | Sum of all line totals |
| `ask_membership()` | Asks whether the customer is a member |
| `get_discount(subtotal, is_member)` | Returns the discount amount (0 if not eligible) |
| `calculate_gst(amount, gst_rate=0.18)` | Returns the GST amount |
| `get_shipping_fee(amount)` | Returns the shipping fee |

Calculation functions only return values. Asking and printing happen outside them.

## Testing

Tested by hand with real program output for these cases:

| Case | Result |
|---|---|
| Member, subtotal exactly 3000 | No discount, because the rule says "above 3000" |
| Member, subtotal 3500 | Discount of 350.00 |
| Non-member, subtotal 3500 | No discount |
| Subtotal 1900 | Shipping fee of 100 |

## Known limitations

- Items are hard-coded in the program. Typing items in at run time is planned.
- Typing letters where a number is expected will crash the program with a `ValueError`.
- Bills are not saved anywhere.

## Roadmap

- [x] Calculation functions and receipt
- [ ] Enter items at run time, with input validation
- [ ] Handle invalid input without crashing
- [ ] Save bills to a file
- [ ] Automated tests with pytest