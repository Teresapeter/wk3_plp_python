# Define the function to calculate the discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price  # No discount applied

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount)

    # Display the result
    if discount >= 20:
        print(f"✅ Discount applied! Final price: {final_price:.2f}")
    else:
        print(f"❌ Discount too low. You pay the full price: {final_price:.2f}")

except ValueError:
    print("⚠️ Please enter valid numbers for price and discount.")
