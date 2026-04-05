# part2_order_system.py

# ==========================================================
# Provided Data
# ==========================================================

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

# ==========================================================
# Task 1 — Menu Exploration
# ==========================================================

print("\n--- MENU ---")

categories = set(menu[item]["category"] for item in menu)

for cat in categories:
    print(f"\n===== {cat} =====")
    for name, details in menu.items():
        if details["category"] == cat:
            status = "Available" if details["available"] else "Unavailable"
            print(f"{name:<15} ₹{details['price']:.2f} [{status}]")

print("\nTotal items:", len(menu))

available_count = sum(1 for item in menu.values() if item["available"])
print("Available items:", available_count)

exp_item = max(menu, key=lambda x: menu[x]["price"])
print("Most expensive:", exp_item, "-", menu[exp_item]["price"])

print("\nItems under ₹150:")
for name, d in menu.items():
    if d["price"] < 150:
        print(name, "-", d["price"])


# ==========================================================
# Task 2 — Cart Operations
# ==========================================================

cart = []

def show_cart():
    print("\nCurrent cart:")
    if not cart:
        print("Cart is empty")
    else:
        for item in cart:
            print(f"{item['item']} x{item['quantity']}")

def add_item(name, qty):
    if name not in menu:
        print("Item not in menu")
        return
    
    if not menu[name]["available"]:
        print("Item currently unavailable")
        return
    
    for item in cart:
        if item["item"] == name:
            item["quantity"] += qty
            print(name, "updated in cart")
            return
    
    cart.append({
        "item": name,
        "quantity": qty,
        "price": menu[name]["price"]
    })
    print(name, "added to cart")

def remove_item(name):
    for item in cart:
        if item["item"] == name:
            cart.remove(item)
            print(name, "removed from cart")
            return
    print("Item not found in cart")

print("\n--- CART OPERATIONS ---")

add_item("Paneer Tikka", 2)
show_cart()

add_item("Gulab Jamun", 1)
show_cart()

add_item("Paneer Tikka", 1)
show_cart()

add_item("Mystery Burger", 1)
show_cart()

add_item("Chicken Wings", 1)
show_cart()

remove_item("Gulab Jamun")
show_cart()

# Order Summary
print("\n========== Order Summary ==========")

subtotal = 0
for item in cart:
    total = item["quantity"] * item["price"]
    subtotal += total
    print(f"{item['item']:<15} x{item['quantity']} ₹{total:.2f}")

gst = subtotal * 0.05
total_pay = subtotal + gst

print("-" * 35)
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"GST (5%): ₹{gst:.2f}")
print(f"Total Payable: ₹{total_pay:.2f}")
print("=" * 40)


# ==========================================================
# Task 3 — Inventory (Deep Copy)
# ==========================================================

import copy

inventory_backup = copy.deepcopy(inventory)

# testing deep copy
inventory["Paneer Tikka"]["stock"] = 2

print("\nAfter manual change:")
print("Current:", inventory["Paneer Tikka"])
print("Backup :", inventory_backup["Paneer Tikka"])

# restore original
inventory = copy.deepcopy(inventory_backup)

# deduct stock
for item in cart:
    name = item["item"]
    qty = item["quantity"]
    
    if inventory[name]["stock"] >= qty:
        inventory[name]["stock"] -= qty
    else:
        print("Not enough stock for", name)
        inventory[name]["stock"] = 0

# reorder alerts
print("\n--- Reorder Alerts ---")
for name, d in inventory.items():
    if d["stock"] <= d["reorder_level"]:
        print(f"⚠ Reorder Alert: {name} — Only {d['stock']} unit(s) left (reorder level: {d['reorder_level']})")

# print full inventory comparison
print("\nFinal Inventory:")
for k, v in inventory.items():
    print(k, v)

print("\nBackup Inventory:")
for k, v in inventory_backup.items():
    print(k, v)


# ==========================================================
# Task 4 — Sales Log Analysis
# ==========================================================

print("\n--- SALES REPORT ---")

daily_rev = {}

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_rev[date] = total
    print(date, ":", total)

best_day = max(daily_rev, key=daily_rev.get)
print("Best day:", best_day)

# most ordered item
item_count = {}

for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_count[item] = item_count.get(item, 0) + 1

top_item = max(item_count, key=item_count.get)
print("Most ordered item:", top_item)

# add new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

# recompute revenue
print("\nUpdated revenue per day:")

daily_rev = {}
for date, orders in sales_log.items():
    total = sum(o["total"] for o in orders)
    daily_rev[date] = total
    print(date, ":", total)

best_day = max(daily_rev, key=daily_rev.get)
print("New best day:", best_day)

# enumerate all orders
print("\n--- All Orders ---")

count = 1
for date, orders in sales_log.items():
    for order in orders:
        items = ", ".join(order["items"])
        print(f"{count}. [{date}] Order #{order['order_id']} — ₹{order['total']:.2f} — Items: {items}")
        count += 1

print("\nDone.")