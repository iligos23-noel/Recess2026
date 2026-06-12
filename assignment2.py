
#               USER DATABASE (login credentials)

users = {
    "iligo": {"password": "iligo23", "role": "admin"},
    "cashier": {"password": "cash123", "role": "Cashier"},
    "kennedy": {"password": "kennedy23", "role": "customer"}
}

#                     LOGIN SYSTEM

print("===================================")
print("   Welcome to Shopwise Supermarket  ")
print("===================================")
print()

# Ask the user to log in
entered_username = input("Enter your username: ")


print()

# Check which user is logging in using nested conditions
if entered_username in users:
    user_info = users[entered_username]
    entered_password = input("Enter your password: ")
    if entered_password == user_info["password"]:
        role = user_info["role"]
        print(f" Login successful! Welcome, {role}.")
        print(f" Access Level: {role.upper()} ACCESS")
    else:
        role = "None"
        print(" Wrong password for Admin!")

else:
    role = "None"
    print(" Username not found. Please try again.")

print()

# ============================================================
#          PRICE CALCULATOR (only if login succeeded)
# ============================================================

if role == "None":
    print(" Access denied. Please restart and try again.")

else:
    print("===================================")
    print("         Price Calculator        ")
    print("===================================")

    # Step 1: Get the subtotal from the user
    subtotal = float(input("Enter the product subtotal (UGX): "))

    # -------------------------------------------------------
    # Step 2: Apply discount based on subtotal amount
    # -------------------------------------------------------
    print()
    print("--- Discount Calculation ---")

    if subtotal >= 500000:
        discount_percent = 20  # 20% discount for large purchases
        print(" You qualify for a 20% bulk discount!")
    elif subtotal >= 200000:
        discount_percent = 10  # 10% discount for medium purchases
        print(" You qualify for a 10% mid-range discount!")
    elif subtotal >= 50000:
        discount_percent = 5   # 5% discount for small purchases
        print(" You qualify for a 5% discount!")
    else:
        discount_percent = 0   # No discount
        print("No automatic discount for this amount.")

    discount_amount = (discount_percent / 100) * subtotal
    subtotal_after_discount = subtotal - discount_amount

    # Apply coupon code (extra discount)
    print()
    print("--- Coupon Code ---")

    coupon = input("Enter a coupon code (or press Enter to skip): ")
    coupon_discount = 0

    if coupon == "SAVE10":
        coupon_discount = 0.10 * subtotal_after_discount
        print(" Coupon SAVE10 applied! Extra 10% off.")
    elif coupon == "WELCOME5":
        coupon_discount = 0.05 * subtotal_after_discount
        print(" Coupon WELCOME5 applied! Extra 5% off.")
    elif coupon == "":
        print("No coupon code entered.")
    else:
        print(" Invalid coupon code. No extra discount applied.")

    subtotal_after_coupon = subtotal_after_discount - coupon_discount

    # Apply tax based on location
    print()
    print("--- Tax Calculation ---")
    print("Select your location:")
    print("1 - Kampala (18% VAT)")
    print("2 - Other Uganda cities (15% VAT)")
    print("3 - International (0% - tax-free)")

    location_choice = input("Enter your choice (1/2/3): ")

    if location_choice == "1":
        tax_rate = 18
        location_name = "Kampala"
    elif location_choice == "2":
        tax_rate = 15
        location_name = "Other Uganda City"
    elif location_choice == "3":
        tax_rate = 0
        location_name = "International"
    else:
        tax_rate = 18  # default to Kampala rate
        location_name = "Unknown (defaulting to Kampala rate)"
        print("  Invalid choice. Defaulting to Kampala tax rate.")

    tax_amount = (tax_rate / 100) * subtotal_after_coupon
    final_price = subtotal_after_coupon + tax_amount

    # Show the final receipt
    print()
    print("===================================")
    print("            RECEIPT              ")
    print("===================================")
    print(f"Logged in as        : {role}")
    print(f"Location            : {location_name}")
    print(f"Original Subtotal   : UGX {subtotal:,.0f}")
    print(f"Discount ({discount_percent}%)      : - UGX {discount_amount:,.0f}")
    print(f"Coupon Discount     : - UGX {coupon_discount:,.0f}")
    print(f"Tax ({tax_rate}%)           : + UGX {tax_amount:,.0f}")
    print("-----------------------------------")
    print(f" FINAL PRICE      : UGX {final_price:,.0f}")
    print("===================================")
    print("Thank you for shopping with us! ")