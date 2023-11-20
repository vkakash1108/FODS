# Given data
item_prices = [2.5, 3.0, 1.5, 4.0]  # Prices of individual items
quantities = [3, 2, 4, 1]           # Quantities of each item
discount_rate = 10                  # Discount rate in percentage
tax_rate = 8                        # Tax rate in percentage

# Step 2: Calculate the total cost before any discounts or taxes
total_cost_before_discount = sum(price * quantity for price, quantity in zip(item_prices, quantities))

# Step 3: Apply the discount to the total cost
discount_amount = (discount_rate / 100) * total_cost_before_discount
discounted_total = total_cost_before_discount - discount_amount

# Step 4: Apply the tax to the discounted total
tax_amount = (tax_rate / 100) * discounted_total
total_cost_after_tax = discounted_total + tax_amount

# Step 5: Display the final total cost
print("Total cost after discounts and taxes: ${:.2f}".format(total_cost_after_tax))
