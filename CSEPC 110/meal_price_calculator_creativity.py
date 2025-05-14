"""
Creativity part explanation: I decided to create different responses for the user after the payment:

1 - Return the change if the payment is higher than the final price.
2 - Return a personalized message if the payment is equal to the final price.
3 - Return the amount due if the payment is less than the final price.
"""

price_child_meal = float(input("The price of a child's meal: "))
price_adult_meal = float(input("The price of an adult's meal: "))
number_children  = int(input("The number of children: "))
number_adults    = int(input("The number of adults: "))
sales_tax_rate   = float(input("The sales tax rate as a percentage(Please note that this percentage should be entered and stored as a number such as 6, or 6.5, not 0.06 or 0.065.): "))

total_price_child_meal = price_child_meal * number_children
total_price_adult_meal = price_adult_meal * number_adults
total_price_meal = total_price_adult_meal + total_price_child_meal
sales_tax_rate_price = (sales_tax_rate * total_price_meal)/100
final_price = total_price_meal + sales_tax_rate_price

print(f"Subtotal: ${total_price_meal:.2f}")
print(f"Sales Tax Rate: {sales_tax_rate:.2f}%")
print(f"Sales Tax: ${sales_tax_rate_price:.2f}")
print(f"Total Price: ${final_price:.2f}")

payment_amount = float(input("Payment amount: "))

if payment_amount > final_price:
    change = payment_amount - final_price
    print(f"Change: ${change:.2f}")

if payment_amount == final_price:
    print("There is no change, debt paid in full")

if payment_amount < final_price:
    amount_due = final_price - payment_amount
    print(f"You paid ${payment_amount:.2f} and there's still a balance of ${amount_due:.2f}")