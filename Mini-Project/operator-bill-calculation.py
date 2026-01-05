# # Billing calculation script for a retail store

# amount = float(input("Enter the total amount: "))
# if amount < 100:
#     discount = 0    
# elif 100 <= amount < 500:
#     discount = 0.05 * amount
# elif 500 <= amount < 1000:
#     discount = 0.10 * amount
# else:
#     discount = 0.15 * amount

# final_amount = amount - discount
# print(f"Discount applied: ${discount:.2f}") 
# print(f"Final amount to be paid: ${final_amount:.2f}")


amount = 1200
tax = amount * 0.18
total = amount + tax
print(total)

if total > 1000:
    discount = total * 0.10
    total -= discount
print(total)
