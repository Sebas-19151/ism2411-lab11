#reflection
#1. I would use .get() for emails since it allows me to provide a default value if the key does not exist, preventing potential KeyErrors. This is especially useful in cases where the email might not be present in the customer dictionary. While I would use a bracket notation when having to use a customer's name, because a missing key should be noticed and corrected. My rule of thumb is whether I want something to be corrected.
#2. The pattern reminds of an Excel PivotTable because it can do group sales by region and add their amounts. 


print("--- Exercise 1 --- ")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spending": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spending"])
print(customer)

print("--- Exercise 2 --- ")
customer["phone"] = "813-555-0142"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

print("--- Exercise 3 --- ")
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError as error:
    print(f"KeyError Caught: {error}")

print("--- Exercise 4 --- ")
for key, value in customer.items():
    print(f"{key}: {value}")
for item in customer:
    print(item)

print("--- Exercise 5 --- ")
tier_discounts = {"bronze": 0
                , "silver": 0.05, 
                "gold": 0.1, 
                "platinum": 0.15}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"],0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount: {discount_rate * 100:.0f}%")
print(f"Final Price: ${final_price:.2f}")

print("--- Exercise 6 --- ")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spending": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spending": 8750},
    {"name": "David", "tier": "bronze", "ytd_spending": 450}
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase")

print("--- Exercise 7 --- ")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Widget B": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left in stock!")

print("--- Exercise 8 --- ")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]
print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")
