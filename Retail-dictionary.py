inventory = {
    "Laptop": 25,
    "Phone": 11,
    "Tablet": 11,
    "Headphones": 20,
    "Charger": 10
}

inventory["Smartwatch"] = 11
inventory["Phone"] = 13

def low_stock(inv):
    return {k:v for k,v in inv.items() if v < 10}

del inventory["Charger"]

for product, qty in inventory.items():
    print(product, ":", qty)

print("Low stock products:", low_stock(inventory))