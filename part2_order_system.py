# ---------------- DATA ----------------

menu = {
    "Paneer Tikka": {"category": "Starters", "price": 180.0, "available": True},
    "Chicken Wings": {"category": "Starters", "price": 220.0, "available": False},
    "Veg Soup": {"category": "Starters", "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains", "price": 320.0, "available": True},
    "Dal Tadka": {"category": "Mains", "price": 180.0, "available": True},
    "Veg Biryani": {"category": "Mains", "price": 250.0, "available": True},
    "Garlic Naan": {"category": "Mains", "price": 40.0, "available": True},
    "Gulab Jamun": {"category": "Desserts", "price": 90.0, "available": True},
    "Rasgulla": {"category": "Desserts", "price": 80.0, "available": True},
    "Ice Cream": {"category": "Desserts", "price": 110.0, "available": False},
}

import copy

# ---------------- TASK 1 ----------------

print("\n--- MENU ---")

categories = set(item["category"] for item in menu.values())

for cat in categories:
    print(f"\n--- {cat} ---")
    for name, data in menu.items():
        if data["category"] == cat:
            status = "Available" if data["available"] else "Unavailable"
            print(f"{name} ₹{data['price']} [{status}]")

print("\nTotal items:", len(menu))
print("Available items:", sum(1 for i in menu.values() if i["available"]))

most_expensive = max(menu.items(), key=lambda x: x[1]["price"])
print("Most expensive:", most_expensive[0], most_expensive[1]["price"])

print("Items under 150:")
for name, data in menu.items():
    if data["price"] < 150:
        print(name, data["price"])


# ---------------- TASK 2 ----------------

cart = []

def add_item(item, qty):
    if item not in menu:
        print("Item not found")
        return

    if not menu[item]["available"]:
        print("Item not available")
        return

    for c in cart:
        if c["item"] == item:
            c["quantity"] += qty
            return

    cart.append({"item": item, "quantity": qty, "price": menu[item]["price"]})


def remove_item(item):
    for c in cart:
        if c["item"] == item:
            cart.remove(c)
            return
    print("Item not in cart")


def update_quantity(item, qty):
    for c in cart:
        if c["item"] == item:
            c["quantity"] = qty
            return


# simulation
add_item("Paneer Tikka", 2)
add_item("Gulab Jamun", 1)
add_item("Paneer Tikka", 1)
add_item("Mystery Burger", 1)
add_item("Chicken Wings", 1)
remove_item("Gulab Jamun")

print("\n--- CART ---")
subtotal = 0
for c in cart:
    total = c["quantity"] * c["price"]
    subtotal += total
    print(c["item"], c["quantity"], total)

gst = subtotal * 0.05
print("Subtotal:", subtotal)
print("GST:", gst)
print("Total:", subtotal + gst)


# ---------------- TASK 3 ----------------

inventory = {
    "Paneer Tikka": {"stock": 10, "reorder_level": 3},
    "Gulab Jamun": {"stock": 5, "reorder_level": 2},
}

inventory_backup = copy.deepcopy(inventory)

# deduct stock
for c in cart:
    item = c["item"]
    qty = c["quantity"]

    if item in inventory:
        if inventory[item]["stock"] >= qty:
            inventory[item]["stock"] -= qty
        else:
            print("Not enough stock for", item)

# reorder alert
for item, data in inventory.items():
    if data["stock"] <= data["reorder_level"]:
        print("Reorder:", item)

print("\nInventory:", inventory)
print("Backup:", inventory_backup)


# ---------------- TASK 4 ----------------

sales_log = {
    "2025-01-01": [{"total": 200}, {"total": 300}],
    "2025-01-02": [{"total": 150}],
}

# revenue per day
for date, orders in sales_log.items():
    total = sum(o["total"] for o in orders)
    print(date, total)

best_day = max(sales_log.items(), key=lambda x: sum(o["total"] for o in x[1]))
print("Best day:", best_day[0])