# ISM2411 Lab 11 - Customer Dictionary & Lookup
# Sebastian Martinez
#
# Reflection 1:
# I would use .get() for an optional field, such as a customer's email,
# because it can return a default when the key is missing. I would use
# bracket notation for a required field, such as a customer's name,
# because a missing key should be noticed and corrected. In Exercise 3,
# the email was deleted, so .get() returns the default while brackets
# raise a KeyError.
#
# Reflection 2:
# Building a summary dictionary reminds me of an Excel PivotTable or
# SUMIF because both can group sales by region and add their amounts.
# The Python version can repeat the same calculation automatically when
# new transactions are added. This makes it useful for large datasets
# because the same code can process the records without manually
# updating spreadsheet formulas or ranges.


# Exercise 1 - One customer
print("Exercise 1 - One customer")

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.00,
}

print("Name:", customer["name"])
print("Email:", customer["email"])
print("Tier:", customer["tier"])
print("YTD spend:", customer["ytd_spend"])
print("Whole dictionary:", customer)


# Exercise 2 - Update and add
print("\nExercise 2 - Update and add")

customer["phone"] = "813-555-0101"
print("After adding phone:", customer)

customer["tier"] = "platinum"
print("After updating tier:", customer)

del customer["email"]
print("After deleting email:", customer)


# Exercise 3 - Safe lookup
print("\nExercise 3 - Safe lookup")

print(customer.get("email", "no email on file"))

# Catch the KeyError so the remaining exercises can still run.
try:
    print(customer["email"])
except KeyError as error:
    print(f"KeyError: {error}")


# Exercise 4 - Iterate
print("\nExercise 4 - Iterate")

for key, value in customer.items():
    print(f"{key}: {value}")

print("Keys only:")
for key in customer.keys():
    print(key)

# .items() provides each key and its value as a pair.
# .keys() provides only the keys, so it does not directly give the values.


# Exercise 5 - Lookup table
print("\nExercise 5 - Lookup table")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15,
}

purchase_amount = 200.00
tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)
discount_amount = purchase_amount * discount_rate
final_price = purchase_amount - discount_amount

print("Tier:", tier)
print(f"Discount rate: {discount_rate:.0%}")
print(f"Discount amount: ${discount_amount:.2f}")
print(f"Final price: ${final_price:.2f}")


# Exercise 6 - List of dicts
print("\nExercise 6 - List of dicts")

customers = [
    customer,
    {
        "name": "Bob",
        "email": "bob@example.com",
        "tier": "silver",
        "ytd_spend": 600.00,
    },
    {
        "name": "Carla",
        "email": "carla@example.com",
        "tier": "bronze",
        "ytd_spend": 250.00,
    },
]

purchase_amount = 500.00

for person in customers:
    tier = person["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = purchase_amount * discount_rate
    print(
        f"Name: {person['name']} | Tier: {tier} | "
        f"Discount on ${purchase_amount:.2f}: ${discount_amount:.2f}"
    )


# Exercise 7 - Nested catalog
print("\nExercise 7 - Nested catalog")

catalog = {
    "Widget A": {"price": 9.99, "stock": 120},
    "Widget B": {"price": 24.99, "stock": 30},
}

for product_name, details in catalog.items():
    if details["stock"] < 50:
        print(f"LOW STOCK: {product_name} - {details['stock']} remaining")


# Exercise 8 - Sales by region
print("\nExercise 8 - Sales by region")

transactions = [
    {"region": "North", "amount": 200},
    {"region": "South", "amount": 150},
    {"region": "North", "amount": 300},
]

summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    summary[region] = summary.get(region, 0) + amount

for region in sorted(summary):
    print(f"{region}: ${summary[region]:.2f}")
