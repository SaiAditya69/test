# Part 2 — Restaurant Menu & Order Management System

This project is part of my Python assignment (Part 2).
In this task, I built a simple restaurant order system using Python data structures like dictionaries and lists.

---

## What I implemented

### 1. Menu Exploration

* Displayed the full menu grouped by category (Starters, Mains, Desserts)
* Showed item name, price, and availability
* Calculated:

  * Total number of items
  * Number of available items
  * Most expensive item
  * Items priced below ₹150

---

### 2. Cart Operations

* Created a cart using a list of dictionaries
* Added items to cart with quantity
* Updated quantity if item already exists in cart
* Handled cases where:

  * Item does not exist
  * Item is unavailable
* Removed items from cart
* Printed final order summary including:

  * Subtotal
  * GST (5%)
  * Total payable amount

---

### 3. Inventory Management

* Used `copy.deepcopy()` to create a backup of inventory
* Demonstrated that changes in inventory do not affect the backup
* Deducted stock based on cart items
* Handled insufficient stock cases
* Printed reorder alerts for low stock items

---

### 4. Sales Analysis

* Calculated total revenue for each day
* Identified the best-selling day
* Found the most ordered item across all orders
* Added a new day’s sales data and updated results
* Printed a full order log using `enumerate`

---

## Files Included

* `part2_order_system.py` → main Python script

---

## How to Run

1. Make sure Python is installed
2. Run the script:

   ```
   python part2_order_system.py
   ```

---

## Notes

* Only core Python data structures were used (no external libraries except `copy`)
* The program handles edge cases like unavailable items and low stock
* Code is written in a simple and readable way with comments

---
